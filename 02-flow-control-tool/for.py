words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))


# 很难正确地在迭代多项集的同时修改多项集的内容。更简单的方法是迭代多项集的副本或者创建新的多项集
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]



active_users = {}
for user, status in users.copy().items():
    if status == 'active':
        active_users[user] = status