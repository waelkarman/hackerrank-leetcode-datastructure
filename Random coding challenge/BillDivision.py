
def bonAppetit(bill, k, b):
    # Write your code here
    k=[k]
    sum_b=0
    for a in bill:
        sum_b+=a
    for a in k:
        sum_b=sum_b-bill[a]
    sum_b=sum_b/2
    if sum_b == b:
        print("Bon Appetit")
    else:
        print(int(b-sum_b))


