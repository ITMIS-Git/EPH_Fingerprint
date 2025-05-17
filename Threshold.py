##########################################################
# Import dependencies
import csv,sys
import pandas as pd
from utils import ensure_dir_exists
##########################################################
def tableforRobustness(hamming_distances, threshold):
    count = 0
    for hamming_distance in hamming_distances:
        if hamming_distance <= threshold:
            count += 1
    return count/len(hamming_distances)

def tableforDiscrimination(hamming_distances, threshold):
    count = 0
    for hamming_distance in hamming_distances:
        if hamming_distance >= threshold:
            count += 1
    return count/len(hamming_distances)
##########################################################
if __name__ == "__main__":
    RobustnessDict = {}
    Dict = {}
    thresholdList = [3,6,9,12,15,18,21,24,27,30,33,36]
    HammingDistance_with_Robustness_filepath = sys.argv[1]
    HammingDistance_with_Discrimination_filepath = sys.argv[2]
    Robustness_threshold = sys.argv[3]
    Discrimination_threshold = sys.argv[4]
    RobustnessHeader = ['Threshold', 'Frequency of Fingerprints']
    DiscriminationHeader = ['Threshold', 'Frequency of Fingerprints']
    with open(HammingDistance_with_Robustness_filepath, 'r') as f1, open(HammingDistance_with_Discrimination_filepath, 'r') as f2:
        Robustness_readerDf = pd.read_csv(f1)
        Discrimination_readerDf = pd.read_csv(f2)
    HammingDistanceListforRobustness = []
    HammingDistanceListforDiscrimination = []
    for threshold in thresholdList:
        for i in range(len(Robustness_readerDf)): 
            HammingDistanceListforRobustness.append(Robustness_readerDf.loc[i,"Hamming Distance"])
        num_of_fingerprints_for_robustness = tableforRobustness(HammingDistanceListforRobustness,  threshold)
        RobustnessDict[threshold] = round(num_of_fingerprints_for_robustness,4)
        for j in range(len(Discrimination_readerDf)): 
            HammingDistanceListforDiscrimination.append(Discrimination_readerDf.loc[j,"Hamming Distance"])
        num_of_fingerprints_for_discrimination = tableforDiscrimination(HammingDistanceListforDiscrimination,  threshold)
        Dict[threshold] = round(num_of_fingerprints_for_discrimination,4)
    ensure_dir_exists(Robustness_threshold)
    with open(Robustness_threshold, 'w') as f3:
        w1 = csv.writer(f3)
        w1.writerow(RobustnessHeader)
        w1.writerows(RobustnessDict.items())
    ensure_dir_exists(Discrimination_threshold)
    with open(Discrimination_threshold, 'w') as f4:
        w2 = csv.writer(f4)
        w2.writerow(DiscriminationHeader)
        w2.writerows(Dict.items())
##########################################################