# Student Performance Analysis
Statistical analysis of how study habits relate to
academic performance — with real correlation numbers,
not just assumptions.

## The Problem
Everyone says "study more and sleep well" but nobody
shows the actual numbers behind it.
This project does.

## What I Built
Analysis of 6 variables across a structured student dataset:
- Study hours
- Sleep hours
- Attendance percentage
- Social media hours
- Previous GPA
- Current score

## Key Results
| Variable | Pearson r | P-Value | Significant? |
|---|---|---|---|
| Study Hours vs Score | 0.85 | 0.001 | ✅ Yes |
| Attendance vs Score | Positive | < 0.05 | ✅ Yes |
| Social Media vs Score | Negative | < 0.05 | ✅ Yes |

![Correlation Output](Study-hours-vs-Current-Score.ss.pngg)


**Attendance turned out to be a stronger predictor
than raw study hours — that finding surprised me.**

## Tech Stack
Python · Pandas · Scipy · Matplotlib · Numpy

## How to Run
pip install -r requirements.txt
python student_performance_analysis.py

## Honest Limitation
Dataset is structured and clean —
real student data would be messier and
correlations would likely be weaker.
Next version: test on a public Kaggle dataset.
