def main():
    noun = ['Therapy','Knife','Kitten','Hairy legs','Cow','Rocket','Toilet seat','Poop']
    Verbs = ["Swat","Trip","Busy"
        ,"Pull","Run","Dig"]
    Adjective = ["Angry","Naked","Shaky","Bat shit crazy","Idiotic"]
    Sentence_List = ["The {Noun} has {Verbs} the doorman and is {Adjective}","{Noun} {Verbs} to the {Adjective} ground","Man {Verbs} on a {Adjective} {Noun}","{Verbs} the Guard again and ask him to fix the beautiful {Noun} otherwise I will be {Adjective}"]
    while True:
        number = int(input("Please enter a integer number greater than 0"))
        while number!="":
            try:
                n = int(number)
            if n<0:
                print("the number is not greater than 0, please try again")
                UserInput = str(input('Enter \'y\' to continue playing and \'n\' to exit'))
                if(UserInput[0]=='y'):
                    continue
                else:
                    break
            except ValueError:
                print("Sorry did not understand the input, please enter an integer greater than 0")
        NounSelected = Noun(len(Noun) % number)
        VerbSelected = Verbs(len(Verbs) % number)
        AdjectiveSelected = Adjective(len(Adjective) % number)
        SentenceSelected = Sentence_List(len(Sentence_List) % number)
        SentenceSelected.format(Noun = "NounSelected", Verb = "VerbSelected", Adjective = "AdjectiveSelected")
        myset = set(SentenceSelected)
        print (myset)

