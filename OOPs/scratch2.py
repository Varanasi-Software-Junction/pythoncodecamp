try:
    a = int(input("Enter price :"))
    if a < 0:
        raise ValueError('Price Negative me nahi ho sakta')
except Exception as e:
    print("Error :" + str(e))