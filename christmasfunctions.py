# import for getting random number
from random import randint

def GetChrismasJoke():
    jokes = ["What does Santa suffer from if he gets stuck in a chimney?", "What happened to the man who stole an Advent Calendar?", "Who delivers presents to baby sharks at Christmas?", "What do they sing at a snowman’s birthday party?", "What do Santa’s little helpers learn at school?", "What kind of motorbike does Santa ride?", "What did Santa do when he went speed dating?", "Why was the turkey in the pop group?", "What do you get if you cross Santa with a duck?"]
    JokeSecondLines = ["Claus-trophobia", "He got 25 days!", "Santa Jaws!", "Freeze a jolly good fellow!", "The elf-abet!", "A Holly Davidson!", "He pulled a cracker!", "Because he was the only one with drumsticks!", "A Christmas Quacker!"]
    JokeNumber = randint(0, len(jokes) - 1)
    OutputJoke = [jokes[JokeNumber], JokeSecondLines[JokeNumber]]
    return OutputJoke

def GetChrismasFilm():
    films = ["The Polar Express", "Home Alone", "Nativity", "The Chrismas Chronicles", "The Snowman", "Love Actually", "How the Grinch Stole Chrismas", "Die Hard", "Elf", "The Nightmare Before Chrismas", "A Chrismas Carol", "Bad Santa", "Get Santa", "Authur Christmas", "Miracle on 34th St."]
    return films[randint(0, len(films) - 1)]