# VANGUARD AB TEST

## Links

- Presentation : 
- Kanban : <https://trello.com/b/6V2tF5uU/vanguard-ab>

## Project Overview
This project focuses on analyzing A/B test results from Vanguard's client interactions. The analysis aims to understand client behavior and preferences through various steps of their digital journey. Key metrics include client demographics, visit duration, process step analysis, and success rates between control and test groups.

## Table of Contents
- [Project Overview](#project-overview)
- [Metadata Help](#metadata-help)
- [Setup Instructions](#setup-instructions)
- [Data Mining](#data-mining)
- [Data Cleaning](#data-cleaning)
- [Data Separation](#data-separation)
- [Data Export and Caching](#data-export-and-caching)
- [Data Exploration](#data-exploration)
- [Path Analysis](#path-analysis)
  - [Happy Path](#happy-path)
  - [Confused Path](#confused-path)
  - [Dropped Path](#dropped-path)
- [Statistical Analysis](#statistical-analysis)
- [Conclusions](#conclusions)

## Metadata Help
This comprehensive set of fields will guide your analysis, helping you unravel the intricacies of client behavior and preferences:

- **client_id**: Unique ID for each client.
- **variation**: Indicates if a client was part of the experiment.
- **visitor_id**: Unique ID for each client-device combination.
- **visit_id**: Unique ID for each web visit/session.
- **process_step**: Marks each step in the digital process.
- **date_time**: Timestamp of each web activity.
- **clnt_tenure_yr**: Client's tenure with Vanguard in years.
- **clnt_tenure_mnth**: Client's tenure with Vanguard in months.
- **clnt_age**: Age of the client.
- **gendr**: Gender of the client.
- **num_accts**: Number of accounts the client holds.
- **bal**: Total balance across all accounts.
- **calls_6_mnth**: Number of client calls in the last six months.
- **logons_6_mnth**: Client's login frequency over the last six months.
