# 1 Introduction

In assignment 1, you explored the use of genetic algorithms to find solutions to the travelling salesperson problem. In this assignment, we can use the same genetic algorithm framework but will explore the application of evolutionary computation to game theory. In this assignment, you will use genetic algorithms to evolve strategies for playing the Iterated Prisoner’s Dilemma (IPD). This assignment consists of two parts: first evolving strategies against fixed opponents; the second part allows you to explore an extension on this.

# 2 Background

The Prisoner’s Dilemma is a fundamental problem in game theory. In each round, two players must choose to either cooperate (C) or defect (D). A commonly used payoff matrix is:

|          | Player 2 C | Player 2 D |
|----------|-------------|-------------|
| Player 1 C | (3,3)       | (0,5)       |
| Player 1 D | (5,0)       | (1,1)       |

Where (x,y) represents the score for Player 1 and Player 2 respectively.

# 3 Part 1: Evolution Against Fixed Strategies (60 marks)

The fitness function will be how the strategy performs against other well-known strategies. In effect, you will be evolving strategies with fixed landscapes defined by the strategies the agents play against.

## 3.1 Fixed Strategies

Implement the following standard strategies:
- Always Cooperate
- Always Defect
- Tit-for-Tat (do what opponent did last round)
- Others ...?

## 3.2 Evolutionary Algorithm

- Population size: 50-100 individuals
- Tournament selection
- Maintain diversity in the population
- Explore convergence with different fitness evaluations (different portions of all-c, all-d, other...)

## 3.3 Analysis Requirements

Provide a short report on:
- Analysis of evolved strategies
- Performance against the fixed strategies
- Discussion of any interesting findings
- Visualization of fitness progression over generations

# 4 Part 2: Extension (40 marks)

Consider the scenario you have explored in Part 1 and consider an extension of interest. Some suggestions, but please do propose your own ones too:
- Extend your representation (genotype) and compare the findings
- Consider the introduction of noise
- Co-evolutionary approach

Submit a short report outlining your findings.

# 5 Submission Requirements

## 5.1 Report submission

- Reports for part 1 and part 2
- Link to code