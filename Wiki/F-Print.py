import requests
from bs4 import BeautifulSoup


def print_secret_message(doc_url):
    response = requests.get(doc_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")

    points = []
    max_x = 0
    max_y = 0

    rows = table.find_all("tr")
    for row in rows[1:]:
        cells = row.find_all("td")
        if len(cells) < 3:
            continue
        x = int(cells[0].get_text(strip=True))
        char = cells[1].get_text(strip=True)
        y = int(cells[2].get_text(strip=True))

        points.append((x, y, char))
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in points:
        grid[y][x] = char

    # y = 0 is the bottom row, so print from max_y down to 0
    for y in range(max_y, -1, -1):
        print(''.join(grid[y]))


if __name__ == '__main__':
    url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
    print_secret_message(url)