from House_book import House
Name = input("Enter your name:  ")
n = House(Name)
print("Welcome to the Hogwarts House Sorting Hat Quiz", Name)
print("Answer the following questions to find out which house you belong to:")
def main():
    print("Q1) Do you like Dawn or Dusk? ","\n","1) Dawn","2) Dusk")
    q1 = int(input("ans: 1 0r 2:"))
    print("Q2) when i am dead, I want people to remember me as: ","\n","1) The good","2) The great","3) The wise","4) The Bold")
    q2 = int(input("ans: 1,2,3,4:"))
    print("Q3) What kind of instrument most pleases your ear? ","\n","1) The Violin","2) The trumpet","3) The piano","4) The drum")
    q3 = int(input("ans: 1,2,3,4:"))

    Gryffindor = 0
    Ravenclaw = 0
    Hufflepuff = 0
    Slytherin = 0

    if q1 == 1:
     Gryffindor += 1
     Ravenclaw += 1
    elif q1 == 2:
     Hufflepuff += 1
     Slytherin += 1
    else:
     print("Wrong Input")

    if q2 == 1:
     Hufflepuff += 2
    elif q2 == 2:
     Slytherin += 2
    elif q2 == 3:
     Ravenclaw += 2
    elif q2 == 4:
     Gryffindor += 2
    else:
     print("Wring input")

    if q3 == 1:
     Slytherin += 4
    elif q3 == 2:
     Hufflepuff += 4
    elif q3 == 3:
     Ravenclaw += 4
    elif q3 == 4:
     Gryffindor += 4
    else:
     print("Wrong input")

    Houses = [Gryffindor, Ravenclaw, Hufflepuff, Slytherin]
    names =  ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
    i = 0
    for house in Houses:
     print(names[i], house)
     i += 1

    if Gryffindor > Ravenclaw:
     if Gryffindor > Hufflepuff:
        if Gryffindor > Slytherin:
         print("You Have been selected by the house: Gryffindor") 
         n.record("Gryffindor")
        else:
         print("You Have been selected bt the house: Slytherin")
         n.record("Slytherin")
     else:
        if Hufflepuff > Slytherin:
         print("You Have been selected by the house: Hufflepuff")
         n.record("Hufflepuff")
        else:
         print("You have been selected by the house: Slytherin")
         n.record("Slytherin")
    else:
     if Ravenclaw > Hufflepuff:
        if Ravenclaw > Slytherin:
         print("You have been selected by the house: Ravenclaw")
         n.record("Ravenclaw")
        else:
         print("you have been selected by the house: Slytherin")
         n.record("Slytherin")
     else:
        if Hufflepuff > Slytherin:
         print("you have been selected by the house: Hufflepuff")
         n.record("Hufflepuff")
        else:
         print("you have been selected by the house: Slytherin")
         n.record("Slytherin")

if Name := True:
  if __name__ == "__main__":
         main()