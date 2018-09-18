# class Employee():
#     raiseAmount = 1.05
#
#     def __init__(self,first,surname,salary):
#         self.first = first
#         self.surname = surname
#         self.salary = salary
#         self.email = first + "" + surname + "@PythonABC.com"
#
#     def infoSummary(self):
#         return "{}, {}, {}".format(self.first + " " + self.surname, self.salary,self.email)
#
#     def raiseSalary(self):
#         self.salary = self.salary * Employee.raiseAmount
#
# employee1 = Employee("Harry", "Potter",4000)
# employee2 = Employee("Bilbo", "Baggins",6000)
# employee3 = Employee("Mark", "Twain",8000)
# employee4 = Employee("Julius", "Caesar",12000)
#
# print(employee1.infoSummary())
# print(employee2.infoSummary())
#
# employee1.raiseSalary()
# print(employee1.infoSummary())
# print(employee2.infoSummary())

class Node(object):
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None
    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return

