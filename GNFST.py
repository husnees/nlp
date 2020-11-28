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
    def recognize(self, iput):
        self.inp = iput.split(" ")[::-1] if '-' not in iput else iput.split("-")     
        # print(self.inp)
        transduce_inp = f.transduce(self.inp)
        print(transduce_inp)

        return transduce_inp        


def number_to_words(N):
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
            17:'seven-ten', 
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
            100:"one-hundred",
            1000:"one-thousand",
            10000:"ten-thousand",
            100000:"one-hundred-thousand",
            10000000: "one-million"
            }

    if 0 <= N <= 19:
        return ones[N]
    elif 20 <= N <= 99:
        Q, R = divmod(N, 10)
        return tens[Q - 2] + ' and ' + ones[R] if R else tens[Q - 2]
    elif 100 <= N and N in misc:
        return misc[N]
    else:
        return "reject"


def mapping(inp, outp):
    number = eval(inp)
    EN_str = number_to_words(number)
    DE_str = outp

    transduced = f.recognize(EN_str)
    if transduced:
        transduced = '-'.join(transduced)
        print(transduced)
        if transduced== DE_str:
            # input-output mapping
            print("accept: " + str(number) + " --> " + transduced)
        else:
            print("reject")    
    else:
        print("reject")


def finite_state(f):
    # add state
    for i in range(1,9):
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
    f.add_arc('1', '4', ['seven'], ['sieb'])
    f.add_arc('1', '2', ['eight'], ['acht'])
    f.add_arc('1', '2', ['nine'], ['neun'])
    f.add_arc('1', '6', ['ten'], ['zehn'])
    f.add_arc('1', '6', ['eleven'], ['elf'])
    f.add_arc('1', '6', ['twelve'], ['zwolf'])
    f.add_arc('1', '6', ['twenty'], ['zwanzig'])
    f.add_arc('1', '6', ['thirty'], ['dreißig'])
    f.add_arc('1', '6', ['forty'], ['vierzig'])
    f.add_arc('1', '6', ['fifty'], ['fünfzig'])
    f.add_arc('1', '6', ['sixty'], ['sechzig'])
    f.add_arc('1', '6', ['seventy'], ['siebzig'])
    f.add_arc('1', '6', ['eighty'], ['achtzig'])
    f.add_arc('1', '6', ['ninety'], ['neunzig'])

    # and
    f.add_arc('3', '5', ['and'], ['und']) # special 'und' for 'ein
    f.add_arc('2', '5', ['and'], ['und'])

    # tens
    f.add_arc('2', '6', ['ten'], ['zehn'])
    f.add_arc('4', '6', ['ten'], ['zehn']) # special 'zehn' for 'sieb'
    f.add_arc('5', '6', ['twenty'], ['zwanzig'])
    f.add_arc('5', '6', ['thirty'], ['dreißig'])
    f.add_arc('5', '6', ['forty'], ['vierzig'])
    f.add_arc('5', '6', ['fifty'], ['fünfzig'])
    f.add_arc('5', '6', ['sixty'], ['sechzig'])
    f.add_arc('5', '6', ['seventy'], ['siebzig'])
    f.add_arc('5', '6', ['eighty'], ['achtzig'])
    f.add_arc('5', '6', ['ninety'], ['neunzig'])

    # misc
    f.add_arc('3', '7', ['hundred'], ['hundert']) # one hundred
    f.add_arc('2', '7', ['hundred'], ['hundert']) # 2-9 hundred
    f.add_arc('3', '8', ['thousand'], ['tausend']) # one thousand
    f.add_arc('2', '8', ['thousand'], ['tausend']) # 2-9 thousand
    f.add_arc('5', '8', ['thousand'], ['tausend']) # 10-90 thousand
    f.add_arc('6', '8', ['thousand'], ['tausend']) # hundred thousand
    f.add_arc('3', '8', ['million'], ['million']) # one million

    # accept state
    f.set_final('2')
    f.set_final('6')
    f.set_final('7')
    f.set_final('8')

    disp = FSTDisplay(f)


def read_file():
    infile = open("input.dat", "r", encoding='utf-8')
    outfile = open("output.dat", "r", encoding='utf-8')

    inp = [line.rstrip() for line in infile]
    outp = [line.rstrip() for line in outfile]
    
    infile.close()
    outfile.close() 

    return inp, outp


if __name__ == '__main__':
    f = myFST('Finite State Transducer for German Numbers')
    finite_state(f)
    # mapping("60", "sechzig")

    inp, outp = read_file()
    # since line in input file == output file
    for i in range(len(inp)):
        print("\n" + inp[i] + ' ' + outp[i])
        mapping(inp[i], outp[i])