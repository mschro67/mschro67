#by mschro67

from Grid import Grid
from time import sleep

print("\033c",end="")
print("Conways Game Of Life\nType \"help\" for help.")

last=[5,5,10,1.0]

try:
    while True:
        print()
        i=input("> ")
        match (i):
            case "help":
                print("Enter \"[rows] [cols] [gens] [secs/gen]\" and watch the cells changing.\nFor example: \"5 5 10 1\"")
                continue
            case "exit":
                exit(0)
            case "same":
                s=last.copy()
            case _:
                s=i.split()
                if len(s)!=4:
                    print("Invalid input!\n4 numbers required!\nFor example: [rows] [cols] [gens] [secs/gen]")
                    continue
                for x in range(3):
                    s[x]=int(s[x])
                s[3]=float(s[3])
        if s[0]*s[1]<9:
            print("The minimal grid size is 9 Cells! (3x3)")
            continue
        if s[3]>3.5:
            print(f"{s[3]} seconds are a lot of time for one Generation! ({s[3]*s[2]:.1f} secs for all gens)")
            c=input("Confirm Y/y: ")
            if c.lower()!="y":
                continue

        g=Grid(s[0],s[1])
        print("\033c",end="")
        g.display()
        print("Generation: 0")
        current=[-1]
        before=[-1]
        if s[3]>3:
            print("\nPress STRG+C to quit.")
        
        try:
            for gen in range(s[2]):
                before=g.grid.copy()
                sleep(s[3])
                print("\033c",end="")
                f=g.nextGen()
                current=g.grid.copy()
                g.display()
                print(f"Generation: {gen+1}")
                if f==0:
                    print(f"All cells are dead after {gen+1} generations!")
                    break
                if before==current:
                    print(f"Nothing changed from {gen} to {gen+1}!")
                    break
                if s[3]>2:
                    print("\nPress STRG+C to quit.")
            print("\nPress STRG+C to quit.")
            sleep(5)
        except KeyboardInterrupt:
            pass
        
        print("\033c",end="")
        print("Conways Game Of Life")

except Exception as e:
    print(e)
    exit(1)
