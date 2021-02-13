import csv
import Code

my_emaillist=[]

with open("maillist.csv","r") as mail_list:
    pledgers=csv.DictReader(mail_list)
    for pledger in pledgers:
        info={'Name':pledger["NAME"],'Email':pledger["MAIL"]}
        if pledger["SEND"]=="TRUE":
            my_emaillist.append(info)


for person in my_emaillist:
    print(person["Email"])
    Code.send_email(person["Email"])
