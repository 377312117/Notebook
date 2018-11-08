def read_from_file():
    L = []
    try:
        f = open("si.txt","r")
        for line in f:
            # 去掉\n
            line =line.strip()
            items = line.split(",")
            n ,a ,s = items
            a = int (a)
            s = int (s)
            L.append(dict(name=n,age=a,score=s))
        f.close()
    except OSError:
        print("打开文件失败")

            