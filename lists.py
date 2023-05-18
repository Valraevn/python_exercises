nakeds = ['vulcan', 'rebel', 'hornet', 'bandit']
for naked in nakeds:
        print(f"{naked.title()} is a bike")
        print(f"{naked.title()} is a worthy bike.\n")
print("Bikes go vroom")

cruisers=['VN800', 'Intruder', 'SVX1100', 'vulcan']
also_nakeds=nakeds[:]
also_nakeds.append('bulldog')

bikes=list(set(nakeds+cruisers))
print(f"The full list of bikes is : \n{bikes}")
print()
print(f"of which these are nakeds:")
for naked in nakeds:
        print(naked.title())
print()
print(f"and these are cruisers:")
for cruiser in cruisers:
        print(cruiser)
print()
perfect_bike=[bike for bike in cruisers if bike in nakeds]
print("Hence the optimal bike; the bike in both lists is:")
for bike in perfect_bike:
        print(bike.title())
