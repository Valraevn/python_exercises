responses={}
#set flag to indicate active polling
polling_active=True

while polling_active:
    name=input("\nWhat's ur name?   ")
    response=input("\nWhich mountain would you like to climb someday?")

    #store the reponse in responses{}
    responses[name]=response
    #add peeps
    repeat=input("Next person? (y/n)")
    if repeat=='n':
        polling_active=False
#Now the results:
print("\n--- Poll results ---")
for name, response in responses.items():
    print (f"\n{name} would like to climb {response}.")
