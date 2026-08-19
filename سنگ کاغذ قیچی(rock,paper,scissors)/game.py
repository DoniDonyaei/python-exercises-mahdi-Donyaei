import random

OPTIONS = ["سنگ", "کاغذ", "قیچی"]

user_wins = 0
computer_wins = 0

while True:
    user_choice = input(
        "\nانتخاب کنید (سنگ، کاغذ، قیچی یا خروج): "
    ).strip()

    if user_choice == "خروج":
        break

    if user_choice not in OPTIONS:
        print("لطفاً یکی از گزینه‌های صحیح را انتخاب کنید.")
        continue

    computer_choice = random.choice(OPTIONS)
    print(f"انتخاب کامپیوتر: {computer_choice}")

    if user_choice == computer_choice:
        print("مساوی شدید! 😐")

    elif (
        (user_choice == "سنگ" and computer_choice == "قیچی")
        or (user_choice == "کاغذ" and computer_choice == "سنگ")
        or (user_choice == "قیچی" and computer_choice == "کاغذ")
    ):
        print("شما برنده شدید! 🎉")
        user_wins += 1

    else:
        print("شما باختید. 😔")
        computer_wins += 1

print("\n--- نتیجه نهایی ---")
print(f"شما {user_wins} بار برنده شدید.")
print(f"کامپیوتر {computer_wins} بار برنده شد.")
print("خدا نگهدار 👋")