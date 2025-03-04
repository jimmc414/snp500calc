# S&P 500 Monthly Investment Growth Calculator

A simple Python tool that demonstrates the long-term impact of consistent monthly investments in the S&P 500 index.

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

## S&P 500 Historical Data

# S&P 500 Historical Returns (1928-2024)

| Year | Return (%) | Year | Return (%) | Year | Return (%) | Year | Return (%) |
|------|------------|------|------------|------|------------|------|------------|
| 1928 | 43.61% | 1953 | -0.99% | 1978 | 6.56% | 2003 | 28.68% |
| 1929 | -8.42% | 1954 | 52.62% | 1979 | 18.44% | 2004 | 10.88% |
| 1930 | -24.90% | 1955 | 31.56% | 1980 | 32.42% | 2005 | 4.91% |
| 1931 | -43.34% | 1956 | 6.56% | 1981 | -4.91% | 2006 | 15.79% |
| 1932 | -8.19% | 1957 | -10.78% | 1982 | 21.55% | 2007 | 5.49% |
| 1933 | 53.99% | 1958 | 43.36% | 1983 | 22.56% | 2008 | -37.00% |
| 1934 | -1.44% | 1959 | 11.96% | 1984 | 6.27% | 2009 | 26.46% |
| 1935 | 47.67% | 1960 | 0.47% | 1985 | 31.73% | 2010 | 15.06% |
| 1936 | 33.92% | 1961 | 26.89% | 1986 | 18.67% | 2011 | 2.11% |
| 1937 | -35.03% | 1962 | -8.73% | 1987 | 5.25% | 2012 | 16.00% |
| 1938 | 31.12% | 1963 | 22.80% | 1988 | 16.61% | 2013 | 32.39% |
| 1939 | -0.41% | 1964 | 16.48% | 1989 | 31.69% | 2014 | 13.69% |
| 1940 | -9.78% | 1965 | 12.45% | 1990 | -3.10% | 2015 | 1.38% |
| 1941 | -11.59% | 1966 | -10.06% | 1991 | 30.47% | 2016 | 11.96% |
| 1942 | 20.34% | 1967 | 23.98% | 1992 | 7.62% | 2017 | 21.83% |
| 1943 | 25.90% | 1968 | 11.06% | 1993 | 10.08% | 2018 | -4.38% |
| 1944 | 19.75% | 1969 | -8.50% | 1994 | 1.32% | 2019 | 31.49% |
| 1945 | 36.44% | 1970 | 4.01% | 1995 | 37.58% | 2020 | 18.40% |
| 1946 | -8.07% | 1971 | 14.31% | 1996 | 22.96% | 2021 | 28.71% |
| 1947 | 5.71% | 1972 | 18.98% | 1997 | 33.36% | 2022 | -18.11% |
| 1948 | 5.50% | 1973 | -14.66% | 1998 | 28.58% | 2023 | 26.29% |
| 1949 | 18.79% | 1974 | -26.47% | 1999 | 21.04% | 2024 | 25.02% |
| 1950 | 31.71% | 1975 | 37.20% | 2000 | -9.10% |  |  |
| 1951 | 24.02% | 1976 | 23.84% | 2001 | -11.89% |  |  |
| 1952 | 18.37% | 1977 | -7.18% | 2002 | -22.10% |  |  |

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

![image](https://github.com/user-attachments/assets/8fd514c0-2d62-4dc1-a00d-26fe2ebc8456)


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
