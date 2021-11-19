lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
lst_input = input()
for i in range(1, len(lst_input)+1):
    for j in lst:
        lst_input = lst_input.replace(j, "*")
print(len(lst_input))
