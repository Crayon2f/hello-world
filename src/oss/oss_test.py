from oss import oss_kit

if __name__ == '__main__':
    # oss_kit.OssKit().upload('temp/oss.jpg', '/Users/goufeifan/Downloads/oss.jpg')
    oss_kit.OssKit().download(
        'artwork_main/2018/03/27/ARTWORK_MAIN_9F53E0AC7FD423F149B4FABBEC24389D/701fd22e0165422bad72cf83fdc5f4a3.jpg',
        '/Users/goufeifan/Downloads/temp.jpg')
    # oss_kit.OssKit().delete("")
