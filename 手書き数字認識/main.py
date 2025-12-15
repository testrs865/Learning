import torch
from pathlib import Path
from predict_10_15 import SimpleCNN, predict_image
import writing_picture

if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # モデル読み込み
    model = SimpleCNN().to(device)
    model_path = Path.home() / "data_sets" / "model.pth"
    model.load_state_dict(torch.load(model_path, map_location=device))

    # 推論したい画像（280×560 など）
    #img_path = Path.home() / "drawing.png"

    result = predict_image(model, img_path, device)
    print(f"予測結果: {result}")