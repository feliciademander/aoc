#ifndef STACK_HPP
#define STACK_HPP

#include <iostream>
#include <vector>

class Stack
{
public:
    Stack() {}
    void print();
    std::vector<char> crates;
};

void Stack::print()
{
    std::cout << "Stack(";
    for (char &c : this->crates)
        std::cout << c;
    std::cout << ")" << std::endl;
}

#endif // STACK_HPP
