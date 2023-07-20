
# Damavis Challenge
Code proposal as part of the application to Data Engineer.


## Rellevant Information
It is important to mention the following things:
- All the work done does not use any library or framework.
- The idea of using the AStar algorithm is because is a very reliable algorithm (that is widely studied in my degree) and optimises the memory and the execution time needed to solve the problem.
- Comment that the AStar Algorithm implemented is not the original because of the existence of a shape (that has "volume") to be transported.
- It was considered to create a Cell class to make the process of the AStar algorithm more efficient.
- Nevertheless, if the labyrinth is small this can make the algorithm slower than others.
- Moreover, if its a large labyrinth, the memory needed increases rapidly.
- However, this algorithm is more efficient in execution time than backtracking (that could have worked only with the initial input which allows using less memory). This is why the AStar algorithm was preferred.
- Also say that the decision to make the variable labyrinth global is because it was needed in too many functions and passing it as a parameter was not seen as a good idea.


## Other Considerations and Ideas
Despite the work done, some ideas or considerations have not been done and could be a good idea to implement in further updates/optimizations of the program.
- The use of the global variable labyrinth could not be written again and create other variables that save the cell class version of the labyrinth.
- The Functions used in the program could be distributed in other files to make the program more clear.
- The application of a Dijkstra algorithm in the input "labyrinth map" could also be a good idea to consider.
- An Implementation of a function that confirms the existence or inexistence of a path to the exit could be an idea to implement to save time if a path does not exist.


## Conclusion
To sum up, the code proposed works perfectly and passes all 4 tests.
The time to obtain the result is negligible in the biggest test (test 4) and comments have been implemented in all the code to understand all the process done by the program.

In case of continue developing this program recomend to take into consideration the considerations and ideas proposed in the before section.


## Author
- [Gerard Lahuerta Martin](https://es.linkedin.com/in/gerard-lahuerta-mart%C3%ADn)

