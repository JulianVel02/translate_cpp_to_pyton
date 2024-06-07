from PIL import Image
import os

downloads_folder = "C:/Users/velaz/Downloads"
pictures_folder = "D:/Archivos del Programa/audiosVidImg/images"
music_folder = "D:/Archivos del Programa/audiosVidImg/music"
# Cambié la carpeta para videos
vid_folder = "D:/Archivos del Programa/audiosVidImg/videos"

if __name__ == "__main__":
    for filename in os.listdir(downloads_folder):
        filepath = os.path.join(downloads_folder, filename)
        name, extension = os.path.splitext(filename)

        if extension.lower() in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(filepath)
            picture.save(os.path.join(pictures_folder,
                         "compressed_" + filename), optimize=True, quality=85)
            os.remove(filepath)
            print(name + ": " + extension)

        elif extension.lower() == ".mp3":
            os.rename(filepath, os.path.join(music_folder, filename))

        elif extension.lower() == ".mp4":
            os.rename(filepath, os.path.join(vid_folder, filename))
