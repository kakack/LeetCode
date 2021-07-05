/*
Given a chemical formula (given as a string), return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.





Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Example 4:

Input: formula = "Be32"
Output: "Be32"


Constraints:

1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.
*/
#include <string>
#include <unordered_map>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    string countOfAtoms(string formula) {
        int i = 0, n = formula.length();
        auto parseAtom = [&]() -> string {
            string atom;
            atom += formula[i++];
            while (i < n && islower(formula[i])) {
                atom += formula[i++];
            }
            return atom;
        };

        auto parseNum = [&]() -> int {
            if (i ==n || !isdigit(formula[i])) {
                return 1;
            }
            int num = 0;
            while (i < n && isdigit(formula[i])) {
                num = num * 10 + int(formula[i++] - '0');
            }
            return num;
        };
        stack<unordered_map<string, int>> stk;
        stk.push({});
        while (i < n) {
            char ch = formula[i]; 
            if (ch == '(') {
                i ++;
                stk.push({});
            } else if (ch == ')') {
                i ++;
                int num = parseNum();
                auto atomNum = stk.top();
                stk.pop();
                for (auto &[atom, v]: atomNum) {
                    stk.top()[atom] += v* num;
                }
            } else {
                string atom = parseAtom();
                int num = parseNum();
                stk.top()[atom] += num;
            }
        }
        auto &atomNum = stk.top();
        vector<pair<string, int>> pairs;
        for (auto &[atom, v]: atomNum) {
            pairs.emplace_back(atom, v);
        }
        sort(pairs.begin(), pairs.end());
        string ans;
        for (auto &p : pairs) {
            ans += p.first;
            if (p.second > 1) {
                ans += to_string(p.second);
            }
        }
        return ans;
    }
};