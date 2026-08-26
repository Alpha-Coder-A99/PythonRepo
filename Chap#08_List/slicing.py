# Areeba's Study Schedule List
hours = ["9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm"]

# 1. Basic Slice (11am se 2pm tak)
# Index 2 se shuru, Index 5 par stop (taake 4 tak count ho)
print("Morning to Noon:", hours[2:5]) 
# Output: ['11am', '12pm', '1pm']

# 2. Step Slice (Ek ghanta chor kar ek)
# Shuru se aakhir tak, 2 ki chhalang
print("Alternate Hours:", hours[::2])
# Output: ['9am', '11am', '1pm', '3pm']

# 3. Reverse Slice (Ulat ginti)
print("Reverse Schedule:", hours[::-1])
# Output: ['4pm', '3pm', '2pm', '1pm', '12pm', '11am', '10am', '9am']

# 4. Negative Indexing Slice (Aakhir ke 3 ghante)
print("Last 3 Hours:", hours[-3:])
# Output: ['2pm', '3pm', '4pm']