from stack_queue import Stack, Queue


class Operator:

    """A non alphabetical one character long symbol (e.g., "+")."""

    def __init__(self, symbol, precedence, arity, associativity, actual_function):

        """
        :parameter symbol: a non alphabetical character. Should be unique among Operators (and Functions).
        :parameter precedence: positive integer representing operator evaluation precedence.
        :parameter arity: number of parameters the operator takes.
        :parameter associativity: should be "left" or "right". Denotes the associativity type of the operator.
        :parameter actual_function: python function with <arity> parameters used to evaluate expressions.
        """

        self.symbol = symbol
        self.precedence = precedence
        self.arity = arity
        self.associativity = associativity
        self.actual_function = actual_function

    def __eq__(self, other):

        """:parameter other: Operator or string."""

        return self.symbol == other.symbol if type(other) == Operator else self.symbol == other

    def __lt__(self, other):

        """Compares operators arities."""

        return self.arity < other.arity


class Function:

    """A sequence of letters representing a mathematical function (e.g., "max") with a fixed number of parameters."""

    def __init__(self, name, params, actual_function):

        """
        :parameter name: name of the function used for identification. Should be unique among Functions (and Operators).
        :parameter params: number of parameters that the function takes.
        :parameter actual_function: python function used for expression evaluation.
        """

        self.name = name
        self.params = params
        self.actual_function = actual_function

    def __eq__(self, other):

        """:parameter other: Operator or string."""

        return self.name == other.name if type(other) == Function else self.name == other


class ShuntingYard:

    def __init__(self, functions=(), operators=(), load_basic=True):

        """
        :parameter functions: dictionary of functions with their names as keys.
        :parameter operators: dictionary of operators with their symbols as keys.
        :parameter load_basic: boolean indicating whether to load basic functions and operators.
        """

        self.functions = {f.name: f for f in functions}
        self.operators = {op.symbol: op for op in operators}
        self.postfix = None  # Last output of the algorithm

        if load_basic:
            # TODO: load basic functions and operators into the attributes
            pass

    def parse(self, expression):

        """
        Converts an infix mathematical expression into a postfix one using the Shunting Yard Algorithm.
        :parameter expression: string representing a mathematical infix expression.
        :returns: a queue with the tokens ordered in Reverse Polish Notation (postfix notation).
        """

        input_tokens = self._tokenize(expression)
        output_tokens = Queue()
        operator_stack = Stack()

        while len(input_tokens):
            token = input_tokens.pull()
            if token.isnumeric():  # If the token is a number
                output_tokens.push(token)
            if token in self.operators:  # If the token is an operator
                next_op = operator_stack.view_next()
                while next_op in self.operators and \
                        self.operators[next_op] >= self.operators[token] and \
                        next_op.associativity == "left":
                    output_tokens.push(operator_stack.pull())
                    next_op = operator_stack.view_next()
                operator_stack.push(token)
            if token is '(':
                operator_stack.push(token)
            if token is ')':
                while operator_stack.view_next() is not '(':
                    output_tokens.push(operator_stack.pull())
                operator_stack.pull()  # Pull the left bracket
        while operator_stack:
            output_tokens.push(operator_stack.pull())

        self.postfix = output_tokens
        return output_tokens

    def _load_basic(self):
        pass

    @staticmethod
    def _tokenize(expression):

        """
        Parses an expression into tokens for the Shunting Yard Algorithm. Behaves indefinitely for ill written and non
        infix expressions.
        :parameter expression: string containing an infix mathematical expression.
        :returns: a queue with the tokens.
        """

        expression = ''.join(expression.split())  # remove whitespace, probably inefficient
        tokens = Queue()  # Input tokens for the Shunting Yard

        token_index = 0
        char_index = 0
        # Each loop of this while loop processes one token
        while char_index < len(expression):
            token_start_char = expression[token_index]  # The first character of the token

            if token_start_char.isdigit():  # If the token is a number
                while char_index < len(expression) and \
                        (expression[char_index].isdigit() or
                         expression[char_index] is '.'):
                    char_index += 1
            elif token_start_char.isalpha():  # If the token is a function (no numbers are allowed for functions)
                while char_index < len(expression) and expression[char_index].isalpha():
                    char_index += 1
            else:  # If the character is a single character operator
                char_index += 1

            if token_start_char is not ",":  # The commas are not used in the Shunting Yard Algorithm
                tokens.push(expression[token_index: char_index])  # Add the found token to the queue

            token_index = char_index
        print(tokens)
        return tokens
