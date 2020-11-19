# Input Data for Person 1
# Shedule
person1Shedule = [["9:00","10:30"], ["12:00","13:00"], ["16:00","18:00"]]
# Time lapse for a meet
person1MeetTiming = ["9:00","20:00"]
# Input Data for Person 2
# Shedule
person2Shedule = [["10:00","11:30"], ["12:30","14:30"], ["14:30","15:00"], ["16:00","17:00"]]
# Time lapse for a meet
person2MeetTiming = ["10:00","18:30"]

# Helper function to convert hour format to integer
def TimeToInt(time):
    (h, m) = time.split(':')
    result = int(h) * 60 + int(m)
    return result
# Helper function to convert integer format to hour
def InToTime(minutes):
    hour, min = divmod(minutes, 60)
    return "%d:%02d" % (hour, min)

# Helper function to find valid time lapse for meeting of both person
def validMeetDayLapse():
	validTime = []
	validTime.append(InToTime(max(TimeToInt(person1MeetTiming[0]),TimeToInt(person2MeetTiming[0]))))
	validTime.append(InToTime(min(TimeToInt(person1MeetTiming[1]),TimeToInt(person2MeetTiming[1]))))
	return validTime

# Helper function to check and append valid free time lapse to make a meet of X minutes of duration
def validFreeTime(end,start, duration, list):
    if end - start >= duration:
        free = []
        free.append(start)
        free.append(end)
        list.append(free)

# Function to obtain valid a list of free time lapse for meetings in the valid time lapse for do that
def freeTime(shedule, meetDuration):
    personFreeTime = []
    # lapse is the lapse of time valid for both person to meet
    lapse = validMeetDayLapse()
    i = 0
    # adding free valid time from the begin of valid lapse to the first free time of the person
    validFreeTime(TimeToInt(shedule[i][0]),TimeToInt(lapse[0]),meetDuration,personFreeTime)
    # Person free time taking from the shedule
    while i < len(shedule)-1:
        validFreeTime(TimeToInt(shedule[i+1][0]),TimeToInt(shedule[i][1]),meetDuration,personFreeTime)
        i+=1
    # Person free time after finish the shedule and the valid lapse of time allowed
    validFreeTime(TimeToInt(lapse[1]),TimeToInt(shedule[i][1]),meetDuration,personFreeTime)
    # Return a list of integer intervals [[480,540]...] or [] if dont have free time
    return personFreeTime
# Main function, receive a duration in minutes ... 15, 30, 45, etc... in this case 30
def meetingPlanning(duration):
    listValidMeet = []
    # Free time valid for meetings for person1
    person1FreeTime = freeTime(person1Shedule, duration)
    # Free time valid for meetings for person2
    person2FreeTime = freeTime(person2Shedule, duration)
    i = 0
    # Checking intervals intersections, free time was expresed as integer intervals, so the intersection with a large of the duration amount are valid for meet	
    while i < len(person1FreeTime):
        j = 0
        while j < len(person2FreeTime):
	    # Getting start of intersection
            start = max(person1FreeTime[i][0],person2FreeTime[j][0])
	    # Getting end of intersection
            end = min(person1FreeTime[i][1],person2FreeTime[j][1])
	    # Checking the "distance" of the intersection is equal or bigger than the duration
            if end - start >= duration:
                # Creating de meet time lapse available
                meet = []
                meet.append(InToTime(start))
                meet.append(InToTime(end))
		# Appending to the list of availables time to meet for both persons
                listValidMeet.append(meet)
            j+=1
        i+=1
    # Printing the result
    print(listValidMeet)

# Calling the function to execute full algorithm -> 30 minutes is the duration 
meetingPlanning(30)
