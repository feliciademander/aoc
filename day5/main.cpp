#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

#include "Stack.hpp"

const std::string fname = "./input.txt";
typedef std::vector<std::string> str_vec;
typedef std::vector<Stack> stack_vec;

void parse_file(std::string filename,
				str_vec &moves,
				str_vec &stack_input)
{
	std::ifstream input;
	input.open(filename, std::ios::in);

	if (input.is_open())
	{
		std::string line = "";
		while (getline(input, line))
		{
			if (line[0] == 'm')
			{
				moves.push_back(line);
			}
			else if (!empty(line)) // Stacks
			{
				stack_input.push_back(line);
			}
		}
		input.close();
	}
	else
		exit(EXIT_FAILURE);
}

int get_num_stacks(std::string str)
{
	int num = -1;
	try
	{
		num = atoi(&str[str.length() - 2]);
	}
	catch (...)
	{
	}

	return num;
}

void init_stacks(stack_vec &stacks, str_vec &stack_input)
{
	std::string line = stack_input.back();
	int num_stacks = get_num_stacks(line);
	if (num_stacks == -1)
		exit(EXIT_FAILURE);

	for (int i = num_stacks; i > 0; i--)
	{
		stacks.push_back(Stack());
	}

	for (int j = stack_input.size() - 2; j >= 0; j--)
	{
		std::string line = stack_input[j];
		for (size_t k = 0; k < line.length(); k += 4)
		{
			std::string pos = line.substr(k, 4);
			char c = pos[1];
			if (!isspace(c))
				stacks[k / 4].crates.push_back(c);
		}
	}
}

void move_crate(Stack &dest, Stack &src, int n)
{
	char crate;
	for (int i = n; i > 0; i--)
	{
		if (!src.crates.size())
			continue;
		crate = src.crates.back();
		src.crates.pop_back();
		dest.crates.push_back(crate);
	}
}

void print_vecs(str_vec &moves, str_vec &stack_input)
{
	std::cout << "Stack input: " << std::endl;
	for (auto &el : stack_input)
		std::cout << el << std::endl;
	std::cout << "\nMoves: " << std::endl;
	for (auto &el : moves)
		std::cout << el << std::endl;
}

void print_stacks(stack_vec &stacks)
{
	std::cout << "\nPrinting stacks:" << std::endl;
	for (auto &el : stacks)
		el.print();
}

int main(int argc, char *argv[])
{
	str_vec moves;
	str_vec stack_input;
	std::vector<Stack> stacks;

	parse_file(fname, moves, stack_input);
	init_stacks(stacks, stack_input);
	// print_stacks(stacks); // Debug

	// Perform moves
	int count;
	std::vector<int> numbers;
	for (auto &move : moves)
	{
		std::string value;
		std::stringstream linestream = std::stringstream(move);
		while (getline(linestream, value, ' '))
		{
			if (++count % 2)
				continue;
			numbers.push_back(stoi(value));
		}
	}

	for (size_t i = 0; i < numbers.size(); i += 3)
	{
		int n = numbers[i];
		int from = numbers[i + 1];
		int to = numbers[i + 2];
		move_crate(stacks[to - 1], stacks[from - 1], n);
	}
	print_stacks(stacks);
}
