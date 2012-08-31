


class fizz_buzz:
        
        
    def get(self, number):
        
        if (not (number % 3) and not (number % 5)):
            return 'fizzbuzz'
        
        if (not (number % 3)):
            return "fizz"
        
        if (not (number % 5)):
            return "buzz"
        
        return number