#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 of Synthesizing"""

import decimal

NAME = raw_input('What is your name? ')

AMOUNT = raw_input('What is the principal of the loan? ')
AMOUNT = int(AMOUNT)

DURATION = raw_input('For how long is this being borrowed? ')
DURATION = int(DURATION)

PRE_QUALIFIED = raw_input('Are you pre-qualified? ')

STATUS = PRE_QUALIFIED[:1].lower() == 'y'
ANSWER = 'Yes'
TOTAL = 0
INT_RATE = 0

if AMOUNT <= 199999:
    if 1 <= DURATION <= 15:
        if STATUS:
            INT_RATE = decimal.Decimal(3.63) / 100
        else:
            INT_RATE = decimal.Decimal(4.65) / 100
            ANSWER = 'No'
    elif 16 <= DURATION <= 20:
        if STATUS:
            INT_RATE = decimal.Decimal(4.04) / 100
        else:
            INT_RATE = decimal.Decimal(4.98) / 100
            ANSWER = 'No'

    elif 21 <= DURATION <= 30:
        if STATUS:
            INT_RATE = decimal.Decimal(5.77) / 100
        else:
            INT_RATE = decimal.Decimal(6.39) / 100
            ANSWER = 'No'
elif 200000 <= AMOUNT <= 999999:
    if 1 <= DURATION <= 15:
        if STATUS:
            INT_RATE = decimal.Decimal(3.02) / 100
        else:
            INT_RATE = decimal.Decimal(3.98) / 100
            ANSWER = 'No'
    elif 16 <= DURATION <= 20:
        if STATUS:
            INT_RATE = decimal.Decimal(3.27) / 100
        else:
            INT_RATE = decimal.Decimal(4.08) / 100
            ANSWER = 'No'
    elif 21 <= DURATION <= 30:
        if STATUS:
            INT_RATE = decimal.Decimal(4.66) / 100
        else:
            INT_RATE is None
            ANSWER = 'No'
else:
    if 1 <= DURATION <= 15:
        if STATUS:
            INT_RATE = decimal.Decimal(2.05) / 100
        else:
            INT_RATE = 0
            ANSWER = 'No'
    elif 16 <= DURATION <= 20:
        if STATUS:
            INT_RATE = decimal.Decimal(2.62) / 100
        else:
            INT_RATE is None
            ANSWER = 'No'
    else:
        if STATUS:
            INT_RATE is None
        else:
            INT_RATE is None
            ANSWER = 'No'
        if not STATUS:
            ANSWER = 'No'

if INT_RATE is None:
    TOTAL = None
else:
    TOTAL = int(
        round(AMOUNT * ((1 + (INT_RATE / 12))
                                  ** (12 * DURATION))))


REPORT = ('Loan Report for: {:>15}\n'
          '----------------------------------------------------\n'
          'Principal: ${:>20,.0f}\n'
          'Duration: {:>18}yrs\n'
          'Pre-qualified?: {:>14}\n'
          '\n'
          'Total: ${:>24,.0f}')

print REPORT.format(NAME, AMOUNT, DURATION, ANSWER, TOTAL)
