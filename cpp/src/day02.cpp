#include <cstdint>
#include <iostream>
#include <sstream>
#include "fmt/ranges.h"
#include "../include/aoc.h"

int64_t day02::part01(const std::shared_ptr<std::vector<std::string>>& input_data) {
    std::vector<std::vector<int8_t>> reports;
    int64_t total = 0;

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

bool
day02::isSequenceValid(std::vector<int8_t> report)
{
    if (report.size() < 2) {
        return false; // A valid sequence must have at least two elements
    }

    auto it = report.begin();
    int8_t currentNumber = *it;
    ++it;
    int8_t nextNumber = *it;
    bool isIncreasing = (nextNumber - currentNumber > 0);
    bool isValid = true;

    for (; it != report.end(); ++it)
    {
        int8_t difference = *it - currentNumber;

        if (difference < -3 || difference == 0 || difference > 3) {
            isValid = false;
            break;
        }

        if (!isIncreasing == (difference > 0)) {
            isValid = false;
            break;
        }

        currentNumber = *it;
    }

    return isValid;
}

int64_t
day02::part02(const std::shared_ptr<std::vector<std::string>> &input_data)
{

    std::vector<std::vector<int8_t>> reports;
    int64_t total = 0;

    for (std::basic_string<char> line: *input_data) {
        std::vector<int8_t> report;

        std::istringstream stream(line);
        int num;
        while (stream >> num) {
            report.push_back(num);
        }

        reports.push_back(report);
    }

    for (std::vector<int8_t> report : reports) {
        for (unsigned long i = 0; i != report.size(); i++) {
            report.erase(report.begin() + 1);
            if(day02::isSequenceValid(report)){
                total++;
            }
        }
    }
    return total;
}



