---
title: Email Assistant OpenEnv
emoji: 📧
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---
# Smart Email Assistant OpenEnv

## Overview
This project simulates a real-world email assistant environment where an AI agent performs tasks like classification, prioritization, and reply generation.

## Tasks

### 1. Classification (Easy)
Classify email as spam, important, or normal.

### 2. Prioritization (Medium)
Rank multiple emails based on importance.

### 3. Reply Generation (Hard)
Generate appropriate replies to emails.

## Actions
- spam
- important
- normal
- ranking (list of indices)
- reply (text)

## Observations
- Email text
- List of emails (for prioritization)

## Reward System
- Correct classification: +1
- Partial correctness: +0.5
- Wrong: -0.2
- Dangerous mistakes: -1

## How to Run
```bash
python baseline.py
python grader.py
