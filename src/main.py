import funcs

def main():

    r = funcs.get_request("https://augusto-test.free.beeceptor.com/patient")
    print(r)
    return


if __name__ == "__main__":
    main()
