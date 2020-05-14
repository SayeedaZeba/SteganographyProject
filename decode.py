from PIL import Image
import binascii
import optparse
import codecs

class Decode:
    
    def __init__(self, image_file):
        self.image_path = image_file                    #image file path
        self.image = Image.open(image_file, 'r')        #extracting image
    
    #converting RGB to Hex 
    def RGB_to_Hex(self, R, G, B):
        return '#{:02x}{:02x}{:02x}'.format(R, G, B)
    
    #converting Binary to String
    def Bin_to_Str(self, binary_value):
        message_text = binascii.unhexlify('%x' % (int(binary_value, 2)))
        message_text = message_text.decode()
        return message_text
    
    #decodes the message from the hex code
    def decode_function(self, hex_code):
        if hex_code[-1] in ('0', '1'):
            return hex_code[-1]
        else:
            return None
    
    #reveals the hidden message in the image
    def reveal_function(self):
            img =  self.image
            binary = ""

            if img.mode in ('RGBA'):
                img = img.convert('RGBA')
                datas = img.getdata()

                for item in datas:
                    digit = self.decode_function(self.RGB_to_Hex(item[0], item[1], item[2]))

                    if digit == None:
                        pass
                    else:
                        binary += digit
                        if binary[-16:] == '1111111111111110':
                            return self.Bin_to_Str(binary[:-16]) # success

                return self.Bin_to_Str(binary)

            return False
