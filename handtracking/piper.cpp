#include <iostream>
#include <string>
#include <iostream>
#include <fstream>
#include <unistd.h>
// int main() {
//     std::ofstream myfile;

//     for (std::string line; std::getline(std::cin, line);) {
//         myfile.open ("bigpp.txt", std::ofstream::app);
//         myfile << line << std::endl;
//         myfile.close();
//     }
//     return 0;
// }

int main() {
    std::ifstream ifs("test.txt");

    std::string line;
    while(1) {
        while(std::getline(ifs, line)) {
            std::cout << line << std::endl;
        }
        ifs.clear();
    }
}