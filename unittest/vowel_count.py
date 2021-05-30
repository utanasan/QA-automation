"""Write a function that accepts a string and returns a dictionary with the keys as the vowels and
values as the count of times that vowel appears in the string."""

def vowel(string):
  lower_s = string.lower()
  return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}

#print(vowel("Helicopter and airplane"))
