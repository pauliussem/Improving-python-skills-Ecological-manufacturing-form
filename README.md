## 		Ecological manufacturing form
This project was made since problem which I had to solve, seemed interesting to try to solve and visualise with python help. 

Target was to improve python skills and challenge myself.

### Project:

Move from regular ecological manufacturing form to internet.
This form consists of 13 tables and farmers must to fill it depending on actions he has made.

The most complicated table was 1st one. I had to find a way to relate 1st and 5th tables, so entered data regarding production by field would sum up and move to table 5 automatically depending on production and status.

![1](https://github.com/user-attachments/assets/356a00eb-fa6f-4d49-8e96-827ac9aba2c0)


Since there was not enough information, I had to make few modifications with 1st table.

![2](https://github.com/user-attachments/assets/147d242c-6421-495d-8f11-a20ec930ddcc)

The first 4 fields are imported from our declaration system. Plant code could consist of only one plant or more plants and regardless of this production could consist of 1 plant or mixed plants e.g. hay could be made of 3 different or more grasses.

### So I had to apply 3 logics:

    1. Plant code, which can consist of different plants.
    2. Plant code, which can consist of different plant groups.
    3. Plant code, which can consist only from 1 plant.

NOTE. If plant code consists of independet different plants and production is entered with regular plant code, I change it to first plant code and sum up everything as one production. E.g. If "Cucumbers" are entered by code "CUC" and we have code "MIV" (mixed vegetables), I change code "CUC" to "MIV" and sum up both productions.

![3](https://github.com/user-attachments/assets/b841001b-a2fa-4c6c-ba85-0ce997ed7c3e)
