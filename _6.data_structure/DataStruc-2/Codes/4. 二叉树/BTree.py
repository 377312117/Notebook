# 二叉树的实现
# 二叉树结点类


class TreeNode:
	# 构造空白节点
    def __init__(self, data=None, left=None, right=None):
        self.elem = data # 存在数据元素
        self.l_child = left # 存放左子节点的链接域
        self.r_child = right # 存放右子节点的链接域


# 二叉树类
class Tree:
    # 创建空树
    def __init__(self):
        # 初始化根节点为空白节点
        self.root = TreeNode()
        # 存放不完整的节点的列表
        self.incomplete = []

    # 判空
    def is_empty(self):
        return self.root.elem is None

    # 添加结点
    def add(self, data):
        # 为新数据创建结点
        tmp = TreeNode(data)
        
        
        if self.is_empty():
			# 若为空树：
			# 直接到对根结点赋值新结点
            self.root = tmp
			# 维护不完整节点列表: 加入当前的根节点
            self.incomplete.append(self.root)
        else:
			# 若为非空树：
			# 添加新节点到子树不完整的结点(incomplete)
            first_incomplete = self.incomplete[0]
            if first_incomplete.l_child is None:
                # 左子节点为空：添加到左子节点处
                first_incomplete.l_child = tmp
				# 将新创建的节点放入不完整节点的列表中
                self.incomplete.append(first_incomplete.l_child)
            else:
                # 右子节点为空：添加到右子节点处
                first_incomplete.r_child = tmp
				# 将新创建的节点放到不完整节点列表中
                self.incomplete.append(first_incomplete.r_child)
				# 当前不完整节点first_incomplete已经包含左子节点和右子节点, 需要从不完整节点列表中提出
                self.incomplete.pop(0)

    # 先序遍历二叉树并显示
    def front_show(self, tree):
        if tree is None:
            # 遍历到最后一层结点
            return
		# 先打印根节点的元素
        print(tree.elem)
		# 递归遍历左子树
        self.front_show(tree.l_child)
		# 递归遍历右子树
        self.front_show(tree.r_child)

    # 中序遍历二叉树并显示
    def middle_show(self, tree):
        if tree is None:
            # 空树
            return
		# 先递归打印左子树的节点
        self.middle_show(tree.l_child)
		# 打印根节点的数据
        print(tree.elem)
		# 递归打印右子树的节点
        self.middle_show(tree.r_child)

    # 后序遍历二叉树并显示
    def post_show(self, tree):
        if tree is None:
            # 空树
            return
		# 递归打印左子树的节点
        self.post_show(tree.l_child)
		# 递归打印右子树的节点
        self.post_show(tree.r_child)
		# 打印根节点的数据
        print(tree.elem)

    # 广度优先遍历并显示
    def level_show(self):
        if self.root is None:
            # 空树
            return
        nodes = [] # 存放访问到的节点列表
        current = self.root
        nodes.append(current)
		# 从维护的节点列表中取出数据
        while nodes:  # nodes => [A]
			# 取出第一个元素并打印
            current = nodes.pop(0)  # A取出, nodes => [] 
            print(current.elem)
			# 判断当前取出节点是否存在左子节点,若存在,则追加到nodes列表中
            if current.l_child is not None:
                nodes.append(current.l_child) 
				# nodes => [B]
			# 判断当前取出节点是否存在右子节点,若存在,则追加到nodes列表中
            if current.r_child is not None:
                nodes.append(current.r_child)
				# nodes => [B C]

if __name__ == "__main__":
    # 产生10个数据放入二叉树中
    values = range(10)
    my_tree = Tree()
    for value in values:
        my_tree.add(value)
    # 遍历二叉树
    print("前序遍历")
    my_tree.front_show(my_tree.root)
    print("中序遍历")
    my_tree.middle_show(my_tree.root)
    print("后序遍历")
    my_tree.post_show(my_tree.root)
    print("广度优先遍历")
    my_tree.level_show()
