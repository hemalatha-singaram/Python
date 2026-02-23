boys = {
    "v": {"age": 30, "role": "dancer"},
    "jk": {"age": 25, "role": "singer"},
    "jimin": {"age": 28, "role": "rapper"},
    "rm": {"age": 27, "role": "vocal"},
    "jhope": {"age": 26, "role": "dancer"},
    "suga": {"age": 29, "role": "producer"}
}

for name, info in boys.items():
    print(f"Name: {name}")
    for key, value in info.items():
        print(f"{key}:{value}")
    print()