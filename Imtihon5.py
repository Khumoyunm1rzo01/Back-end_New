workers = [
    {
        "name": "Qo'shaqboy",
        "salary": 3500
    },
    {
        "name": "Muhammadzikir",
        "salary": 4000
    },
    {
        "name": "Humoyunmirzo",
        "salary": 5000
    },
    {
        "name": "Quvonchbek",
        "salary": 7000
    }]

salary_for_1_month = 0
for worker in workers:
    salary_for_1_month += worker["salary"]
n = int(input("N oyni kiriting: "))
print("Ishchilarga jami", salary_for_1_month*n, "to'lashimiz kerak!")