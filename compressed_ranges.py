from sklearn.cluster import AgglomerativeClustering
import numpy as np

size = input()
size = int(size)

data = input().split()
nums = [int(x) for x in data]
nums = np.array(nums)

groups = []

nums = nums.reshape(-1, 1)

model = AgglomerativeClustering(distance_threshold=1.5, n_clusters=None, linkage='single')
# dist_threshold can be any number between 1 and 2
# n_clusters = None cause we dont know in advance
# linkage='single' means the distance between a cluster and the neighbors is the min distance between the elements (not the centroid)

model.fit(nums)

labels = model.labels_.flatten().tolist()

nums = nums.flatten().tolist()

i = 0

labels_dict = {l:labels.count(l) for l in set(labels)}

for _ in range(size):
    current_element = nums[i]
    current_label = labels[i]
    how_many_in_group = labels_dict[current_label]
    
    if how_many_in_group == 1:
        groups.append(str(current_element))
        i+=1
    else:
        i+=how_many_in_group
        last_element = nums[i-1]
        groups.append(f"{current_element}->{last_element}")
    if i >= size:
            break
    
output =" ".join(groups)
    
print(output)