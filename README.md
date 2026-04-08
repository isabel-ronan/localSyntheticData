# Synthetic Local Document Generation


## Project overview
**Fictitious Data Creation:** We use LangChain to generate synthetic data for use in the extension of [Measuring the Measuring Tools](https://doi.org/10.18653/v1/2022.gem-1.35) we implement using Biber dimensions and zero-shot prompting. 

## Additional Information
- Python version (3.14.3) and Pip version (26.0.1). 

- All necessary packages can be installed using the `./requirements.txt` file. 
- The pip package list was created using `pip list --format=freeze > requirements.txt` command.
- Packages can be installed using the `sed 's/[<>=!].*//' requirements.txt | pip install -r /dev/stdin` command.
- Additionally run the `python -m spacy download en_core_web_sm` command in your Python environment to install additional Spacy dependencies.

