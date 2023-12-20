# Unique consonants

def unique(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = {}

    for i in string:
        lower = i.lower()
        if lower.isalpha() and lower not in vowels:
            if i in consonants:
                consonants[i] += 1
            else:
                consonants[i] = 1

    unique_consonants = {char for char, count in consonants.items() if count == 1}

    return len(unique_consonants)


print(unique('cataract'))



# How many squares are in X by X grid. For examples a 2 X 2 Gris has 5 squares
# recursive solution

def how_many_squares(num):
    if num == 0:
        var = 0
        return var
    else:
        square = num * num + how_many_squares(num - 1)
        return square

print(how_many_squares(2), how_many_squares(3))


