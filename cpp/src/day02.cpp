#include <iostream>
#include <sstream>
#include "fmt/ranges.h"
#include "../include/day02.h"

int64_t day02::part01(const std::shared_ptr<std::vector<std::string>>& input_data) {
    std::vector<std::vector<int8_t>> reports;
    int64_t total = 0;

    for (const std::string& line : *input_data) {
        std::cout << line << std::endl;
    }

    for (std::basic_string<char> line: *input_data) {
        std::vector<int8_t> report;

        std::istringstream stream(line);
        int num;
        while (stream >> num) {
            report.push_back(num);
        }

        reports.push_back(report);
    }

    for (const std::vector<int8_t>& report : reports) {
        int8_t currentNumber = report[0];
        bool isIncreasing = (report[1] - report[0] > 0);
        bool isValid = true;
        for (auto nextNumber = report.begin() + 1;
            nextNumber != report.end();
            ++nextNumber)
        {
            int8_t difference = *nextNumber - currentNumber;

            if (difference < -3 || difference == 0 || difference > 3) {
                isValid = false;
                break;
            }

            if (!isIncreasing == (difference > 0)) {
                isValid = false;
                break;
            }

            currentNumber = *nextNumber;
        }

        if (isValid){
            total++;
        }
    }

    return total;
}
