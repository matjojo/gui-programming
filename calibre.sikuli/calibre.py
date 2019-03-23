import time
adultSet = False
notDone = True
while notDone:
    try:
        if find("1553270172366.png"):
         click(Pattern("1553270172366.png").targetOffset(110,27))
    except:
        time.sleep(5)
    if not adultSet: # Make sure we do not search for this all the time when not needed
        try:
            if find("1553360794403.png"):
                click(Pattern("1553360794403.png").targetOffset(126,15))
        except:
             pass
    try:
        if find("1553362571821.png"):
            click(Pattern("1553362571821.png").targetOffset(100,13))
            notDone = False # when we open the log we know this was the last button to press
        except:
            pass
        