import os
from PIL import Image
import pyocr
import pyocr.builders

def tessert(img_rgb):
    tools = pyocr.get_available_tools()
    tool = tools[0]
    builder = pyocr.builders.TextBuilder()
    result = tool.image_to_string(img_rgb, lang='eng', builder=builder)
    return result

if __name__ == "__main__":
    img_org = Image.open("C:/Users/keisu/Downloads/ocr-test.png")
    imgs_path = "C:/Users/keisu/venv/test/Include/"
    text_out = "C:/Users/keisu/venv/test/Outputs/"
    imgs = os.listdir(imgs_path)
    if (imgs):
        for img in imgs:
            img_path = os.path.join(imgs_path, img)
            img_org = Image.open(img_path)
            # 画像編集
            img_rgb = img_org.convert("RGB")
            pixels = img_rgb.load()
            cmax =90
            for j in range(img_rgb.size[1]):
                for i in range(img_rgb.size[0]):
                    if (pixels[i, j][0] > cmax or pixels[i, j][1] > cmax or pixels[i, j][2] > cmax):
                        pixels[i, j] = (255, 255, 255)
            img_rgb.show()
            # function
            result = tessert(img_rgb)
            filename = os.path.splitext(os.path.basename(img))[0]
            f = open(os.path.join(text_out, filename + ".txt"), "w", encoding="utf-8")
            f.write(result)
            f.close()
            # os.remove(img_path)
    else:
        print("No images")
