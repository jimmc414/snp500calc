import math
import random
from rich.table import Table
from rich.console import Console

def run_snp_investment_calc():
    """
    This program is built to illustrate that consistent monthly contributions
    can grow dramatically through the magic of compounding—provided you stay
    invested and let time do its work.

    **“Time in the market beats timing the market.”**
    """

    # ------------------------------------------------------------------------------------
    # 1. Inspirational Quotes
    # ------------------------------------------------------------------------------------
    quotes = [
        "“The first rule of compounding: Never interrupt it unnecessarily.”  —Munger",
        "“The stock market is a device for transferring money from the impatient to the patient.”  —Buffett",
        "“The big money is not in the buying and the selling … but in the waiting.”  —Munger"
    ]

    # Randomly select one quote to display:
    selected_quote = random.choice(quotes)

    # ------------------------------------------------------------------------------------
    # 2. Print Intro / Quote
    # ------------------------------------------------------------------------------------
    console = Console()
    console.print("[bold cyan]Welcome to the S&P 500 Monthly Investment Growth Calculator[/bold cyan]")
    console.print(
        "This program is built to illustrate that consistent monthly contributions "
        "can grow dramatically through the magic of compounding—provided you stay "
        "invested and let time do its work.\n\n"
        "[bold italic yellow]“Time in the market beats timing the market.”[/bold italic yellow]\n"
    )
    console.print(f"[magenta]{selected_quote}[/magenta]\n")

    # ------------------------------------------------------------------------------------
    # 3. Historical Returns Dictionary
    # ------------------------------------------------------------------------------------
    historical_returns = {
        1928: 0.4361,
        1929: -0.0842,
        1930: -0.2490,
        1931: -0.4334,
        1932: -0.0819,
        1933: 0.5399,
        1934: -0.0144,
        1935: 0.4767,
        1936: 0.3392,
        1937: -0.3503,
        1938: 0.3112,
        1939: -0.0041,
        1940: -0.0978,
        1941: -0.1159,
        1942: 0.2034,
        1943: 0.2590,
        1944: 0.1975,
        1945: 0.3644,
        1946: -0.0807,
        1947: 0.0571,
        1948: 0.0550,
        1949: 0.1879,
        1950: 0.3171,
        1951: 0.2402,
        1952: 0.1837,
        1953: -0.0099,
        1954: 0.5262,
        1955: 0.3156,
        1956: 0.0656,
        1957: -0.1078,
        1958: 0.4336,
        1959: 0.1196,
        1960: 0.0047,
        1961: 0.2689,
        1962: -0.0873,
        1963: 0.2280,
        1964: 0.1648,
        1965: 0.1245,
        1966: -0.1006,
        1967: 0.2398,
        1968: 0.1106,
        1969: -0.0850,
        1970: 0.0401,
        1971: 0.1431,
        1972: 0.1898,
        1973: -0.1466,
        1974: -0.2647,
        1975: 0.3720,
        1976: 0.2384,
        1977: -0.0718,
        1978: 0.0656,
        1979: 0.1844,
        1980: 0.3242,
        1981: -0.0491,
        1982: 0.2155,
        1983: 0.2256,
        1984: 0.0627,
        1985: 0.3173,
        1986: 0.1867,
        1987: 0.0525,
        1988: 0.1661,
        1989: 0.3169,
        1990: -0.0310,
        1991: 0.3047,
        1992: 0.0762,
        1993: 0.1008,
        1994: 0.0132,
        1995: 0.3758,
        1996: 0.2296,
        1997: 0.3336,
        1998: 0.2858,
        1999: 0.2104,
        2000: -0.0910,
        2001: -0.1189,
        2002: -0.2210,
        2003: 0.2868,
        2004: 0.1088,
        2005: 0.0491,
        2006: 0.1579,
        2007: 0.0549,
        2008: -0.3700,
        2009: 0.2646,
        2010: 0.1506,
        2011: 0.0211,
        2012: 0.1600,
        2013: 0.3239,
        2014: 0.1369,
        2015: 0.0138,
        2016: 0.1196,
        2017: 0.2183,
        2018: -0.0438,
        2019: 0.3149,
        2020: 0.1840,
        2021: 0.2871,
        2022: -0.1811,
        2023: 0.2629,
        2024: 0.2502
    }

    # ------------------------------------------------------------------------------------
    # 4. Collect user input
    # ------------------------------------------------------------------------------------
    try:
        monthly_saving = float(input("Enter your monthly savings amount: "))
        start_month = int(input("Enter the start month (1-12): "))
        start_year = int(input("Enter the start year (1928-2024): "))
    except ValueError:
        console.print("[red]Invalid input. Please enter numeric values.[/red]")
        return

    # ------------------------------------------------------------------------------------
    # 5. Validate user inputs
    # ------------------------------------------------------------------------------------
    if monthly_saving <= 0:
        console.print("[red]Monthly saving must be > 0.[/red]")
        return
    if not (1 <= start_month <= 12):
        console.print("[red]Start month must be between 1 and 12.[/red]")
        return
    if start_year < 1928 or start_year > 2024:
        console.print("[red]Start year must be between 1928 and 2024.[/red]")
        return

    # ------------------------------------------------------------------------------------
    # 6. Set up for the calculation
    # ------------------------------------------------------------------------------------
    balance = 0.0

    # Create a Rich table for the output
    table = Table(title="S&P 500 Investment Growth")
    table.add_column("Year", justify="right", style="bold")
    table.add_column("Months Contributed", justify="right")
    table.add_column("Annual Return", justify="right")
    table.add_column("Year-End Balance", justify="right")

    # ------------------------------------------------------------------------------------
    # 7. Monthly compounding from start_year to 2024
    # ------------------------------------------------------------------------------------
    for year in range(start_year, 2025):
        annual_return = historical_returns[year]
        monthly_rate = (1 + annual_return) ** (1 / 12) - 1

        # Determine how many months to process in this year
        if year == start_year:
            months_in_year = 12 - start_month + 1
        else:
            months_in_year = 12

        # Accumulate and compound each month
        for _ in range(months_in_year):
            balance += monthly_saving
            balance *= (1 + monthly_rate)

        # Format returns/balance in green if >= 0 else red
        if annual_return >= 0:
            return_str = f"[green]{annual_return * 100:.2f}%[/green]"
        else:
            return_str = f"[red]{annual_return * 100:.2f}%[/red]"

        if balance >= 0:
            balance_str = f"[green]${balance:,.2f}[/green]"
        else:
            balance_str = f"[red]${balance:,.2f}[/red]"

        # Add a row to the table
        table.add_row(
            str(year),
            str(months_in_year),
            return_str,
            balance_str
        )

    # ------------------------------------------------------------------------------------
    # 8. Print the table and final total
    # ------------------------------------------------------------------------------------
    console.print(table)

    if balance >= 0:
        final_str = f"[green]${balance:,.2f}[/green]"
    else:
        final_str = f"[red]${balance:,.2f}[/red]"

    console.print(
        f"[bold]Final total as of 12/31/2024: {final_str}[/bold]"
    )


if __name__ == "__main__":
    run_snp_investment_calc()
