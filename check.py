noun = ["school", "home", "star"] #noun list
verb = ["goes", "stays", "is", "was"] #verb list
adjective = ["daily", "lonely", "sweet", "good", "bad"] #adjective list
sentence = ["Ram {verb} to {noun} {adjective}", "She {verb} {noun} so {adjective}","I {noun} to {verb} as {adjective}",
            "He {adjective} {verb} on {noun}", "Sita {verb} on {noun} {adjective}",
            "Rama {verb} on {adjective} {noun}"] #sentence list
len_noun = len(noun)                            #length of noun, verb, adjective and sentence list are different
print("length of noun list:", len_noun)
len_verb = len(verb)
print("length of verb", len_verb)
len_adjective = len(adjective)
print("length of adjective", len_adjective)
len_sentence = len(sentence)
print("length of sentence", len_sentence)
currSentence = []
output = []
cont = True
while cont:                                                      #ask user to continue or not
    user_input = input("continue? y/n :")
    if user_input == 'y':
       x = input("please enter the input:")                      #asking user fo input
       number = int(x)
       if type(number) == int:                                   #check no is integer
           number = int(x)
           print("number is integer")
       else:
            print("invalid input/input should be numeric")
       if number >= 0:                                             #check no is positive
            print("number is positive")
       else:
            print("invalid input/ input must be positive")
       if number >= len_noun:                                        # if input > length of noun
           modified_input_noun = number % len_noun
           currSentence = (sentence[modified_input_noun].format(verb=verb[modified_input_noun], noun=noun[modified_input_noun],
                                            adjective=adjective[modified_input_noun]))
       elif number >= len_verb:                                       # if input > length of verb
           modified_input_verb = number % len_verb
           currSentence =(sentence[modified_input_verb].format(verb=verb[modified_input_verb], noun=noun[modified_input_verb],
                                            adjective=adjective[modified_input_verb]))
       elif number >= len_adjective:                                    # if input > length of adjective
           modified_input_adjective = number % len_adjective
           currSentence =(sentence[modified_input_adjective].format(verb=verb[modified_input_adjective], noun=noun[modified_input_adjective],
                                            adjective=adjective[modified_input_adjective]))
       elif number >= len_sentence:                                     # if input > length of sentence
           modified_input_sentence = number % len_sentence
           currSentence = (sentence[modified_input_sentence].format(verb=verb[modified_input_sentence], noun=noun[modified_input_sentence],
                                                             adjective=adjective[modified_input_sentence]))
       elif number >= len_adjective and number >= len_verb and number >= len_noun and number >= len_sentence:
           modified_input = number % max(len_adjective, len_sentence, len_noun, len_verb) #input > length of all 4 lists
           currSentence.append(sentence[modified_input].format(verb=verb[modified_input],
                                                         noun=noun[modified_input],adjective=adjective[modified_input]))
       else:
           currSentence = (sentence[number].format(verb=verb[number],
                                                 noun=noun[number], adjective=adjective[number])) #if input < length of all 4 lists
       print("the final sentence after replacing noun, verb and adjective", currSentence)
       if currSentence in output:
           print("duplicate sentence can not be save in mad lib; skip it") # check for duplicate
       elif currSentence not in output:                                                       # saving the output in final mad lib
           output.append(currSentence)
           print("my mad lib:", output)
    else:
       exit(print("User exit")) #u said use sys.exit..