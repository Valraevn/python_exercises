nakeds = ['vulcan', 'rebel', 'hornet', 'bandit']
cruisers=['VN800', 'Intruder', 'SVX1100', 'vulcan']

bikes=list(set(nakeds+cruisers))
print(f"\nThe full list of bikes is : \n{bikes}")

print(f"of which these are nakeds:")
for naked in nakeds:
        print(naked.title())

print(f"\nAnd these are cruisers:")
for cruiser in cruisers:
        print(cruiser)

perfect_bike=[bike for bike in cruisers if bike in nakeds]
print("\nHence the optimal bike; the bike in both lists is:")
for bike in perfect_bike:
        print(bike.title())
