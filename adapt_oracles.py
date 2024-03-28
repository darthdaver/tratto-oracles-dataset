"""Script used to insert the Javadoc information about method and attribute
tokens from an existing oracles dataset into this one.
"""

import json
import os

def adapt_oracles():

    # Read all files in 'oracles-dataset'
    for filename in os.listdir('oracles-dataset'):
        print(f"Processing file: {filename}")

        with open('oracles-dataset/' + filename, 'r') as file1:
            data1 = json.load(file1)
        with open('oracles-dataset-info/' + filename, 'r') as file2:
            data2 = json.load(file2)

        # For each object in file1
        for obj1 in data1:
            # Find the object in file2 with the same 'id'
            obj2 = next(obj2 for obj2 in data2 if obj2['id'] == obj1['id'])
            # Replace the fields
            obj1['tokensProjectClassesNonPrivateStaticNonVoidMethods'] = obj2['tokensProjectClassesNonPrivateStaticNonVoidMethods']
            obj1['tokensProjectClassesNonPrivateStaticAttributes'] = obj2['tokensProjectClassesNonPrivateStaticAttributes']
            obj1['tokensMethodVariablesNonPrivateNonStaticNonVoidMethods'] = obj2['tokensMethodVariablesNonPrivateNonStaticNonVoidMethods']
            obj1['tokensMethodVariablesNonPrivateNonStaticAttributes'] = obj2['tokensMethodVariablesNonPrivateNonStaticAttributes']
            obj1['tokensOracleVariablesNonPrivateNonStaticNonVoidMethods'] = obj2['tokensOracleVariablesNonPrivateNonStaticNonVoidMethods']
            obj1['tokensOracleVariablesNonPrivateNonStaticAttributes'] = obj2['tokensOracleVariablesNonPrivateNonStaticAttributes']

        # Write the modified file
        with open('oracles-dataset/' + filename, 'w') as file1:
            json.dump(data1, file1, indent=4)

if __name__ == '__main__':
    adapt_oracles()
