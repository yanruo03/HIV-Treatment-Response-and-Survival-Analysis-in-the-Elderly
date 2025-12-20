# HIV-Treatment-Response-and-Survival-Analysis-in-the-Elderly
In recent years, the number of elderly HIV patients has been gradually increasing. Although ART (arterial therapy) is widely used, elderly HIV patients still face significant survival challenges due to comorbidities.
The research questions are divided into the following three research questions:
Q1: What is the relationship between ART duration and treatment effectiveness?
Q2: Which clinical characteristics are associated with patient survival time?
Q3: Which characteristics are most important for predicting viral suppression?

## Project Structure
- `S1_Ageing_Study_Dataset.csv` – Raw unprocessed HIV patient dataset from Figshare
- `Cleaned_S1_Ageing_Study_Dataset.csv` – Preprocessed data after Data_prep_and_Q2_code.py
- `Q1_code.py` – Analysis code for Research Question Q1
- `Q3_code.py` – Analysis code for Research Question Q3
- `Data_prep_and_Q2_code.py` – Data preprocessing + Q2 analysis code
- `LICENSE` – MIT License file
- `README.md` – Project overview, dependencies, contributors and core info

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
