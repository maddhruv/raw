fw = open('sample.txt', 'w')
fw.write('Hello World\nthis is a sample file')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()