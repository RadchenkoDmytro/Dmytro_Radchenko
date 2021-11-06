import math

#TASK - 1
def FilterList(list):
    return [i for i in list if isinstance(i, int)]

#TASK - 2
def FirstNonRepeatingLetter(string):
    lowString = string.lower() 
    for ch in lowString:
        if(lowString.count(ch)==1):
            return string[lowString.index(ch)]
    return "None"

#TASK - 3
def DigitalRoot(number):
    result = sum([int(char) for char in str(number)])
    return result if result < 10 else DigitalRoot(result)

#TASK - 4
#Faster but less clear function
def PairsNumber(array, target):
    count = 0
    array.sort()
    for step in array:
        if not step < target/2:
            break
        count += array.count(target-step)
    if(target/2 ==(int)(target/2) and array.count(target/2)>1):
            count += int(math.factorial(array.count(step))/2/math.factorial(array.count(step)-2))
    return count

#A clearer but slower function
def PairsNumber1(array, target):
    return sum([sum([1 for y in array[i+1:] if x + y == target]) for i, x in enumerate(array)])

#TASK - 5
def FriendsList (string):
    list = string.upper().split(";")
    list = [list[item].split(":")[::-1] for item in range(len(list))]
    list.sort()
    return ''.join([("(" + list[i][0] + ", " + list[i][1] + ")") for i in range(len(list))])

#EXTRA TASK - 1
def NextBigger(number):
    number = str(number)
    for i in range(2, len(number)+1):
        tail = number[-i:]
        biggerDigits = [item for item in tail if item > tail[0]]
        if len(biggerDigits) == 0:
            continue
        minimum = min(biggerDigits)
        tail = tail.replace(minimum,"",1)
        tail = ''.join(sorted(tail))
        tail = minimum + tail
        if(tail != ""): 
            return int(number[0:-i]+tail)
    return -1

#EXTRA TASK - 2
def IPv4(bitNumber):
    return '.'.join([str((bitNumber & (255 << i*8)) >> i*8) for i in reversed(range(4))])


print("First task:")
print("Filter the list: [1, 2, 'a', 'b'].")
print("Result:",FilterList([1, 2, 'a', 'b'])) 
print("\nFilter the list: [1, 'a', 'b', 0, 15].")
print("Result:",FilterList([1, 'a', 'b', 0, 15])) 
print("\nFilter the list: [1, 2, 'aasf', '1', '123', 123].")
print("Result:",FilterList([1, 2, 'aasf', '1', '123', 123])) 

print("\n\nSecond task")
print("Search for the first unique character in the string: sTress")
print("Result:", FirstNonRepeatingLetter("sTress"))
print("\nSearch for the first unique character in the string: aann")
print("Result:", FirstNonRepeatingLetter("aann"))
print("\nSearch for the first unique character in the string: letetelf")
print("Result:", FirstNonRepeatingLetter("letetelf"))

print("\n\nThird task")
print("Digital root of number 16.")
print("Result:",DigitalRoot(16)) 
print("\nDigital root of number 942.")
print("Result:",DigitalRoot(942)) 
print("\nDigital root of number 132189.")
print("Result:",DigitalRoot(132189)) 
print("\nDigital root of number 132189.")
print("Result:",DigitalRoot(493193)) 

print("\n\nFourth task")
print("Count the number of pairs for the array [1,3,6,2,2,0,4,5] and the target 6.")
print("Result:",PairsNumber([1,3,6,2,2,0,4,5], 6)) 
print("Count the number of pairs for the array [9,8,7,6,6,5,5,5,5,4,3,2,1,5,7,3] and the target 10.")
print("Result:",PairsNumber([9,8,7,6,6,5,5,5,5,4,3,2,1,5,7,3], 10)) 

print("\n\nFifth task")
print("Make a list of friends for Den's party from notes: Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill")
print(FriendsList("Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))
print("\nMake a list of friends for Den's party from notes: Stiven:Brown;Fred:Afleck;Britnie:Felton;Betty:Kollins;Oscar:Queen;Reichel:Brown;Stiven:Afleck")
print(FriendsList("Stiven:Brown;Fred:Afleck;Britnie:Felton;Betty:Kollins;Oscar:Queen;Reichel:Brown;Stiven:Afleck"))

print("\n\nSixth task")
print("Search next bigger for number: 12")
print("Result", NextBigger(12))
print("\nSearch next bigger for number: 513")
print("Result", NextBigger(513))
print("\nSearch next bigger for number: 2017")
print("Result", NextBigger(2071))
print("\nSearch next bigger for number: 9")
print("Result", NextBigger(9))
print("\nSearch next bigger for number: 111")
print("Result", NextBigger(111))
print("\nSearch next bigger for number: 531")
print("Result", NextBigger(531))

print("\n\nSeventh task")
print("Turn an unsigned 32 bit number: 2149583361 into a string representation of its IPv4 address.")
print("Result:", IPv4(2149583361))
print("\nTurn an unsigned 32 bit number: 32 into a string representation of its IPv4 address.")
print("Result:", IPv4(32))
print("\nTurn an unsigned 32 bit number: 0 into a string representation of its IPv4 address.")
print("Result:", IPv4(0))

