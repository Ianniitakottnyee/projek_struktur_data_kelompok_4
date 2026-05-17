game_time = {
    "hari": 1,
    "jam": 95,       # Mulai dari jam 6 pagi agar bisa melihat transisi ke jam 7
    "menit": 30,
    "detik": 0,
    "berjalan": True
}

def reset():
    global game_time
    if game_time["jam"] % 24 >= 22:
        game_time["jam"] = game_time["jam"] + (31 - (game_time["jam"] % 24))
        game_time["menit"] = 0
    elif game_time["jam"] % 24 <= 7:
        game_time["jam"] = game_time["jam"] + (7 - (game_time["jam"] % 24))
        game_time["menit"] = 0


reset()