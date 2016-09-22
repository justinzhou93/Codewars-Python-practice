def format_duration(seconds):
    # your code here
    time = [seconds/(3600*24*365), (seconds%(60*60*24*365))/(60*60*24), (seconds%(60*60*24))/(60*60),
            (seconds%(60*60))/60, seconds%(60)]
    units = ["year", "day", "hour", "minute", "second"]
    count = 0
    mystr = ""

    for i in range(len(time)):
        if time[len(time) - i - 1] > 0:
            count += 1
            if count == 1:
                if time[len(time) - i - 1] > 1:
                    mystr = mystr + str(time[len(time) - i - 1]) + " " + units[len(time) - i - 1] + "s"
                else:
                    mystr = mystr + str(time[len(time) - i - 1]) + " " + units[len(time) - i - 1]
            elif count == 2:
                mystr = " and " + mystr
                if time[len(time) - i - 1] > 1:
                    mystr = str(time[len(time) - i - 1]) + " " + units[len(time) - i - 1] + "s" + mystr
                else:
                    mystr = str(time[len(time) - i - 1]) + " " + units[len(time) - i - 1] + mystr
            else:
                mystr = ", " + mystr
                if time[len(time) - i - 1] > 1:
                    mystr = str(time[len(time) - i - 1]) + " " + units[len(time) - i - 1] + "s" + mystr
                else:
                    mystr = str(time[len(time) - i - 1]) + " " + units[len(time) - i - 1] + mystr
    print mystr

format_duration(0) 
