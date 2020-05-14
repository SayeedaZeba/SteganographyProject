from PIL import Image
import encode
import decode

# Encode the message into the image
def EncodeMessage():
    UserInputImage = input("Enter the name of the image in which you would like to encrypt your message (with extension): ")
    #image = Image.open(UserInputImage, 'r')

    SecretMessage = input("Enter the message you would like to encode : ")
    if (len(SecretMessage) == 0):
        raise ValueError('Message is empty')

    EncryptPasscode = input("Set a passcode for you to decrypt the message in future: ")

    print("Your secret message: '" + SecretMessage + "' is getting encoded in the image: '" + UserInputImage + "' . \nPlease use the passphrase: '" + EncryptPasscode + "' as a future reference to decode the message!" )
    print ("Encoding your message")
    EncryptPasscode = " " + EncryptPasscode
    SecretMessage += EncryptPasscode

    # Encode the message into the image
    EncodeImage = encode.Encode(UserInputImage,SecretMessage)
    EncodeImage.hide_function()

def DecodeMessage():
    ImageToDecrypt = input("Enter the name of the image which you would like to decrypt (with extension): ")
    #image = Image.open(UserInputImage, 'r')

    DecryptPasscode = input("Please enter the correct passphrase to decrypt the image: ")

    print("We are decrypting your image: '" + ImageToDecrypt + "' using the passcode you provided: '" + DecryptPasscode + "' . \nPlease wait for a while..." )
    print ("Decoding your message")

    # Decode the message from the image
    DecodeImage = decode.Decode(ImageToDecrypt)
    MessageRetrieved = DecodeImage.reveal_function()

    if(MessageRetrieved.endswith(DecryptPasscode)):
        print( MessageRetrieved )

    else:
        print("Incorrect passcode. Please try again!")

# Main Function
def main():
    userInput = int(input("Hello User! \n Welcome to the Image Encryption/Decryption System ::\n 1. Encode\n 2. Decode\n What would you like to do today?  "))

    if (userInput == 1):
        EncodeMessage()

    elif (userInput == 2):
        DecodeMessage()

    else:
        raise Exception("Enter correct input")

# Driver
if __name__ == '__main__' :

    # Calling main function
    main()