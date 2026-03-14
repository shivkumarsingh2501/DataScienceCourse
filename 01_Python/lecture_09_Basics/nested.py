students = {
    "student1" :{
        "name" : "chris",
        "age" : 32
    },
    "student2" :{
        "name" :"Peter",
        "age":35
    }

}
print(students["student2"] ["name"])


for id,info in students.items():
    print(id)
    for key,value in info.items():
        print(key.value)

        