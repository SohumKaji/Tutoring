def check(num):
    split = list(num)
    
    if(len(split) == 9 and len(set(split)) == len(split)): return True
    return False

start = "0"
while(not check(start)): start = input("Enter a 9 digit number where no digit appears twice: ")

start = int(start)
finish = start + 1
while((not check(str(finish))) or set(list(str(start))) != set(list(str(finish)))): finish +=1

print("The next highest 9-digit number with the same digits is: ", finish)