from pystruct.LinearLine import LinearList


class ChainNode:
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next
        # self._check_node()

    def _check_node(self):
        if ~isinstance(self.next, ChainNode):
            self.next = None
            raise Exception('Node Type Error!')


class Chain(LinearList):
    def __init__(self, arraylist=None):
        self.first_node = ChainNode()
        self.list_size = 0
        super(Chain, self).__init__()
        if arraylist:
            if ~isinstance(arraylist, Chain):
                raise Exception('Type Error!')
            self.first_node = ChainNode(arraylist.first_node)
            self.list_size = arraylist.list_size
            temp_node = self.first_node
            source_node = arraylist.first_node
            source_node = source_node.next
            while source_node:
                temp_node.next = ChainNode(source_node.element)
                temp_node = temp_node.next
                source_node = source_node.next

    """
    -----------------------------------------------------------------------------------------------
    Template Chain
    -----------------------------------------------------------------------------------------------
    Object:
        LinearLine->Chain
        单向链表
    -----------------------------------------------------------------------------------------------
    Methods(From LinearLine):
        empty() 判断是否为空
        size() 返回数组大小
        get(index) 返回线性表中索引为index的元素
        index_of(x) 返回线性表中第一次出现的x的索引，else return -1
        erase(index) 删除索引为index的元素
        insert(index, x) 把x插入线性表中索引为index的位置上，索引大于等于index的元素其索引加1
        output(end=' ') 输出
        
    Other Methods:
        _check_index(index)
        add(element)
        print_info(info=False)
    -----------------------------------------------------------------------------------------------
    Members:
        first_node -> ChainNode
        list_size -> int
    -----------------------------------------------------------------------------------------------
    """

    def _check_index(self, index):
        if index < 0 or index >= self.list_size:
            raise Exception('Size Error!')

    def print_info(self, info=False):
        if self.list_size == 0:
            print('this is a empty Chain')
            return 0
        print('<first_node>:' + str(self.first_node))
        print('<first_node.element>:' + str(self.first_node.element))
        print('<first_node.next>:' + str(self.first_node.next))
        print('<chain size>:' + str(self.size()))
        if info:
            index = 0
            n = self.first_node
            while n.element:
                print('<node:' + str(index) + ', self:' + str(n) + ', element:' + str(n.element) + ', next:' + str(n.next) + '>')
                n = n.next
                index += 1

    def empty(self) -> bool:
        return self.list_size == 0

    def size(self) -> int:
        return self.list_size

    def get(self, index):
        self._check_index(index)
        temp = 0
        ele_n = self.first_node
        while temp != index:
            ele_n = ele_n.next
            temp += 1
        return ele_n.element

    def add(self, element):
        if self.first_node.element is None:
            self.first_node = ChainNode(element.element, next=None)
        else:
            self.first_node = ChainNode(element.element, self.first_node)
            self.list_size += 1

    def index_of(self, x):
        index = 0
        n = self.first_node
        while n.element:
            if n.element == x:
                break
            index += 1
            n = n.next
        if ~n.element:
            print("can\'t find index, return None")
            return None
        return index

    def erase(self, index):
        self._check_index(index)
        if index == 0:
            self.first_node = self.first_node.next
            return 1
        temp = 0
        n = self.first_node
        while temp != index - 1:
            temp += 1
            n = n.next
        delate_node = n.next
        n = n.next.next
        del(delate_node)

    def output(self, end=' '):
        if self.list_size == 0:
            print('it is empty!')
            return 0
        n = self.first_node
        while n.element:
            print(n.element, end=end)
            n = n.next
        print('\n')


if __name__ == '__main__':
    l = []
    res = Chain()
    for i in range(10):
        l.append(ChainNode(element=i))
        res.add(l[i])
    res.output()
    res.print_info(info=True)
    print(res.index_of(11))
