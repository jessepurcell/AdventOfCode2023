"""
Advent of Code 2023
Day 2
"""
test_strings = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]


def main():
    games = []
    sum_of_ids = 0
    # for s in test_strings:
    #     games.append(parse_game(s))
    with open('input.txt') as file_in:
        for line in file_in.readlines():
            games.append(parse_game(line))

    for game in games:
        if is_valid_game(game[1]):
            sum_of_ids += game[0]
    print(sum_of_ids)

    sum_of_ids = 0
    for game in games:
        power = calculate_power(merge_games(game[1]))
        sum_of_ids += power
    print(sum_of_ids)


def calculate_power(game):
    print(game)
    power = 1
    for value in game.values():
        power *= value
    return power


def merge_games(games):
    new_dict = dict()
    keys = ['red', 'green', 'blue']
    for key in keys:
        for game in games:
            # print(game)
            game = dict(game)
            if game.get(key):
                if new_dict.get(key) is None:
                    new_dict[key] = game.get(key)
                elif game.get(key) > new_dict.get(key):
                    new_dict[key] = game.get(key)

    return new_dict


def is_valid_game(games, red=12, green=13, blue=14):
    for g in games:
        g = dict(g)
        if g.get('red') and g.get('red') > red:
            return False
        if g.get('green') and g.get('green') > green:
            return False
        if g.get('blue') and g.get('blue') > blue:
            return False
    return True


def parse_game(line):
    game_id, game_results = line.split(':')
    game_id = int(game_id.split()[1])
    games = []
    for game_attempt in game_results.split('; '):
        color_to_number = {game.split()[1]: int(game.split()[0]) for game in game_attempt.strip().split(', ')}
        games.append(color_to_number)

    # print(f"Game ID: {game_id}")
    # print(f"Games: {games}")
    return game_id, games


if __name__ == '__main__':
    main()
