# HIV-Treatment-Response-and-Survival-Analysis-in-the-Elderly
In recent years, the number of elderly HIV patients has been gradually increasing. Although ART (arterial therapy) is widely used, elderly HIV patients still face significant survival challenges due to comorbidities.
The research questions are divided into the following three research questions:
Q1: What is the relationship between ART duration and treatment effectiveness?
Q2: Which clinical characteristics are associated with patient survival time?
Q3: Which characteristics are most important for predicting viral suppression?

## Project structure:
├── S1 Ageing Study Dataset.csv                          # Raw data, original unprocessed HIV patient dataset from https://figshare.com/articles/dataset/S1_Ageing_Study_Dataset_csv/14525487/2
├── Cleaned_S1_Ageing_Study_Dataset_Cleaned.csv          # Cleaned data, preprocessed data after Data_prep_and_Q2_code.py
├── Q1_code.py                    # Analysis code corresponding to Research Question Q1
├── Q3_code.py                    # Analysis code corresponding to Research Question Q3
├── Data_prep_and_Q2_code.py      # Data preprocessing script + analysis code for Research Question Q2
├── LICENSE                       # MIT License file
└── README.md                     # Project overview, usage instructions, contributors, license and other core information

## Dependencies
- Python 3.10+
- Libraries:
  - pandas/numpy (data processing)
  - matplotlib/seaborn (visualization)
  - lifelines (survival analysis)
  - statsmodels (statistical modeling)
  - os (system operations)

## Contributors
| Name          | Contribution                                    |
|---------------|-------------------------------------------------|
| Nuo Cheng     | Main developer: Data preprocessing, Q2 analysis |
| Zhaoyin Peng  | Q1 code implementation                          |
| Yang Zhang    | Q3 code implementation                          |

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
