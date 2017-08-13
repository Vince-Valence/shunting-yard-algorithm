# Shunting Yard Algorithm
In this repository, you can find an implementation of Dijkstra's [Shunting Yard Algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm). It can convert an infix math expression into a postfix one, and it can evaluate the latter. It is not intended to be a maximally efficient implementation. 

# Usage
```python
from shunting_yard import ShuntingYard

yard = ShuntingYard()  # Create a shunting yard. This class has knowledge of some operators and functions
postfix = yard.parse("(1+2)*4^3.14")  # Returns a queue with the postfix tokens
yard.evaluate(postfix)  # Returns the value of the postfix expression
```

The following operators and functions are known to the ShuntingYard class by default, if you don't want them, set `load_basic` to `False` when instantiating the ShuntingYard:

+ Operators: +, -, /, *, ^. With respective precedences 2, 2, 3, 3, 4 and all with arity 2
+ Functions: *min*, *max*. Both with two arguments and precedence 5

You can define your own operators or functions with the Operator class, with certain constraints:

+ Their symbol or identification should be unique
+ If you don't use letters for their symbols, you must use one character
+ If you use letters for their symbols, you must only use letters, but can use more characters

Like this:

```python
import operator
op1 = Operator(symbol="%", arity=2, precedence=3, actual_function=operator.mod) 
