# 有一个bytearray字节数组
ba = bytearray(b"a1b2c3d4")
# 如何得到字节串"1234"和 "abcd"
# 将上述字节数组改为:
    # ba = bytearray(b"A1B2C3D4")
print(bytes(ba[::2]))
print(bytes(ba[1::2]))
ba[::2] = b"ABCD"
print(ba)