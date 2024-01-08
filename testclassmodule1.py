print("You have imported TestClassModule successfully - the following module is intended to test classes through modules.")

class TestClass:
    testclassvar = None
    testclassvar1 = None

    def testclassact():
        print("Test Class action done!")
    def testclassvarsact():
        testclassvar = input ("Type something: ")
        testclassvar1 = input ("Add some extra info: ")
        print(testclassvar, testclassvar1)
    pass