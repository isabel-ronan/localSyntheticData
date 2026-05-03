# Dataset Specific Prompt Preparation 

- This synthetic data generation process is an adaptation of ["A LangChain-based pipeline for one-shot synthetic text generation using generative pre-trained transformers in palliative care research."](https://doi.org/10.1016/j.jbi.2025.104936)
- In the aforementioned paper, prompt engineering, as part of LLM orchestration, is very important. In order to run the same pipeline with multiple datasets, different prompts are extracted from the datasets we are aiming to create synthetic data for. 
- Each dataset is loaded, randomly shuffled, and a sample of (the same) 500 notes is passed into the topic models (reduce computational load and also smallest dataset is just over 500 samples). 

## MATAVE
- Automatically detects optimal number of topics (using a given range) and returns soft-topic assignments. 
- The most representative topic is taken as a "hard" topic assignment for each document. 
- The top topics are then counted ('strong' topics) and weak topics are removed. 
- Top words for each topic are then used to make topic_keywords part of prompts. 
- For each 'strong' topic in the data modelled, one random example is taken as the one-shot input example_note. 
- Coherence, diversity, redundancy, and model timing metrics are stored along with the dataset name, the domain (taken from dataset descriptions), an example note from each topic (example_notes), and the top words of each of the 'strong' MATAVE topics (topic_keywords).


## LDA
- Run LDA for given range of possible topic numbers (same as given range to MATAVE).
- Coherence, redundancy, diversity are computed for each topic number and combined and averaged to get the best score. 
- LDA is rerun with chosen k (number of topics resulting from best score). 
- Top words for each topic are then used to make topic_keywords part of prompts.
- Each document is assigned to a topic and a random sample from each topic is used as the one-shot input example_note.
- Coherence, diversity, redundancy, and model timing metrics are stored along with the dataset name, the domain (taken from dataset descriptions), an example note from each topic (example_notes), and the top words of each of the LDA topics (topic_keywords).