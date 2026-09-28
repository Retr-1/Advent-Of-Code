#include <iostream>
#include <vector>
using namespace std;

int main() {
    cout << "Hello World\n";
    vector<int> nums;
    nums.push_back(10);
    cout << nums.at(0)<<'\n';
    return 0;    
}