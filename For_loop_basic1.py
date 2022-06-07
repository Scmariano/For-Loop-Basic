# 1.Basic - Print all integers from 0 to 150.
for i in range(151):
    print(i)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for i in range(5,1005,5):
    print(i)

# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

num = 0

while num<100:
    num+=1
    if num%10==0:
        print("Coding Dojo")
    elif num%5==0:
        print("Coding")
    else:
        print(num)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

maxnum = 500000
Oddint = 0
num = 1
while num <= maxnum:
    if(num % 2 != 0):
        Oddint = Oddint + num
    num = num + 1

print(Oddint)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for i in range(2018, -1, -4):
    print(i)

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNUm = 9
mult = 3

for i in range(lowNum,highNUm + 1):
        if i % mult == 0:
            print(i)