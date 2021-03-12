# Visualize the boxplot of a rule's measure over a log.
# input: MegaMatrixMonster
import matplotlib.pyplot as plt
import json

file = open("offline-test-00-output.json")
mega_matrix = json.load(file)
# print(mega_matrix)

mapping = [];

for trace in mega_matrix:
    if len(mapping) == 0:
        for i in range(len(mega_matrix[trace])):
            mapping += [[]]
    for i in range(len(mega_matrix[trace])):
        mapping[i] += [mega_matrix[trace][i]['Confidence']]


# for i in mapping:
for i in mapping[0:50]:
    plt.boxplot(i)
    plt.ylim(-0.1, 1.1)
    plt.show()

# plt.boxplot(0)
# plt.show()
