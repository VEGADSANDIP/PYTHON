import pickle

my_list = [10, 20, 30, 40, 50, 60]

# Save the list to a file (e.g., "my_list.pkl")
with open("my_list.pkl", "wb") as file:
    pickle.dump(my_list, file)
