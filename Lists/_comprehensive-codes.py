squares = [i * i for i in range(10)]
print(squares)

number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)


li = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(li)


sentence = 'the rocket came back from mars'
print(' '.join([i for i in sentence if i not in 'aeiou']))


c='string methods helps to do the task easier'
l=c.split()
s=l[0]+' '+' '.join(str(w[::-1]) for w in l[1:len(l)-1])+' '+ l[len(l)-1]
print(s)



txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

def get_price_with_tax(txn):
    return round(txn * (1 + TAX_RATE),4)

final_prices = [get_price_with_tax(i) for i in txns]
print(final_prices)