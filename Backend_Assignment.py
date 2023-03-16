import pandas as pd
import numpy as np



def main():
    ch = 1
    df = pd.read_csv("C:/1_cpp_allProgram_vscode/Jupyter Notebook/archive/diabetes.csv")


    while(ch != 7):
        print("Menu : \n\t "
              "1. Print The File \n\t 2. Print Total Number Of The Rows In The File \n\t 3. Print Total Number Of "
              "The Coloumns In The File \n\t 4. Mean Of The Numeric Coloumn \n\t 5. Filter The File \n\t 6. Sort The Coloumns In "
              "File On The Basis Of Coloumn Name \n\t 7. Exit \n")

        ch = int(input("Enter Your Choice : "))

        if(ch == 1):
            print(df)

        elif(ch == 2):
            row_count = sum(1 for row in df)
            print(row_count)

        elif(ch == 3):
            col_name = input("Enter The Row Name : ")

            key = 0
            for i in df:
                if(i == col_name):
                    col_count = sum(1 for coloumn in df[col_name])
                    print(col_count)
                    key = 1
                    break

            if(key == 0):
                print("Sorry! , Coloumn Named With ",col_name," Is Not Present In The File.\n")




        elif(ch == 4):
            col_name = input("Enter The Coloumn Name : ")

            key = 0
            for i in df:
                if(i == col_name):
                    col_mean = df[col_name].mean()
                    print(col_mean)
                    key = 1
                    break

            if(key == 0):
                print("Sorry! ,May Be The Coloumn Name Doesn't Match Or May Be It Is Not A Integer Typed Row")


        elif(ch == 5):
            col_name = input("Enter The Coloumn Name : ")
            val = int(input("Enter The Value : "))
            key = 0
            for i in range(0, len(df[col_name])):
                if val == df[col_name][i]:
                    key = 1
                    foundval = i
                    print(df.iloc[foundval:foundval + 1, :])

            if(key == 0):
                print("Sorry! Coloumn Name Doesn't Match")


        elif(ch == 6):
            col_name = input("Enter The Coloumn Name : ")

            ab = df.sort_values(by=[col_name])
            print(ab)




main()