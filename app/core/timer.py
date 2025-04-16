import time

def countdown(minutes, label_widget):
    total_seconds = minutes * 60

    def update_timer():
        nonlocal total_seconds
        if total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            label_widget.config(text=f"{mins:02d}:{secs:02d}")
            total_seconds -= 1
            label_widget.after(1000, update_timer)
        else:
            label_widget.config(text="⏰ The timer is up!")

    update_timer()


if __name__== "__main__":
    user_input = int(input("How many minutes should the timer be set for?"))
    countdown(user_input)

