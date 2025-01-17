import csv
import pandas
import matplotlib.pyplot as plt
print("EXPENSE TRACKER")
ch=0
while(ch!=4):
    print("1.Add Your Expense \n2.view data \n3.visualize \n4.exit")
    ch=int(input("enter the choice :"))
    if(ch==1):
        cat=input("Enter the category : ")
        amount=int(input("Enter the amount : "))
        date1=input("Enter the date : ")
        try:
            file=open("datas.csv",'r')
            file.close()
        except:
            file=open("datas.csv",mode='w',newline='')
            writer=csv.writer(file)
            writer.writerow(["category","amount","date"])
            file.close()
        row=[cat,amount,date1]
        file=open("datas.csv",'a')
        writer=csv.writer(file)
        writer.writerow(row)
        file.close()
    if(ch==2):
        pd=pandas.read_csv("datas.csv")
        print(pd.tail(10))
        sum=0
        for i in pd["amount"]:
            sum=sum+i
        print("total = ",sum)
    if(ch==3):
        pd=pandas.read_csv("datas.csv")
        plt.subplot(1,2,1)
        show=pd.groupby("category")["amount"].sum()
        colors = ['red', 'green', 'blue', 'orange']
        show.plot(kind="bar", figsize=(8, 6), title="Expenses by Category", color=colors)

        plt.xlabel("Category")
        plt.ylabel("Total Amount")
        
        plt.subplot(1,2,2)
        show1=pd.groupby("date")["amount"].sum()
     
        show1.plot(kind="line", figsize=(8, 6), title="Expenses by date", marker = 'o', ms = 15, mfc = 'r')
        plt.xlabel("date")
        plt.ylabel("Total Amount")
        plt.show()
        
        