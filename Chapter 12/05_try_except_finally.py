try: 
    i = int(input("Enter a number: "))
    c = 1/i

except Exception as e:
    print(e)
    exit()

finally: #used for cleanup  #always run finally
    print("We are done")

print("Thanks for using the program")#print only if all condition are true



