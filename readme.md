# S&P 500 Monthly Investment Growth Calculator

A simple yet informative Python tool that demonstrates the long-term impact of consistent monthly investments in the S&P 500 index.

> **"Time in the market beats timing the market."**

## Purpose

This program is designed to illustrate the power of compounding when making regular monthly contributions to an S&P 500 index fund. By using actual historical S&P 500 returns data from 1928 to 2024, it shows what your investment would be worth today if you had started investing a fixed monthly amount at any point during this period.

The calculator emphasizes the importance of long-term investing and demonstrates how patience can lead to significant wealth accumulation through the "magic of compounding."

## Features

- Uses **real historical S&P 500 annual returns** from 1928 to 2024
- Calculates month-by-month compounding for accuracy
- Allows customized monthly contribution amounts
- Flexible start date (any month/year from 1928-2024)
- Color-coded display highlighting positive and negative returns
- Visual table showing year-by-year progress
- Inspirational investing quotes from Warren Buffett and Charlie Munger

## Requirements

- Python 3.6+
- Rich library (`pip install rich`)

## Installation

1. Clone this repository or download the script file
2. Install the required dependencies:

```bash
pip install rich
```

## Usage

Run the script and follow the prompts:

```bash
python snp500calc.py
```

You'll be asked to provide:
1. Your monthly savings amount (e.g., $500)
2. Start month (1-12)
3. Start year (1928-2024)

The program will then calculate and display a year-by-year breakdown of your investment growth.

## Example

```
Enter your monthly savings amount: 500
Enter the start month (1-12): 1
Enter the start year (1928-2024): 1990
```

This would show the growth of a $500 monthly investment starting in January 1990 through December 2024.

## Sample Output

The program generates a rich table showing:
- Year
- Months contributed that year
- Annual S&P 500 return (color-coded)
- Year-end balance (color-coded)

The final total is highlighted at the bottom, showing the cumulative value of all investments plus compounded returns.

## Notes on Calculations

- Returns are based on S&P 500 annual performance including dividends
- Monthly returns are calculated by taking the 12th root of the annual return
- The calculator assumes consistent monthly investments with no missed contributions
- All returns are reinvested (as with an index fund)
- The simulation does not account for inflation, taxes, or investment fees

## Disclaimer

Past performance is not indicative of future results. This tool is for educational purposes only and should not be considered investment advice.
