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

## Step 1: Specify the problem, deﬁne constraints and optimum criteria

