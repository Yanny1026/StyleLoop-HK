from rembg import remove
from PIL import Image
import io
import os

def process_clothing_image(input_path):
    # 檢查文件是否存在
    if not os.path.exists(input_path):
        print(f"找不到檔案: {input_path}")
        return

    # 打開圖片
    with open(input_path, 'rb') as i:
        input_image = i.read()
        
    # AI 去背處理
    print("AI 正在處理中，請稍候...")
    output_image = remove(input_image)
    
    # 儲存結果
    output_path = input_path.replace(".jpg", "_no_bg.png").replace(".png", "_no_bg.png")
    img = Image.open(io.BytesIO(output_image)).convert("RGBA")
    img.save(output_path)
    
    print(f"成功！去背後的圖片已儲存至: {output_path}")

# 測試用 (你可以上傳一張 T-shirt 照片到 backend 文件夾試試)
# process_clothing_image('backend/test_shirt.jpg')