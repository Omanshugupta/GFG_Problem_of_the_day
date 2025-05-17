class Solution:
    def sortArray(self, arr, A, B, C):
        def f(x):
            return A * x * x + B * x + C

        n = len(arr)
        result = [0] * n
        i, j = 0, n - 1
        index = n - 1 if A >= 0 else 0

        while i <= j:
            left, right = f(arr[i]), f(arr[j])
            if A >= 0:
                if left > right:
                    result[index] = left
                    i += 1
                else:
                    result[index] = right
                    j -= 1
                index -= 1
            else:
                if left < right:
                    result[index] = left
                    i += 1
                else:
                    result[index] = right
                    j -= 1
                index += 1

        return result


def main():
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        arr = [-4, -2, 0, 2, 4]
        A = 1
        B = 3
        C = 5

        ob = Solution()  # Fix: instantiate the class
        ans = ob.sortArray(arr, A, B, C)
        print(' '.join(map(str, ans)))
        print("~")

if __name__ == "__main__":
    main()
