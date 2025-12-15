import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------
# モデル定義
# ----------------------------
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)

        self.fc1 = nn.Linear(64 * 7 * 14, 128)
        self.fc2 = nn.Linear(128, 6)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

# ----------------------------
# 前処理：数字部分を切り出して 28×56 に整形
# ----------------------------
def crop_and_resize(img, target_size=(56, 28), threshold=50):
    """
    手書き数字領域を抽出 → 縦横比維持 → 28×56 にパディング
    """
    img_np = np.array(img)

    # 二値化（背景黒・文字白を想定）
    mask = img_np > threshold
    coords = np.column_stack(np.where(mask))

    if coords.size == 0:
        return Image.new("L", target_size, 0)

    y_min, x_min = coords.min(0)
    y_max, x_max = coords.max(0)

    # 数字部分を切り出し
    digit = img.crop((x_min, y_min, x_max + 1, y_max + 1))

    # 縦横比維持リサイズ
    w, h = digit.size
    target_w, target_h = target_size
    scale = min(target_w / w, target_h / h)
    new_w, new_h = int(w * scale), int(h * scale)
    digit = digit.resize((new_w, new_h))

    # パディングして中央配置
    canvas = Image.new("L", target_size, 0)
    offset_x = (target_w - new_w) // 2
    offset_y = (target_h - new_h) // 2
    canvas.paste(digit, (offset_x, offset_y))

    return canvas

# ----------------------------
# 推論関数
# ----------------------------
def predict_image(model, img_path, device, show_processed=True):
    # 画像読み込み
    img = Image.open(img_path).convert("L")

    # 前処理
    processed = crop_and_resize(img, target_size=(56, 28))

    # 前処理後の画像を表示
    if show_processed:
        plt.imshow(processed, cmap="gray")
        plt.title("Processed Image (28x56)")
        plt.axis("off")
        plt.show()

    # Tensor化
    img_tensor = transforms.ToTensor()(processed).unsqueeze(0).to(device)

    # 推論
    model.eval()
    with torch.no_grad():
        output = model(img_tensor)
        pred = output.argmax(dim=1).item()

    return pred + 10  # 10〜20 に変換

# ----------------------------
# main
# ----------------------------
if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # モデル読み込み
    model = SimpleCNN().to(device)
    model_path = Path.home() / "data_sets" / "model.pth"
    model.load_state_dict(torch.load(model_path, map_location=device))

    # 推論したい画像（280×560 など）
    img_path = Path.home() / "drawing.png"

    result = predict_image(model, img_path, device)
    print(f"予測結果: {result}")
