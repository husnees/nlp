'''
CSC 4309 Natural Language Processing
Semester 1 2020/2021
Assignment 1: Finite State Transducer for German Numbers

Team Member:
1.
2.
3.
4. Muhammad Amiruddin bin Bustaman (1711905)
'''

from nltk.nltk_contrib.fst.fst import *

class myFST(FST):    
    def recognize(self, iput, oput):
        
        self.inp = iput.split("-")[::-1]
        self.outp = oput.split("-")     

        print(self.inp)
        print(self.outp)

        transduce_inp = f.transduce(self.inp)

        if self.outp == transduce_inp:        
            return True
        else:
            return False

def numberToWords(N):

    ones = {
            0:'zero',
            1:'one',
            2:'two', 
            3:'three', 
            4:'four', 
            5:'five', 
            6:'six', 
            7:'seven', 
            8:'eight',
            9:'nine', 
            10:'ten', 
            11:'eleven', 
            12:'twelve', 
            13:'three-ten', 
            14:'four-ten', 
            15:'five-ten',
            16:'six-ten', 
            17:'seven ten', 
            18:'eight-ten', 
            19:'nine-ten'
            }
    
    tens = [
            'twenty', 
            'thirty', 
            'forty', 
            'fifty', 
            'sixty', 
            'seventy', 
            'eighty', 
            'ninety'
            ]
    
    misc = {
            100:"one hundred",
            1000:"one thousand",
            10000:"ten thousand",
            100000:"one hundred thousand",
            10000000: "one million"
            }

    if 0 <= N <= 19:
        return ones[N]
    elif 20 <= N <= 99:
        Q, R = divmod(N, 10)
        return tens[Q - 2] + '-and-' + ones[R] if R else tens[Q - 2]
    elif 100 <= N:
        return misc[N]
    else:
        return "reject"

if __name__ == '__main__':
    number = eval(input("Enter input: "))
    EN_str = numberToWords(number)
    DE_str = input("Enter output: ")

    f = myFST('Finite State Transducer for German Numbers')
    # add state
    for i in range(1,7):
        f.add_state(str(i))

    # initial state
    f.initial_state = '1'

    # ones
    f.add_arc('1', '2', ['zero'], ['null'])
    f.add_arc('1', '2', ['one'], ['eins'])
    f.add_arc('1', '3', ['one'], ['ein']) # not accepted one
    f.add_arc('1', '2', ['two'], ['zwei'])
    f.add_arc('1', '2', ['three'], ['drei'])
    f.add_arc('1', '2', ['four'], ['vier'])
    f.add_arc('1', '2', ['five'], ['fünf'])
    f.add_arc('1', '2', ['six'], ['sechs'])
    f.add_arc('1', '2', ['seven'], ['sieben'])
    f.add_arc('1', '2', ['eight'], ['acht'])
    f.add_arc('1', '2', ['nine'], ['neun'])
    f.add_arc('1', '2', ['ten'], ['zehn'])
    f.add_arc('2', '2', ['ten'], ['zehn'])
    f.add_arc('1', '2', ['eleven'], ['elf'])
    f.add_arc('1', '2', ['twelve'], ['zwolf'])
    f.add_arc('1', '2', ['seven ten'], ['siebzehn'])

    # and
    f.add_arc('3', '4', ['and'], ['und']) # special 'und' for 'ein
    f.add_arc('2', '4', ['and'], ['und'])

    # tens
    f.add_arc('4', '5', ['twenty'], ['zwanzig'])
    f.add_arc('4', '5', ['thirty'], ['dreißig'])
    f.add_arc('4', '5', ['forty'], ['vierzig'])
    f.add_arc('4', '5', ['fifty'], ['fünfzig'])
    f.add_arc('4', '5', ['sixty'], ['sechzig'])
    f.add_arc('4', '5', ['seventy'], ['siebzig'])
    f.add_arc('4', '5', ['eighty'], ['achtzig'])
    f.add_arc('4', '5', ['ninety'], ['neunzig'])

    # misc
    f.add_arc('1', '6', ['one hundred'], ['einhundert'])
    f.add_arc('1', '6', ['one thousand'], ['eintausend'])
    f.add_arc('1', '6', ['ten thousand'], 'zehntaunsend')
    f.add_arc('1', '6', ['one hundred thousand'], ['einhunderttausend'])
    f.add_arc('1', '6', ['one million'], ['einemillion'])

    # accept state
    f.set_final('2')
    f.set_final('5')
    f.set_final('6')

    if f.recognize(EN_str, DE_str):
        print("accept")
        # input-output mapping
        print(str(number) + " --> " + DE_str)
    else:
        print("reject")

    disp = FSTDisplay(f)