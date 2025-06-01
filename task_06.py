class WrongNumberOfPlayersError(Exception):
    def __init__(self, *args):
        self.num = args[0]

    def __str__(self):
        return 'there are {0} players, not 2'.format(self.num)


class NoSuchStrategyError(Exception):
    def __init__(self, *args):
        self.strat = args[0]

    def __str__(self):
        return '{0} is not a valid move'.format(self.strat)


valid_moves = 'RPS'


def rps_game_winner(players_moves):
    if len(players_moves) > 2:
        raise WrongNumberOfPlayersError(len(players_moves))
    mv_1 = players_moves[0][1]
    mv_2 = players_moves[1][1]
    if mv_1 not in valid_moves:
        raise NoSuchStrategyError(mv_1)

    elif mv_2 not in valid_moves:
        raise NoSuchStrategyError(mv_2)

    if (mv_1 == 'R' and mv_2 == 'S') or (mv_1 == 'P' and mv_2 == 'R') or (mv_1 == 'S' and mv_2 == 'P'):
        return '{0} {1}'.format(players_moves[0][0], mv_1)
    elif (mv_2 == 'R' and mv_1 == 'S') or (mv_2 == 'P' and mv_1 == 'R') or (mv_2 == 'S' and mv_1 == 'P'):
        return '{0} {1}'.format(players_moves[1][0], mv_2)
    elif mv_1 == mv_2:
        return '{0} {1}'.format(players_moves[0][0], mv_1)


# print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
# print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))
