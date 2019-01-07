from bs4 import BeautifulSoup


html = '''
    <div class="test">雄霸</div>
    <div class="test">聂风</div>
    <div class="test2">
        <span>步惊云</span>
    </div>
'''

soup = BeautifulSoup(html,'lxml')


rLsit = soup.find_all('div',{"class":"test"})
print(rLsit)

for r in rLsit:
    # string属性只能获取当前节点内文本内容
    # 能获取当前节点所有的文本内容,包括子节点的文本内容
    print(r.get_text())
