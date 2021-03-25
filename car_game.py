move = ""
started = True
while True:
    move = input("> ").lower()
    if move == "start":
        if not started:
            print("already started")
        else:
            started = False
            print("ready to go")
    elif move == "stop":
        if started:
            print("not yet started")
        else:
            started = True
            print("car stopped")
    elif move == "help":
        print("""
start - to start
stop - to stop
quit - to exit""")
    elif move == "quit":
        break
    else:
        print("I dont understand")