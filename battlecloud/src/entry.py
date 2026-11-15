from workers import wsgi

import server
from battle_handler import BattleSnakeHandlers

game_handler = BattleSnakeHandlers(1, "a", "#008800", "chicken", "swoop")
Default = wsgi.entrypoint(server.start_server(game_handler))

def main():
    pass

if __name__ == "__main__":
    main()