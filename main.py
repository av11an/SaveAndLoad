import pickle


class Pixelart:
    def __init__(self, name, length, width, ar):
        self.name = name
        self.length = length
        self.width = width
        self.ar = ar

    def set_size(self, length, width):
        self.length = length
        self.width = width

    def get_size(self):
        return self.length, self.width

    def set_array(self, ar):
        self.ar = ar

    def get_array(self):
        return self.ar

    def __str__(self):
        return '\n{} has a length and width of {}, with an array code of {}.'.format(self.name, self.get_size(),
                                                                                     self.get_array())


# Save a new pixel art object function, saves it as a binary file.
# If the filename already exist it just overwrites the file, might add a warning in the future
def addNewPixelArt(name, length, width, array):
    newPixelArt = Pixelart(name, length, width, array)
    with open((name + '.pkl'), 'wb') as save_mcpa:
        pickle.dump(newPixelArt, save_mcpa)


# main
n = int(input("\nHow many Pixel Arts will you be adding?: "))


emptyArray = []
for i in range(n):
    name = input("\nName of Pixel Art [WARNING: If you name the pixel art the same name as one previously saved it will overwrite that pixel art!]: ")
    l = int(input("Length of Pixel Art: "))
    w = int(input("Width of Pixel Art: "))
    for x in range(0, w):
        b = list(map(int, input("Paste row #"+str(x+1)+": ").split(', ')))
        print(b)
        emptyArray.append(b)
    addNewPixelArt(name, l, w, emptyArray)
    emptyArray = []

conVar = input("\nDo you want to load a Pixel Art? input [yes] or [no]: ")

# Load code, if the name exist it will print the __str__ function in the Pixelart class, if not it will say no saved data
# If no files exist it will also say no saved data

if conVar == "yes":
    nameOfArt = input("Which Pixel art? input [name]: ")
    try:
        with open((nameOfArt + '.pkl'), 'rb') as load_mcpa:
            pixelArtLoaded = pickle.load(load_mcpa)
            print(pixelArtLoaded)

            # Debug Array
            s = pixelArtLoaded.get_array()
            print("\n")
            print(str(s[0][0]))
    except:
        print("\nNo saved Pixel Art found!")
else:
    print("\nHave a good day.")
