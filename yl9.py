a =float(input("kolmnurga külg a:"))
b =float(input("kolmnurga külg b:"))
c =float(input("kolmnurga külg c:"))

if a + b > c and a + c > b and b +c > a:
    if a==b==c:
        print("võrdkülgnekomnurk")
    elif a==b or a==c or b==c:
        print("võrdhaarnekolmnurk")
    else:
        print("erikülgnekolmnurk")
else:
    print("pole kolmnurk")