from bs4 import BeautifulSoup
from selenium import webdriver
import time

blank_sudoku = [[0 for i in range(9)] for j in range(9)] # 0 represents empty cell

# URL for sudoku website
URL = "https://www.sudokuweb.org/"


def get_sudoku():
    '''
    Get a sudoku from the website in URL and return it as a 2D list
    '''
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    sudoku = [[0 for i in range(9)] for j in range(9)]

    sudoku_div = soup.find(id="sudoku") # get div that sudoku is inside

    try:
        soduku_table = sudoku_div.find("tbody")
        cells = soduku_table.find_all("span")
        element = 0
        for cell in cells:
            if cell.has_attr("class"):
                if(cell["class"][0] == "sedy"): # sedy is their name for numbers given at start
                    sudoku[element//9][element%9] = int(cell.text)
                    element += 1
                elif(cell["class"][0] == "true"): # True is for hidden numbers
                    element += 1

    except:
        print("Error getting sudoku")
    
    return sudoku

