# 单向链表的实现

# 链接节点
# 构造函数



# 链表类
class SLink:
    # 创建空链表
    def __init__(self):
        self._head = None
    # 判空
    def is_empty(self):
        return self._head == None
    
    # 遍历显示
    def show(self):
        # 获取第一个链表节点
        cur = self._head
        # 若节点为空时结束遍历
        while cur != None:
            print(cur._elem)
            # 将当前的节点后移一位
            cur = cur._next
    
    def add(self,elem):
        # 创建新节点
        tmp = Node(elem)
        #  新节点插入首部
        tmp._next = self._head
        # 更改链表首结点
        self._head = tmp

    # 删除链表中元素
    def delete(self,data):
        # 两个变量存放遍历时前后两个元素的结点
        cur,pre = self._head,None
        found = False
        while not found and (cur != None):
            if cur._elem == data:
                # 找到数据
                # 更改标志位found
                found = True
                if pre == None:
                    self._head
