print("\033c")

class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    
    def __str__(self):
        return f"{self.word}: {self.meaning}"

flash = []
print("Welcome to the flashcard application!")

while True:
    word = input("Enter the word: ")
    meaning = input("Enter the meaning of the said word: ")
    
    flash.append(Flashcard(word, meaning))
    
    option = int(input("Enter 0 to continue and 1 to exit: "))
    
    if option:
        break

print("\nYour flashcard:")
for i in flash:
    print(f"> {i}")