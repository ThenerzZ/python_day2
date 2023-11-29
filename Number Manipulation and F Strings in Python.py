print(8/3) #wenn wir das as integer machen lässt er die nachstellen einfach weg -> output = 2
print(round(8 / 3)) #benutzen wird die round function so komnmt ein gerundetes ergebnis raus -> output = 3
print(round(8 / 3, 2)) #die 2 beduetet zu welcher stelle gerundet wird -> output 2.67

print(8 // 3) #floor divition macht es zu eiunem integer also output -> 2

#wenn wir eine variable speichern z.b.
score = 0
#und diese nun verrechenne  wollen können wir einerseits klassisch
#score = score + 1
#oder einfacher(verkürtzt)
score +=1
print(score) #output ->1

#f-strings

height = 1.8
score2 = 0
isWinning = True

print(f"your score is {score2}") #wenn wir ein f vor die "" setzte ist das ein f-String und wir können variablen einfügen ohne diese vorher zu einerm string machen zu müssen
print(f"your score is {score2}, your height is {height}, you are winning is {isWinning}")

