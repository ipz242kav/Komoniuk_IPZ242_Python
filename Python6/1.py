"""
ЛАБОРАТОРНА РОБОТА: ВСІ 12 ЗАВДАНЬ
Функціональне програмування + Робота з файлами
"""

from datetime import datetime
import re
import csv
import os
from collections import defaultdict, Counter

print("="*80)
print("ЛАБОРАТОРНА РОБОТА: ВСІ ЗАВДАННЯ")
print("="*80)

# ============================================================================
# ЧАСТИНА 1: ФУНКЦІОНАЛЬНЕ ПРОГРАМУВАННЯ (5 завдань)
# ============================================================================

print("\n" + "="*80)
print("ЧАСТИНА 1: ФУНКЦІОНАЛЬНЕ ПРОГРАМУВАННЯ")
print("="*80)

# ЗАВДАННЯ 1: Пошук простих чисел

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

print("\n### ЗАВДАННЯ 1: Пошук простих чисел ###\n")
result1 = find_primes(20, 'list')
print(f"Прості числа до 20: {result1}")
result2 = find_primes(20, 'count')
print(f"Кількість: {result2}")

# ЗАВДАННЯ 2: Аналіз вкладених категорій

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

print("\n### ЗАВДАННЯ 2: Аналіз вкладених категорій ###\n")
nested_data = [
    [{"офіс": 100}, {"маркетинг": 200}],
    [[{"офіс": 50}, {"маркетинг": 150}], {"офіс": 200}],
    {"офіс": 300},
    [{"офіс": 100, "extra": 1}]
]
result = analyze_nested_categories(nested_data)
print(f"Категорії: {result[0]}")
print(f"Суми: {result[1]}")

# ЗАВДАННЯ 3: Аналіз клієнтів

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

print("\n### ЗАВДАННЯ 3: Аналіз клієнтів ###\n")
clients = [
    ("Іван", "новий", "ivan@email.com"),
    ("Олена", "постійний", "olena@email.com"),
]
result = analyze_clients(clients)
print(f"Статистика по статусах: {result['status_count']}")
print(f"Нові клієнти: {result['new_clients']}")

# ЗАВДАННЯ 4: Аналіз витрат

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

print("\n### ЗАВДАННЯ 4: Аналіз витрат ###\n")
expenses = [
    (100, "офіс", "2024-06-01"),
    (200, "маркетинг", "2024-06-02"),
]
result = analyze_expenses(expenses)
print(f"Витрати по категоріях: {result['category_totals']}")
print(f"Максимальна витрата: {result['max_expense']}")

# ЗАВДАННЯ 5: Фільтрація звітів

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

print("\n### ЗАВДАННЯ 5: Фільтрація звітів ###\n")
reports = [
    ("Звіт1", "Іван Іванов", "pdf"),
    ("Звіт2", "Олена Петрівна", "docx"),
]
result = filter_reports(reports, "pdf", "Іва")
print(f"Відфільтровані звіти: {result[0]}")
print(f"Кількість: {result[1]}")

# ============================================================================
# ЧАСТИНА 2: РОБОТА З ФАЙЛАМИ (7 завдань)
# ============================================================================

print("\n" + "="*80)
print("ЧАСТИНА 2: РОБОТА З ФАЙЛАМИ")
print("="*80)

# ЗАВДАННЯ 1: Зчитування чисел з файла

print("\n### ЗАВДАННЯ 1: Зчитування чисел з файла ###\n")

with open('numbers.txt', 'w') as f:
    for i in range(1, 11):
        f.write(f"{i * 10}\n")

numbers = []
with open('numbers.txt', 'r') as f:
    for line in f:
        numbers.append(int(line.strip()))

total_sum = sum(numbers)
print(f"Числа: {numbers}")
print(f"Сума: {total_sum}")

with open('sum_numbers.txt', 'w') as f:
    f.write(str(total_sum))

print("✓ Створено: numbers.txt, sum_numbers.txt")

# ЗАВДАННЯ 2: Аналіз парності/непарності

print("\n### ЗАВДАННЯ 2: Аналіз парності/непарності ###\n")

test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with open('even_odd.txt', 'w', encoding='utf-8') as f:
    for num in test_numbers:
        if num % 2 == 0:
            f.write(f"{num} - парне\n")
        else:
            f.write(f"{num} - непарне\n")

print("Результати:")
with open('even_odd.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(f"  {line.strip()}")

print("✓ Створено: even_odd.txt")

# ЗАВДАННЯ 3: Сортування за довжиною рядків

print("\n### ЗАВДАННЯ 3: Сортування за довжиною рядків ###\n")

python_uses = [
    "Python можна використати для веб-розробки",
    "Python можна використати для аналізу даних",
    "Python можна використати для машинного навчання",
    "Python можна використати для автоматизації задач",
    "Python можна використати для написання скриптів"
]

with open('learning_python.txt', 'w', encoding='utf-8') as f:
    for line in python_uses:
        f.write(line + "\n")

lines = []
with open('learning_python.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

sorted_lines = sorted(lines, key=len, reverse=True)
print("Відсортовані рядки (спадаючо):")
for line in sorted_lines:
    print(f"  [{len(line):3}] {line.strip()}")

print("✓ Створено: learning_python.txt")

# ЗАВДАННЯ 4: Заміна та фільтрація текста

print("\n### ЗАВДАННЯ 4: Заміна та фільтрація текста ###\n")

os.makedirs('modified_reports', exist_ok=True)

true_statements = []
false_statements = []

for line in lines:
    c_line = line.replace("Python", "C")
    if "веб" in c_line or "аналіз" in c_line:
        true_statements.append(c_line)
    else:
        false_statements.append(c_line)

with open('modified_reports/true_statements.txt', 'w', encoding='utf-8') as f:
    f.writelines(true_statements)

with open('modified_reports/false_statements.txt', 'w', encoding='utf-8') as f:
    f.writelines(false_statements)

print(f"Істинні твердження ({len(true_statements)}):")
for stmt in true_statements:
    print(f"  ✓ {stmt.strip()}")

print("✓ Створено: modified_reports/")

# ЗАВДАННЯ 5: Гостева книга

print("\n### ЗАВДАННЯ 5: Гостева книга ###\n")

guest_book_path = 'guest_book.txt'
creation_time = datetime.now()
guests = ["Іван", "Марія", "Петро"]

with open(guest_book_path, 'w', encoding='utf-8') as f:
    f.write(f"=== ГОСТЕВА КНИГА ===\n")
    f.write(f"Час створення: {creation_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("="*50 + "\n\n")
    
    for guest in guests:
        entry_time = datetime.now()
        greeting = f"Вітаємо, {guest}! Дякуємо за відвідування.\n"
        f.write(f"[{entry_time.strftime('%Y-%m-%d %H:%M:%S')}] {greeting}")

print("Гостева книга:")
with open(guest_book_path, 'r', encoding='utf-8') as f:
    content = f.read()
print(content)

print("✓ Створено: guest_book.txt")

# ЗАВДАННЯ 6: Аналіз частоти букв та слів

print("\n### ЗАВДАННЯ 6: Аналіз частоти букв та слів ###\n")

python_text = """Python is a high-level, interpreted programming language known for its simplicity and readability. 
Created by Guido van Rossum and first released in 1991, Python has become one of the most popular 
programming languages in the world. Its design philosophy emphasizes code readability, allowing 
programmers to express concepts in fewer lines of code than would be possible in languages such as 
C++ or Java. Python's syntax is intuitive and allows developers to write clear and logical code."""

with open('python_text.txt', 'w', encoding='utf-8') as f:
    f.write(python_text)

letter_freq = Counter()
for char in python_text.lower():
    if char.isalpha():
        letter_freq[char] += 1

words = re.findall(r'\b[a-z]+\b', python_text.lower())
word_freq = Counter(words)

start_time = datetime.now()
total_letters = sum(letter_freq.values())
total_words = len(words)

print(f"Загальна кількість букв: {total_letters}")
print(f"Загальна кількість слів: {total_words}\n")

print(f"ТОП 10 букв:")
for letter, count in letter_freq.most_common(10):
    print(f"  '{letter}': {count} ({count/total_letters*100:.2f}%)")

print(f"\nТОП 10 слів:")
for word, count in word_freq.most_common(10):
    print(f"  '{word}': {count}")

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()

with open('analysis_report.txt', 'w', encoding='utf-8') as f:
    f.write(f"Звіт аналізу\n")
    f.write(f"Час створення: {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"Час завершення: {end_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"Час виконання: {execution_time:.4f} сек\n")
    f.write("="*60 + "\n\n")
    f.write(f"ТОП 15 букв:\n")
    for i, (letter, count) in enumerate(letter_freq.most_common(15), 1):
        f.write(f"  {i:2}. '{letter}': {count:4} ({count/total_letters*100:5.2f}%)\n")

print(f"\n✓ Створено: python_text.txt, analysis_report.txt")
print(f"  Час виконання: {execution_time:.4f} сек")

# ЗАВДАННЯ 7: Аналіз marks.csv

print("\n### ЗАВДАННЯ 7: Аналіз marks.csv ###\n")

students = []
try:
    with open('marks.lab6.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 4:
                try:
                    score = float(row[4].replace(',', '.'))
                    answers = [float(x.replace(',', '.')) for x in row[5:] if x and x != '-']
                    
                    students.append({
                        'id': row[0],
                        'start': row[1],
                        'end': row[2],
                        'duration': row[3],
                        'score': score,
                        'answers': answers
                    })
                except:
                    continue
    
    if students:
        total_students = len(students)
        print(f"1. Кількість студентів: {total_students}\n")
        
        score_distribution = defaultdict(int)
        for student in students:
            score = int(student['score'])
            score_distribution[score] += 1
        
        print(f"2. Розподіл оцінок:")
        for score in sorted(score_distribution.keys()):
            count = score_distribution[score]
            print(f"   Оцінка {score}: {count} студентів ({count/total_students*100:.1f}%)")
        
        def parse_duration(duration_str):
            parts = duration_str.split()
            minutes = int(parts[0])
            if len(parts) > 1 and 'сек' in parts[1]:
                seconds = int(parts[1].replace('сек', ''))
                total_minutes = minutes + seconds/60
            else:
                total_minutes = minutes
            return total_minutes
        
        scores_time_ratio = []
        for student in students:
            total_minutes = parse_duration(student['duration'])
            ratio = student['score'] / total_minutes if total_minutes > 0 else 0
            scores_time_ratio.append({
                'score': student['score'],
                'time': total_minutes,
                'ratio': ratio
            })
        
        scores_time_ratio.sort(key=lambda x: x['ratio'], reverse=True)
        top_5 = scores_time_ratio[:5]
        
        print(f"\n3. ТОП 5 найкращих (оцінка/час):")
        for idx, item in enumerate(top_5, 1):
            print(f"   {idx}. Оцінка: {item['score']:.2f}, Час: {item['time']:.2f} хв, Коефіцієнт: {item['ratio']:.4f}")
        
        with open('exam_statistics.txt', 'w', encoding='utf-8') as f:
            f.write(f"ЗВІТ СТАТИСТИКИ КМР\n")
            f.write(f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*70 + "\n\n")
            f.write(f"Кількість студентів: {total_students}\n\n")
            f.write(f"Розподіл оцінок:\n")
            for score in sorted(score_distribution.keys()):
                count = score_distribution[score]
                f.write(f"  Оцінка {score}: {count} студентів\n")
            f.write(f"\nТОП 5 найкращих:\n")
            for idx, item in enumerate(top_5, 1):
                f.write(f"  {idx}. Оцінка: {item['score']:.2f}, Час: {item['time']:.2f} хв\n")
        
        print(f"\n✓ Створено: exam_statistics.txt")
    else:
        print("⚠ Файл marks.csv не знайдено")
        
except Exception as e:
    print(f"⚠ Помилка: {e}")

print("\n" + "="*80)
print("ВСІ ЗАВДАННЯ ВИКОНАНО!")
print("="*80)
print("\nСписок створених файлів:")
print("  1. numbers.txt, sum_numbers.txt")
print("  2. even_odd.txt")
print("  3. learning_python.txt")
print("  4. modified_reports/ (папка)")
print("  5. guest_book.txt")
print("  6. python_text.txt, analysis_report.txt")
print("  7. exam_statistics.txt")
print("="*80)
