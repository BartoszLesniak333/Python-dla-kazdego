import pickle, shelve

variety = ["łagodny", "pikantny", "kwaszony"]
shape = ["cały", "krojony wzdłuż", "w plasterkach"]
brand = ["Dawtona", "Klimex", "Vortumnus"]

f = open("pikle1.dat","wb")

pickle.dump(variety,f)
pickle.dump(shape,f)
pickle.dump(brand,f)

f.close()

f= open("pikle1.dat","rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()

s = shelve.open("pikle2.dat")

s["odmiana"] = ["łagodny", "pikantny", "kwaszony"]
s["kształt"] = ["cały", "krojony wzdłuż", "w plasterkach"]
s["marka"] = ["Dawtona", "Klimex", "Vortumnus"]

s.sync()

print("marka -", s["marka"])

s.close()