class sentence():
    def __init__(self,sentence_string):
        self.frequencies = {}
        self.string = sentence_string
    def letter_frequency(self):    
        for letter in self.string:
            frequency = self.frequencies.setdefault(letter,0)
            self.frequencies[letter] = frequency + 1
        return self.frequencies
    
        
if __name__ == "main":
    main()
    
