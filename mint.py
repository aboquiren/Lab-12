

ret = True
with open('main.py') as f:
    for line in f:
        if line.find('min') > 0:
            ret = False

print(ret)
