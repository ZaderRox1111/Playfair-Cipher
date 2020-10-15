# Playfair-Cipher
Encrypt and decrypt messages using the playfair cipher.



Zach Derrick zcd22@nau.edu
# Understanding the Problem
The goal of this lab is to create a program that can encrypt and decrypt a
sentence using a keyword and the Playfair cipher.
- We need a keyword input
- We need a sentence to encrypt/decrypt
- U becomes V, in the same space
- Q becomes K, in the same space
# Plan a Solution
We are going to start off by handling the inputs, so that we can have some
variables and keys to work with. Then we are going to create an ‘alphabet’
with the missing letters and the space, so that we can create the table. We
will make a function that creates the table using the key. We’re planning on
it going letter by letter in the phrase, adding the letter to the table, then
removing the used letter from the alphabet and the key, so it doesn’t get
used again. For the table, we’re going to create a full 25 character string
for the table. After the table, we are going to make the phrase digramed
by checking if each letter is repeated after, then add it all to a new string
with the diagrams separated by periods, then split the string into a list of
the diagrams, along the periods. After that, we’ll work on the encryption,
using the rules on the digrams that were created. For the first rule, we’ll
need to check row by row if the numbers on the same row, and if they are
we’ll increase their index by one, or make the index the beginning of the
row.
# Implementing and Testing
We created all of the inputs and variables at the beginning. We then
began working on the table, and we originally wanted to create the 5x5
table, but realized that would be too hard right now, so we just created a
25 character long string with no repeated characters. After the table, we
needed to split the phrase into digrams, and discovered that splitting the
phrase like we wanted was not a good way to go. We created a function to
find the even numbers in the length of the phrase so that we could
properly move along the digrams in a for loop. Then we added the
digrams to a new string, making sure to add in X’s where there was an odd
number and where the two digram letters were the same.
- Starting on the encryption, we needed a new function that checks if a
character is in a row, so that we can see if the digram in in the same row,
for rule 1. Then we checked each row to see if the digram elements were
there together. If they were, we checked if the letter was on the end of the
row. However the code was running into a lot of indexing errors with the
first rule, so we made the digram message a list of all the digrams, instead
of just a string. We also sliced up the table into 5 separate rows so we
could keep track of its position better, and doing both made it easier to
do the first rule. We just checked if the elements of the digrams were on
the same row with a boolean, and if they are, we added one to their index
(for the end elements, the index was changed to -1 so that the addition
would be equal to 0, the beginning of the row).
- For rule 2, we just added another if statement to check if the column
indexes were the same, so for that we needed a way to access the column
index. We made a function that returns the row that the letter is on, for the
column index. Similar process as rule 1.
- For rule 3, it is the only other option, so it is an else statement. All we did
was basically swap the row indexes of the two letters for each other, and it
makes the rectangular pattern.
For the decryption, we can use the same function as encryption, except
the rules are applied in reverse. Rather than moving the index forward
through the table, the index is moved backwards.
- Finally the finished digrams are returned to the main function, and
combined into the final message. The final message is then displayed to
the user. This process works the same way for both encryption and
decryption.
For the final testing, we encrypted 3 messages and proceeded to decrypt
them. In each case the decrypted message was the same as the message
imputed.
# Reflect and Refactor
Lab 3 has been the most challenging lab so far. In order to complete the
lab, we had to attempt the code several times and even completely restart
the code. For our first attempt, random letters would appear when
decrypting the message. After deciding to restart the code, we
reorganized and cleaned up the code, using two strings instead of trying
to organize a table, and it ended up working. We had trouble setting up
the required table since we haven’t covered multidimensional data,
hopefully in the future once we have discussed matrices more,
requirements like this might become easier. This lab required us to
consider solutions that weren’t initially apparent to us in order to come to
a complete solution.
