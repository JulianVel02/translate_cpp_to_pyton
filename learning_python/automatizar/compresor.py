from PIL import Image
import os

downloads_folder = "D:/Archivos del Programa/audiosVidImg"

if __name__ == "__main__":
    for filename in os.listdir(downloads_folder):
        filepath = os.path.join(downloads_folder, filename)
        name, extension = os.path.splitext(filename)

        if extension.lower() in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(filepath)
            picture.save(os.path.join(downloads_folder, "compressed_" + filename),
                         optimize=True, quality=85)
