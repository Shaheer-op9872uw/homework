class RomanConverter:
    def to_roman(self, number):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]7
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""
        for i in range(len(values)):
            while number >= values[i]:
                roman += symbols[i]
                number -= values[i]
        return roman

num = int(input("Enter a number: "))
converter = RomanConverter()
print("Roman numeral:", converter.to_roman(num))
