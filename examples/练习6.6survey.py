person=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']
favourite_languages={
    'Alice':'Python',
    'Bob':'Java',
    'Charlie':'C++',
}
for name in person:
    if name in favourite_languages.keys():
        print(f"Thank you {name} for taking the poll.")
    else:
        print(f"{name}, please take the poll.")