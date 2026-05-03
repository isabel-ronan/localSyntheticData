import pandas as pd
from collections import Counter

df = pd.read_csv('./promptDataPreparation.csv')

scores = {'coherence': [], 'diversity': [], 'redundancy': [], 'time': []}
for dataset in df['dataset'].value_counts().keys().tolist():
    temp_df = df[df['dataset'] == dataset]
    for model in ['MATAVE', 'LDA']:
        assert len(temp_df[temp_df['topic_model'] == model]['example_notes'].tolist()[0].split('*** SEPARATION ***')) == len([text for text in temp_df[temp_df['topic_model'] == model]['topic_keywords'].tolist()[0].split('Other topic keywords: ') if text != '']), "Topic keywords and example texts should be of the same length."
        print(f"{model} Topic Number {dataset} Dataset: {len(temp_df[temp_df['topic_model'] == model]['example_notes'].tolist()[0].split('*** SEPARATION ***'))}")
    for score, score_list in scores.items():
        score_list.append(df.iloc[temp_df[score].idxmax()]['topic_model'])

scores_count = {}
for score, score_list in scores.items():
    temp_counter = Counter(score_list).most_common(1)[0]
    print(f"The model with the highest number of higher {score} scores across datasets is {temp_counter[0]} scoring highest on {temp_counter[1]} out of {len(Counter(df['dataset']))} datasets.")

