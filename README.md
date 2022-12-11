# Tweet_Classifier
Project for the subject Human-Centered Artificial Intelligence for the master's degree in Engineering and Data Science at the University of Coimbra, done by students Rafael S. Gouveia and Andrei Fokin Teixeira. 

This repository contains the codes of the decision tree model that classifies between Positive, Negative and Neutral tweets related to the presidential candidates, Lula and Bolsonaro, of the 2022 Brazilian elections.

### This Repository is organized as follows:
- Two main folders, one containing the codes and one containing the data.
 1. The folder "cod" contains the codes have three folders:
     - getData which is the first step, i.e. first code to be run, because it is the code that will collect the data.
     - The second step is in the normalization folder, which has four codes that are organized as follows: 
          1. Three notebooks, where it will do the normalization.
          2. A python file that contains the codes that will perform the normalization transformations of the tweets, we did it this way because it would be faster, more organized and easier to perform the same data normalization operations.
          
     - Finally we have the model folder, which has the notebook "modelos_treino_teste.ipynb" that will do the training and testing using the data that was collected and normalized previously and will also save the models, vectorizers and the target categories to be used later without the need to train again. There is also another notebook named "utilizandoModelos.ipynb" that will use the previously saved models, vectorizers and target categories. This folder also has another folder "classificadores", where the templates, vectorizers and target categories have been saved.

  2. The "data" folder contains the data in three folders:
     - The "raw data" folder contains the data that was collected by the "getTweets_toCSV.ipynb" code.
    - The "train_data" folder contains the normalized data that will be used by the code in the notebook "train_test_templates.ipynb".
    - The "test_data" folder contains the test data that will be used by the code in the notebook "utilizandoModelos.ipynb".

  3. The folder that contains the Project paper.
     - It contains the paper files in .pdf and .docx.
