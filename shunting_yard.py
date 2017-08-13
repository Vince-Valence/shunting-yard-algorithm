from stack_queue import Stack, Queue
from datetime import datetime


class ShuntingYard:

    @staticmethod
    def parse(expression):

        """Converts an infix mathematical expression into a postfix one using the Shunting Yard Algorithm.
        :parameter expression: string representing a mathematical infix expression
        :returns: a deque with"""

        pass

    @staticmethod
    def _tokenize(expression):

        """Parses an expression into tokens for the Shunting Yard Algorithm. Behaves indefinitely for ill written and
         non infix expressions.
        :parameter expression: string containing an infix mathematical expression.
        :returns: a queue with the tokens"""

        expression = ''.join(expression.split())  # remove whitespace, probably inefficient
        tokens = Queue()  # Input tokens for the Shunting Yard

        token_index = 0
        char_index = 0
        # Each loop of this while loop processes one token
        while char_index < len(expression):
            token_start_char = expression[token_index]  # The first character of the token

            if token_start_char.isdigit():  # If the token is a number
                while char_index < len(expression) and \
                        expression[char_index].isdigit() or \
                        expression[char_index] == '.':
                    char_index += 1
            elif token_start_char.isalpha():  # If the token is a function (no numbers are allowed for functions)
                while char_index < len(expression) and expression[char_index].isalpha():
                    char_index += 1
            else:  # If the character is a single character operator
                char_index += 1

            if not token_start_char == ",":
                tokens.push(expression[token_index: char_index])  # Add the found token to the queue

            token_index = char_index

        return tokens


if __name__ == '__main__':
    start = datetime.now()
    print(ShuntingYard._tokenize("sin(10+lol(30))*max(1.5634,7,0)"))
    print(datetime.now() - start)

