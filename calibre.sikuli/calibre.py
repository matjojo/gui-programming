import time

while True:
    try:
        if find("1553110042070.png"):
            click(Pattern("1553110042070.png").targetOffset(124,28))
    except:
        time.sleep(10)