''' D'ni Numerals
Convert a decimal to base 25 D'ni numerals.

There can be rounding errors with some fractional number.

    2024-06-05 - v0.01
    stone@stone-shard.com
    Stone {Matt Cascone}
'''

from math import fabs
from fractions import Fraction


# 
class Alphanumericals:
    ''' Convert a decimal to a base 25 D'ni numeral.
            "Alphanumericals or Alphanumeric characters are any collection of
             number characters and letters in a certian language. --Wiki"
             
            .alphabetic() -> "-sehnsee+fah/vahgahbree"
            .alphanumeric() -> "-3.3DC8E", "-3+1/7"
            .numeric() -> "|-|3|.|3|13|12|8|14|", "|-|3|+|1|/|7|" '''

    # Punctuation
    apostrophe = "'"
    comma = ','
    divide = '/'
    hyphen = '~'
    negative = '-'
    plus = '+'
    powers = '|'
    radix = '.'

    # Largest denominator value
    limit_denominator = 25  # max= 244140624


    #
    def __init__(self, decimal=None):

        ''' Takes a decimal to convert to base 25 .
        
            Perameters
            ----------
                decimal : float, optional
                    The decmal to convert to base 25. 
                    Will ask user if None given. '''
        if decimal is not None:
            self.decimal = decimal
        else:
             self.decimal = self._AskDecimal()


    # Ask for number
    def _AskDecimal(self) -> float:
        ''' Ask user to input a decimal.
            Errors: ValueError, will ask again. 
            Returns: int or float '''
    
        decimal = 'nan'
        while decimal == 'nan':
            text = input("\nInput a number to convert to D'ni.\n-> ")
            try:
                decimal = float(text)
                if decimal.is_integer():
                    decimal = int(decimal)
            except ValueError:
                print("ERROR: Not a number")
        return decimal


    # List of base 25 integers. # [9, 8]
    def _base25(self, fraction=False) -> list:
        ''' Convert a decimal to a list of base 25 integers.
            Punctuation is included as string
    
            Perameters
            ----------
                fraction : bool, optional
                    Convert to a base 25 'decimal' or fraction.
            Returns
            -------
                list :
                    of base 25 integers ['-', 3, '.', 3, 13, 12, 8, 14]
                    or as fraction ['-', 3, '+', 1, '/', 7] '''

        base_25 = []
        base_10 = self.decimal

        #
        def _integral25(integral):
            result = []
            while integral >= 0:
                result.insert(0, integral % 25)
                integral = integral // 25
                if integral == 0:
                    break
            return result

        #
        if base_10 < 0:
            base_10 = fabs(base_10)
            base_25.append(self.negative)

        integral = int(base_10)
        base_25 += _integral25(integral)

        if type(self.decimal) is not float:
            return base_25

        # fractional = base10 - int(base10)
        fractional = float(str(base_10)[len(str(int(base_10))):])

        if fraction:
#            limit_denominator = 25  # max= 244140624
            fract = Fraction(fractional).limit_denominator(self.limit_denominator)
            numerator, denominator = fract.as_integer_ratio()
            base_25.append(self.plus)
            base_25 += _integral25(numerator)
            base_25.append(self.divide)
            base_25 += _integral25(denominator)
            return base_25

        else:  # as 'decimal'
            limit = len(str(fractional)) - 2
            base_25.append(self.radix)
            i = 1
            while fractional >= 0:
                fract_25 = fractional * 25
                fractional = fract_25 - int(fract_25)
                base_25.append(int(fract_25))
                i += 1
                if i > limit or i >= 15:
                    break
            return base_25


    # Alphanumeric number system
    def alphanumeric(self, fraction=False) -> str:
        ''' Base 25 Alphanumeric Number System.
                0123456789ABCDEFGHIJKLMNO
    
            Perameters
            ----------
                fraction : bool, optional
                    Convert to a base 25 'decimal' or fraction.
            Returns
            -------
                string :
                    Base-25 Alphanumeric Number System.
                    "-3.3DC8E" or as fraction "-3+1/7" '''

        result = ""
        for item in self._base25(fraction):
            if type(item) is int and item > 9:
                item = chr(ord('A') + item - 10)
            result += str(item)
        return result


    # Numeric string # |9|8|
    def numeric(self, fraction=False) -> str:
        ''' Numeric String. Base 25 numbers 0-24
        with powers seperated with a bar.

            Perameters
            ----------
                fraction : bool, optional
                    Convert to a base 25 'decimal' or fraction.
            Returns
            -------
                string :
                    Base 25 numbers with the powers seperated with a bar.
                    "|-|3|.|3|13|12|8|14|" or as fraction "|-|3|+|1|/|7|" '''

        string = self.powers.join(map(str, self._base25(fraction)))
        return f'{self.powers}{string}{self.powers}'


    # Alphabetic Text Standard # vagatorsí,vagasen
    def alphabetic(self, standard='nts') -> str:
        ''' D'ni Alphabetic Text Standards.

            Perameters
            ----------
                standard : string, optional
                    'ots' = Old Text Standard
                    'nts' = New Text Standard
            Errors
            ------
                OverflowError :
                    D'ni does not have a word for powers over 6.
                    The larges decimal that can be represented is 244,140,624.
            Returns
            -------
                string :
                    Alphabetic numbers using the given Text Standard.
                    "-sehnsee+fah/vahgahbree" '''

        standards = ('ots', 'nts')  # , 'dni')
        ones_stems = (  # (('ots', ), ('nts', ))
            ('roon', 'fah', 'bree', 'sehn', 'tor'),
            ('rún', 'fa', 'brí', 'sen', 'tor'))
#            ('rUn', 'fa', 'brE', 'sen', 'tor'))
        conjunctions = ('gah', 'ga')  # , 'ga')
        fives_stems = (  # value: (stem, reduced),
            {20: ('rish', 'ri'), 15: ('heebor', 'hee'),
             10: ('nayvoo', 'nay'), 5: ('vaht', 'vah')},
            {20: ('riš', 'ri'), 15: ('híbor', 'hí'),
             10: ('névú', 'né'), 5: ('vat', 'va')})
#            {20: ('riS', 'ri'), 15: ('hEbor', 'hE'),
#             10: ('nAvU', 'nA'), 5: ('vat', 'va')})
        powers_suffixes = (  # 25 ** index
            ('', 'see', 'rah', 'lahn', 'mel', 'blo'),
            ('', 'sí', 'ra', 'lan', 'mel', 'blo'))
#            ('', 'sE', 'ra', 'lan', 'mel', 'blo'))

        #
        def _build_stems(n: int) -> str:
            result = ''
            for k, v in fives_stems[standard].items():
                if n // k:
                    n = n - k
                    if n == 0:
                        return v[0]
                    else:
                        result += v[1] + conjunctions[standard]
            result += ones_stems[standard][n]
            return result

        #
        def _buildPowers(base_25):
            i = len(base_25)
            if i > 6:  # 244140624
                raise OverflowError("244,140,624 is the largest number that"
                                    " can be represented alphabetically in D'ni")

            if i == 1 and base_25[0] == 0:
                return ones_stems[standard][0]

            result = ''
            if base_25[0] == self.negative:
                base_25 = base_25[1:]
                result += self.negative

            for n in base_25:
                i -= 1
                if n > 0:
                    result += _build_stems(n)
                    result += powers_suffixes[standard][i]
                    if i > 0:
                        result += self.comma

            if result.endswith(self.comma):
                result = result[:-1]
            return result

        #
        if standard in standards:
            standard = standards.index(standard)
        else:
            raise KeyError(f"The text standard '{standard}' was not found."
                           f" Standard must be from {standards}")

        base_25 = self._base25(fraction=True)
        if self.divide not in base_25:
            return _buildPowers(base_25)

        id1 = base_25.index(self.plus)
        id2 = base_25.index(self.divide)

        integral = _buildPowers(base_25[:id1])
        numerator = _buildPowers(base_25[id1+1:id2])
        denominator = _buildPowers(base_25[id2+1:])

        return ''.join((integral, self.plus, numerator, self.divide, denominator))



#
def ntsToDnifont(text: str) -> str:
    ''' Map alphanumeric and New Translation Standards to Cyan's D'ni Font.
        The D'ni Font does not have a symbol for division, 
        fractions will use a period.

            Perameters
            ----------
                text : string
                    Can be a nts or alphanumeric.
                        The result from Alphanumericals().alphbetic() or...
                        The result from Alphanumericals().alphanumeric()
            Errors
            ------
                The D'ni Font is missing some math symbols. 
                They will be removed.
                    The plus symbol '+' is maped to infinity. 
                    The division symbol '/' does not exist.
                    ...
            Returns
            -------
                string :
                    Cyan's D'ni Font 
                    "-3.3#@8$" '''
    # Dn'i Font
    # | -> 25 
    # = -> mod12 
    # + -> infinity 
    # / -> None
    # ~ -> None
    # ' -> comma
    
    # (("NTS", "D'ni Font"), )
    punctuation = (('+', '.'), ('=', ' '), ('-', '-'), ('~', '-'), 
                   ('|', ' '), ('/', '.'), ('‘', "'"))
   
    alphanumeric = (('A', ')'), ('B', '!'), ('C', '@'), ('D', '#'), ('E', '$'),
                    ('F', '%'), ('G', '^'), ('H', '&'), ('I', '*'), ('J', '('),
                    ('K', '['), ('L', ']'), ('M', '\\'), ('N', '{'), ('O', '}'),
                    ('P', '|'), ('Y', '='), ('Z', '+'))
  
    alphabetic = (('æ', 'å'), ('é', 'A'), ('ç', 'c'), ('d', 'D'), ('ð', 'd'),
                  ('í', 'E'), ('á', 'I'), ('k', 'K'), ('x', 'k'), ('ó', 'O'), 
                  ('š', 'S'), ('þ', 'T'), ('c', 'x'), ('ú', 'U'))
    
    for k, v in punctuation + alphanumeric + alphabetic:
        text = text.replace(k, v)
    return text


def _main():
    help(Alphanumericals)
    print(''' |  ----------------------------------------------------------------------
 |  Usage examples shown here:
 |
 |  >>> x = Alphanumericals(-3.14159)
 |
 |  >>> x.alphanumeric()
 |  -3.3DC8E
 |
 |  >>> x.alphanumeric(fraction=True)
 |  -3+1/7
 |
 |  >>> x.numeric()
 |  |-|3|.|3|13|12|8|14|
 |
 |  >>> x.numeric(fraction=True)
 |  |-|3|+|1|/|7|
 |
 |  >>> x.alphabetic(standard='ots')
 |  -sehnsee+fah/vahgahbree
 |
 |  >>> x.plus = ' • '
 |  >>> x.divide = ' / '
 |  >>> x.alphabetic(standard='nts')
 |  -sensí • fa / vagabrí
 |
    ''')
    help(ntsToDnifont)

    
if __name__ == "__main__":
    _main()


