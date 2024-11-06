#
#
# def admin():
#
#     while True:
#         print("\nМеню администратора:")
#         print("0. Добавить пользователя")
#         print("1. Просмотреть всех пользователей")
#         print("2. Изменить данные пользователя")
#         print("3. Выход")
#
#
#         choice = input("Выберите действие: ")
#         if choice == 0:
#
#
#
#         if choice == "1":
#             print("\nСписок всех пользователей:")
#             for idx, user in enumerate(giperuser, 1):
#                 print(f"{idx}. {user}")
#
#         elif choice == "2":
#             user_passport_id = input("Введите паспортный ID пользователя для изменения данных: ")
#             found_user = next((user for user in giperuser if user.passportid == user_passport_id), None)
#
#             if not found_user:
#                 print("Пользователь с таким паспортным ID не найден.")
#                 continue
#
#             print(f"Выбранный пользователь: {found_user}")
#             print("\nДоступные данные для изменения:")
#             print("1. Имя")
#             print("2. Фамилия")
#             print("3. Возраст")
#             print("4. Баланс")
#             print("5. Номер телефона")
#
#             field_choice = input("Введите номер поля для изменения: ")
#
#             try:
#                 if field_choice == "1":
#                     found_user.name = input("Введите новое имя: ")
#                 elif field_choice == "2":
#                     found_user.surname = input("Введите новую фамилию: ")
#                 elif field_choice == "3":
#                     found_user.age = int(input("Введите новый возраст: "))
#                 elif field_choice == "4":
#                     if isinstance(found_user.balance, list):
#                         print("Доступные балансы:")
#                         for idx, bal in enumerate(found_user.balance, 1):
#                             print(f"{idx}. {bal}")
#                         balance_idx = int(input("Введите номер баланса для изменения: ")) - 1
#                         found_user.balance[balance_idx] = int(input("Введите новый баланс: "))
#                     else:
#                         found_user.balance = int(input("Введите новый баланс: "))
#                 elif field_choice == "5":
#                     found_user.phonenumber = input("Введите новый номер телефона: ")
#                 else:
#                     print("Неверный выбор.")
#                 print("Данные успешно изменены.")
#             except (ValueError, IndexError):
#                 print("Ошибка при изменении данных.")
#
#         elif choice == "3":
#             print("Выход из режима администратора.")
#             return enter()
#
#
#         else:
#             print("Некорректный выбор. Попробуйте снова.")
#
