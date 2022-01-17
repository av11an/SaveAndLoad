# SaveAndLoad
Quick put together of a save load system that saves names, sizes, and arrays into a object that is saved in a binary file.


Instructions
------------------

If you want to add a pixel art save, tell it how many you want to add, then answer the following inputs. You will have to insert contents of each row in the 2d array example..

2d Array [[1, 2, 3], [4, 5, 6]],,, Paste row#1: 1, 2, 3  ,,, then ,, Paste row#2: 4, 5, 6,, until you have filled out the entire width of the pixelart

If you want to load a pixel art you can either answer yes at the end of the prompts if you add, or you can answer 0 to saving a pixel art and it will directly ask you to load one. *I should just ask if you want to load or save in the beginning.

When answering yes to load enter the name in which you inputed for your saved pixel art, if no pixel arts with that name are present or there are no pixel arts saved then it should just say no saved pixel art found. If you name the pixel art to something already saved it just overwrites it.
