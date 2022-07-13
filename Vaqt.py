from datetime import datetime, timedelta

vaqt = datetime.now()

print(vaqt.year)
print(vaqt.month)
print(vaqt.day)
print(vaqt.hour)
print(vaqt.minute)
print(vaqt.second)
print(vaqt.microsecond)
print(vaqt.weekday())

delta = timedelta(days=40, seconds=45)

vaqt_40_kundan_keyin = vaqt + delta
print(vaqt_40_kundan_keyin)

print(vaqt.strftime("%Y-%m-%d %A %B %a %b %H:%M"))
matn = "2021-12-01 Wednesday December Wed Dec 10:22"

kecha = datetime(year=2021, month=11, day=30)
print(kecha.year)
print(kecha)