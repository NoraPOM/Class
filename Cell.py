#Program Cell
#Autor Nora Orozco 
#Version 1.0
#Date 14 June 2022

class Cell:

    def __init__(self, purpose, leader, creation_date):
        self.purpose = purpose
        self.leader = leader
        self.creation_date = creation_date

    def get_purpose(self):
        return self.purpose

    def set_purpose(self, purpose):
        self.purpose = purpose
    
    def get_leader(self):
        return self.leader

    def set_leader(self, leader):
        self.leader = leader
    
