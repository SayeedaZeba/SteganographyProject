from PIL import Image
import binascii
import optparse
import codecs


class Encode:   

    #takes in an input of an image file path and text message
    def __init__(self, image_file, text):
        self.image_path = image_file                    #image file path
        self.image = Image.open(image_file, 'r')        #extracting image
        self.message = text                             #text message

    #converting RGB to Hex    
    def RGB_to_Hex(self, R, G, B):
        return '#{:02x}{:02x}{:02x}'.format(R, G, B)

    #converting Hex to RGB
    def Hex_to_RGB(self, hex_value):
        return (int(hex_value[1:3], 16), int(hex_value[3:5], 16), int(hex_value[5:7], 16))

    #converting String to Binary
    def Str_to_Bin(self, message_text):
        binary_value = bin(int(binascii.hexlify(bytes(message_text, 'UTF-8')), 16))
        return binary_value[2:]
    
    #encodes the Hex value using the Digit 
    def encode_function(self, hex_code, digit_value):
        if hex_code[-1] in ('0' , '1'):
            hex_code = hex_code[:-1] + digit_value
            return hex_code
        else:
            return None

    #hides the message in the image
    def hide_function(self):
        image_file = self.image
        message_text = self.message

        binary_message = self.Str_to_Bin(message_text) + '1111111111111110'
        if image_file.mode in ('RGBA'):
            image_file = image_file.convert('RGBA')
            image_data = image_file.getdata()

            digit_index = 0
            new_Image = []
            for i in image_data:
                if digit_index < len(binary_message):
                    new_image_pixel = self.encode_function(self.RGB_to_Hex(i[0],i[1],i[2]),binary_message[digit_index])

                    if new_image_pixel == None:
                        new_Image.append(i)
                    else:
                        R,G,B = self.Hex_to_RGB(new_image_pixel)
                        new_Image.append((R,G,B,255))
                        digit_index +=1
                else:
                    new_Image.append(i)
            
            image_file.putdata(new_Image)
            image_file.save(self.image_path,"PNG")
            print( "Your image has been modified with the text hidden in it!" )

        else:
            print( "Unsupported image mode " + image_file.mode() + "!")


