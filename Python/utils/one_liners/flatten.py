flatten = lambda target: sum((flatten(sub) if isinstance(sub, list) else [sub] for sub in target), [])

user_list = [1,2,3, [4,5,6, [7,8,9]]]
print(f'{flatten(user_list)=}')