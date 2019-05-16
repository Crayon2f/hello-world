# coding=utf-8
import os
import shutil


def copy_file(source_dir, target_dir):
    for child in os.listdir(source_dir):
        sourceFile = os.path.join(source_dir, child)
        targetFile = os.path.join(target_dir, child)
        if os.path.isfile(sourceFile):
            open(targetFile, "wb").write(open(sourceFile, "rb").read())


if __name__ == '__main__':
    shutil.copytree(u"F:\\artworks\\00b4b485a03a498a82b066b2c19a21fd",
                    u"F:\\final_round\\00b4b485a03a498a82b066b2c19a21fd\\")
