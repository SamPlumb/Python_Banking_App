# CBbox
def d_box(text: list[str], align: int = 0):

    longest_item = max(text, key=len)

    box_width = len(longest_item) + 4  # Adding padding

    print(f"╔{'═' * box_width}╗")

    for item in text:

        # Align Left
        if align == 0:
            print(f"║ {item:<{box_width - 2}} ║")

        # Align Right
        elif align == 1:
            print(f"║ {item:>{box_width - 2}} ║")

        # Align Center
        elif align == 2:
            print(f"║ {item:^{box_width - 2}} ║")

        else:
            raise ValueError("Alignment must be 0, 1, or 2.")

    print(f"╚{'═' * box_width}╝")


if __name__ == "__main__":

    # Box Ascii -
    top_bot = "═"
    sides = "║"

    top_left = "╔"
    top_right = "╗"
    bot_left = "╚"
    bot_right = "╝"

    example_text = ["Hello World!", "This is a resizable box.", "Enjoy!"]

    d_box(example_text)
