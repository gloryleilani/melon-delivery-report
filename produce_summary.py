
#Problematic output to fix in Exercise:
#Ex.1: Delivered White Wonder Watermelon White Wonder Watermelons for total of $White Wonder Watermelon
#Goal of exercise: Output like this: Delivered 18 Scaly Bark Watermelons for total of $72.00


day_1 = (1,"um-deliveries-20140519.txt")
day_2 = (2,"um-deliveries-20140520.txt")
day_3 = (3,"um-deliveries-20140521.txt")

def report_on_deliveries(day):
    """This function takes in the day number and path to the file for the day
    and returns a report. The file is opened and each line is processed to create
    each daily report."""

    print(f"Day {day[0]}") #This prints the day number, e.g. "Day 1"
    daily_melon_deliveries = open(day[1]) #This opens the file of the daily delivery info.
    for line in daily_melon_deliveries: #This sets us up to read each line in the file.
        line = line.rstrip() #This strips away the trailing whitespace.
        words = line.split('|') #This uses the "|" symbol as the delimiter between columns of data.

        melon = words[0] #Type of melon
        count = words[1] #Count for a single melon type
        amount = words[2] #Cost for a single melon type

        print(f"Delivered {count} {melon}s for total of ${amount}") #Daily report per melon type
    
    daily_melon_deliveries.close() #Close file command

report_on_deliveries(day_1) #Calling the function to produce the report per day
report_on_deliveries(day_2)
report_on_deliveries(day_3)


#ORIGIINAL CODING EXERCISE (GOAL TO FIND PROBLEMS IN CODE):

# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
