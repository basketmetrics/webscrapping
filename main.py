from ws.bs import Soup

def main():
    soup = Soup("https://www.espn.com/wnba/boxscore/_/gameId/401736233")
    soup = soup.soup
    print("Hola, ¿Cómo estamos?")

main()