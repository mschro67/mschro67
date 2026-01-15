#forms v2.0.3
#by mschro67

config = {
    "scope" : 500,
    "wait" : 1,
    "speed" : 400,
    "needMoreThan3Edges" : True,
    "useTime" : True,
    "tellAboutHelp" : True,
    "showErrors" : True,
    "tellAboutCreator" : True
}

if config["tellAboutCreator"]:
    print("This programm was made by mschro67.")

if config["tellAboutHelp"]:
    print("Type \"help\" to get more information.")

try:
    from turtle import Turtle
    
    if config["useTime"]:
        try:
            print()
            from time import sleep
        except ModuleNotFoundError:
            if config["showErrors"]:
                print("module \"time\" not found!")
            config["useTime"] = False

    turtle = Turtle()
    turtle.speed=config["speed"]

    while True:
        turtle.reset()
        print()
        if config["useTime"]:
            sleep(0.1)
        
        try:
            i = input("> ")
            match i:
                case "help":
                    print("This programm generates a form based on the number of edges, you enter.\nEnter the number of edges you want, after the \">\" or enter \"exit\" to exit the programm.")
                    continue
                case "exit":
                    exit(0)

            i=int(i)
            if ["needMoreThan3Edges"] and i<3:
                print("there cant be less than 3 edges")
                continue
            
            turtle.backward(config["scope"]/i/2)
            for x in range(i):
                turtle.forward(config["scope"]/i)
                turtle.left(360/i)
            
            if config["useTime"]:
                sleep(config["wait"])
        except Exception as e:
            if config["showErrors"]:
                print(f"{e}!")

except ModuleNotFoundError:
    if config["showErrors"]:
        print("module \"turtle\" not found!")
    exit(1)
except:
    exit(1)
