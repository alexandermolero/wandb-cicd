from currency_converter import CurrencyConverter
c = CurrencyConverter()

def xe(amount=100,input_currency='eur',output_currency='usd'):
    converted_amount=round(c.convert(float(amount), input_currency.upper(),output_currency.upper()),2)
    msg='Currently '+str(amount)+' '+input_currency.upper()+' is equivalent to '+str(converted_amount)+' '+output_currency.upper()
    return print(msg)
    
xe(amount=100,input_currency='eur',output_currency='usd')