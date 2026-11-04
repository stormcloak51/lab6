#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

int main() {
    std::string text;
    std::cout << "Введите текст: ";
    std::getline(std::cin, text);

    std::string vowels = "aeiouаеёиоуыэюя";
    int count = 0;

    for (char c : text) {
        char lower_c = std::tolower(static_cast<unsigned char>(c));
        if (vowels.find(lower_c) != std::string::npos) {
            count++;
        }
    }

    std::cout << "Количество гласных: " << count << "\n";
    return 0;
}
