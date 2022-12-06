//
// Created by peer on 6-12-22.
//
#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>

void	find_start_of_packet(const std::string& line, const size_t packet_length) {
	const char* const line_start = line.data();
	for (size_t i = packet_length; i < line.size(); i++) {
		auto end = line_start + i;
		std::unordered_set packet(end - packet_length, end);
		if (packet.size() == packet_length) {
			std::cout << i << '\n';
			return ;
		}
	}
}

int main() {
	std::ifstream input_file("../input.txt", std::ios::in);
	std::string line;

	if (!input_file.is_open()) {
		return (EXIT_FAILURE);
	}
	getline(input_file, line);
	find_start_of_packet(line, 4);
	find_start_of_packet(line, 14);
	return (EXIT_SUCCESS);
}
