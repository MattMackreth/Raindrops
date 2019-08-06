# Raindrops Factor Program

The  purpose of this program was to create a function that takes a number and returns a string depending on it's factors.

## Approach
I decided to use a dictionary to contain the factors and the corresponding strings to be returned. The program then cycles through the factors (stored as the keys) and checks whether there is a remainder, if not it adds the corresponding string to be returned. If no factors are found the number is just returned.

##Testing

For my testing I used pytest.