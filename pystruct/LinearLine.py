# 线性表


class LinearList:
    def __init__(self):
        pass
    """
    -----------------------------------------------------------------------------------------------
    ADT LineList
    -----------------------------------------------------------------------------------------------
    Base Class:
        有限元素的集合
    -----------------------------------------------------------------------------------------------
    Methods:
        empty() 判断是否为空
        size() 返回数组大小
        get(index) 返回线性表中索引为index的元素
        index_of(x) 返回线性表中第一次出现的x的索引，else return -1
        erase(index) 删除索引为index的元素
        insert(index, x) 把x插入线性表中索引为index的位置上，索引大于等于index的元素其索引加1
        output() 输出
    -----------------------------------------------------------------------------------------------
    Decribe:
        LineList作为一个父类存在，没有具体实现的方法，也不会有具体的数据对象。
    -----------------------------------------------------------------------------------------------
    """
    def empty(self) -> bool:
        pass

    def size(self) -> int:
        pass

    def get(self, index):
        pass

    def index_of(self, x) -> int:
        pass

    def erase(self, index) -> bool:
        pass

    def insert(self, index, x) -> bool:
        pass

    def output(self):
        pass




class ArrayList(LinearList):
    def __init__(self, element, array_list=None):
        super(ArrayList, self).__init__()
        if ~isinstance(element, list):
            print('element must be list')
            return 0
        self.element = element
        self.list_size = 0
        if array_list:
            if ~isinstance(array_list, ArrayList):
                print('Type Error!')
                return 0
            self.element = array_list.element
            self.list_size = array_list.size()

    """
    -----------------------------------------------------------------------------------------------
    Template ArrayList
    -----------------------------------------------------------------------------------------------
    Object:
        LinearList->ArrayList
        数组
    -----------------------------------------------------------------------------------------------
    Methods(From LinearList):
        empty() 判断是否为空
        size() 返回数组大小
        get(index) 返回线性表中索引为index的元素
        index_of(x) 返回线性表中第一次出现的x的索引，else return -1
        erase(index) 删除索引为index的元素
        insert(index, x) 把x插入线性表中索引为index的位置上，索引大于等于index的元素其索引加1
        output() 输出
        
    Other Methods:
        _check_index(index) 检查index是否合法
    -----------------------------------------------------------------------------------------------
    Members:
        element 存储线性表元素的一维数组
        list_size 所包含的元素个数
    -----------------------------------------------------------------------------------------------
    """

    def __iter__(self):
        return iter(self.element)

    def _check_index(self, index):
        if index < 0 or index >= self.size():
            raise Exception('请输入正确的index')
        else:
            return True

    def size(self):
        return self.list_size

    def __len__(self):
        self.size()

    def empty(self):
        if self.list_size == 0:
            return True
        else:
            return False

    def get(self, index):
        self._check_index(index)
        return self.element[index]

    def index_of(self, x):
        index = 0
        for i in self.element:
            if i == x:
                return index
            index += 1
        print("没有找到对应元素的index")
        return False

    def erase(self, index):
        self._check_index(index)
        self.element.pop(index)

    def insert(self, index, x):
        self._check_index(index)
        self.element.insert(index, x)

    def output(self):
        if self.size() == 0:
            print('EMPTY!')
        else:
            for i in self.element:
                print(i)

