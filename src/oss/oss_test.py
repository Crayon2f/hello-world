from oss import oss_kit

if __name__ == '__main__':
    # oss_kit.OssKit().upload('temp/oss.jpg', '/Users/goufeifan/Downloads/oss.jpg')
    # oss_kit.OssKit().download('temp/oss.jpg', '/Users/goufeifan/Downloads/temp.jpg')
    oss_kit.OssKit().delete("artwork_main/<attribute 'year' of 'datetime.date' objects>/<attribute 'month' of 'datetime.date' objects>/<attribute 'day' of 'datetime.date' objects>/69BBBAAC05554E6BBE1CEF2518C035FA/C13684145D6441E49BBBECABC67C5DAE.jpg")
