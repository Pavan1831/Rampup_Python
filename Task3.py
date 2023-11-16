import matplotlib.pyplot as plt

# Define custom letter counts
custom_letter_counts = {
    'a': 5,
    'b': 8,
    'c': 3,
    'd': 10,
    'e': 15,
    'f': 7,
    'g': 4,
    'h': 12,
    'i': 9,
    'j': 2,
    'k': 6,
    'l': 11,
    'm': 7,
    'n': 13,
    'o': 14,
    'p': 6,
    'q': 1,
    'r': 12,
    's': 10,
    't': 13,
    'u': 5,
    'v': 3,
    'w': 4,
    'x': 2,
    'y': 5,
    'z': 1,
}

# Extract the counts and letters
counts = list(custom_letter_counts.values())
letters = list(custom_letter_counts.keys())

# Create the bar chart
plt.bar(letters, counts)

# Label the axes and add a title
plt.xlabel("Letters")
plt.ylabel("Counts")
plt.title("Custom Letter Counts")

plt.show()
