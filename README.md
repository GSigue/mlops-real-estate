# MLOps Real Estate Project

## Overview
This project demonstrates production-grade MLOps practices using Azure ML and GitHub Actions.

## CI/CD Status
![CI Pipeline](https://github.com/GSigue/mlops-real-estate/actions/workflows/ci.yml/badge.svg)
![CD Pipeline](https://github.com/GSigue/mlops-real-estate/actions/workflows/cd.yml/badge.svg)

## Repository Structure
\\\
mlops-real-estate/
└── .github/
    └── workflows/
        ├── ci.yml              # Continuous Integration
        ├── cd.yml              # Continuous Deployment
        └── test-connection.yml # Test Azure connection
\\\

## Setup
1. Add Azure credentials as GitHub secret: \AZURE_CREDENTIALS\
2. Push to main branch to trigger CI/CD

## Author
GSigue
