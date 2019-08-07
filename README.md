# Raindrops Factor Program

The  purpose of this program was to create a function that takes a number and returns a string depending on it's factors.

## Approach
I decided to use a dictionary to contain the factors and the corresponding strings to be returned. The program then cycles through the factors (stored as the keys) and checks whether there is a remainder, if not it adds the corresponding string to be returned. If no factors are found the number is just returned.

## Testing

For my testing I used pytest.
I used pytest as it is a much simpler and more versatile form of unit testing.
For my testing I performed 17 tests which included tests for every possible form of the strings Pling Plang and Plong being concatenated and output as well as edge cases such as negative numbers and 0.
I used the definition of factors to include natural numbers meaning negative numbers should be accepted.
As the brief said numbers specifically should be input into my function I tested to ensure that strings and other non-number datatypes would not work with the function although all number datatypes including decimals should.

Based on my testing I did add a statement that checked if a number was a numeric string and converted it into an integer if this was the case.

## Running the program and tests
To run the program you will need Python installed on the machine.<br>
My tests run using the pytest module.<br>
To run my tests simply the following in the terminal:
>pytest Test_RaindropsMain.py 

To use the function you will need to import it from the RaindropsMain.py file
into a new python file and call it with convert_number(n) where n is any number.