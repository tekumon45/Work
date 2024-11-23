from collections import namedtuple, defaultdict

# フィールド名のリストから動的に生成
fields = ["x", "y", "z"]
Point3D = namedtuple("Point3d", fields)

p = Point3D(1, 2, 3)
print(p.x, p.y, p.z)

# リストを値とするdefaultdictを生成
group_by_age = defaultdict(list)

people = [("Alice", 25), ("Bob", 30), ("Sana", 25)]

for name, age in people:
    group_by_age[age].append(name)
    
print(group_by_age)