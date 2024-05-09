import re

#exercício 8
print("exercício 8")
def inteiros(s):
    num = re.findall(r"-?\d+", s)
    return [int(n) for n in num]


string = "String 123 456 7 -4 -10 String fewnjfnweifweji"
res = inteiros(string)
print(res)

result = re.search("([a-z]+)(,)","teste,ujuuji,") # teste,
print(result)


#exercício 1.1
print("\nexercício 1.1")

line1 = "hello world"
line2 = "goodbye world"
line3 = "hi, hello there"

if re.match("hello", line1):
    print(line1)

if re.match("hello", line2):
    print(line2)

if re.match("hello", line3):
    print(line3)

#exercício 1.2
print("\nexercício 1.2")

line1 = "hello world"
line2 = "goodbye world"
line3 = "hi, hello there"

if re.search("hello", line1):
    print(line1)

if re.search("hello", line2):
    print(line2)

if re.search("hello", line3):
    print(line3)

#exercício 1.3
print("\nexercício 1.3")

line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"

ocorrencias = re.findall(r"(?i)hello", line)

for indice, ocorrencia in enumerate(ocorrencias):
    print(f"Ocorrência {indice+1}: {ocorrencia}")

#exercício 1.4
print("\nexercício 1.4")

line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"

s = re.sub(r"(?i)hello", "*Yep", line)
print(s)