#!/usrbin/python3

cabbage={'colour':'green', 'fryable':'kind_of', 'throwable':'yes'}
egg={'colour':'creme', 'fryable':'yes', 'throwable':'yes'}
milk={'colour':'white', 'fryable':'no', 'throwable':'no'}

print(cabbage['fryable'])

cabbage['crunchy']= 'kind_of'

for key, value in cabbage.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("\nThese are the keys:")
for attribute in egg:
    print(attribute)

print("\nThese are the key values:")
for attribute in egg.values():
    print(attribute)

print('##########################################')
