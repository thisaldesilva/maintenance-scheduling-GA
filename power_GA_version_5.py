#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 18:24:08 2019

@author: Thisal
"""

import random

POPULATION = 10
GENERATIONS = 10
MUTATION_RATE = 0.1

#pool of random genes
pool_one = [[1,1,0,0], [0,1,1,0], [0,0,1,1]]
pool_two = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

TOTAL_POWER_OUTPUT = 150

INTERVAL1_EXPECTED_LOAD = 80
INTERVAL2_EXPECTED_LOAD = 90
INTERVAL3_EXPECTED_LOAD = 65
INTERVAL4_EXPECTED_LOAD = 70

#capacities of each unit 
UNIT_CAPACITIES = [20, 15, 35, 40, 15, 15, 10]

def main():

    #declare a list to hold the population /  generation
    population = []

    #step 2 in the slides
    #generate the initial population
    for ch in range(POPULATION):

        #declare an array to hold the genes / chromosome
        chromo = []

        #get the forst two genes from the pool one since it requres two intervals
        for i in range(2):
            chromo.append(random.choice(pool_one))

        #get the other genes reuired for the chromosome from pool 2
        for j in range(5):
            chromo.append(random.choice(pool_two))

        #add the chromosome into the population
        population.append(chromo)

        #print(chromo)

    #go through // loop for all the generations
    for g in range(GENERATIONS):

        #declare an array to hold the fitness values of each chromosome in the population
        fitness_values = []

        #step 2 in the slides
        #calculate the fitness 
        for chromosome in population:
            fitness_values.append(fitnessFunction(chromosome))

        #print(fitness_values)
        
        #display generation's best chromosome / best answer so far for the grid
        maximum_firtness_value = max(fitness_values)
        best_index = fitness_values.index(maximum_firtness_value)
        print("Generation (", g, ") best solution - ", population[best_index])
        
        mating_pool = generate_mating_pool(fitness_values, population)
        
        #generte the new population 
        population = generate_new_population(mating_pool, fitness_values)

        #print(mating_pool)
        
    
    
def generate_new_population(mating_pool , fit_values):
    
    #declare an array to hold new generation / population
    new_population = []
    
    for i in range(POPULATION):
        
        #select the two parents from the mating pool
        parent1 = random.choice(mating_pool)
        parent2 = random.choice(mating_pool)
        
        #do the crossover 
        child = crossover(parent1, parent2)
        
        #do the mutation
        child = mutation(child, MUTATION_RATE)
        
        new_population.append(child)
        
    return new_population
        
def mutation(child_chromosome, mutation_rate):
    #first add mutation to the first two genes
    for i in range(0,2):
        if (random.random() < mutation_rate):
            
            #choose a gene different to the one already at that position
            new_gene = random.choice(pool_one)
            
            while(child_chromosome[i] == new_gene):
                new_gene = random.choice(pool_one)
             
            #change the gene at the particular index
            child_chromosome[i] = new_gene
        
    #add mutation for the last 5 genes on the list
    for i in range(2,7):
        if (random.random() < mutation_rate):
            
            #choose a gene different to the one already at that position
            new_gene = random.choice(pool_two)
            
            while(child_chromosome[i] == new_gene):
                new_gene = random.choice(pool_two)
                
            #change the gene at the particular index
            child_chromosome[i] = random.choice(pool_two)
    
    #print("chilm - ", child_chromosome)
    return child_chromosome
        

def crossover(parent1, parent2):
    
    #declare an array to hold genes from parent chromosomes
    child = []
    
    #first consider only about the first two genes of the chromosomes
    #in this task , first two genes in the chromosome is treated and taken seperatly for better performance 
    
    r = random.randint(0,3)
    
    if (r == 0):
        child.append(parent1[0])
        child.append(parent2[1])
    elif (r == 1):
        child.append(parent2[0])
        child.append(parent1[1])
    elif ( r == 2):
        child.append(parent1[0])
        child.append(parent1[1])
    else:
        child.append(parent2[0])
        child.append(parent2[1])
        
    
    #now consider about the other part of the chromosome /  5 genes from the right
    
    gene_seperate_index = random.randint(2,7)
    
    #copy from the first parent
    for p1_index in range(2, gene_seperate_index):
        child.append(parent1[p1_index])
        
    #copy from the second parent
    for p2_index in range(gene_seperate_index , len(parent1)):
        child.append(parent2[p2_index])
    
    #print("seperate index: " ,gene_seperate_index)        
    #print("parent1 - ", parent1)
    #print("parent2 - ", parent2)
    #print("Child - ", child)
    
    return child

        
    
    


def generate_mating_pool(fit_values, population):

    #get the sum of the fitness values
    fitness_sum = sum(fit_values)
    #print("Fittness sum - ", fitness_sum)

    #declare mating pool of chromosomes
    mating_pool = []

    percentage = 0
    
    for chromo_index, fit_value in enumerate(fit_values):
        if fit_value != 0:
            percentage =  int(round(fit_value / fitness_sum * 100))

        #add the chromosome to the mating pool according to it's importance or fitness percentage
            for times in range(percentage):
                mating_pool.append(population[chromo_index])

    #for i in range(len(mating_pool)):
        #print( i+1, "  -   " , mating_pool[i])
    return mating_pool

    
        
    
        
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
    #print("Interval1: " , interval_power_output[0], "-" ,INTERVAL1_EXPECTED_LOAD, " = " , reserves[0])
    #print("Interval2: " , interval_power_output[1], "-" ,INTERVAL2_EXPECTED_LOAD, " = " , reserves[1])
    #print("Interval3: " , interval_power_output[2], "-" ,INTERVAL3_EXPECTED_LOAD, " = " , reserves[2])
    #print("Interval4: " , interval_power_output[3], "-" ,INTERVAL4_EXPECTED_LOAD, " = " , reserves[3])

    #check if the chromosome is invalid
    if min(reserves) < 0:
        return 0

    else:
        return min(reserves)

if __name__ == "__main__":
    main()
