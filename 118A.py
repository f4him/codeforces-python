string = input()
string2=0
string = string.lower()
vowels = {'a','e','i','o','u','y'}
for i in range(len(string)):
    if string[i] in vowels:
        continue
    else:
        print('.'+string[i],end='')
    