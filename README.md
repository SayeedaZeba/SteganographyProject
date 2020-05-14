# steganography
A steganography program for security class

This program is used to implement the basic concept of Steganography on images.

Steganography is a method of hiding secret messages or data by embedding it into a media file. Using this, messages can securely be sent in a hidden form to anyone, provided they have the ability to decode the encoded image.

When the user chooses to 'Encode', they are allowed to upload an image, a text message to hide in it, and a passcode with it.
They are returned a modified image with the message encoded in it.

When the user chooses to 'Decode;, they are allowed to upload the encoded image and the respective passcode. Once the passcode has been verified, the user is returned the text message hidden inside the image.


References:
https://www.geeksforgeeks.org/image-steganography-in-cryptography/
https://hackernoon.com/simple-image-steganography-in-python-18c7b534854f 
https://github.com/lloistborn/ldpc-img
