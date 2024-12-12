#pragma once
#include <vector>
#include <list>
#include <memory>
#include <string>

namespace day02 {
    int64_t part01(const std::shared_ptr<std::vector<std::string>>& input_data);
    int64_t part02(const std::shared_ptr<std::vector<std::string>>& input_data);
    bool isSequenceValid(std::vector<int8_t> report);
}
