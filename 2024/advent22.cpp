#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;
typedef long long unsigned ll;

template <typename Container> // we can make this generic for any container [1]
struct container_hash {
    std::size_t operator()(Container const& c) const {
        size_t h = 0;
        int m = 1;
        for (int i=0; i<4; i++) {
            h += (c[i]+9)*m;
            m *= 30;
        }
        // cout<<h<<'\n';
        return h;
    }
};

const ll mod = 16777216;

ll next_random(ll secret) {
    secret = (secret ^ (secret*64))%mod;
    secret = ((secret/32)^secret)%mod;
    secret = (((secret*2048)^secret)%mod);
    return secret;
}

void part1() {
    ifstream file("input22.txt");
    string line;

    ll s = 0;


    while (getline(file, line)) {
        ll n = stoi(line);
        for (int i=0; i<2000; i++) {
            n = next_random(n);
        }
        s += n;
    }

    cout<<'\n'<<s<<'\n'<<next_random(123);
}

void part2() {
    unordered_map<vector<int>, int, container_hash<vector<int>>> prices;

    ifstream file("input22.txt");
    string line;

    while (getline(file, line)) {
        ll prev = stoi(line);
        vector<int> diffs;
        unordered_set<vector<int>, container_hash<vector<int>>> seen;


        for (int i=0; i<4; i++) {
            ll nxt = next_random(prev);
            diffs.push_back(nxt%10-prev%10);
            prev = nxt;
        }

        for (int i=0; i<2000-3; i++) {
            int price = prev%10;
            if (seen.find(diffs) == seen.end()) {
                seen.insert(diffs);
                prices[diffs] += price;
            }

            ll nxt = next_random(prev);
            diffs.push_back(nxt%10-prev%10);
            diffs.erase(diffs.begin());
            prev = nxt;

        }
        
    }

    int best = 0;
    for (auto& item : prices) {
        best = std::max(best, item.second);
    }

    cout << best;
}

int main() {
    cout <<"\n";
    part2();

    return 0;
}