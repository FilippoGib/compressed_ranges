from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd
import time

# testati: 
# 00
# 01
# 02
# 03
# 04
# 05
# 06
# 07

def compressed_ranges(i: int):
    start = time.perf_counter()
    
    with open(f"/home/filippo/coding_gym/compressed-ranges-testcases/input/input0{i}.txt") as f:
        size, input = f.readlines()
        
    f.close()

    size = int(size)
    
    data = input.split()
    nums = [int(x) for x in data]
    nums = np.array(nums)

    outputs = []
    
    with open(f"/home/filippo/coding_gym/compressed-ranges-testcases/output/output0{i}.txt") as f:
        expected_output = f.readlines()[0]

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
            outputs.append(str(current_element))
            i+=1
        else:
            i+=how_many_in_group
            last_element = nums[i-1]
            outputs.append(f"{current_element}->{last_element}")
        if i >= size:
            break
        
    my_output =" ".join(outputs)
    
    end = time.perf_counter()
    
    number_of_groups = len(outputs)
        
    print(size)
    # print(input)
    # print(my_output)
    # print(expected_output)
    print(expected_output == my_output)
    
    print(f"exec time = {end-start:.6f} s")
    
    return size, number_of_groups, end-start, expected_output == my_output
    
def main():
    results = []
    for i in range(9):
        size, number_of_groups, time_elapsed, success = compressed_ranges(i)
        results.append({"i":i, "size":size, "number_of_groups":number_of_groups, "time_elapsed":time_elapsed, "success": success})
        print("##############")
    df = pd.DataFrame(results, columns=["i", "size", "number_of_groups", "time_elapsed", "success"])
    print(df)
    df.to_csv("results.csv", index=False)

if __name__ == "__main__":
    main()