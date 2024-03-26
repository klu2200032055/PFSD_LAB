

'''
import pandas as pd
my_dict={
    "Name":["Ravi","Ram","Raja"],
    "Marks":[50,55,53]
}
df=pd.DataFrame(data=my_dict)
df.plot.line(title="Marks")
pic=df.plot.line()
pic=pic.get_figure()
#pic.savefig('a.jpg')

'''



import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])
mylabels=["DBMS","Python","OS","MP"]
plt.pie(y,labels=mylabels,startangle=90)
plt.show()



'''

#Example 4


#------------------------------------
#************************************
#------------------------------------


#Example 5
import matplotlib.pyplot as plt
import numpy as np
regnum = ['1', '2', '3','4']
categories = ["DBMS", "Python", "OS", "MP"]
values = np.array([
    [35, 25, 25, 15],  # Values for category "DBMS"
    [20, 30, 15, 35],  # Values for category "Python"
    [10, 40, 20, 30],  # Values for category "OS"
    [15, 30, 45, 40],
])
colors = ['red', 'blue', 'yellow', 'green']
# Plot area for each registration number and category
for i, reg in enumerate(regnum):
    plt.fill_between(categories, 0, values[i], label=f'Registration {reg}', color=colors[i], alpha=0.7)
# Add labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Area Plot with Different Colors")
plt.legend()
plt.show()






import pandas as pd
import matplotlib.pyplot as plt
def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df
def generate_graph(data_frame):
    x_values = data_frame['REGNUM']
    y_columns = data_frame.columns[1:]
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i,column in enumerate(y_columns):
        y_values = data_frame[column]
        plt.plot(x_values, y_values, marker='o', linestyle='-', label=column, color = colors[i])
    # plt.plot(x_values, y_values, marker='o', linestyle='-', color=colors)
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('CSV Data Plot')
    plt.grid(True)
    plt.legend()
    #plt.savefig("a1.png")
    plt.show()

if __name__ == "__main__":
    file_path = "csf.csv"
    data_frame = read_csv_file(file_path)
    generate_graph(data_frame)


import random
import string
S=10
ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=S))
s1=4
ran1=''.join(random.sample(string.digits,k=6))
print(ran1)
print("Random of Alpha and Digits ")
print(ran)





n=random.randbytes(4)
print(n)
print(random.randrange(0,9)) #in increasing order it includes  and 9 Also

print(random.randint(100,211))
print("||")
mylist=("Jai","Sri","Ram","Hari","Om","Kapardhi")
mylist1={"Jai","Sri","Ram","Hari","Om","Kapardhi"}
mylist2=["Jai","Sri","Ram","Hari","Om","Kapardhi"]
print(random.choice(mylist))
#print(random.choice(mylist1))
#print(random.choice(mylist2))

print(random.shuffle(mylist2))
'''





'''
() = tupple 
{} = Set 
[] = list 
'''

'''

class Parent:
    def function1(self):
        print("this is function one")

class Child(Parent):
    def function2(self,a):
        print("this is function two")
        print(a)
    b=20

y=Child()
y.function1()
y.function2(10)
print(y.b)

'''



