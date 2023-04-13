"""
 Name: Noemi Turner  
 Filename: eliza.py
 Description: This program modifies the eliza.py program. 
              This exercise helps us become more familiar with regular expressions.
"""

'''
Simple Eliza program
To execute:
    >>csuser ->python3 eliza.py
'''

import sys
import re
def doreply(instr):
    instr = instr.lower()
    if re.search(r'^hello|hi$', instr):
        return 'Hi there!'
    
    if re.search(r'\W(dislike|hate|despise|loathe)\W', instr):
        return 'Those are some strong negative feelings you have!'
    
    if re.search(r"^(are|aren't|what|where|who|when|is|isn't|why|how)\W", instr):
        return 'I often ask myself the same question!'
    
    # 1. Words that decribe good cooking
    if re.search(r"\byummy($|\b)|\bexcellent($|\b)|\bdelicious($|\b)|\btasty($|\b)|\bflavorful($|\b)|\bsavory($|\b)|\bsweet($|\b)|\btender($|\b)|\bjuicy($|\b)|\bwell-seasoned($|\b)|\bcrispy($|\b)", instr):
        return 'It sounds like you have positive reviews about their cooking.'
    
    # 2. Words that describe bad cooking
    if re.search(r"\bburnt($|\b)|\bundercooked($|\b)|\braw($|\b)|\bcold($|\b)|\bstale($|\b)|\bsoggy($|\b)|\bdry($|\b)|\bovercooked($|\b)|\bhard($|\b)|\btough($|\b)|\bstringy($|\b)", instr):
        return 'It sounds like you have negative reviews about their cooking. Perhaps on a subconscious level, effects your relationship with them?'
    
    # 3. Searches for the word yes or the word no
    if re.search(r"(^|\b)yes($|\b)|(^|\b)no($|\b)|(^|\b)maybe($|\b)|(^|\b)perhaps($|\b)", instr):
        return 'And how does (or how did) that make you feel?'
    
    # 4. when while where as since because
    if re.search(r"(^|\b)because($|\b)|(^|\b)when($|\b)|(^|\b)while($|\b)|(^|\b)as($|\b)|(^|\b)since($|\b)", instr):
        return 'hmmm, why do you think that is?'
       
    # 5. Searches for do not love, don't love, did not love, didn't love, does not love, never loved
    if re.search(r"(^|\b)do not love($|\b)|(^|\b)don't love($|\b)|(^|\b)did not love($|\b)|(^|\b)didn't love($|\b)|(^|\b)doesn't love($|\b)|(^|\b)does not love($|\b)|(^|\b)never loved($|\b)", instr):
        return 'That sounds difficult. Can you tell me more about that?'
    
    # 6. Searches for words that describe people
    if re.search(r"\bbestfriend\b|\bgrandfather\b|\bgrandmother\b|\bgrandpa\b|\bgrandma\b|\bmom\b|\bdad\b|\bsister\b|\bbrother\b|\bhusband\b|\bwife\b|\bmother\b|\bfather\b|\bboss\b|\bgirlfriend\b|\bboyfriend\b", instr):
        return 'Describe their cooking to me. It can sometimes provide me insights about your relationship with them.'
    
    # 7. Searches for I need, I want, I wish 
    if re.search(r"^(i need|i want|i wish|i can't)\b", instr):
        return 'What\'s one small step you can take to help with this?'
    
    # 8. Searches for can you..., should i...
    if re.search(r"^(can you|should i)\b", instr):
        return 'My expertise are limited because I\'m only a computer program. I suggest asking the next avaliable trust-worthy, wise, and empathetic human you encounter.'
    
    # 9. Searches for should've, could've, would've 
    if re.search(r"\b(should've|could've|would've)\b", instr):
        return 'We cannot change the past. Mindfullness and radical acceptance are very helpful coping mechanisms though.'
    
    # 10. Searches for anxious, depressed, lonely, sad, mad, afraid, scared
    if re.search(r"\banxious\b|\bdepressed\b|\blonely\b|\bsad\b|\bmad\b|\bafraid\b|\bscared\b", instr):
        return 'I think you should consult your doctor or therapist about this. They are much more qualified to help you. I am just a computer program.'
    
    # Eliza's default reply 
    return 'Interesting concept. Tell me more about what\'s been on your mind?'

def main():
    print ("Welcome! How may I help you? (type \"bye\" to quit.)\n")
    while True:
        # Read user's input
        instr = input("Patient: ")
        instr = instr.lower()
        if re.search(r'\bbye\b', instr):
            print ("Nice chatting with you!\n")
            return 0
        print (doreply(instr))
        print()

main()
