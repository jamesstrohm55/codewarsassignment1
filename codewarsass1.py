#Even or Odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

#Convert a Number to a String!
def number_to_string(num):
    return str(num)

#Vowel Count
def get_count(string):
    vowels = "a,e,i,o,u"
    return sum(1 for character in string if character in vowels) 