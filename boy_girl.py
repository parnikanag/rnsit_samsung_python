def can_arrange_students(n, boys, girls):
    boys.sort()
    girls.sort()

    arrangement1 = []
    arrangement2 = []

    for i in range(n):
        arrangement1.append(boys[i])
        arrangement1.append(girls[i])

        arrangement2.append(girls[i])
        arrangement2.append(boys[i])

    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    if is_sorted(arrangement1) or is_sorted(arrangement2):
        return "YES"
    return "NO"

t = int(input("Enter number of test cases: "))

for i in range(t):
    n = int(input("\nEnter number of boys and girls: "))
    
    boys = list(map(int, input("Enter boys' heights: ").split()))
    girls = list(map(int, input("Enter girls' heights: ").split()))

    print(can_arrange_students(n, boys, girls))
