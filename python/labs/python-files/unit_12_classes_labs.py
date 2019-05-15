"""
title: classes_exercises
author: eam3kzn
date: 6/18/18 9:33 AM
"""


class StringManipulation:

    def __init__(self, altering_str):
        self.altering_str = altering_str

    def string_reversal(self,reverse=None):
        if reverse is not None:
            print(reverse[::-1])
            return reverse[::-1]
        else:
            print(self.altering_str[::-1])
            return self.altering_str[::-1]

    def removing_case(self, removed=None):
        if removed is not None:
            removed = removed.lower().replace(" ", "").replace(",", "").replace("'", "")
            print(removed)
            return removed
        else:
            self.altering_str = self.altering_str.lower().replace(' ', '').replace(',', '').replace("'", '')
            print(self.altering_str)
            return self.altering_str

    def is_vowel(self,searching=None):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        if searching is not None:
            if vowels.intersection(searching):
                print(True)
                return True
            else:
                print(False)
                return False
        else:
            if vowels.intersection(self.altering_str):
                print(True)
                return True
            else:
                print(False)
                return False

    def is_palindrome(self,searching=None):
        if searching is not None:
            if searching == searching[::-1]:
                print(True)
                return True
            else:
                print(False)
                return False
        else:
            if self.altering_str == self.altering_str[::-1]:
                print(True)
                return True
            else:
                print(False)
                return False

    def short_hand(self,short=None):
        if short is not None:
            if 'U' in short:
                short = short.replace('U', '')
            if 'and' in short:
                short = short.replace('and', '&')
            if 'to' in short:
                short = short.replace('to', '2')
            if 'you' in short:
                short = short.replace('you', 'U')
            if 'for' in short:
                short = short.replace('for', '4')
            if 'a' in short:
                short = short.replace('a', '')
            if 'A' in short:
                short = short.replace('A', '')
            if 'e' in short:
                short = short.replace('e', '')
            if 'E' in short:
                short = short.replace('E', '')
            if 'i' in short:
                short = short.replace('i', '')
            if 'I' in short:
                short = short.replace('I', '')
            if 'o' in short:
                short = short.replace('o', '')
            if 'O' in short:
                short = short.replace('O', '')
            if 'u' in short:
                short = short.replace('u', '')
            print(short)
            return short
        else:
            if 'U' in self.altering_str:
                self.altering_str = self.altering_str.replace('U', '')
            if 'and' in self.altering_str:
                self.altering_str = self.altering_str.replace('and', '&')
            if 'to' in self.altering_str:
                self.altering_str = self.altering_str.replace('to', '2')
            if 'you' in self.altering_str:
                self.altering_str = self.altering_str.replace('you', 'U')
            if 'for' in self.altering_str:
                self.altering_str = self.altering_str.replace('for', '4')
            if 'a' in self.altering_str:
                self.altering_str = self.altering_str.replace('a', '')
            if 'A' in self.altering_str:
                self.altering_str = self.altering_str.replace('A', '')
            if 'e' in self.altering_str:
                self.altering_str = self.altering_str.replace('e', '')
            if 'E' in self.altering_str:
                self.altering_str = self.altering_str.replace('E', '')
            if 'i' in self.altering_str:
                self.altering_str = self.altering_str.replace('i', '')
            if 'I' in self.altering_str:
                self.altering_str = self.altering_str.replace('I', '')
            if 'o' in self.altering_str:
                self.altering_str = self.altering_str.replace('o', '')
            if 'O' in self.altering_str:
                self.altering_str = self.altering_str.replace('O', '')
            if 'u' in self.altering_str:
                self.altering_str = self.altering_str.replace('u', '')
            print(self.altering_str)
            return self.altering_str

    def pig_latin(self,pig=None):
        if pig is not None:
            if not set('aeiouAEIOU').intersection(pig):
                pig += "ay"
            elif set('aeiouAEIOU').intersection(pig[0]):
                pig += "yay"
            else:
                vowel_index = 0
                first_chunk = ""
                second_chunk = ""
                while not set('aeiouAEIOU').intersection(pig[vowel_index]):
                    first_chunk += pig[vowel_index]
                    vowel_index += 1
                second_chunk += pig[vowel_index:len(pig)]
                pig = second_chunk + first_chunk + "ay"
            print(pig)
            return pig
        else:
            if not set('aeiouAEIOU').intersection(self.altering_str):
                self.altering_str += "ay"
            elif set('aeiouAEIOU').intersection(self.altering_str[0]):
                self.altering_str += "yay"
            else:
                vowel_index = 0
                first_chunk = ""
                second_chunk = ""
                while not set('aeiouAEIOU').intersection(self.altering_str[vowel_index]):
                    first_chunk += self.altering_str[vowel_index]
                    vowel_index += 1
                second_chunk += self.altering_str[vowel_index:len(self.altering_str)]
                self.altering_str = second_chunk + first_chunk + "ay"
            print(self.altering_str)
            return self.altering_str


def main():
    word = StringManipulation("Hello, for you to - here's a string to CHANGE")
    word.string_reversal()
    word.removing_case()
    word.is_vowel(searching="ffff")
    word.is_palindrome(searching="ffffff")
    word.short_hand()
    word.pig_latin()


if __name__ == "__main__":
    main()
