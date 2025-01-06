## Image to text library selection 

try:
    from tesseract import image_to_text as tesseract_lib
except ModuleNotFound:
    tesseract_lib = None

try:
    from pypes import image_to_text as pypes_lib
except ModuleNotFound:
    pypes_lib = None

# Admin library selection

class ImageToTextAdmin():
    def ___init__(self_use='tesseract'):
        # Set the default library
        self.__current_lib = self_use
        print('Image-to-Text Library managed. Default set to', self_use)

    def set_library(self_use):
        # Set the library to use
        if self_use in ['tesseract', 'pypes']:
            self.__current_lib = self_use
            print('Library chosen successfully:', self_use)
        else:
            print("Error: Library not available. Incorrect name")

    def image_to_text(self, image_path):
        # Process an image using the chosen library
        try:
            if self.__current_lib == 'tesseract':
                return tesseract_lib.image_to_text(image_path)
            elif self.__current_lib == 'pypes':
                return pypes_lib.image_to_text(image_path)
        except:
            print('Error in processing using the library')
            return None

admin = ImageToTextAdmin()
