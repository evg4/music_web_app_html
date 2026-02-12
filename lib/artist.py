class Artist:
    def __init__(self, id, name, genre):
        self.id = id
        self.name = name
        self.genre = genre

    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__