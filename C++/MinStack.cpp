// Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

// push(x) -- Push element x onto stack.
// pop() -- Removes the element on top of the stack.
// top() -- Get the top element.
// getMin() -- Retrieve the minimum element in the stack.

// Example:

// MinStack minStack = new MinStack();
// minStack.push(-2);
// minStack.push(0);
// minStack.push(-3);
// minStack.getMin();   --> Returns -3.
// minStack.pop();
// minStack.top();      --> Returns 0.
// minStack.getMin();   --> Returns -2.

#include <stack>
#include <iostream>

using namespace std;

class MinStack
{
public:
    /** initialize your data structure here. */
    MinStack()
    {
    }

    void push(int x)
    {
        if(min.empty() || x < min.top()){
            min.push(x);
        }
        origin.push(x);
    }

    void pop()
    {
        if(origin.top() == min.top()){
            min.pop();
        }
        origin.pop();
    }

    int top()
    {
        return origin.top();
    }

    int getMin()
    {
        return min.top()
    }

private:
    stack<int> origin, min;
};
