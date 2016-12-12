from __future__ import print_function

from nltk.chat.util import Chat, reflections


responses = (

    (r'(hello(.*))|(good [a-zA-Z]+)',
    ( "Ello my fellow bushie, how ya goin'?",
      "G'day my fella!")),

# I need
    (r'i need (.*)',
    ( "You don't need %1. All you need is vegemite and armadillos, mate.",
      "%1 isn't gonna solve your problems, mate!")),
#I want
    (r'i want (.*)',
    ( "And I want a million dollas. But ya don't see me complainin'. Crikey.",
      "Will %1 really help you mate?")),

#Why questions
    (r'why (.*) i (.*)\?',
    ( "You %1 %2?",
      "Perhaps ya only think ya %1 %2, mate!")),

    (r'why (.*) you(.*)\?',
    ( "Why %1 ya %2?",
      "Are ya sure I %2, mate?")),

    (r'why (.*)\?',
    ( "I can't tell ya why %1.",
      "The REAL question is why do ya think %1?" )),
    
#Are you questions
    (r'are you (.*)\?',
    ( "Maybe %1, maybe not %1.",
      "Whether I am %1 or not is God's business, mate.")),


    (r'am i (.*)\?',
    ( "Perhaps %1, perhaps not %1. I can't say mate.",
      "Maybe %1, maybe not %1 mate.")),

# what questions
    (r'what (.*)\?',
    ( "You should get your answers by takin a long, reflective walk in the outback. Not askin' a computa mate. What %1. Pfft.",
      "What %1 shouldn't be of any concern to ya, fella.")),

# how questions
    (r'how (.*)\?',
    ( "Crikey! How do ya suppose, mate. I live in a computa!",
      "Ask yourself not how mate....but why.")),

# can questions
    (r'can you (.*)\?',
    ( "I probably can my mate, but I've got armadillas to fight off.",
      "Maybe I will think about %1 after my rugby match.")),

# can questions
    (r'can i (.*)\?',
    ( "You can %1 if ya believe ya can %1. I believe in ya mate.",
      "Neva. Neva in a million years.")),

# "It is"
    (r'it is (.*)',
    ( "Crikey! How can ya be so certain that %1?",
      "Whetha it is %1 or not doesn't change the fact that there are still boomerangs hittin' people in the face EVERY. DAY. ")),

# "is there?"
    (r'is there (.*)\?',
    ( "There only is %1 if you believe there is, my friend. Ask a kangaroo.",
      "Crikey, absolutely not..")),

# "is it?"
    (r'is(.*)\?',
    ( "%1 is not relevant when you're gettin trampled by elephants.",
      "Does this REALLY matta?")),

# non-specific question
    (r'(.*)\?',
    ( "Do ya really think %1, mate?",
      "I can't answer that mate. All I know is kangaroos and boomerangs..")),

# hate
    (r'(.*) (hate[s]?)|(dislike[s]?)|(don\'t like)(.*)',
    ( "Weeds only grow in the outback when we dislike 'em, friend.",
      "Hate is a bloody strong emotion, mate.",
      "Eh..why do ya hate %1?")),

# truth
    (r'(.*) truth(.*)',
    ( "Seek truth, and truth will seek you, mate.",
      "The search for truth is like a long matcha rugby.")),

# desire to do an action
    (r'i want to (.*)',
    ( "Why do ya want to %1, mate?",
      "Would it ACTUALLY help you to %1, dingy?")),

# desire for an object
    (r'i want (.*)',
    ( "Why do ya want a %1, mate?",
      "Would it ACTUALLY help you to get a %1, dingy?")),

# "I can't"
    (r'i can\'t (.*)',
    ( "Crikey you're negative! You can do anything mate.",
      "Of course you can't mate. You're trying to validate yourself with an opinion froma COMPUTA.")),

# "I think.."
    (r'i think (.*)',
    ( "Uncertainty in an uncertain world, friend.",
     "Well I think that %1 is useless in the bush mate.")),

# "I feel.."
    (r'i feel (.*)',
    ( "Wah wah wah, there's no time to complain when the kangaroo war begins.",
      "Crikey, go take an advil.")),



# exclaimation mark indicating emotion
    (r'(.*)!',
    ( "Wow mate, you are bloody rocked up ova this.",
      "Fair suck of the sav!")),

# because [statement]
    (r'because (.*)',
    ( "Does knowin that a %1 really change things, mate?",
      "If %1, what else must be true?")),

# yes or no 
    (r'(yes)|(no)',
    ( "There is no certainty in the bush.",
      "Crikey, you're really sure of that..")),

# 'love'
    (r'(.*)love(.*)',
    ( "Free love, mate!"
      "Awh, how touching friend!")),
    #like
(r'(.*)like(.*)',
    ( "Free love, mate!"
      "Awh, how touching friend!")),

# 'I', 'me', 'my' 
    (r'(.*)(me )|( me)|(my)|(mine)|(i)(.*)',
    ( "'I', 'me', 'my'... ya soundin' a bit big-notey, mate.",
      "...Have ya eva considered that ya might be a selfish person?")),

# 'you' 
    (r'you (.*)',
    ( "Hey hey hey!! My ways are not of conern to ya, mate.",
      "I would expect a bogan like you to say something like that.")),

# goodbye
    (r'exit (.*)',
    ( "See ya lata, mate! Don't trip on an armadilla on the way out!")),


# fall through case 
    (r'(.*)',
    ( "Keep talkin like that n you'll get a roundhouse kick to the face by a roo, mate.",
      "Random talk is useless out in the bush, mate.",
      "Fair suck of the sav!"))
)

barry_chatbot = Chat(responses, reflections)

def barry_chat():
    print('~'*75)
    print("Barry from the Bush".center(75))
    print('~'*75)
    print('"Lets put anotha shrimp on tha barbie!"'.center(75))
    print("* Talk with Barry.")
    print("* Type 'quit' when you have had enough of him.")
    print('~'*75)
    print("G'day mate! 'Ow are ya this fine arvo?")

    barry_chatbot.converse()

def demo():
    barry_chat()

if __name__ == "__main__":
    demo()
