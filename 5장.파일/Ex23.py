import json
import glob
def print_scores(dirname):
    scores = {}
    for filename in glob.glob(f'{dirname}/*.json'):
        scores[filename] = {}

        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)
    #
    for one_class in scores:
        print(one_class)
        for subject, subject_score in scores[one_class].items():
            min_score = min(subject_score)
            max_score = max(subject_score)
            avg_score = sum(subject_score)/len(subject_score)

            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {avg_score}')


#
# with open('.\etc\scores\9a.json') as f:
#     for result in json.load(f):
#         for key, value in result.items():
#             print(key, value)

print(print_scores('.\etc\scores'))