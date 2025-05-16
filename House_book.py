class House:
    def __init__(self,name):
        self.name = name
        self.house = []
    def record(self,selected):
        self.house.append(selected)
        with open(r"C:\Users\Karan\Desktop\python_practice\HarryPotters_Game\Records.txt","a")as f:
            f.write(f"{self.name}:{selected}\n")


