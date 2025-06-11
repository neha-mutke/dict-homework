
bigdb = {}

movies_2022 = {}

name1 = "Bhool Bhulaiyaa2"
name2 = "Brahmastra"

casting1 = ('Tabu', 'Kartik Aaryan', 'Kiara Advan' )
casting2 = ("Amitabh Bachchan", "Ranbir Kapoor", "Alia Bhatt", "Mouni Roy", "Nagarjuna" )

movies_2022[name1] = casting1
movies_2022[name2] = casting2
# print(type(movies_2022),movies_2022)

movies_2023 = {}

name3 = "Pathaan"
name4 = "Tu Jhoothi Main Makkaar"

casting1 = ("SRK","Deepika Padukone","John Abraham","Dimple Kapadia","Ashutosh Rana")
casting2 = ( "Ranbir Kapoor","Shraddha Kapoor","Dimple Kapadia","Boney Kapoor","Kartik Aaryan")

movies_2023[name3] = casting1
movies_2023[name4] = casting2
# print(movies_2023)

movies_2024 = {}

name5 = "Shaitaan"
name6 = "Bade Miyan Chote Miyan"

casting1 = ( "Ajay Devgn","R. Madhavan","Jyothika","Janki Bodiwala")
casting2 = ("Akshay Kumar","Tiger Shroff","Manushi Chhillar","Alaya F" )

movies_2024[name5] = casting1
movies_2024[name6] = casting2
# print(movies_2024)

movies_2025 = {}

name7 = "Kesari Chapter2" 
name8 = "Sikandar"

casting1 = ( "Akshay Kumar", "R. Madhavan", "Ananya Panday" )
casting2 = ("Salman Khan","Rashmika Mandanna","Kajal Aggarwal", "Sanjay Kapoor", "Prateik Babbar",)

movies_2025[name7] = casting1
movies_2025[name8] = casting2
# print(movies_2025)

bigdb.update(movies_2022)
bigdb.update(movies_2023)
bigdb.update(movies_2024)
bigdb.update(movies_2025)
print(bigdb)

# slicing the big dictionary
print(bigdb[name1][0])  #Tabu
print(bigdb[name2][0])  #Amitabh Bachchan
print(bigdb[name3][0])  #SRK
print(bigdb[name4][0])  #Ranbir kapoor
print(bigdb[name5][0])  #Ajay devgan
print(bigdb[name6][0])  #Akshay kumar
print(bigdb[name7][0])  #Akshay kumar
print(bigdb[name8][0])  #Salman khan
print(bigdb[name3][2])  #john abhram random accesing

# print cast with movie name from each dict
for i in bigdb[name6],[name6]:
    print("casting from given dict :-",i)

print(bigdb.keys())  
print(bigdb.values()) 


for names in bigdb.keys():
    print(names,"====>",bigdb[names])


for i in bigdb.values():
    print(i)
    for cast in i:
        if cast == "Akshay Kumar":
           print(cast)

for k,v in bigdb.items():
    print(k,"===>",v)   

for t in bigdb.items():
    k,v=t            
print(t)