def centering(window):
    window_height = 500
    window_width = 700
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    return (window_width, window_height, x_cordinate, y_cordinate)