import time
while True:
    try:
        if find("1553112404444.png"):
            click(Pattern("1553112404444.png").targetOffset(10,-1))
    except:
        time.sleep(5)
