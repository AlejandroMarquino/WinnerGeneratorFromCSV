import pandas as pd
if __name__ == '__main__':
   dataFrame = pd.read_csv() #The file path is entered here.
   lifetimeAmount = dataFrame[dataFrame["Lifetime Amount"] >= 50]
   name = lifetimeAmount["Name"]
   email = lifetimeAmount["Email"].str.slice(stop=3)
   joinedEmailName = pd.concat([name, email], axis=1)
   joinedEmailName = joinedEmailName.sample(n=5, axis=0, replace=False)
   print (joinedEmailName)






