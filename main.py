#iasianhack
#importing all the dependencies
import numpy as np
import pandas as pd
from tkinter import *
from tkinter import messagebox
from datas import disease
from datas import l1
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from datas import *


#defining the message function
def message():
    #use of if else statement to get the different value of user input symptoms and run of machine learning algorithm
    if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
        messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
       #calling the NaiveBayes function
    else :
        NaiveBayes()

#defination of naivebayes machine model
def NaiveBayes():
#creaing the instance gnb of the class MultinomialNB() class
    gnb = MultinomialNB()
    gnb=gnb.fit(X,np.ravel(y))#using the fit method of MultinomialNb Class to fit the dependent and independent data value from the given dataset

#predicting the new data using the data set and assigning it to y_pred using the naive bayes algorithm
    y_pred = gnb.predict(X_test)

#printing the accuracy of the test model using accuracy_score
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

#assigning the symptoms entered by the user to psymptoms
    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

#using the for loop from 0 to length og list l1
    for k in range(0,len(l1)):
        #use of the for loop till psymptoms
        for z in psymptoms:

            #if z is found in l1[k] l2[k]=1
            if(z==l1[k]):
                l2[k]=1
#assigning the inputtest=[l2]
    inputtest = [l2]
#prediction of the input test using the gnb instance created from the class MultinomialNB
    predict = gnb.predict(inputtest)

#predicting the different disease according to train machine model
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(disease[predicted] == disease[a]):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "No Disease")


#making and emplty list of length of the list l1
l2=[]
for x in range(0,len(l1)): #using the for loop
    l2.append(0)#using append funcion for the appending 0 on the empty list l2

# TESTING DATA
tr=pd.read_csv("Testing.csv")#reading the data set using panda
#replacing the tr with the values below
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)#all the multi dimensional are converted into single

# trainging the data
#reading the data set from csv file
df=pd.read_csv("Training.csv")
#replacing the prognosis in df
df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)
#assigning the df[l1] to X
X= df[l1]
#assigning y to df[prognosis]
y = df[["prognosis"]]
np.ravel(y)#changing the multidimensional list to single dimension


#initializing tkinter for gui
root = Tk()
root.title("Disease Prediction System")
root.configure()
#label for different smptoms
Symptom1 = StringVar()
Symptom1.set('👉🏻 Choose Symptom')
Symptom2 = StringVar()
Symptom2.set('👉🏻 Choose Symptom')
Symptom3 = StringVar()
Symptom3.set('👉🏻 Choose Symptom')
Symptom4 = StringVar()
Symptom4.set('👉🏻 Choose Symptom')
Symptom5 = StringVar()
Symptom5.set('👉🏻 Choose Symptom')

#creating text label for the title with different attributes
w2 = Label(root, justify=CENTER, text="    👨‍⚕ DISEASE---PREDICTION---BY---CURE---ME ‍⚕👩‍ ")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)

NameLb1 = Label(root, text="")
NameLb1.config(font=("Elephant", 20))
NameLb1.grid(row=5, column=1, pady=10,  sticky=W)

#creating the text label for symptoms with its different attributes
S1Lb = Label(root,  text="Symptom 1")
S1Lb.config(font=("Elephant", 15))
S1Lb.grid(row=7, column=1, pady=10 , sticky=W)

S2Lb = Label(root,  text="Symptom 2")
S2Lb.config(font=("Elephant", 15))
S2Lb.grid(row=8, column=1, pady=10, sticky=W)

S3Lb = Label(root,  text="Symptom 3")
S3Lb.config(font=("Elephant", 15))
S3Lb.grid(row=9, column=1, pady=10, sticky=W)

S4Lb = Label(root,  text="Symptom 4")
S4Lb.config(font=("Elephant", 15))
S4Lb.grid(row=10, column=1, pady=10, sticky=W)

S5Lb = Label(root,  text="Symptom 5")
S5Lb.config(font=("Elephant", 15))
S5Lb.grid(row=11, column=1, pady=10, sticky=W)

#creating the button named predict which predicts the different deseases according to our machine learning model
lr = Button(root, text="🏥 Predict 🏥",height=2, width=41, command=message)#command attribute calls the message fucntion
lr.config(font=("Elephant", 15))
lr.grid(row=13, column=1,pady=20, sticky=W)

#the option contains the sorted elements of the list l1
OPTIONS = sorted(l1)

#creating the option menue which contains the symptoms for different deasease which is inputted by the user
S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=7, column=1)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=8, column=1)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=9, column=1)

S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.grid(row=10, column=1)

S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.grid(row=11, column=1)

#creating the text label
NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 20))
NameLb.grid(row=13, column=0, pady=0,  sticky=W)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 15))
NameLb.grid(row=15, column=0, pady=0,  sticky=W)

#instances
t3 = Text(root, height=2, width=29)
t3.config(font=("Elephant", 20))
t3.grid(row=20, column=1,pady=0, sticky=W)

#end of the tkinter
root.mainloop()
