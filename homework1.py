import re

data = open('actualdata.txt')
end = []
for line in data:
    line = line.strip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) != 0:
        for number in numbers:
            end.append(int(number))
print end
print "There are " + str(len(end)) + " numbers found."
print "The sum is " + str(sum(end))
