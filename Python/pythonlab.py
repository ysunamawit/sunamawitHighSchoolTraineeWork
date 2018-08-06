import json

# """
# Construct a dictionary that maps time to words!

# For this lab, we will only be considering times ending in 00, 10, 15, 30, or 45.
# For any other time inputs, output 'unknown'.

# Examples
# Time: '1:00'    Output: 'one '
# Time: '2:10'    Output: 'two ten'
# Time: '3:15'    Output: 'three fifteen'
# Time: '4:30'    Output: 'four thirty'
# Time: '5:45'    Output: 'five forty-five'
# Time: '9:09'    Output: 'unknown'
# """

def main():
  # Construct a dictionary that will contain the necessary number to string
  # mappings for you to do translations.
  time_mappings = {"1":"one", "2":"two", "3": "three", "4":"four", "5":"five", "6":"six","45":"forty-five" , "00":"oclock","23":"twenty-three", "10":"ten", "30":"thirty", "15":"fifteen", "7":"seven"}
  #{"1": "one", "2": "two", "00": "", "15": "fifteen"}

  # Load in this JSON data using the `loads` function from the imported `json` library
  appointments_data = '{"monday": "3:45", "tuesday": "4:00", "wednesday": "2:15", "thursday": "5:30", "friday": "7:23", "weekends": "1:10"}'
  appointments_dict = json.loads(appointments_data)

  # Extract all the times from the loaded data and store them in a list
    # ex. times = ["3:45", "4:00", "2:15", "5:30", "7:23", "1:10"]
    # get the values out of the appointments dictionary
  times = appointments_dict.values()
#   firstTime = unicode.encode(times[0])
#   splitTimes = firstTime.split(":")
#   #print(splitTimes)
#   hours = splitTimes[0]
#   minutes = splitTimes[1]
#   hoursWords = time_mappings[hours]
#   #print(hoursWords)
#   minuteWords = time_mappings[minutes]
#   #print(minuteWords)
#   bothWords = hoursWords + " " + minuteWords
#   #print(bothWords)
  for time in times:
     incoded = unicode.encode(time)
     splitTime = incoded.split(":")
     hours = splitTime[0]
     minutes = splitTime[1]
     hoursWords = time_mappings[hours]
     minuteWords = time_mappings[minutes]
     bothWords = hoursWords + " " + minuteWords
     print(bothWords)

     

  # For each time, you will need to separate it into hours (left of the :) and minutes (right of the :)
    # do a for loop through the times
    # ex. for time in times:
  # Hint: Lookup the `split` function for strings in Python
  


#  time = "12:30"
  #splitTime = time.split(":")
  #print(splitTime)
  #splitTime = ['12', '30']
  #wordTime = time_mappings[splitTime[0]] + " " + time_mappings[splitTime[1]]
  #print(wordTime)


    # appointments_data = "int"text.split()
  #

#Return the list of results
  #
        # return = [appointments_data]
  #

# """
# The `if __name__ == "__main__":` structure is commonly seen in Python files.
# It tests if this module is being run as the main program, and if so, enters the if clause
# and executes that code block.

# A module is a file containing Python definitions and statements--for example, this file!

# Every module in Python has a special attribute called __name__.
# When the Python interpreter is running a module as the main program, it sets value of __name__ to "__main__".
# If this file is being imported from another module, __name__ will be set to that module's name.
# """
if __name__ == "__main__":
    print(main())


