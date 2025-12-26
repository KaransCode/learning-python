def func1():
    if __name__ == "__main__":
        print("Hello World!!, From Module")
    else:
        print("Hello World!!")


if __name__ == "__main__":
    # if we run this function from the source file Then
    print("We are running this file directly")
    func1()
    print(__name__)