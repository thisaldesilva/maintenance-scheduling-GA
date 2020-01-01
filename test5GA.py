UNIT1_CAPACITY = 20
UNIT2_CAPACITY = 15
UNIT3_CAPACITY = 35
UNIT4_CAPACITY = 40
UNIT5_CAPACITY = 15
UNIT6_CAPACITY = 15
UNIT7_CAPACITY = 10

TOTAL_POWER_OUTPUT = 150

INTERVAL1_EXPECTED_LOAD = 80
INTERVAL2_EXPECTED_LOAD = 90
INTERVAL3_EXPECTED_LOAD = 65
INTERVAL4_EXPECTED_LOAD = 70

UNIT_CAPACITIES = [20, 15, 35, 40, 15, 15, 10]


def main():
    fitnessFunction([[0, 0, 1, 1], [0, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]])

def fitnessFunction(chromosome):
    #calculate loss output of energy for each interval to the given chromosome  

    #declare an array that keep the number of units lost per interval
    invervals_lost_power = [0,0,0,0]

    interval_loss = 0
    
    for unit_index , unit in enumerate(chromosome):

        for index, interval in enumerate(unit):
            if (interval == 1):
                invervals_lost_power[index] += UNIT_CAPACITIES[unit_index]
                #calculate the total power output on each interval by substracting the
    #total power lost on each interval

    interval_power_output = [0,0,0,0]

    for index in range(len(interval_power_output)):
        interval_power_output[index] = TOTAL_POWER_OUTPUT - invervals_lost_power[index]

        #for debugging
        #print("interval" + str(index) + ":  " + str(TOTAL_POWER_OUTPUT) + " - " + str(invervals_lost_power[index]) + " = " + str(interval_power_output[index]))

    #print()

    #delcare an array to store the respective net reserves
    reserves = []

    #calculate the respective reserves and append it to the list
    reserves.append(interval_power_output[0] - INTERVAL1_EXPECTED_LOAD )
    reserves.append(interval_power_output[1] - INTERVAL2_EXPECTED_LOAD )
    reserves.append(interval_power_output[2] - INTERVAL3_EXPECTED_LOAD )
    reserves.append(interval_power_output[3] - INTERVAL4_EXPECTED_LOAD )


    #debugging purposes
    print("Interval1: " , interval_power_output[0], "-" ,INTERVAL1_EXPECTED_LOAD, " = " , reserves[0])
    print("Interval2: " , interval_power_output[1], "-" ,INTERVAL2_EXPECTED_LOAD, " = " , reserves[1])
    print("Interval3: " , interval_power_output[2], "-" ,INTERVAL3_EXPECTED_LOAD, " = " , reserves[2])
    print("Interval4: " , interval_power_output[3], "-" ,INTERVAL4_EXPECTED_LOAD, " = " , reserves[3])


if __name__ == "__main__":
    main()
