s1 = 'abc'
s1 = s1[::-1]

s2 = 'Hell"o worl"d!'
n = 0
k = 0
s2r = []
for i in range(len(s2)):
    if s2[i] == '"' and n == 0:
        n = i
    if s2[i] == '"' and n != 0 and i != n:
        k = i
    if k != 0 and n != 0:
        s2r.append(s2[n+1:k])
        n = 0
        k = 0
print(s2r)

s3 = str(input())
s3 = int(s3)
print(s3*2)

s4 = '12132 3453453'
n = 0
for i in range(len(s4)):
    if s2[i] == ' ':
        n = i
print(s4[n::] + ' ' + s4[0:n])

n = int(input())
s = str(input())
d = []
number = 0
query = ''

for i in range(n):
    if s[i] not in d:
        d.append(s[i])

amount = len(d)

def count_overlapping_substrings(haystack, needle):
    count = 0
    i = -1
    while True:
        i = haystack.find(needle, i+1)
        if i == -1:
            return count
        count += 1

maximum = 0
index = 0
for i in range(amount):
    m = count_overlapping_substrings(s, d[i])
    if m > maximum:
        maximum = m
        index = i

number += maximum
query = query + str(d[index])
print(maximum, query)

for i in range(n-1):
    maximum = 0
    index = 0
    for j in range(amount):
        m = count_overlapping_substrings(s, d[j] + query)
        if m >= maximum:
            maximum = m
            index = j

    for t in range(amount):
        m = count_overlapping_substrings(s, query + d[t])
        if m >= maximum:
            maximum = m
            index = t

    number += maximum
    query = query + str(d[index])
    print(maximum, query)

print(number)



#formula = str(input())

form = '?1+5*6+7*3?'

pointsBrackets = []
for i in range(len(form)):
    if form[i] == '(':
        pointsBrackets.append(i)
    if form[i] == ')':
        pointsBrackets.append(i)



def calculationMultiply(form):
    oneNumber = 0
    twoNumber = 0
    startPoint = 0
    endPoint = 0
    for i in range(len(form)):
        if form[i] == '*':
            for j in range(i + 1, len(form)):
                if not form[j].isdigit():
                    twoNumber = form[i+1:j]
                    endPoint = j
                    break
            for j in range(i - 1, -1, -1):
                if not form[j].isdigit():
                    oneNumber = form[j+1:i]
                    startPoint = j+1
                    break
            break

    newForm = form.replace(form[startPoint:endPoint], str(int(oneNumber) * int(twoNumber)), 1)
    return newForm

while True:
    if form.find('*') > 0:
        form = calculationMultiply(form)
    else:
        break

def calculationPlus(form):
    oneNumber = 0
    twoNumber = 0
    startPoint = 0
    endPoint = 0
    for i in range(len(form)):
        if form[i] == '+':
            for j in range(i + 1, len(form)):
                if not form[j].isdigit():
                    twoNumber = form[i+1:j]
                    endPoint = j
                    break
            for j in range(i - 1, -1, -1):
                if not form[j].isdigit():
                    oneNumber = form[j+1:i]
                    startPoint = j+1
                    break
            break

    newForm = form.replace(form[startPoint:endPoint], str(int(oneNumber) + int(twoNumber)), 1)
    return newForm

while True:
    if form.find('+') > 0:
        form = calculationPlus(form)
    else:
        break

print(form)