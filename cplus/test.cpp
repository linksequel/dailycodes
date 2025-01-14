#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>
using namespace std;

template <typename T>
class Set {
public:
    Set(T *input, int inputlen);
    void display(string s) {
        cout << "total len of "<< s << " is: " << totalLen << endl; 
        for (int i = 0; i < totalLen; i++) {
            cout << deduplication[i] << " ";
        }
        cout << endl;
    }
    static Set<T> unionFuc(const Set<T>& A, const Set<T>& B);
    // 声明为静态成员函数
    static bool checkCurrentDuplicated(T current, const Set<T>& before);

private:
    int totalLen;
    T *deduplication;
    // 去重函数
    T* removeDuplicates(T* input, int inputlen) {
        if (inputlen == 0) {
            totalLen = 0;
            deduplication = nullptr;
            return nullptr;
        }
        totalLen = inputlen;
        deduplication = new T[totalLen];
        for (int i = 0; i < totalLen; ++i) {
            deduplication[i] = input[i];
        }
        int newSize = 1;
        for (int i = 1; i < totalLen; ++i) {
            bool isDuplicate = false;
            for (int j = 0; j < newSize; ++j) {
                if (deduplication[j] == deduplication[i]) {
                    isDuplicate = true;
                    break;
                }
            }
            if (!isDuplicate) {
                deduplication[newSize++] = deduplication[i];
            }
        }
        // inputlen太大，删除没用的空间
        T* newDeduplication = new T[newSize];
        for (int i = 0; i < newSize; ++i) {
            newDeduplication[i] = deduplication[i];
        }
        delete[] deduplication;
        deduplication = newDeduplication;
        totalLen = newSize;
        return deduplication;
    }

};


template <typename T>
// 实现为静态成员函数
bool Set<T>::checkCurrentDuplicated(T current, const Set<T>& before) {
    if (before.deduplication == nullptr) {
        return false;
    }
    for (int i = 0; i < before.totalLen; ++i) {
        if (before.deduplication[i] == current) {
            return true;
        }
    }
    return false;
}


template <typename T>
Set<T>::Set(T *input, int inputlen) {
    deduplication = removeDuplicates(input, inputlen);
}


template <typename T>
Set<T> Set<T>::unionFuc(const Set<T>& input1, const Set<T>& input2) {
    int finalLen = input1.totalLen + input2.totalLen;
    T *res = new T[finalLen];
    int idx = 0;
    // 将 input1 的元素复制到 res 中
    for (int curIdx = 0; curIdx < input1.totalLen; curIdx++) {
        res[idx++] = input1.deduplication[curIdx];
    }
    // 检查 input2 的元素是否在 input1 中出现过，如果没有则添加到 res 中
    for (int curIdx = 0; curIdx < input2.totalLen; curIdx++) {
        bool showsOnInput1 = checkCurrentDuplicated(input2.deduplication[curIdx], input1);
        if (!showsOnInput1) {
            res[idx++] = input2.deduplication[curIdx];
        }
    }
    // 创建新的 Set 对象存储结果
    T* finalDeduplication = new T[idx];
    for (int i = 0; i < idx; ++i) {
        finalDeduplication[i] = res[i];
    }
    delete[] res;
    Set<T> result(finalDeduplication, idx);
    delete[] finalDeduplication;
    return result;
}


int main() {
    int a[] = {1, 2, 2, 3, 4, 5};
    int b[] = {6, 7, 5, 8, 4, 5};
    Set<int> input1(a, 6);
    Set<int> input2(b, 6);
    Set<int> merge = Set<int>::unionFuc(input1, input2);
    input1.display("input1");
    input2.display("input2");
    merge.display("merge");
    return 0;
}