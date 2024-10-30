def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date_str = input("Date: ").strip()

            if "/" in date_str:
                month, day, year = date_str.split("/")
                if month.isdigit() and day.isdigit() and year.isdigit():
                    month_num = int(month)
                    day_num = int(day)
                    if 1 <= month_num <= 12 and 1 <= day_num <= 31:
                        print(f"{int(year)}-{month_num:02d}-{day_num:02d}")
                        break
                    else:
                        continue

            elif "," in date_str:
                month_name, day, year = date_str.replace(",", "").split()
                if month_name in months and day.isdigit() and year.isdigit():
                    month_num = months.index(month_name) + 1
                    day_num = int(day)
                    if 1 <= month_num <= 12 and 1 <= day_num <= 31:
                        print(f"{int(year)}-{month_num:02d}-{day_num:02d}")
                        break
                    else:
                        continue

        except EOFError:
            break

if __name__ == "__main__":
    main()
