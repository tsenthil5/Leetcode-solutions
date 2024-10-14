class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        1) split it into lists
        2) check if the first word of both string is same or not
        3) if same then check if last word is same or not
        4) if same then check if all the words in the shroter sentence is in longer sentence or not
        5) if yes then return true
        6) return false

        7) if words in the end are not same then start checking from the start
        8) if aall present return true else false

        9) if first word is not similar and last word is similar
        10) start checking from last word if all matched return True else false
        11) else if shorter string is empty return True
        12) relse return False
        """

        def checkBothEnds(short, longer):
            shortLeft, shortRight = 0, len(short)-1
            longLeft, longRight = 0, len(longer)-1
            while shortLeft <= shortRight:
                
                if short[shortLeft] == longer[longLeft]:
                    shortLeft+=1
                    longLeft+=1

                elif short[shortRight] == longer[longRight]:
                    shortRight-=1
                    longRight-=1

                else:
                    return False

            return True

        def checkStart(short, longer):
            shortLeft = 0
            longLeft = 0
            while shortLeft!=len(short):
                if short[shortLeft] == longer[longLeft]:
                    shortLeft+=1
                    longLeft+=1

                else:
                    return False
            return True

        def checkEnd(short, longer):
            shortRight = len(short)-1
            longRight = len(longer)-1
            while shortRight>=0:
                if short[shortRight] == longer[longRight]:
                    shortRight-=1
                    longRight-=1

                else:
                    return False
            return True
                
            


        def sentenceSimilar(short, longer):
            if len(short) == "":
                return True

            elif short[0] == longer[0]:
                if short[-1] == longer[-1]:
                    return checkBothEnds(short, longer)
                else:
                    return checkStart(short, longer)

            elif short[-1] == longer[-1]:
                return checkEnd(short, longer)
                


        sentence1 = sentence1.split(" ")
        sentence2 = sentence2.split(" ")
        if len(sentence1) < len(sentence2):
            return sentenceSimilar(sentence1, sentence2)

        else:
            return sentenceSimilar(sentence2, sentence1)

        


        