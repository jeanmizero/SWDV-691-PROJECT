# SWDV-691-PROJECT

## SWDV-691-INTERFACE FOR E-COMMERCE

## E-commerce MVP

This E-commerce web application I will use HTML ,CSS, JavaSript for UI and Python with Django Framework. The web application loads products a PostgreSQL database and displays them.
Users can

- Create user account
- Log In and Log Out
- View products List
- Add/ Remove items
- Review and Rating products
- Make a payment

## Tech Stack

- HTML
- CSS
- Bootstrap
- Python

## Install and startup steps

### Linux/macOS/BASH

python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt

#### Windows

python -m venv venv
.\\venv\\scripts\\activate
pip install -r requirements.txt

## Installation required for Stripe

- pip install stripe

  For Testing payment[Stripe](https://stripe.com/docs/testing)
  CARD NUMBER (VISA): 4242 4242 4242 4242.
  CVC: Any 3 digits
  DATE: Any future date
  ADDRESS: Any Address
  NAME: Any name
