import pandas as pd

cim=pd.read_csv("/storage/emulated/0/Download/census_income.csv")


#__________________________________________________________

print(" __________How many people of each race are represented__________  ")
#How many people of each race are represented
print("")





print(cim.race.value_counts())

#__________________________________________________________


print("")
print("__________Avarage of Men__________")
#avarge of mens
print("")






men=cim[cim.sex=='Male']
print(men)
print("Avarage of men is :", men.age.mean())


#__________________________________________________________


print("")
print("__________Percentage of people who have Bachelors degree___________")
#Bachelor presentage
print("    :")








a=cim.education[cim.education=='Bachelors']
percentage=(len(a) / len(cim.education))*100
print(percentage ,"%")


#__________________________________________________________
print("  ")
print("__________ percentage of people with advanced education (Bachelors Masters, or Doctorate) make more than 50K___________ ")
#percentage of people with advanced education (Bachelors Masters, or Doctorate) make more than 50K
print("     :")








b=cim[((cim.education=='Bachelors') | (cim.education=='Masters') | (cim.education=='Doctorate'))

&

(cim.income == '>50K')

]

print(
(len(b)/len(cim.education))*100," %"
)


#__________________________________________________________

print(" ")
print("__________percentage of people without advanced education make more than 50K__________")

# percentage of people without advanced education make more than 50K
print("     :")





c=cim[~((cim.education=='Bachelors') | (cim.education=='Masters') | (cim.education=='Doctorate'))

&

(cim.income == '>50K')

]

print(
(len(c)/len(cim.education))*100," %"
)

#__________________________________________________________

print("")
print("__________What is the minimum number of hours a person works per week__________")

# What is the minimum number of hours a person works per week
print("      :")




minh=cim.hours_per_week.min()
print('Minimum number of hours per week ' , minh)
d=cim[

(cim.hours_per_week==minh)

&

(cim.income == '>50K')

]

print(
(len(d)/len(cim.hours_per_week))*100," %"
)


#__________________________________________________________

print("")
print("__________percentage of the people who work the minimum number of hours per week have a salary of more than 50K__________")
#percentage of the people who work the minimum number of hours per week have a salary of more than 50K
print("")






e=cim[cim.income=='>50K'].native_country.value_counts()


print(

cim.native_country[e.max()] , 
" : " ,
 (e.max()/e.sum())*100 ,
  " % "
  
  )


#__________________________________________________________


print("")
print("__________most popular occupation for those who earn >50K in India__________ ")
#most popular occupation for those who earn >50K in India.
print("")




f=cim[

(cim.native_country=="India")

&

(cim.income==">50K")

]

print(

cim.occupation[
f.occupation.value_counts().max()
] ,
 " : " ,f.occupation.value_counts().max()

)










