class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    print("New student details:")

    def change_name (self, name):
        self.name = name
        print (self.name) 

    def change_age (self, age):
        self.age = age
        print (self.age)  

    def add_track (self, tracks):
        self.tracks.append(tracks)
        print ("Track is", self.tracks)

    def get_score (self, score):
        self.score = score
        print (self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(99.34)
