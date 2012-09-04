class fizz_buzz:
        
    def get(self, number):
        
        response = ""
        
        if (not (number % 3)):
            response = "fizz"
        
        if (not (number % 5)):
            response += "buzz"
        
        return response if response else number