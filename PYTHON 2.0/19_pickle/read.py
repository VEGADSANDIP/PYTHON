# Read the list from the file
with open("my_list.pkl", "rb") as file:
    loaded_list = pickle.load(file)

print("Loaded list:", loaded_list)
