
# user1 = chatbook()
# lst = [1,2,3]
# a1= len(lst)
# print(f"Print the list - {a1}")

# --> Getter and setter
# from  oops_proj import chatbook
# user1 = chatbook()
# print(user1.get_name())
# user1.set_name("Aman")

# print(user1.get_name())


from oops_proj import chatbook
# user1 = chatbook()
# print(user1.user_id) 



#Using static
chatbook.set_id(10)
user2=chatbook()
print(user2.id)