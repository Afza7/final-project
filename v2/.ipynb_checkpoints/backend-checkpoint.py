#imports
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

hex_matrix_raw = 
# take input of hex matrix

# convert to 8x32 matrix form

# create difference files

hex_matrix = [
['03', 'F0', '95', 'A3', '80', '09', 'EB', '59'],
['07', '8A', '1F', '8A', 'E7', '1E', '21', '65'],
['49', 'EF', '1D', '7E', 'F1', '49', '04', 'BB'],
['B9', '65', '48', '2C', '65', 'AE', 'CE', '37'],
['62', '3D', 'BE', 'EA', '44', '81', '5B', '73'],
['02', '5F', 'E9', '0B', 'C8', '6B', '82', '49'],
['0A', '33', 'FD', 'D9', '67', '89', '54', '74'],
['B5', '5F', '3E', '2D', '1D', '4C', 'BA', '9F'],
['40', '56', '6C', '08', '4A', '38', '90', '00'],
['D0', '3A', '8C', '6D', '1B', 'AA', '31', 'DC'],
['87', 'BE', 'D0', '7D', '37', '28', '54', '6B'],
['53', '39', 'C9', 'D9', '9F', '63', '37', '43'],
['E1', '54', '11', '51', 'FE', 'EF', '23', '6B'],
['0F', '86', '6F', 'B8', 'B7', 'D7', 'BA', 'F6'],
['FE', 'E5', '34', '16', 'F9', 'A1', '06', 'C6'],
['78', 'DF', '61', 'E6', '79', 'F7', '48', '23'],
['05', '25', '5F', '01', '5F', '0B', '72', '8D'],
['77', 'A0', '52', '69', 'EE', '84', 'B0', '63'],
['5A', '7B', 'D7', 'D4', '64', '61', '3A', '80'],
['99', '5C', '04', '9E', '13', '63', 'B5', '48'],
['E0', 'D6', '15', 'B3', '6E', '25', '58', '93'],
['14', '9D', 'CA', '2D', '1B', '5D', '42', 'FF'],
['17', '45', 'FF', '5C', '2C', 'C3', '2A', '2A'],
['2F', '7B', '90', '9B', '1E', 'E7', '43', '81'],
['E6', '98', '48', '68', 'B3', 'BA', '94', 'A6'],
['32', '97', 'E0', 'A4', '25', 'D7', '46', 'D3'],
['C4', '51', '69', 'A2', '8C', '2A', '4B', '06'],
['C5', 'C0', '94', '78', '29', '30', '97', '96'],
['FB', '14', '17', 'C2', '30', '93', '29', '50'],
['41', '47', '01', 'B1', 'A6', 'A1', 'FF', 'BD'],
['01', '75', '12', '75', '21', '09', '92', '35'],
['B9', '07', 'AA', '51', 'D1', '43', 'AB', '1C']]

difference_files=[]
n = len(hex_matrix)
print("Length:", n)

difference_files.append(s)
difference_files.append("rc4")
difference_files.append(hex_string)

for i in range(0,n-1):
    xor_result = []
    difference_file_n=[]
    for i in range(len(hex_matrix) - 1):
        row_xor = [hex(int(hex_matrix[i][j], 16) ^ int(hex_matrix[i+1][j], 16))[2:].upper().zfill(2)
                   for j in range(len(hex_matrix[i]))]
        xor_result.append(row_xor)
    difference_file_n.append(xor_result)
    hex_matrix = xor_result
    difference_files.append(difference_file_n)



# create a dataset corresponding each hex character to a number


# perform clustering for each difference file

# set up a classification model
# req: data and target
X = data
y = target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
dt = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)
dt.fit(X_train, y_train)
#X_test is compatible for both csv input of ciphertext and single input(list of one element)
#X_test needs to be the row of cluster_no for the difference files of our input cipher
# use this row of cluster_no data and predict the value for a model

y_pred = dt.predict(X_test)
print("predicted output")
print(y_pred)

#y_pred is what mounika will get as an output


