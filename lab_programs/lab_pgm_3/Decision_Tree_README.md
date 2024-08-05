# Decision Tree using ID3 Algorithm

This repository contains a Python implementation of the decision tree algorithm using the ID3 algorithm. The decision tree is built using a training dataset, and it is used to classify new samples from a test dataset.

## Files

- `main.py`: The main Python script that contains the implementation of the ID3 algorithm and the functions to build and use the decision tree.
- `data.csv`: The training dataset used to build the decision tree.
- `data_test.csv`: The test dataset used to classify new samples using the built decision tree.

## Usage

### Prerequisites

- Python 3.x
- Ensure you have the following CSV files in the same directory as the `main.py` script:
  - `data.csv` (training dataset)
  - `data_test.csv` (test dataset)

### Running the Program

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/decision-tree-id3.git
    cd decision-tree-id3
    ```

2. **Ensure you have the required CSV files:**

    - `data.csv`
    - `data_test.csv`

3. **Run the Python script:**
    ```bash
    python main.py
    ```

4. **Output:**
    - The program will print the structure of the decision tree built using the training dataset.
    - The program will classify each test instance from `data_test.csv` and print the classification results.

### Example Output

After running the program, you should see an output similar to the following:

```plaintext
The decision tree for the dataset using the ID3 algorithm is:
 Outlook
  Sunny
    Humidity
      High
        No
      Normal
        Yes
  Overcast
    Yes
  Rain
    Wind
      Weak
        Yes
      Strong
        No

The test instance: ['Sunny', 'Hot', 'High', 'Weak']
The label for the test instance: No
The test instance: ['Rain', 'Cool', 'Normal', 'Strong']
The label for the test instance: No
The test instance: ['Overcast', 'Mild', 'High', 'Weak']
The label for the test instance: Yes
The test instance: ['Sunny', 'Cool', 'High', 'Strong']
The label for the test instance: No
```

## Functions

### load_csv(filename)
Loads the CSV file and returns the dataset and headers.

Input: The name of the CSV file to load.
Output: The dataset (list of lists) and the headers (list).
Purpose: This function reads the CSV file containing the dataset, separates the header row from the data, and returns both.

### subtables(data, col, delete)
Creates subtables for each unique value of a column.

Input: The dataset, column index to split on, and a boolean indicating whether to delete the column after splitting.
Output: A dictionary of subtables keyed by unique column values.
Purpose: This function divides the dataset into subsets (subtables) based on the unique values in the specified column. This is essential for building the tree as each node splits the data based on the value of an attribute.

### entropy(S)
Calculates the entropy of a set.

Input: A list of values.
Output: The entropy value.
Purpose: Entropy measures the impurity or disorder of a set. It is used in the ID3 algorithm to determine the best attribute to split the data on by calculating the information gain.

### compute_gain(data, col)
Computes the information gain of a column.

Input: The dataset and column index.
Output: The information gain for the column.
Purpose: Information gain measures how well a given attribute separates the training examples according to their target classification. The attribute with the highest information gain is chosen to make the decision at each node in the tree.

### build_tree(data, features)
Builds the decision tree using the ID3 algorithm.

Input: The dataset and list of feature names.
Output: The root node of the decision tree.
Purpose: This recursive function builds the decision tree by selecting the attribute with the highest information gain at each step and creating child nodes for each unique value of the chosen attribute. The process continues until all data points are correctly classified or no further attributes are available.

### print_tree(node, level=0)
Prints the structure of the decision tree.

Input: The root node of the tree and the current level of depth (default is 0).
Output: None (prints the tree structure).
Purpose: This function visually represents the structure of the decision tree by printing the attribute at each node and the branches for each value of the attribute.

### classify(node, x_test, features)
Classifies a new sample using the decision tree.

Input: The root node of the tree, a test instance, and the list of feature names.
Output: None (prints the classification result).
Purpose: This function traverses the decision tree based on the values of the test instance's attributes and prints the classification result (the label assigned to the test instance).

## Example Datasets
### data.csv (Training Dataset)

Outlook,Temperature,Humidity,Wind,PlayTennis
Sunny,Hot,High,Weak,No
Sunny,Hot,High,Strong,No
Overcast,Hot,High,Weak,Yes
Rain,Mild,High,Weak,Yes
Rain,Cool,Normal,Weak,Yes
Rain,Cool,Normal,Strong,No
Overcast,Cool,Normal,Strong,Yes
Sunny,Mild,High,Weak,No
Sunny,Cool,Normal,Weak,Yes
Rain,Mild,Normal,Weak,Yes
Sunny,Mild,Normal,Strong,Yes
Overcast,Mild,High,Strong,Yes
Overcast,Hot,Normal,Weak,Yes
Rain,Mild,High,Strong,No

### data_test.csv (Test Dataset)
