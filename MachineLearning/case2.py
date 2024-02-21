#with input n and array a[]. write program print element numbers
def print_elements(n, a):
    for i in range(n):
        print("Element number {}: {}".format(i, a[i]))

a=[1,2,3,4,5,6,7,8,9,10]
n = len(a)  # assuming a is your array
print_elements(n, a)
