class Value():
    def __init__(self):
        self.commission = None

    def __get__(self, obj, obj_type):
        if self.commission is None:
            self.commission = obj.commission
        return self.value

    def __set__(self, obj, value):
        if self.commission is None:
            self.commission = obj.commission
        self.value = value * (1 - self.commission)


#class Account:
#    amount = Value()
#
#    def __init__(self, commission):
#        self.commission = commission


#new_account = Account(0.1)
#new_account.amount = 100

#print(new_account.amount)
