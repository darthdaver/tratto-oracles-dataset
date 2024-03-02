# tratto-oracles-dataset
This repository keeps track of the changes on the original _OraclesDatapoints_ Dataset of [TRATTO](https://github.com/AML14/tratto). 
The `oracles-dataset` folder contains the updated dataset.
The `oracles-backup` folder contains the oracles removed from the `oracles-dataset` files.
The folder contains 3 subfolders: `complex`, `grammar`, and `wrong`.
The `complex` folder contains the oracles that are too complex to generate an oracle, and therefore had been removed.
The `grammar` folder contains the oracles that are not compliant with the grammar implemented in TRATTO, and therefore had been removed.
The `wrong`folder contains the oracles that are wrong, and therefore had been removed.
Each subfolder contains a json file for each project processed in the oracles dataset (e.g. `commons-collections4-4.1`, `commons-math3-3.6.1`, etc.).
Each file contains a list of the json objects representing the oracles removed from the original dataset.

To easily remove an oracle from a file of the original dataset, there are two options.

1. Open the file as plain text and select the oracle with the following regex:
    ```shell
    
    ```shell
    \{\s*"id"\s*:\s*NUMBER[.\s\S]*?"tokensOracleVariablesNonPrivateNonStaticAttributes"[.\s\S]*?\},?
    ```
   Where you have to substitute the `NUMBER` with the identifier of the datapoint you want to select. For example:
    ```shell
    \{\s*"id"\s*:\s*7050[.\s\S]*?"tokensOracleVariablesNonPrivateNonStaticAttributes"[.\s\S]*?\},?
    ```
   Copy the selected text and paste it in the corrsponding `oracles-backup` folder. Remove the selected text from the original file.

2. Use the `remove_oracle.py` script. The script takes three arguments:
   * The absolute path to the file of the original dataset
   * The type of oracle to remove (complex, grammar, wrong)
   * The identifier of the oracle to remove (it can be a list of numbers separated by a white space, if you want to eliminate more than one oracle with a single command)
   The command is the following:
    ```shell
    python remove_oracle.py path_to_file type id_1 id_2 ... id_n
    ``` 
   The script will remove the oracles with the given identifiers from the file and will append them in the list of the corresponding `oracles-backup` file.  

   For example:
    ```shell
    python remove_oracle.py [path_to_oracles_dataset]/tratto-oracles-dataset/oracles-dataset/commons-collections4-4.1_0.json grammar 7050 7051 7052
    ```

Within the repository there are also a couples of additional files.

1. `negative_oracles_bookmark.txt` contains a reference to the first negative oracle datapoint, for each project (so that it is easy to individuate where to start to analyze the negative examples).
2. `oracles_changed_register.txt` contains a link to a google sheet: we can use it to keep track of the changes, 
   even before to push, so that we can contribute in parallel without overlapping. The sheet is very simple so that the 
   update it is not time consuming. There are two tables: the first one is composed of 6 columns that are `filename`, `id`, 
   `author`, `operation`, `type` and `notes`. The second one is composed of 3 columns: `project name`, `checked up to file`, `id`. 
   The first table keep track of the oracles changed and the operation performed (`fixed`or `removed`). 
   If the operation is `fixed`, the column `type` specifies the type of fix (e.g. `complex`, `grammar`, `wrong`), otherwise that column is empty.
   The second table keep track of the last changes to the project.