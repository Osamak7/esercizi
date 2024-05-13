        

class Room:
    def __init__(self, id :str , piano :int , Posti_a_sedere : int) -> None:
        self.id :str =id
        self.piano :int =piano
        self.Posti_a_sedere :int =Posti_a_sedere
    def get_num_floors(self):
        pass
    def add_room(self,room):
        pass

class Building:
    def __init__(self , name:str ,addres:str , stanze:list=[]) -> None:
        self.name=name
        self.addres=addres
        self.stanze:list[stanze]=stanze