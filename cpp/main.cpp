#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <memory>
#include <vector>
#include <iomanip>
#include "include/day02.h"


std::string handleArgs(int argc, char* argv[], int &day, int &part) {
    std::string final_flag, path;
    bool isFinal = false;

    // Parse command-line arguments
    for (int i = 1; i < argc; i++) {
        std::string arg = argv[i];

        if (arg == "-p" || arg == "--part") {
            if (i + 1 < argc) {
                part = std::stoi(argv[++i]);  // Get part (1 or 2)
            }
        } else if (arg == "-d" || arg == "--day") {
            if (i + 1 < argc) {
                day = std::stoi(argv[++i]);  // Get the day (1 to 25)
            }
        } else if (arg == "-f" || arg == "--final") {
            isFinal = true;  // Set final flag if present
        }
    }

    // Validate day (1 to 25)
    if (day < 1 || day > 25) {
        std::cerr << "Error: Day must be between 1 and 25." << std::endl;
        exit(EXIT_FAILURE);
    }

    // Validate part
    if (part != 1 && part != 2) {
        std::cerr << "Error: Part must be 1 or 2." << std::endl;
        exit(EXIT_FAILURE);
    }

    // Construct the path based on the input arguments
    std::ostringstream filename;
    filename << "input/" << std::setw(2) << std::setfill('0') << day;
    
    // Append "-test" if -f or --final is not present
    if (!isFinal) {
        filename << "-test";
    }
    filename << ".txt";

    path = filename.str();

    // Return the final path
    return path;
}


std::shared_ptr<std::vector<std::string>> readFile(const std::string& filename) {
    auto lines = std::make_shared<std::vector<std::string>>(); // Dynamically allocated vector
    std::ifstream file(filename);

    if (!file) {
        std::cerr << "Error: Could not open the file." << std::endl;
        return nullptr; // Return nullptr if file can't be opened
    }

    std::string line;
    while (std::getline(file, line)) {
        lines->push_back(line); // Store each line in the vector
    }

    return lines;
}

int main(int argc, char* argv[]) {
    int day, part;
    std::string filePath = handleArgs(argc, argv, day, part);

    auto lines = readFile(filePath);

    if (!lines) {
        return 1; // Exit if file couldn't be read
    }

    int combo = day * 10 + part;

    switch (combo) {
        case 21:
            day02::part01(lines);
    }
    return 0;
}

