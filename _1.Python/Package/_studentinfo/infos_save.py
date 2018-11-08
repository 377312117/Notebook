def save_to_file(L):
    try:
        f = open("si.txt","w")
        for d in L:
            f.write(d["name"])
            f.write(",")
            f.write(str(d["age"]))
            f.write(",")
            f.write(str(d["score"]))
            f.write("\n")
        f.close()
        print("保存成功")
    except OSError:
        print("保存文件失败")