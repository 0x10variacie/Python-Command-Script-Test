# Python Script Test
# imports
import math
import time
import random
import os
import shutil
import functools
import threading
from multiprocessing import Process, cpu_count

#some functions go here
def introtext(itprompt):
    for x in itprompt:
        time.sleep(0.1)
        print (x,end="",flush=True)
    print("\n")
    return itprompt

def testfunc():
    print("My name is Function")
    func1 = "TEST"
    func1_times = 3
    print(func1*func1_times)

def testfunc1(varik):
    print("You said: " + varik)

def testfuncglob(name,from1,study):
    print("Your name is " + str(name) + " and you're from " + str(from1) + ", studying at " + str(study) + ".")

def operation(_1num,_2num):
    roo = _1num + _2num
    return roo

def orderfunc(ord1,ord2,ord3):
    print(ord1 + " " + ord2 + " and " + ord3 + ".")

def multiplication(*mulres):
    mlpl = 0
    mulres = list(mulres)
    mulres[0] = 0
    for index in mulres:
        mlpl *= index
    return mulres

def rodeo(**kwargs):
    print("Gonna catch "+kwargs['bull']+" at the lane(s) "+kwargs['lane'])
    print("Gonna catch ",end="_")
    for bull,lane in kwargs.items():
        print(lane,end="_")

#The script itself goes here
print ("Hello, my name is python test.py")
print ("you are durik btw =)")
print ("")
print ("-=PYTHON TEST=-")


block = input("Type the number from 0 to 10 or type NEXT to proceed to the next 10: ")
while block != ("NEXT") or block != ("next"):
    if block == str("0"):
        introtext("-•*Variables*•-")
        x = 600
        print (x)
        y = x + 40
        print (y)
        testvar1 = "Dysh!"
        print ("OOOOOO, A HUMAN!!! " +testvar1)
        break
    elif block == str("1"):
        introtext("-•*Input*•-")
        name_ = input ("name (please type smth): ")
        print (name_)
        _name = input ("Say smth to see magic!  input: ")
        print (_name.upper() + " - pper case")
        print (_name.lower() + " - lower case")
        print (_name.capitalize() + " - capitalize")
        print (str(_name.find("a")) + " - search through string")
        print (_name.replace("a","b") + " - replacement")
        break
    elif block == str("2"):
        introtext("-•*Range*•-")
        x = 1
        for x in range (1,20):
            print (x)
        break
    elif block == str("3"):
        introtext("-•*Mathematics*•-")
        mathnum = float(input("Enter the number: "))
        print (math.ceil(mathnum))
        print (math.floor(mathnum))
        print (abs(mathnum))
        print(str(float(pow(mathnum, 2))) + " is " + str(mathnum) + " to the power of 2!")
        print(str(float(math.sqrt(mathnum))) + " is a square root of " + str(mathnum))

        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("And now enter c: "))
        print(max(a,b,c))
        print(min(a,b,c))
        break
    elif block == str("4"):
        introtext("-•*String manipulation*•-")
        pie = "Iwannacutthepie!"
        print("The following phrase contains " + str(pie.count("")) + " letters.")
        piepart1 = pie[:4]
        piepart2 = pie[4:8]
        piepart3 = pie[8:12]
        piepart4 = pie[12:]
        print(str(piepart1) + " " + str(piepart2) + " " + str(piepart3) + " " + str(piepart4))
        pie1 = int(pie.count("") - 1)
        print("But it contains " + str(pie1) + " instead.")
        eip = pie[::-1]
        print("But in the parallel universe, it says '" + str(eip) + "'.")
        print("")
        world = "the world is living"
        print(str(world))
        slice = slice(3,-9)
        print(str(world[slice]))
        break
    elif block == str("5"):
        introtext("-•*IF statements*•-")
        number1 = int(input ("Gimme a number: "))
        if number1 >= 0 and number1 <= 50:
            print("Yes")
        else:
            print("No")

        if number1 < 25 or number1 > 100:
            print("OK")
        else:
            print("NOT OK")  

        #if number1 < 1000 not number1 > 1000:
            print ("fair enough")
        #else
            print("too much!!!")  
        break
    elif block == str("6"):
        introtext("-•*Loop*•-")
        zaloopa = input("Straight away speaking, if the condition for WHILE is value A equals value B, it will make a loop. Do you still want to proceed? ")
        if zaloopa == "y" or zaloopa == "yes":
            while 1==1:
                print("Great, now if you want to terminate this shitty loop, terminate this script RIGHT NOW!")
        elif zaloopa == "n" or zaloopa == "no":
            pass
        lena = ""
        while len(lena) == 0:
            lena = input("U cannot pass unless you say something: ")
        print ("Thanks for speaking out! This is why one should not be quiet!")
        for i in range(5):
            print(i)
        for i in range(5):
            print(i+1)
        for i in "This phrase is written letter-by-letter":
            print(i)
        for i in "This phrase is written letter-by-letter with 0.1 seconds delay":
            print(i)
            time.sleep(0.1)
        for i in "This phrase is written letter-by-letter with 0.1 seconds delay on a single line":
            time.sleep(0.1)
            print(i, end="",flush=True)
        print(".")
        print(":D")
        break
    elif block == str("7"):
        introtext("-•*Nested loops*•-")
        rows = int(input("Rows: "))
        columns = int(input("Columns: "))
        symbol = input("Symbol: ")
        for i in range(rows):
            for j in range(columns):
                print(symbol, end="")
                time.sleep(0.1)
            print()
        break
    elif block == str("8"):
        introtext("-•*Loop manipulation*•-")
        while True:
            name = input("Who are you?")
            if name != "":
                break
            elif name == "name":
                continue
            else:
                print("Alright, sorry for the inconvenience")
                pass
        break
    elif block == str("9"):
        introtext("-•*Sets*•-")
        print("We offer the following: ", end="")
        tlist = ["vodka","beer","tequila","wine"]
        print(tlist)
        chosen = int(input("What would you choose? Type a number: "))
        if chosen <= 1 or chosen >= 4:
            tlist.pop(chosen)
            print(tlist)
            print("You're a burglar!")
        print("")
        moma = {"child", "toddler", "enfant"}
        print("Mom A has: " + str(moma))
        momb = {"teen", "kid", "son"}
        print ("Mom B has got: " + str(momb))
        moma.add("adopted")
        print(moma)
        momb.remove("kid")
        print(momb)
        print("Mom B's children went home after they found out a mysterious new")
        momb.clear()
        print(str(momb))
        print("")
        set1 = {"1","2","3","4"}
        set2 = {"4","5","6","7"}
        print("Set 1 is "+ str(set1))
        print("Set 2 is "+ str(set2))
        set1.add("0")
        print(str(set1))
        set2.remove("7")
        print(str(set))
        print("Now getting rid of the set 2...")
        set2.clear()
        print(str(set2) + " - the set 2 is now cleared")
        set2.update(set1)
        print(str(set1) + " and " + str(set2))
        set1.update(set2)
        print(str(set1) + " and " + str(set2))
        print("That's it with set example!")
        break 
    elif block == str("10"):
        introtext("-•*DICTIONARY*•-")
        time.sleep(0.5)
        print("No, it's not about language dictionaries ;P")
        time.sleep(0.5)
        continents={'Europe':'Russia','Asia':'China','Africa':'South Africa','America':'USA'}
        print("Given the following: "+str(continents))
        search = ""
        while search == "":
            search = input("Gimme a continent: ")
        print(continents.get(search))

        print(continents.keys())
        print(continents.values())
        print(continents.items())
        print("Hence:")
        for key,value in continents.items():
            print(key,value)
            time.sleep(0.5)
        newcountry = str(input("Give me a country located in Australia: "))
        if newcountry != "Australia" or newcountry != "New Zealand":
            continents.update({'Australia':str(newcountry)})
            for key,value in continents.items():
                print(key,value)
                time.sleep(0.5)
        else:
            print("Either you don't know Australia continent well or I know only either Australia or New Zealand. Sorry mate!")
        print("Wait a minute...")
        time.sleep(2)
        print("The countries are a part of BRICS except two...")
        time.sleep(2)
        print("Time to fix it!")
        continents.update({'America':'Brazil'})
        continents.pop('Australia')
        for key,value in continents.items():
                print(key,value)
                time.sleep(0.5)
        print("Now it should make sense even though Asia has 2 members of BRICS!")        
        break
    elif block == "HELP" or block == "help":
        help("modules")
        break
    elif block == "NEXT" or block == "next":
        print ("OK!")
        break
    else:
        print("Invalid choice...")
        break
        
block = input("Type the number from 11 to 20 or type NEXT to proceed to the next 10: ")
while block != ("NEXT"):
    if block == "11":
        introtext("-•*String manipulation*•-")
        word1 = input("Type something here (min 5 characters): ")
        if len(word1) >= 5:
           word1_up = word1[:5].upper()
        else:
            continue

        if len(word1) > 10:
            word1_down = word1[5:10].lower()
            word1_last = word1[10:][-1]

            print(str(word1_up))
            print(str(word1_down))
            print(str(word1_last))
            print(str(word1))
            print(str(word1_up)+str(word1_down)+str(word1_last))
        else:
            word1_up = word1[:5].upper()
            word1_last = word1[:][-1]
            print(str(word1_up)+str(word1_last))
        time.sleep(0.5)
        break
    elif block == str("12"):
        introtext("-•*Function*•-")
        print("Look up the code to see why I wrote this!")
        testfunc()
        varik = input("Tell me something: ")
        testfunc1(varik)
        print("")
        print("Real life example goes here:")
        name = ""
        from1 = ""
        study = ""
        while len(name) == 0:
            name = input("Hey there, what's your name? ")
        while len(from1) == 0:
            from1 = input("Where are you from? ")
        while len(study) == 0:
            study = input("Where do you study? ")
        testfuncglob(name,from1,study)
        print("")
        print("Function with return")
        _1num = float(input("Gimme a number: "))
        _2num = float(input("Gimme another one: "))
        roo = operation(_1num, _2num)
        print("It's " + str(float(roo)) +".")
        print("")
        orderfunc(ord1="lol",ord3="lmao",ord2="rofl")
        break
    elif block == str("13"):
        introtext("-•*NESTED FUNCTION CALLS*•-")
        time.sleep(0.3)
        number2 = round(abs(float(input("Gimme some complicated number that can be round and absolute in the end: "))))
        print("You got " + str(number2) + ".")
        break
    elif block == str("14"):
        introtext("-•* *args *•-")
        print(multiplication(1,2,3,4,5,6,7,8,9,0))
        rodeo(bull="Joe",lane="5")
        print("\n")
        break
    elif block == str("15"):
        introtext("-•*String format*•-")
        drink1 = "vodka"
        bodypart = "vein"
        print("I feel {} flowing through my {}s.".format(drink1,bodypart))
        print("I feel {1} flowing through my {0}s.".format(drink1,bodypart))
        print("I feel {0} flowing through my {1}s.".format(drink1,bodypart))
        print("I feel {drink1} flowing through my {bodypart}s.".format(drink1="tequila",bodypart="urine"))
        print("I feel {bodypart} flowing through my {drink1}s.".format(drink1="tequila",bodypart="urine"))
        print("I feel {bodypart} flowing through my {bodypart}s.".format(drink1="tequila",bodypart="urine"))
        print("I feel {drink1} flowing through my {drink1}s.".format(drink1="tequila",bodypart="urine"))
        text1 = "I drink {} while my {}s are cold at the sun!"
        print(text1.format(drink1,bodypart))
        print(text1.format(bodypart,drink1))
        drunkman = "Herych"
        print("And here came my friend {:10}".format(drunkman))
        print("And here came my friend {:10}. We buhali zayebis'.".format(drunkman))
        print("And here came my friend... {drunkman:40}. We buhali zayebis.".format(drunkman="Wait, where the hell he is???"))
        time.sleep(0.5)
        print("\nRemember kids: don't f*cking drink a lot of alcohol!!")
        time.sleep(0.5)
        experience = math.exp(5)
        print("{:.2f}".format(experience))
        experience = 5500
        print("{:,}".format(experience))
        print("{:b}".format(experience))
        print("{:o}".format(experience))
        print("{:X}".format(experience))
        print("{:e}".format(experience))
        print("{:E}".format(experience))
        print("So do numbers work!")
        break
    elif block == str("16"):
        introtext("-•*Random*•-")
        x = random.randint(1,10)
        print(x)
        y = random.random()
        print(y*5)
        zlist = ['lol','rofl','lmao']
        z = random.choice(zlist)
        print(z)
        z = random.choice(zlist)
        print(z)
        z = random.choice(zlist)
        print(z)
        random.shuffle(zlist)
        for x in zlist:
            print(x)
            print(zlist)
        break
    elif block == str("17"):
        introtext("-•*Exception*•-")
        try:
            drink2 = input("You may offer me any drink, whatever you'd like to, but don't you dare offer me vodka! ")
            print("OMG I LIKE {}".format(drink2))
        except ValueError:
            print("I TOLD YOU NOT TO OFFER VODKA!!!")
        finally:
            print("You're still durik nya")
        break
    elif block == str("18"):
        introtext("-•*File manipulation*•-")
        introtext("Disclaimer: the following example manipulates your workplace directory!")
        print("Hi, my name is h4xor\n\n")
        time.sleep(2)
        print("aight, bad joke\n\n")
        loc = input("1. Open any window on your PC;\n1.1.Or you can manually type the location\n2. Copy and paste the location.\n3. You can even run this script while running this script!\n4. make sure that \\ or // is written twice as \n occurs! Location: ")
        if os.path.exists(loc):
            print("Yo, I can see it!")
            if os.path.isfile(loc):
                print("It's a file.")
            elif os.path.isdir(loc):
                print("It's a dir.")
        else:
            print ("Nah, I can't see it.")

        with open('texttxt.txt') as file: #open
            print(file.read()) #read
            print(file.closed)
        with open('texttxt.txt','a') as file:
            file.write(" Now open the file and take a look ;)\n") #write
        print("Some magic goes...")
        shutil.copyfile('texttxt.txt','blol.txt') #copy
        shutil.copyfile('texttxt.txt','gonnamoveit.txt')
        source = "gonnamoveit.txt"
        movedir = "/Users/pankoles/Documents/Prog/movefolder/"
        try:
            if os.path.exists(movedir):
                print("already there ;)")
            else:
                os.replace(source,movedir) #move
                print("Moved, check the directory NOW!")
        except FileNotFoundError:
            print("{} not found".format(source))
        time.sleep(5)
        print("OK, gonna delete some bytes. Removing file...")
        os.remove('gonnamoveit.txt')
        time.sleep(4)
        os.rmdir(movedir) #remove directory
        print("Done!")

        break
    elif block == str("19"):
        introtext("-•*Modules*•-")
        import testmodule
        moduleplay = input("Would you like to call a module? (y,n) ")
        moduleplay_yn = ['y','n']
        while True:
            try:
                if moduleplay == 'y':
                    testmodule.modulefunc()
                    break
                elif moduleplay == 'n':
                    break 
                else:
                    print("Yes or No only ;)")
            except ValueError:
                print("Yes or No only ;)")
            finally:
                print("So does module work!")
                break
        print("Thank you for your attention to the block 19! For classes, check the block no. 20.")
        break
    elif block == str("20"):
        introtext("-•*Classes*•-")
        from testclassmodule1 import TestClass as tc
        tc.testclassact()
        tc.testclassvarsact()
        print("Tip: make sure you saved classes and module as separate files before testing your script!")
        break
    elif block == "HELP" or block == "help":
        help("modules")
        break
    elif block == str("NEXT") or block == str("next"):
        print ("OK!")
        break
    else:
        print("Invalid choice...")
        break

block = input("Type the number from 21 to 30 or type NEXT to proceed to the next 10: ")
while block != ("NEXT"):
    if block == "21":
        introtext("-•*Classes (continuation)*•-")
        from toworkwith import toworkwith as tww
        tww.moduletoworkwith()
        break
    elif block == str("22"):
        introtext("-•*Inheritance*•-")
        class Book:
            isread = False
            genre = ["fiction", "schoolbook", "storytale"]

            def reading(self):
                print("A book is taken")
                return self
            
            def returning(self):
                print("The book is returned")
                return self

        class Fiction(Book):
            Genre = genre[0]
            pass
        class SBook(Book):
            Genre = genre[1]
            pass
        class STBook(Book):
            Genre = genre[2]
            pass

        fiction_book = Fiction()
        s_book = SBook()
        st_book = STBook()

        print(fiction_book.isread)
        print(fiction_book.Genre)
        print(fiction_book.reading)
        print(fiction_book.returning)
        print(s_book.isread)
        print(s_book.Genre)
        print(s_book.reading)
        print(s_book.returning)
        print(st_book.isread)
        print(st_book.Genre)
        print(st_book.reading)
        print(st_book.returning)
        break
    elif block == str("23"):
        introtext("-•*Super*•-")
        class Circum:
            def __init__(self, radi):
                self.radi = radi

            def carea(self):
                return 2*3.1415926*self.radi
        class Sphere(Circum):
            def __init__(self, radi):
                super().__init__(radi)

            def sarea(self):
                return 3.1415926*pow(self.radi,2) 
        class Ellipse(Circum):
            def __init__(self,radi,strval):
                super().__init__(radi)
                self.strval = strval
            def sparea(self):
                return 3.1415926*pow(self.radi,2)*self.strval

        Circumarea = Circum(1)
        Spherarea = Sphere(1)
        Ellipsarea = Ellipse(1,2)

        print(Circumarea.carea())
        print(Spherarea.sarea())
        print(Ellipsarea.sparea())
        
        break
    elif block == str("24"):
        introtext("-•*Function as a variable*•-")
        def funcvab():
            print ("The following function is playing role of variable")
        funcvab()
        funcvab_perf = funcvab
        funcvab_perf()

        print("Command can also play a role in the function")
        shout = print
        shout("DYDYSH!!!")
        break
    elif block == str("25"):
        introtext("-•*Walrus*•-")
        try:
            print (viruscheck = "ruilt")
        except TypeError:
            print("Walrus operator is required instead of =")
        finally:
            print(viruscheck := "rulit")
        print("Look up the code to see why the viruscheck variable works the other way.")

        walrusprompt = list()
        while walruselement := input("Create the Walrus List! Type: ") != "stop":
            walrusprompt.append(walruselement)
        for x in walrusprompt:
            print (x)
            time.sleep(0.05)
        print("and so does walrus work!")
        break
    elif block == str("26"):
        introtext("-•*Lambda λ*•-")
        compoundtext = lambda textfr1, textfr2, textfr3: textfr1+" "+textfr2+" "+textfr3+"."
        print (compoundtext("This text", "is written with", "lambda function"))
        for i in "Look up the code to see how it works!\n":
            time.sleep(0.05)
            print (i,end="",flush=True)
        break
    elif block == str("27"):
        introtext("-•*Map*•-")
        print("given the following map")
        maplist = [
            ("object 1 ", 1),
            ("object 2 ", 2),
            ("object 3 ", 3),
            ("object 4 ", 4)]
        print("By the way, it's also a good example of multiline prompt like this!")
        mapshow = lambda mapdata: (mapdata[0]*int(mapdata[1]))
        mapout = list(map(mapshow,maplist))
        for i in mapout:
            time.sleep(0.05)
            print (i,end="\n",flush=True)
        break
    elif block == str("28"):
        introtext("-•*Filter*•-")
        print("given the following map")
        filterlist = [
            ("object 1 ", 5),
            ("object 2 ", 10),
            ("object 3 ", 15),
            ("object 4 ", 20)]
        for i in filterlist:
            time.sleep(0.01)
            print (i,end="\n",flush=True)
        time.sleep(2)
        print("By the way, it's also a good example of multiline prompt like this!")
        filtershow = lambda filterdata: (filterdata[1] >= 10)
        filterout = list(filter(filtershow,filterlist))
        for i in filterout:
            time.sleep(0.05)
            print (i[0],end="\n",flush=True)
        print("Only these elements were displayed because...")
        time.sleep(0.5)
        for i in filterout:
            time.sleep(0.05)
            print (i[1],end="\n",flush=True)
        print("which hence gives us...")
        time.sleep(0.5)
        for i in filterout:
            time.sleep(0.05)
            print(str(i[0])+" "+str(i[1])+".",end="\n",flush=True)
        break
    elif block == str("29"):
        introtext("-•*Reduction*•-")
        print("functools function is required")
        elist = ["1","2","3","4","5","6","7","8","9","10"]
        eorder = functools.reduce(lambda x, y:x + y,elist)
        print(elist)
        for i in elist:
            time.sleep(0.01)
            print(i,end="\n",flush=True)
        elist1 = [1,2,3,4,5,6,7,8,9,10]
        for i in elist1:
            print (str(i),end="\n",flush=True)
            time.sleep(0.01)
        eresult = str(functools.reduce(lambda x, y: x * y,elist1))
        print ("So we've got "+eresult+".")
        break
    elif block == str("30"):
        introtext("-•*Comprehension*•-")
        print("List")
        time.sleep(2)
        triples = [i * 3 for i in range(0,50)]
        for i in triples:
            print (i,end=", ",flush=True)
            time.sleep(0.025)
        print("manual end of the list.")
        numstofilter = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        filterednums = list(filter(lambda x: x/2<=6,numstofilter))
        print("Given that x divided by 2 is less or equal to 6...")
        for i in filterednums:
            print(i,end=", ", flush=True)
            time.sleep(0.025)
        print("manual end of the list.")
        print("or")
        time.sleep(1)
        filterednums = [i for i in numstofilter if i/2<=6]
        for i in filterednums:
            print(i,end=", ", flush=True)
            time.sleep(0.025)
        print("manual end of the list.\nIn this case, x isn't used but i unless x is substituted for the index.")
        filterednums = [i if i/2<=6 else "NOPE" for i in numstofilter]
        for i in filterednums:
            print(i,end=", ", flush=True)
            time.sleep(0.025)
        print("manual end of the list.\nIn this case, the condition is applied.")
        for i in "\n . . . \n":
            time.sleep(0.05)
            print (i,end="",flush=True)
        print("Dictionary")
        time.sleep(2)
        comdic = {
            "Object 1":5,
            "Object 2":10,
            "Object 3":15,
            "Object 4":20,
            "Object 5":25,
            }
        comdicop = {key: value for (key,value) in comdic.items()}
        for i in comdicop:
            time.sleep(0.05)
            print(i,end=", ", flush=True)
        print("manual end of the list.")
        break
    elif block == "HELP" or block == "help":
        help("modules")
        break
    elif block == str("NEXT") or block == str("next"):
        print ("OK!")
        break
    else:
        print("Invalid choice...")
        break

block = input("Type the number from 31 to 40 or type NEXT to proceed to the next 10: ")
while block != ("NEXT"):
    if block == str("31"):
        introtext("-•*ZIP*•-")
        print("No, not archives ;P")
        time.sleep(1.5)
        listx = ["element1","element2","element3"]
        listy = ("always","brackets","only")
        listxy = zip(listx,listy)
        for i,j in listxy:
            print(i+" "+j)
            time.sleep(0.35)
        print("Tip: ",end="")
        for i in "square brackets for the first list and round brackets for the second list ONLY!!!\n":
            time.sleep(0.025)
            print (i,end="",flush=True)
        print("Yet it's not over yet!")
        time.sleep(1.5)
        for i in "You can use more than 2 lists!\n":
            time.sleep(0.25)
            print (i,end="",flush=True)
        listz = ["more","than","two"]
        listxyz = zip(listx,listy,listz)
        for i,j,k in listxyz:
            time.sleep(0.35)
            print(i+" "+j+" "+k,end="\n",flush=True)
        break
    elif block == str("32"):
        introtext("-•*Time*•-")
        print("You may be already familiar with...",end="")
        time.sleep(1)
        print(" delay.\n")
        time.sleep(1)
        print("Today is "+str(time.time()))
        time.sleep(1)
        print("Today is "+str(time.time()))
        time.sleep(1)
        print("Today should be "+time.ctime(time.time()))
        time.sleep(1)
        ltime = time.localtime()
        print("Now for real: the time is "+str(ltime))
        ltime1 = time.strftime("%B %d %Y %H:%M:%S",ltime)
        print("Today is "+ltime1)
        for i in range(1,15):
            time.sleep(1)
            print(ltime1)
            i = i + 1

        def timeloop():
            tloop = time.strftime("%B %d %Y %H:%M:%S",time.localtime())
            print(tloop)
            time.sleep(1)

        for i in range(0,20):
            timeloop()
            i = i + 1

        ttuple = (1999,11,23,12,00,00,00,00,00)
        tstring = time.asctime(ttuple)
        tstring1 = time.mktime(ttuple)
        print("I was born on "+tstring)
        print("in other way, "+str(tstring1))
        break
    elif block == str("33"):
        introtext("-•*Multithreading*•-")
        print(threading.active_count())
        print(threading.enumerate())
        def thread1():
            for i in "Here goes the first thread\n":
                time.sleep(0.1)
                print (i,end="",flush=True)
        def thread2():
            for i in "Here goes the second thread\n":
                time.sleep(0.2)
                print (i,end="",flush=True)
        def thread3():
            for i in "Here goes the third thread\n":
                time.sleep(0.3)
                print (i,end="",flush=True)
        thread1()
        time.sleep(1)
        thread2()
        time.sleep(2)
        thread3()
        time.sleep(3)
        print(threading.active_count())
        print(threading.enumerate())
        simul1 = threading.Thread(target=thread1)
        simul1.start()
        simul2 = threading.Thread(target=thread2)
        simul2.start()
        simul3 = threading.Thread(target=thread3)
        simul3.start()
        print(threading.active_count())
        print(threading.enumerate())
        def thread11():
            print ("Here goes the first thread")
        def thread21():
            print ("Here goes the second thread")
        def thread31():
            print ("Here goes the third thread")
        simul11 = threading.Thread(target=thread11)
        simul11.start()
        simul21 = threading.Thread(target=thread21)
        simul21.start()
        simul31 = threading.Thread(target=thread31)
        simul31.start()
        print(threading.active_count())
        print(threading.enumerate())
        print(time.perf_counter())
        def thread12():
            print ("Here goes the first thread")
        def thread22():
            print ("Here goes the second thread")
        def thread32():
            print ("Here goes the third thread")
        simul12 = threading.Thread(target=thread12)
        simul12.start()
        simul22 = threading.Thread(target=thread22)
        simul22.start()
        simul22.join()
        simul32 = threading.Thread(target=thread32)
        simul32.start()
        simul32.join()
        print(threading.active_count())
        print(threading.enumerate())
        print(time.perf_counter())
        break
    elif block == str("34"):
        introtext("-•*DAEMON*•-")
        def intimer():
            print()
            timcount = 0
            while True:
                time.sleep(1)
                timcount += 1
                print("This script is running for "+str(timcount)+" seconds")
        intx = threading.Thread(target=intimer, daemon=True)
        intx.start()

        termination = input("Let's exit by pressing Enter!")
        break
    elif block == str("35"):
        introtext("-•*Multiprocessing*•-")
        def mpcounter(numer):
            mpcount = 0
            while mpcount < numer:
                mpcount += 1
        mprocess = Process(target=mpcounter, args=(500000,))
        mprocess.start()
        print("mprocess started")
        mprocess.join()
        print("mprocess joined")
        print("the multiprocessing is currently active")
        print("Done in "+str(time.perf_counter()))
        break

    elif block == str("NEXT") or block == str("next"):
        print ("OK!")
        break
    else:
        print("Invalid choice...")
        break
print(
    "This is the entire script for the console test for Python.\n"
    "Link to the video I used for this script is https://www.youtube.com/watch?v=XKHEtdqhLK8 (YouTube channel Bro Code)\n"
    "Credits to this dude:)\n"
    "Written by 0x10variacie\n")

# print ("What if I divide by 0...?")
# nulik = 1 / 0
# print (nulik)
# print ("Oh shit")

# if (x <= 50)
# type (x)
# else
# type ("lol")

#entry = type ("Type - ")
#print (entry)