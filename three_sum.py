"""
20. Write a Python class to find the three elements that sum to zero from
    a list of n real numbers.
    Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
    Output : [[-10, 2, 8], [-7, -3, 10]]
"""


class Three():
    def sum(self, some_list):
        result = []
        some_list = sorted(some_list)
        length = len(some_list)
        for i in range(0, length - 2):
            for j in range(i+1, length - 1):
                for k in range(j+1, length):
                    if some_list[i] + some_list[j] + some_list[k] == 0:
                        result.append([some_list[i], some_list[j], some_list[k]])
                        found = True

        if not found:
            print("No such combination.")
        else:
            return result


obj = Three()
some_list = [-25, -10, -7, -3, 2, 4, 8, 10]
result = obj.sum(some_list)
print("Given list: ", some_list)
print("List with sum zero: ", result)
