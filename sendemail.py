import csv
import Code

my_emaillist=[]

with open("maillist.csv","r") as mail_list:
    pledgers=csv.DictReader(mail_list)
    for pledger in pledgers:
        if pledger[2]:
            info=pledegr[0],pledger[1]
