with open('/Users/Jms/Git/python-laimingxing/ch05/data.txt') as inf, open('./out.txt', 'w') as outf:
    for line in inf:
        outf.write(" ".join([word.capitalize() for word in line.split()]))
        outf.write("\n")
