# Case study: maintenance scheduling with genetic algorithms

One of the most successful areas for GA applications includes the problem of scheduling resources. Scheduling problems are complex and difﬁcult to solve. They are usually approached with a combination of search techniques and heuristics.

## Why are scheduling problems so difﬁcult?

First, scheduling belongs to NP-complete problems. Such problems are likely to be unmanageable and cannot be solved by combinatorial search techniques. Moreover, heuristics alone cannot guarantee the best solution. 

Second, scheduling problems involve a competition for limited resources; as a result, they are complicated by many constraints. The key to the success of the GA lies in deﬁning a ﬁtness function that incorporates all these constraints. 

The problem we discuss here is the maintenance scheduling in modern power systems. This task has to be carried out under several constraints and uncertainties, such as failures and forced outages of power equipment and delays in obtaining spare parts. The schedule often has to be revised at short notice. Human experts usually work out the maintenance scheduling by hand, and there is no guarantee that the optimum or even near-optimum schedule is produced.

A typical process of the GA development includes the following steps:

1. Specify the problem, deﬁne constraints and optimum criteria.

1. Represent the problem domain as a chromosome.

1. Deﬁne a ﬁtness function to evaluate the chromosome’s performance.

1. Construct the genetic operators.

1. Run the GA and tune its parameters.

##### Step 1: Specify the problem, deﬁne constraints and optimum criteria

This is probably the most important step in developing a GA, because if it is not correct and complete a viable schedule cannot be obtained. 

Power system components are made to operate continuously throughout their life by means of preventive maintenance. The purpose of maintenance scheduling is to ﬁnd the sequence of outages of power units over a given period of time (normally a year) such that the security of a power system is maximised. 

Any outage in a power system is associated with some loss in security. The security margin is determined by the system’s net reserve. The net reserve, in turn, is deﬁned as the total installed generating capacity of the system minus the power lost due to a scheduled outage and minus the maximum load forecast during the maintenance period. 

For instance, if we assume that the total installed capacity is 150MW and a unit of 20MW is scheduled for maintenance during the period when the maximum load is predicted to be 100MW, then the net reserve will be 30MW. Maintenance scheduling must ensure that sufﬁcient net reserve is provided for secure power supply during any maintenance period.

Suppose, there are seven power units to be maintained in four equal intervals. The maximum loads expected during these intervals are 80, 90, 65 and 70MW. The unit capacities and their maintenance requirements are presented in Table 7.2.

![](/images/table7.2.png)

The constraints for this problem can be speciﬁed as follows:

* Maintenance of any unit starts at the beginning of an interval and ﬁnishes at the end of the same or adjacent interval. The maintenance cannot be aborted or ﬁnished earlier than scheduled.

* The net reserve of the power system must be greater than or equal to zero at any interval.

The optimum criterion here is that the net reserve must be at the maximum during any maintenance period.

#### Represent the problem domain as a chromosome

Our scheduling problem is essentially an ordering problem, requiring us to list the tasks in a particular order. A complete schedule may consist of a number of overlapping tasks, but not all orderings are legal, since they may violate the constraints. Our job is to represent a complete schedule as a chromosome of a ﬁxed length. 

An obvious coding scheme that comes to mind is to assign each unit a binary number and to let the chromosome be a sequence of these binary numbers. However, an ordering of the units in a sequence is not yet a schedule. Some units can be maintained simultaneously, and we must also incorporate the time required for unit maintenance into the schedule. Thus, rather than ordering units in a sequence, we might build a sequence of maintenance schedules of individual units. The unit schedule can be easily represented as a 4-bit string, where each bit is a maintenance interval. If a unit is to be maintained in a particular interval, the corresponding bit assumes value 1, otherwise it is 0. For example, the string presents a schedule for a unit to be maintained in the second interval. It also shows that the number of intervals required for maintenance of this unit is equal to 1. Thus, a complete maintenance schedule for our problem can be represented as a 28-bit chromosome. 

However, crossover and mutation operators could easily create binary strings that call for maintaining some units more than once and others not at all. In addition, we could call for maintenance periods that would exceed the number of intervals really required for unit maintenance. 

A better approach is to change the chromosome syntax. As already discussed, a chromosome is a collection of elementary parts called genes. Traditionally, each gene is represented by only one bit and cannot be broken into smaller elements. For our problem, we can adopt the same concept, but represent a gene by four bits. In other words, the smallest indivisible part of our chromosome is a 4-bit string. This representation allows crossover and mutation operators to act according to the theoretical grounding of genetic algorithms. What remains to be done is to produce a pool of genes for each unit:

![](/images/units.png)

The GA can now create an initial population of chromosomes by ﬁlling 7-gene chromosomes with genes randomly selected from the corresponding pools. A sample of such a chromosome is shown in Figure 7.9.

#### Deﬁne a ﬁtness function to evaluate the chromosome performance

The chromosome evaluation is a crucial part of the GA, because chromosomes are selected for mating based on their ﬁtness. The ﬁtness function must capture what makes a maintenance schedule either good or bad for the user. For our problem we apply a fairly simple function concerned with constraint violations and the net reserve at each interval.

![](/images/chromosome.png)

The evaluation of a chromosome starts with the sum of capacities of the units scheduled for maintenance at each interval. For the chromosome shown in Figure 7.9, we obtain: 


_Interval 1_: 0 *	20 + 0 * 15 + 0 * 35 + 1 * 40 + 0 * 15 + 0 * 15 + 1 * 10 = 50 

_Interval 2_: 1 * 20 + 0 * 15 + 0 * 35 + 0 * 40 + 1 * 15 + 0 * 15 + 0 * 10 = 35 

_Interval 3_: 1 * 20 + 1 * 15 + 0 * 35 + 0 * 40 + 0 * 15 + 1 * 15 + 0 * 10 = 50

_Interval 4_: 0 * 20 + 1 * 15 + 1 * 35 + 0 * 40 + 0 * 15 + 0 * 15 + 0 * 10 = 50 

Then these values are subtracted from the total installed capacity of the power system (in our case, 150MW):

_Interval_ 1: 150 - 50 =100

Interval 2: 150 - 35 = 115

Interval 3: 150 - 50 = 100

Interval 4: 150 - 50 = 100 

And ﬁnally, by subtracting the maximum loads expected at each interval, we obtain the respective net reserves: 

_Interval_ 1: 100 - 80 = 20 

_Interval_ 2: 115 - 90 = 25 

_Interval 3_: 100 - 65 = 35 

_Interval 4_: 100 - 70 = 30 

Since all the results are positive, this particular chromosome does not violate any constraint, and thus represents a legal schedule. The chromosome’s ﬁtness is determined as the lowest of the net reserves; in our case it is 20. If, however, the net reserve at any interval is negative, the schedule is illegal, and the ﬁtness function returns zero. At the beginning of a run, a randomly built initial population might consist of all illegal schedules. In this case, chromosome ﬁtness values remain unchanged, and selection takes place in accordance with the actual ﬁtness values.

#### Step 4: Construct the genetic operators

Constructing genetic operators is challenging and we must experiment to make crossover andmutation work correctly. The chromosome has to be broken up in a way that is legal for our problem. Since we have already changed the chromosome syntax for this, we can use the GA operators in their classical forms. Each gene in a chromosome is represented by a 4-bit indivisible string, which consists of a possible maintenance schedule for a particular unit. Thus, any random mutation

![](/images/figure7.10.png)

of a gene or recombination of several genes from two parent chromosomes may result only in changes of the maintenance schedules for individual units, but cannot create ‘unnatural’ chromosomes. Figure 7.10(a) shows an example of the crossover application during a run of the GA. The children are made by cutting the parents at the randomly selected point denoted by the vertical line and exchanging parental genes after the cut. Figure 7.10(b) demonstrates an example of mutation. The mutation operator randomly selects a 4-bit gene in a chromosome and replaces it by a gene randomly selected from the corresponding pool. In the example shown in Figure 7.10(b), the chromosome is mutated in its third gene, which is replaced by the gene 0001 chosen from the pool of genes for the Unit 3.

#### Run the GA and tune its parameters

It is time to run the GA. First, we must choose the population size and the number of generations to be run. Common sense suggests that a larger population can achieve better solutions than a smaller one, but will work more slowly. In fact, however, the most effective population size depends on the problem being solved, particularly on the problem coding scheme (Goldberg, 1989). The GA can run only a ﬁnite number of generations to obtain a solution. Perhaps we could choose a very large population and run it only once, or we could choose a smaller population and run it several times. In any case, only experimentation can give us the answer.

![](/images/figure7.11(1).png)


![](/images/figure7.11(2).png)

![](/images/figure7.12(1).png)

![](/images/figure7.12(2).png)

Figure 7.11(a) presents performance graphs and the best schedule created by 50 generations of 20 chromosomes. As you can see, the minimum of the net reserves for the best schedule is 15MW. Let us increase the number of generations to 100 and compare the best schedules. Figure 7.11(b) presents the results. The best schedule now provides the minimum net reserve of 20MW. However, in both cases, the best individuals appeared in the initial generation, and the increasing number of generations did not affect the ﬁnal solution. It indicates that we should try increasing the population size. 

Figure 7.12(a) shows ﬁtness function values across 100 generations, and the best schedule so far. The minimum net reserve has increased to 25MW. To make sure of the quality of the best-so-far schedule, we must compare results obtained under different rates of mutation. Thus, let us increase the mutation rate to 0.01 and rerun the GA once more. Figure 7.12(b) presents the results. The minimum net reserve is still 25MW. Now we can conﬁdently argue that the optimum solution has been found.
