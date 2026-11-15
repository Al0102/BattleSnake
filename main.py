import server
from handlers import BattleSnakeHandlers

def main():
    game_handler = BattleSnakeHandlers(1, "alex", "#0888AF", "chicken", "swoop")
    server.start_server(game_handler)


if __name__ == "__main__":
    main()