# Stress Detection Using EEG and ECG

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
This project implements a data-driven approach to differentiate stress from physiological baseline using the [multi-modal PASS database](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2020.542934/full). The dataset includes mobile, simultaneous recordings of EEG and ECG data under various stress elicitation and physical activity conditions. The method utilizes Limited Penetrable Visibility Graphs (LPVG) to extract frequency-based and shape-based features from adjacency matrix images of the signals. These features are then fed into different machine-learning models. The approach has been rigorously evaluated with real data, demonstrating its feasibility and effectiveness in stress detection.

## Dataset
Please find more detailed information on the multi-modal PASS database at the following link: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2020.542934/full

## Installation
Instructions on how to set up the project locally.

```bash
git clone https://github.com/rocamario/Stress-detection-EEG-ECG.git
cd Stress-detection-EEG-ECG
pip install -r requirements.txt
```

## Model
Details about the machine learning model(s) used, including architecture, training process, and evaluation metrics.

## Results
Present the results of the project, including any visualizations, performance metrics, and analysis.

## Contributing
Guidelines for contributing to the project. Include information on how to report issues, submit pull requests, and any coding standards.

## License
Specify the license under which the project is distributed.

## Contact
Main authors: 
- Maria Sara Nour Sadoun : maria-sara-nour.sadoun@inria.fr
- Juan Manuel Vargas : jm.manuelvg@gmail.com
Contributor:
- Mario Roca : mario.roca21@gmail.com
Under the supervision of:
- Taous-Meriem Laleg-Kirati : taous-meriem.laleg@inria.fr
