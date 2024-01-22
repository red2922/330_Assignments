import matplotlib.pyplot as plt
import numpy as np

#Single Line
x_line = [1,8]
y_line = [3,10]

plt.subplot(5,5,1)
#Rows then columns then index
plt.title("First Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x_line,y_line)

#X and Y Line
x_m = [1,2,3,4]
y_m = [3,8,1,10]

plt.subplot(5,5,3)
plt.title("Second Graph")
plt.xlabel("X_M")
plt.ylabel("Y_M")
plt.plot(x_m,y_m,"o:r",mfc = 'blue', linewidth = '3.2')

#Just Y value
y_p = [3,5,2,1,10,5,6,8,12]

plt.subplot(5,5,5)
plt.title("Third Graph")
plt.xlabel("J_X")
plt.ylabel("J_Y")

plt.grid(axis = 'y')
plt.plot(y_p, "o:b")

#ScatterPlots

x_s = [5,6,7,10,12,13,17,18,20]
y_s = [50,70,90,20,30,35,40,65,60]
colors = [0,10,20,30,40,50,60,70,100]

plt.subplot(5,5,11)
plt.title("Fourth Graph")
plt.xlabel("S_X")
plt.ylabel("S_Y")

plt.scatter(x_s,y_s,c = colors, cmap = 'GnBu', alpha = 0.5)

plt.colorbar()


#Vertical Bar Graph

x_v = ["A","B","C",'D']
y_v = [2,3,1,0]

plt.subplot(5,5,13)
plt.title("Fifth Graph")
plt.xlabel("V_X")
plt.ylabel("V_X")
plt.bar(x_v,y_v,color = 'Green', width = 0.1)

#Horizontal Bar Graph

x_h = ['A','B','C','D']
y_h = [5.5,6.0,6.2,5.3]

plt.subplot(5,5,15)
plt.title("Sixth Graph")
plt.xlabel("Hb_X")
plt.ylabel("Hb_X")
plt.barh(x_h,y_h,color = 'Purple', height = 0.3)


#Histogram
x_g = np.random.normal(170,10,250)

plt.subplot(5,5,21)
plt.title("Seventh Graph")
plt.xlabel("H_X")
plt.ylabel("H_X")

plt.hist(x_g, color = 'orange')

#Standard Pie

pie_array = [35,25,25,2]
my_labels = ["Daisy", "Lily", "Violet", "Rose"]
my_colors = ['Grey', 'Yellow', 'Purple', 'White']

plt.subplot(5,5,23)
plt.title("Flower Graph")

plt.pie(pie_array, labels = my_labels, colors = my_colors)

#Exploded Pie

p_array = [60,30,70,20]
new_labels = ["One", "Two", "Three", "Four"]
new_colors = ['Blue', 'Red', 'Green', 'Black']
explodes = [.5,0,0,0]

plt.subplot(5,5,25)
plt.title("Final Graph")

plt.pie(p_array, labels = new_labels, colors = new_colors, explode = explodes, shadow = True)

plt.suptitle("All Different Types of Graphs")
plt.show()


