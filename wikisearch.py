import wikipedia

research = input("research\n")

query = wikipedia.page(research)

print(query.summary)

# install the package wikipedia 
