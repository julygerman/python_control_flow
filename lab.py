# exercise-01 Vowel or Consonant
# Write the code that:

# Prompts the user to enter a letter in the alphabet: Please enter a letter from the alphabet (a-z or A-Z):
# Write the code that determines whether the letter entered is a vowel
# Print one of following messages (substituting the letter for x):
# The letter x is a vowel
# The letter x is a consonant
# Hints: Use the in operator to check if a character is in another string For example, if some_char in 'abc':

letter = input('please enter a letter from the alphabet(a-z or A-Z): ').lower()
if 'a' in letter:
    print(f'the letter {letter} is a vowel')
elif 'e' in letter:
    print(f'the letter {letter} is a vowel')
elif 'i' in letter:
    print(f'the letter {letter} is a vowel')  
elif 'o' in letter:
    print(f'the letter {letter} is a vowel')
elif 'u' in letter:
    print(f'the letter {letter} is a vowel')                    
else:
    print(f'the letter {letter} is a consonant')






# exercise-02 Length of Phrase
# Write the code that:

# Prompts the user to enter a phrase: Please enter a word or phrase:
# Print the following message:
# What you entered is xx characters long
# Return to step 1, unless the word 'quit' was entered.

word = ''
while word != 'quit':
    word = input('enter a word or phrase(enter:\'quit\' to exit): ')
    print('your word is', len(word), 'letters long')
        
    
    



# exercise-03 Calculate Dog Years
# Write the code that:

# Prompts the user to enter a dog's age in human years like this: Input a dog's age in human years:
# Calculates the equivalent dog years, where:
# The first two years count as 10 years each
# Any remaining years count as 7 years each
# Prints the answer in the following format: The dog's age in dog years is xx
# Hint: Use the int() function to convert the string returned from input() into an integer

h_years = int(input('Input a dog\'s age in human years: '))
if h_years < 0:
	print("Age must be positive number.")
	exit()
elif h_years <= 2:
	d_years = h_years * 10.5
else:
	d_years = 21 + (h_years - 2)*4

print("The dog's age in dog's years is", d_years)



# exercise-04 What kind of Triangle?
# print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")


# exercise-05 Fibonacci sequence for first 50 terms
# Write the code that:

# Calculates and prints the first 50 terms of the fibonacci sequence.
# Print each term and number as follows:
#   term: 1 / number: 1
#   term: 2 / number: 1
#   term: 3 / number: 2
#   term: 4 / number: 3
#   term: 5 / number: 5```
#   etc.

# Hint: The next number is found by adding the two numbers before it

x,y=0,1

while y<50:
    
    print(f'number: {y}')
    x,y = y,x+y
	






# exercise-06 What's the Season?
# Write the code that:

# Prompts the user to enter the month (as three characters): Enter the month of the year (Jan - Dec):
# Then prompts the user to enter the day of the month: Enter the day of the month:
# Calculate what season it is based upon this chart: Dec 21 - Mar 19: Winter Mar 20 - Jun 20: Spring Jun 21 - Sep 21: Summer Sep 22 - Dec 20: Fall
# Print the result as follows:
# is in
# Hints: Consider using the in operator to check if a string is in a particular list/tuple like this: if input_month in ('Jan', 'Feb', 'Mar'):

# After setting the likely season, you can use another if...elif...else statement to "adjust" if the day number falls within a certain range.

month = input("Input the month (e.g. Jan, Feb etc.): ")
day = int(input("Input the day: "))

if month in ('Jan', 'Feb', 'Mar'):
	season = 'winter'
elif month in ('Apr', 'May', 'Jun'):
	season = 'spring'
elif month in ('Jul', 'Aug', 'Sep'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'Mar') and (day > 19):
	season = 'spring'
elif (month == 'Jun') and (day > 20):
	season = 'summer'
elif (month == 'Sep') and (day > 21):
	season = 'autumn'
elif (month == 'Dec') and (day > 20):
	season = 'winter'

print("Season is",season)
