# Multi-dimention List(nested list)
 

customer = ["Joseph", "Nyahururu", ["jose@gmail.com", "07112345678"], ["Vegetables", "Flowers","Fruits"]]

# 1. Access Joseph's phone 
name =customer[2][1]
print(name)

# 2. Access Vegetables and Flowers only
vegitables = customer[3][0:2]
print(vegitables)
