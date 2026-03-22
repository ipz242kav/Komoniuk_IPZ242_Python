from datetime import datetime
import re

# ЗАВДАННЯ 1
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def get_primes_list(n):
    return [num for num in range(n + 1) if is_prime(num)]

def find_primes(n, output_format):
    primes = get_primes_list(n)

    if output_format == 'list':
        return primes
    elif output_format == 'column':
        return '\n'.join(map(str, primes))
    elif output_format == 'count':
        return len(primes)
    return None

# ЗАВДАННЯ 2

def flatten_structure(data):
    result = []
    if isinstance(data, dict):
        result.append(data)
    elif isinstance(data, list):
        for item in data:
            result.extend(flatten_structure(item))
    return result

def analyze_nested_categories(data):
    flat_data = flatten_structure(data)
    categories = []
    category_sums = {}

    for item in flat_data:
        if isinstance(item, dict):
            for category, amount in item.items():
                if category not in categories:
                    categories.append(category)
                category_sums[category] = category_sums.get(category, 0) + amount

    return (categories, category_sums)

# ЗАВДАННЯ 3

def is_valid_email(email):
    if not isinstance(email, str) or not email:
        return False
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def analyze_clients(clients):
    status_count = {}
    invalid_emails = []
    new_clients = []
    errors = []

    for client in clients:
        if not isinstance(client, tuple) or len(client) != 3:
            errors.append(client)
            continue

        name, status, email = client

        if not isinstance(name, str) or not isinstance(status, str) or not isinstance(email, str):
            errors.append(client)
            continue

        if not name or not status or not email:
            errors.append(client)
            continue

        status_count[status] = status_count.get(status, 0) + 1

        if not is_valid_email(email) and email not in invalid_emails:
            invalid_emails.append(email)

        if status == "новий" and name not in new_clients:
            new_clients.append(name)

    return {
        "status_count": status_count,
        "invalid_emails": invalid_emails,
        "new_clients": new_clients,
        "errors": errors
    }

# ЗАВДАННЯ 4

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except:
        return False

def analyze_expenses(expenses):
    category_totals = {}
    max_expense = None
    invalid_dates = []
    errors = []

    for expense in expenses:
        if not isinstance(expense, tuple) or len(expense) != 3:
            errors.append(expense)
            continue

        amount, category, date = expense

        if not isinstance(amount, (int, float)) or amount is None:
            errors.append(expense)
            continue

        if not isinstance(category, str) or category is None:
            errors.append(expense)
            continue

        if not isinstance(date, str) or date is None:
            errors.append(expense)
            continue

        if not is_valid_date(date):
            if date not in invalid_dates:
                invalid_dates.append(date)
            continue

        category_totals[category] = category_totals.get(category, 0) + amount

        if max_expense is None or amount > max_expense[0]:
            max_expense = expense

    return {
        "category_totals": category_totals,
        "max_expense": max_expense,
        "invalid_dates": invalid_dates,
        "errors": errors
    }

# ЗАВДАННЯ 5

def filter_reports(reports, output_format, keyword):
    filtered_reports = []
    errors = []

    for report in reports:
        if not isinstance(report, tuple) or len(report) != 3:
            errors.append(report)
            continue

        title, author, fmt = report

        if not isinstance(title, str) or not isinstance(author, str) or not isinstance(fmt, str):
            errors.append(report)
            continue

        if not title or not author or not fmt:
            errors.append(report)
            continue

        if fmt == output_format and (keyword in title or keyword in author):
            filtered_reports.append(report)

    return (filtered_reports, len(filtered_reports), errors)

if __name__ == "__main__":
    print("ЗАВДАННЯ 1")
    print(find_primes(20, 'list'))
    print(find_primes(20, 'count'))

    print("\nЗАВДАННЯ 2")
    nested_data = [
        [{"офіс": 100}, {"маркетинг": 200}],
        [[{"офіс": 50}, {"маркетинг": 150}], {"офіс": 200}],
        {"офіс": 300},
        [{"офіс": 100, "extra": 1}]
    ]
    print(analyze_nested_categories(nested_data))

    print("\nЗАВДАННЯ 3")
    clients = [("Іван", "новий", "ivan@email.com"), ("Олена", "постійний", "olena@email.com")]
    result = analyze_clients(clients)
    print(result["status_count"])
    print(result["new_clients"])

    print("\nЗАВДАННЯ 4")
    expenses = [(100, "офіс", "2025-06-01"), (200, "маркетинг", "2025-06-02")]
    result = analyze_expenses(expenses)
    print(result["category_totals"])
    print(result["max_expense"])

    print("\nЗАВДАННЯ 5")
    reports = [("Звіт1", "Іван Іванов", "pdf"), ("Звіт2", "Олена Петрівна", "docx")]
    # result = filter_reports(reports, "pdf", "Іва")
    # print(result[0])
    # print(result[1])
    result = filter_reports(
    [
        ("Звіт1", "Іван Іванов", "pdf"),
        ("Звіт2", "Олена Петрівна", "pdf"),
        ("", "Іван Іванов", "pdf"),             # некоректна назва
        ("Звіт3", "", "pdf"),                   # некоректний автор
        ("Звіт4", "Петро Сидоров", ""),         # некоректний формат
        "не кортеж",                            # невірний формат даних
        123,                                    # невірний формат даних
        None,                                   # невірний формат даних
        ("Звіт5",),                             # невірний формат всередині кортежу
        ("Звіт6", "Іван Іванов"),               # невірний формат всередині кортежу
        ("Звіт7", "Іван Іванов", 123),          # невірний тип для формату
    ],
    "pdf",
    "ів"
    )
    print(result)