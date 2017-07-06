class LongNameDict(dict):
    "method to find out the longest key"
    def longest_key(self,key):
        longest = None
        for key in self :
            if not longest or len(key) > len(longest):
                longest = key

        return longest
if __name__ =="main":
    main()
    
