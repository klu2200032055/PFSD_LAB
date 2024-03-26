while True:
    try:
        n=int(input("Enter Integer Please:"))
        m=int(input("Enter Integer Please:"))
        z=n/m
        break
    except Exception as e:
        print("Not an integer!Please again like 108:")
        print(e)
    except ValueError:
        print("Not an Integer Please try again like 116:")
    finally:
        print("You successfully entered an integer!")
        break


