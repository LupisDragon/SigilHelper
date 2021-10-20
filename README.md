# SigilHelper
Helps in sigil creation by removing duplicate letters from a statement of intent.

How it works: The user is asked to enter in a sentence, and then the program converts the input to all uppercase, and generates 2 lists:
1) A list of all the letters in the sentence, without the same letter showing twice.
2) A list of all the letters that only show up once.

For example, a sentence of "this is a really cool program" will generate:
"
Here are your letters without repeats.
THISARELYCOPGM
And these are the letters that are unique (only show up once).
THEYCPGM
"

The user will then be prompted as to whether or not they'd like to enter another. The program loops unless the user enters 'n' for no.
