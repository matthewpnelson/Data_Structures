import operator
import string
import decimal

d = decimal.Decimal


# Define an Array Stack (code via Goodrich et al. )
class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        self._data = []                 # nonpublic list instance

    def len(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self,e):
        """Add element e to the top of the stack."""
        self._data.append(e)            # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
           Raise Empty exception if the stack is empty.
        """

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]           # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
           Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()         # remove last item from list


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass



def eval_postfix(stack):
    """A function to evaluate postfix notation, utilizing an Array based Stack

    Postfix Example:
    5 2 + 8 3 - * 4 /
    is equal to:
    ((5 + 2) * (8 - 3)) / 4

    """
    current = []
    op = ''
    stack_results = ArrayStack()

    while not stack.is_empty():
        current = stack.pop()

        # Select first numbers up to the first operator in the stack
        # Continue to populate the main results stack with input numbers
        if current not in ["+","-","*","/"]:
            try:
                stack_results.push((int(current)))
                continue
            except:
                raise Exception('The input file included non integers or allowable operators "+","-","*","/" ')
        else:
            op = current

        # Calculate the current step when an operator is present
        stack_results2 = stack_results.pop()
        stack_results1 = stack_results.pop()
        if op == "+":
            stack_results.push(d(operator.add(stack_results1, stack_results2)))
        elif op == "-":
            stack_results.push(d(operator.sub(stack_results1, stack_results2)))
        elif op == "*":
            stack_results.push(d(operator.mul(stack_results1, stack_results2)))
        elif op == "/":
            stack_results.push(d(operator.truediv(stack_results1, stack_results2)))

    else:
        pass            # when stack is empty, do not throw an Empty Exception

    return round(stack_results.top(), 2)





def convert(test):
    """Takes an input postfix expression and splits it into individual characters, while reversing
    its order in an array stack
    """

    test2 = test.split()
    stack_out = ArrayStack()

    #reverse the order of operations from the input file so the first number is at the top of the stack
    i = len(test2)-1
    while i >= 0:
        stack_out.push(test2[i])
        i -= 1
    return stack_out



# Run the script to evaluate postfix expressions provided in input.txt and save
# results in output.txt

with open('input.txt', 'rt') as f_in:
    out = ""
    for r in f_in.readlines():
        r = r.strip("\n")
        out += str(eval_postfix(convert(r))) + "\n"
with open('output.txt', 'wt') as f_out:
    f_out.write(out)
