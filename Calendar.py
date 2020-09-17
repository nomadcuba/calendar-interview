person1Shedule = [["9:00","10:30"], ["12:00","13:00"], ["16:00","18:00"]]
person1MeetTiming = ["9:00","20:00"]
person2Shedule = [["10:00","11:30"], ["12:30","14:30"], ["14:30","15:00"], ["16:00","17:00"]]
person2MeetTiming = ["10:00","18:30"]

def TimeToInt(time):
    (h, m) = time.split(':')
    result = int(h) * 60 + int(m)
    return result
def InToTime(minutes): 
    hour, min = divmod(minutes, 60) 
    return "%d:%02d" % (hour, min) 

def validMeetDayLapse():
	validTime = []
	validTime.append(InToTime(max(TimeToInt(person1MeetTiming[0]),TimeToInt(person2MeetTiming[0]))))
	validTime.append(InToTime(min(TimeToInt(person1MeetTiming[1]),TimeToInt(person2MeetTiming[1]))))
	return validTime

def validFreeTime(end,start, duration, list):
    if end - start >= duration:
        free = []
        free.append(start)
        free.append(end)
        list.append(free)


def freeTime(shedule, meetDuration):
    personFreeTime = []
    lapse = validMeetDayLapse()
    i = 0
    validFreeTime(TimeToInt(shedule[i][0]),TimeToInt(lapse[0]),meetDuration,personFreeTime)
    
    while i < len(shedule)-1:
        validFreeTime(TimeToInt(shedule[i+1][0]),TimeToInt(shedule[i][1]),meetDuration,personFreeTime)
        i+=1
    
    validFreeTime(TimeToInt(lapse[1]),TimeToInt(shedule[i][1]),meetDuration,personFreeTime)
    
    return personFreeTime

def meetingPlanning(duration):
    listValidMeet = []
    person1FreeTime = freeTime(person1Shedule, duration)
    person2FreeTime = freeTime(person2Shedule, duration)
    i = 0
    while i < len(person1FreeTime):
        j = 0
        while j < len(person2FreeTime):
            start = max(person1FreeTime[i][0],person2FreeTime[j][0])
            end = min(person1FreeTime[i][1],person2FreeTime[j][1])
            if end - start >= duration:
                meet = []
                meet.append(InToTime(start))
                meet.append(InToTime(end))
                listValidMeet.append(meet)
                break
            j+=1
        i+=1    
    print(listValidMeet)
 
meetingPlanning(30)