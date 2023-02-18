import os


if __name__ == "__main__":
    for root, dirs, files in os.walk("C:/Users/Max/Desktop/Новая папка/ai/Modern Computer Vision PyTorch, Tensorflow2 Keras and OpenCV4__2022-02udemy"):
        if not files:
            continue

        # print(str(files))
        prefix = os.path.basename(root)

        for file in (file for file in files if os.path.splitext(file)[1] == ".mkv"):
            # print(os.path.join(root, f"Module {prefix} - Lesson {file}"))
            os.rename(
                os.path.join(root, file),
                os.path.join(root, f"Module {prefix} - Lesson {file}")
            )
