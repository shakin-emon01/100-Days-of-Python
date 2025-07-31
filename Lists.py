# Lists

Division_of_Bangladesh = ["Dhaka", "Chittagong", "Khulna", "Rajshahi", "Barisal", "Sylhet", "Rangpur", "Mymensingh"]
Division_of_Bangladesh[4] = "Barishal"  # Correcting the spelling of Barisal to Barishal
print("Division of Bangladesh:" + Division_of_Bangladesh[0])
# Adding a new division
Division_of_Bangladesh.append("Gazipur")
# Adding multiple divisions at once
Division_of_Bangladesh.extend(["Cumilla", "Narayanganj", "Narsingdi"])
# Removing a division
Division_of_Bangladesh.remove("Mymensingh")
# Inserting a division at a specific index
Division_of_Bangladesh.insert(2, "Noakhali")
# Sorting the divisions alphabetically
#Division_of_Bangladesh.sort()
print(Division_of_Bangladesh)
