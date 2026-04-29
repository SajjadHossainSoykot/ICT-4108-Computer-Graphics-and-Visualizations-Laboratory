import matplotlib.pyplot as plt

plt.figure(figsize=(10, 7))

plt.text(0.1, 0.9, "Default Font Text", fontsize=14)
plt.text(0.1, 0.8, "Bold Text", fontsize=16, fontweight="bold")
plt.text(0.1, 0.7, "Italic Text", fontsize=16, fontstyle="italic")
plt.text(0.1, 0.6, "Large Red Text", fontsize=22, color="red")
plt.text(0.1, 0.5, "Green Text", fontsize=18, color="green")
plt.text(0.1, 0.4, "Blue Bold Text", fontsize=18, color="blue", fontweight="bold")

plt.text(0.7, 0.5, "Vertical Text", fontsize=16, rotation=90, color="purple")

plt.title("Creating Various Types of Texts and Fonts", fontsize=16, fontweight="bold")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.axis("off")

plt.savefig("Exp12_Output.png")
plt.show()