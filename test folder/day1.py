# Concatenate strings
string1 = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
string2 = ' '.join(['Coding', 'For', 'All'])

# Declare a variable and assign it
company = "Coding For All"

# Print the variable
print(company)

# Print the length of the company string
print(len(company))

# Change all characters to uppercase
print(company.upper())

# Change all characters to lowercase
print(company.lower())

# Use capitalize(), title(), swapcase() methods
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Slice out the first word
print(company[7:])

# Check if the string contains a word
print('Coding' in company)

# Replace the word 'Coding' with 'Python'
print(company.replace('Coding', 'Python'))

# Change 'Python for Everyone' to 'Python for All'
print('Python for Everyone'.replace('Everyone', 'All'))

# Split the string using space as the separator
print(company.split())

# Split the string at the comma
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(', '))

# Character at index 0
print(company[0])

# Last index of the string
print(len(company) - 1)

# Character at index 10
print(company[10])

# Create an acronym for 'Python For Everyone'
acronym1 = ''.join([word[0] for word in 'Python For Everyone'.split()])
print(acronym1)

# Create an acronym for 'Coding For All'
acronym2 = ''.join([word[0] for word in company.split()])
print(acronym2)

# Position of the first occurrence of 'C'
print(company.index('C'))

# Position of the first occurrence of 'F'
print(company.index('F'))

# Position of the last occurrence of 'l'
print('Coding For All People'.rfind('l'))

# Position of the first occurrence of 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# Position of the last occurrence of 'because'
print(sentence.rindex('because'))

# Slice out the phrase 'because because because'
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])

# Does 'Coding For All' start with 'Coding'?
print(company.startswith('Coding'))

# Does 'Coding For All' end with 'coding'?
print(company.endswith('coding'))