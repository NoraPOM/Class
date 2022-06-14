#Program To_Do_List
#Autor Nora Orozco 
#Version 1.0
#Date 14 June 2022

from Item import Item
from User import User
from Cell import Cell

class To_Do_List:
    def __init__(self):
        self.items = []
                
    def add_item(self, item):
       items.append(selft.item)

    def delete_item(self, id_item):
        for i in self.items:
            if (i.get_id() ==  id_item):
                items.remove(i)
                
    def get_item(self, id_item):
        for i in self.items:
            if (i.get_id() == id_item):
                print("id -> " + i.id)
                print("description -> " + i.description)
                print("priority: " + i.priority)
                print("User -> " + i.assigned_to.name + i.assigned_to.astname)

    def show_item(self):
        for i in self.items:
            print("id:" + i.id)
            print("description: " + i.description)
            print("priority: " + i.priority)
            print("user name: " + i.assigned_to.name)
            print("user last_name: " + i.assigned_to.last_name) 

def main():

    if __name__ == "__main__":
        main()


    
