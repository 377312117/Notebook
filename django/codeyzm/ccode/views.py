from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image,ImageDraw,ImageFont
import random

# Create your views here.
def verifycode(request):
    bgcolor = '#997679'
    width = 100
    height = 25
    # 创建画布
    im = Image.new('RGB',(width,height),bgcolor)
    # 创建画笔
    draw = ImageDraw.Draw(im)
    # 画点(方法1)
    xy = (random.randrange(0,width),random.randrange(0,height))
    fill = (random.randrange(0,255),255,random.randrange(0,255))
    draw.point(xy,fill=fill)
    str1 = 'ABCD123DEFGHIJK456LMNOPQRS789TUVWXYZ0'
    rand_str=''
    for i in range(0,4):
        rand_str += str1[random.randrange(0,len(str1))]
    font = ImageFont.truetype(
        '/System/Library/Fonts/Apple Symbols.ttf',23
    )
    draw.text((5,2),rand_str,fill=rmdRGB(),font=font)

    # 方法2,高难度级别
    numb_1 = {"1":"以","2":"贰","3":"叁","4":"肆","5":"伍","6":"陆","7":"柒","8":"捌","9":"玖",}
    numb_2 = random.randint(1,50)
    sign = ["+","-"]
    numb_1_n = random.randrange(1,10)
    numb_1_s = str(numb_1_n)
    first_s = numb_1[numb_1_s]
    third_s = str(numb_2)
    sign_n = random.randrange(0,2)
    second_s = sign[sign_n]
    if sign_n == 0:
        last = numb_1_n +numb_2
    else:
        last = numb_2 - numb_1_n
    last_s = str(last)
    draw.text((5,2),'?',font=font,fill=rmdRGB())
    draw.text((20,2),second_s,font=font,fill=rmdRGB())
    draw.text((35,2),first_s,font=font,fill=rmdRGB())
    draw.text((60,2),'=',font=font,fill=rmdRGB())
    draw.text((75,2),last_s,font=font,fill=rmdRGB())
    # 添加干扰线
    for i  in range(5):
        x1 = random.randrange(0,width)
        y1 = random.randrange(0,height)
        x2 = random.randrange(0,width)
        y2 = random.randrange(0,height)
        draw.line((x1,y1,x2,y2),fill=rmdRGB())

    # 添加圆
    x = random.randrange(0,width)
    y = random.randrange(0,height)
    draw.arc((x,y,x+8,y+4),0,360,fill=rmdRGB())
    # 结束
    del draw
    import io
    buf = io.BytesIO()
    im.save(buf,'png')
    return HttpResponse(buf.getvalue(),'image/png')


def rmdRGB():
    c1 = random.randrange(0,255)
    c2 = random.randrange(0,255)
    c3 = random.randrange(0,255)

