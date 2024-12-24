# Next Word Prediction API

## Overview
A FastAPI-based service for predicting the next word using an N-gram model.

## How to Run

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 2: Run Training file
```bash
python model/train.py
```
### Step 3: Run The API
```bash
uvicorn app.main:app --reload
```
