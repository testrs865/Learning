import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from config import INPUT_WIDTH, INPUT_HEIGHT, THRESHOLD, NUM_CLASSES

# =====================
# CNNモデル
# =====================
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)

        self.fc1 = nn.Linear(64 * 7 * 14, 128)
        self.fc2 = nn.Linear(128, NUM_CLASSES)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

# =====================
# 前処理
# =====================
def crop_and_resize(img):
    img_np = np.array(img)
    mask = img_np > THRESHOLD
    coords = np.column_stack(np.where(mask))

    if coords.size == 0:
        return Image.new("L", (INPUT_WIDTH, INPUT_HEIGHT), 0)

    y_min, x_min = coords.min(0)
    y_max, x_max = coords.max(0)

    digit = img.crop((x_min, y_min, x_max + 1, y_max + 1))

    w, h = digit.size
    scale = min(INPUT_WIDTH / w, INPUT_HEIGHT / h)
    digit = digit.resize((int(w * scale), int(h * scale)))

    canvas = Image.new("L", (INPUT_WIDTH, INPUT_HEIGHT), 0)
    canvas.paste(
        digit,
        ((INPUT_WIDTH - digit.size[0]) // 2,
         (INPUT_HEIGHT - digit.size[1]) // 2)
    )

    return canvas

# =====================
# 推論
# =====================
def predict_image(model, img_path, device, show_processed=True):
    img = Image.open(img_path).convert("L")
    processed = crop_and_resize(img)

    # if show_processed:
    #     plt.imshow(processed, cmap="gray")
    #     plt.title("Processed Image")
    #     plt.axis("off")
    #     plt.show()

    tensor = transforms.ToTensor()(processed).unsqueeze(0).to(device)

    model.eval()
    with torch.no_grad():
        output = model(tensor)
        pred = output.argmax(dim=1).item()

    return pred + 10