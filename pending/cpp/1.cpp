#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    int n;
    cin >> n; // số phần tử
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    int target;
    cin >> target;

    unordered_map<int,int> mp; // lưu giá trị -> chỉ số
    for (int i = 0; i < n; i++) {
        int need = target - nums[i];
        if (mp.find(need) != mp.end()) {
            cout << mp[need] << " " << i << endl;
            return 0;
        }
        mp[nums[i]] = i;
    }
    return 0;
}
