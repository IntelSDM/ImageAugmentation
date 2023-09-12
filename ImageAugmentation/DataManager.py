import os
Files = []
AmountOfImages = 0
def LoadInputs():
    if not(os.path.exists('Input') and os.path.isdir('Input')):
        os.makedirs('Input')
    if not(os.path.exists('Output') and os.path.isdir('Output')):
        os.makedirs('Output')    
    print("Place All Your Images In Your Input Directory")
    input("Type Anything To Continue:")
    files = os.listdir("Input")
    for file in files:
        if file.lower().endswith((".png", ".jpg",".webp")):
            Files.append(file)
    AmountOfImages = int(input("How Many Times Would You Like Each Image Augmented: "))
