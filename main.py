#  Реализуем класс Stack со следующими методами isEmpty, push, pop, peek, size
class Stack:
    def __init__(self):
        self.items = []

    # isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        return self.items == []

    # push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self, item):
        self.items.append(item)

    # pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        return self.items.pop()

    # peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        return self.items[len(self.items) - 1]

    # size - возвращает количество элементов в стеке.
    def size(self):
        return len(self.items)


#  Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок.
#  Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий,
#  и пары скобок правильно вложены друг в друга.
def couples(arg):
    my_stack = Stack()
    for i in arg:
        if i in ["(", "{", "["]:
            my_stack.push(i)
        else:
            if my_stack.isEmpty():
                my_stack.push(i)
                break
            if my_stack.peek() + i in ["()", "[]", "{}"]:
                my_stack.pop()
            else:
                break

    if my_stack.isEmpty():
        print("Сбалансированно")
    else:
        print("Несбалансированно")


my_str = "[([])((([[[]]])))]{()}"

if len(my_str) % 2 == 0:
    couples(my_str)
else:
    print("Несбалансированно")
