# Created temporary lists, where I will store temp data about inserted values.

kodas = []
kultura = []
produkcija = []
statusas = []
kiekis = []

# Created lists, where I will store appended data from temp lists.

kodas1 = []
kultura1 = []
produkcija1 = []
statusas1 = []
kiekis1 = []

# Created empty lists where number of indexes of each group will be stored.
# It is more critical to use it at then end, however just in case.

indexkult = []
indexprod = []
indexstat = []

# For creation of a table.

import pandas as pd

# Created temp list, so I could sort names of inserted values.

bmikultura = []

# Created lists of mixed plant code with only 1 possible value.
# If value from this list will be inserted, logic2 will be applied.
# It consists of more vegetables, however it wouldn't change any point.

DAM = ["DAM", "AGU", "POM", "SVO", "KOP"]

# Variable, so I could use it in a while loop.
i = "t"

# Boolean variable, so it would ask to add one more value mandadory only one time.
darviena = True

# Function, so I could append lists with templists easier.
# Maybe not necessary, because of next function, just wanted to use return function.
def app(x,y):
  return x.append(y)

# Function to append all lists with temp lists.
def appvisi():
  app(kodas1, kodas)
  app(kultura1, kultura)
  app(produkcija1,produkcija)
  app(statusas1,statusas)
  app(kiekis1,kiekis)


# Opened while loop, so it would be possible to enter data as many times as you want.
while i == "t":
  # Opened second while loop to enter as many as needed plants.
  while i == "t":
    kodas = input("Įveskite naudmenų kodą: ")

    # Logic1. Mixed plant code with 2 or more plants and 1 production.
    if kodas in ("BMI"):

      # Opened while loop, so it would be possible to enter 2 or more values.
      while i == "t":
        app(bmikultura, input("Įveskite kultūrą: "))

        # Mandatory to enter second value (for first time).
        # After closing while loop with boolean False.
        while darviena:
          app(bmikultura, input("Įveskite dar vieną kultūrą:"))
          darviena = False

        # For entering plant name as many times as you want.
        i = input("Ar norite suvesti dar vieną kultūra? t/n")
        # bmikultura.sort()
        # kultura = ", ".join(bmikultura)

      # After while loop is closed, sorting inserted values and clear bmikultura list.
      # Inserting relevant information about plant name, production, status and quantyti.
      else:
        bmikultura.sort()
        kultura = ", ".join(bmikultura)
        bmikultura = []
        produkcija = input("Įveskite produkciją: ");
        statusas = input("Įveskite statusą: ");
        kiekis = (int(input("Įveskite derliaus kiekį: ")));

        # If inserted plant name in a production list (table 5) checking for indexes.
        # Else entering data as a new record.
        for a in kultura1:
          if a == kultura:
            indexkult = [index for index, b in enumerate(kultura1) if b == kultura]

            # Checking if entered production match with entered plant name, by their indexes.
            for a in indexkult:
              if produkcija1[a] == produkcija:
                  indexprod += [a]

                  # Checking if entered status match with production.
                  # Since only 1 status out of 3 is possible, summarizing inserted quantyti to existing record.
                  for a in indexprod:
                    if statusas1[a] == statusas:
                      indexstat += [a]
                      kiekis1[min(indexstat)] += kiekis
                      break

                  # Breaking all loops if any of if conditions are not fullfilled and appending inserted values as a new record.
                  else:
                    continue
                  break
            else:
              continue
            break
        else:
          appvisi()
        break

    # Logic2. Mixed code with one possible plant and production.
    elif kodas in DAM:
        kultura = input("Įveskite kultūrą: ");
        produkcija = input("Įveskite produkciją: ");
        statusas = input("Įveskite statusą: ");
        kiekis = (int(input("Įveskite derliaus kiekį: ")));
        for a in kultura1:
          if a == kultura:
            indexkult = [index for index, b in enumerate(kultura1) if b == kultura]
            for a in indexkult:
              if produkcija1[a] == produkcija:
                  indexprod += [a]
                  for a in indexprod:
                    if statusas1[a] == statusas:
                      indexstat += [a]
                      kiekis1[min(indexstat)] += kiekis

                      # Same logic as above untill here. Since DAM(mixed vegetables), changing plant lower level plant code to DAM.
                      # To avoid 2 different records with the same production. E.g. POM-POM-POM-E-10 and DAM-POM-POM-E-20
                      if kodas == "DAM":
                        index = min(indexstat)
                        kodas1[min(indexstat)] = "DAM"
                      break
                  else:
                    continue
                  break
            else:
              continue
            break
        else:
          appvisi()
        break

    # Logic3. Plant code for each plant and production.
    else:
      kultura = input("Įveskite kultūrą: ");
      produkcija = input("Įveskite produkciją: ");
      statusas = input("Įveskite statusą: ");
      kiekis = (int(input("Įveskite derliaus kiekį: ")));
      for a in kultura1:
        if a == kultura:
          indexkult = [index for index, b in enumerate(kultura1) if b == kultura]
          for a in indexkult:
            if produkcija1[a] == produkcija:
                indexprod += [a]
                for a in indexprod:
                  if statusas1[a] == statusas:
                    indexstat += [a]
                    kiekis1[min(indexstat)] += kiekis
                    break
                else:
                  continue
                break
          else:
            continue
          break
      else:
        appvisi()
      break

  # Creating array of all lists and one more for column names.
  array = [kodas1, kultura1, produkcija1, statusas1, kiekis1]
  headers = ["Kodas", "Kultura", "Produkcija", "Statusas", "Kiekis"]

  # Setting temporary lists and variable to primary state.
  indexkult = []
  indexprod = []
  indexstat = []
  darviena = True
  kodas = []
  kultura = []
  produkcija = []
  statusas = []
  kiekis = []

  # Making dictionary out of array.
  d1 = zip(headers, array)
  d = dict(d1)

  # Making table out of dictionary and adding +1 to index, so in table it would begin from 1.
  table = pd.DataFrame(d)
  table.index += 1

  # Creating output for better understanding of applied changes and asking if one more production should be inserted.
  print()
  print("PRODUKCIJA:")
  print(table)
  i = input("Ar norite įvesti dar vieną produkciją?")

# After all production is entered printing final table.
print()
table