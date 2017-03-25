"""This is the entry point of the program."""

def create_box(height, width, character):
    string = ''
    if height and width > 0:
        for h in range(height):
            string = string + character * width + "\n"
   
        return string
            
   

if __name__ == '__main__':
    create_box(3, 4, '*')


    
def create_box1(height, width, character):
    string = ''
    
    for i in range(height):
     if i == 0:
        string = string + (character *(width)) + '\n'
     elif i == (height-1):
        string = string + (character *(width)) + '\n'
     else:
        string = string + (character + " " * (width-2) + character) + '\n'
    return string
    
# print(create_box(10, 10, '@'))

