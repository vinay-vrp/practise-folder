# info = {
#     "name" : "vinay",
#     "age" : 45,
#     "sub" :["math","science","bio","mf"],
#     id : 12
# }
# print(info)

# info["name"]= "jhon-wick"
# print(info)
# info["shambhu"] = 456
# print(info)

name ={
    "name ": "vinay",
      "sub" :{
          "maht":15,
          "scie" :45,
          "bio" : 78 ,        

    }
}

print(name.keys())
print(list(name.values()))
print(name.items())
print(name.get('name'))
print(name.update({"city":"delhi"}))
name.update({"city":"delhi"})
print(name )