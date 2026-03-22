import csv
import os
import re
import matplotlib.pyplot as plt


class KmrCsv:
    ref = 'marks2.lab11.csv'
    num = 1

    def __init__(self, ref=None, num=None):
        if ref is not None:
            self.ref = ref
        if num is not None:
            self.num = num
        self.data = []

    def set_ref(self, ref):
        self.ref = ref

    def get_ref(self):
        return self.ref

    def set_num(self, num):
        self.num = num

    def read_csv(self):
        self.data = []
        file_path = self.ref
        if not os.path.exists(file_path):
            file_path = os.path.join(os.path.dirname(__file__), '..', 'marks2.lab11.csv')
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    self.data.append(row)

    def file_info(self):
        print(f"Номер КМР: {self.num}, Кількість студентів: {len(self.data)}")


class Statistic:
    def parse_float(self, val):
        try:
            return float(val.replace(',', '.'))
        except:
            return 0.0

    def parse_time(self, time_str):
        minutes = 0
        seconds = 0
        m_match = re.search(r'(\d+)\s*хв', time_str)
        s_match = re.search(r'(\d+)\s*сек', time_str)
        if m_match:
            minutes = int(m_match.group(1))
        if s_match:
            seconds = int(s_match.group(1))
        total_minutes = minutes + seconds / 60.0
        return total_minutes if total_minutes > 0 else 1.0

    def avg_stat(self):
        if not self.data:
            return ()
        num_questions = len(self.data[0]) - 5
        if num_questions <= 0:
            return ()
        sums = [0.0] * num_questions
        counts = len(self.data)
        for row in self.data:
            for i in range(num_questions):
                val = self.parse_float(row[i + 5])
                sums[i] += val
        return tuple((s / counts) * 100 / 0.5 for s in sums)

    def marks_stat(self):
        stats = {}
        for row in self.data:
            grade = self.parse_float(row[4])
            if grade in stats:
                stats[grade] += 1
            else:
                stats[grade] = 1
        return stats

    def marks_per_time(self):
        res = {}
        for row in self.data:
            uid = row[0]
            grade = self.parse_float(row[4])
            time_spent = self.parse_time(row[3])
            res[uid] = grade / time_spent
        return res

    def best_marks_per_time(self, bottom_margin, top_margin):
        filtered = []
        mpt = self.marks_per_time()
        for row in self.data:
            uid = row[0]
            grade = self.parse_float(row[4])
            if bottom_margin <= grade <= top_margin:
                if uid in mpt:
                    filtered.append((uid, grade, mpt[uid]))
        filtered.sort(key=lambda x: x[2], reverse=True)
        return tuple(filtered[:5])


class Plots:
    cat = "results"

    def set_cat(self, cat):
        self.cat = cat
        if not os.path.exists(cat):
            os.makedirs(cat)

    def avg_plot(self, percentages):
        plt.figure()
        plt.bar(range(len(percentages)), percentages)
        plt.title("Відсотки правильних відповідей на кожне питання")
        plt.xlabel("Номер питання")
        plt.ylabel("Відсоток")
        plt.savefig(f"{self.cat}/avg_plot.png")
        plt.close()

    def marks_plot(self, marks_counts):
        plt.figure()
        plt.bar([str(k) for k in marks_counts.keys()], marks_counts.values())
        plt.title("Розподіл оцінок")
        plt.xlabel("Оцінка")
        plt.ylabel("Кількість студентів")
        plt.savefig(f"{self.cat}/marks_plot.png")
        plt.close()

    def best_marks_plot(self, best_data):
        uids = [x[0][:8] for x in best_data]
        mpts = [x[2] for x in best_data]
        plt.figure()
        plt.bar(uids, mpts)
        plt.title("Топ-5 найкращих балів за хвилину")
        plt.xlabel("ID студента")
        plt.ylabel("Бал/хвилина")
        plt.savefig(f"{self.cat}/best_marks_plot.png")
        plt.close()


class KmrWork(KmrCsv, Statistic, Plots):
    kmrs = {}
    cat = "results"

    def __init__(self, ref, num):
        KmrCsv.__init__(self, ref, num)
        KmrWork.kmrs[num] = ref
        self.set_cat(KmrWork.cat)

    @staticmethod
    def compare_csv(kmr1, kmr2):
        avg1 = sum([kmr1.parse_float(r[4]) for r in kmr1.data]) / len(kmr1.data) if kmr1.data else 0
        avg2 = sum([kmr2.parse_float(r[4]) for r in kmr2.data]) / len(kmr2.data) if kmr2.data else 0
        
        time1 = sum([kmr1.parse_time(r[3]) for r in kmr1.data]) / len(kmr1.data) if kmr1.data else 0
        time2 = sum([kmr2.parse_time(r[3]) for r in kmr2.data]) / len(kmr2.data) if kmr2.data else 0
        
        res = f"Порівняння КМР {kmr1.num} та КМР {kmr2.num}\n"
        res += f"Кількість виконаних: {len(kmr1.data)} та {len(kmr2.data)}\n"
        res += f"Середній бал: {avg1:.2f} та {avg2:.2f}\n"
        res += f"Середній час (хв): {time1:.2f} та {time2:.2f}\n"
        
        print(res)
        with open("comparison.txt", "w", encoding="utf-8") as f:
            f.write(res)

    @staticmethod
    def compare_avg_plots(kmr1, kmr2):
        data1 = kmr1.avg_stat()
        data2 = kmr2.avg_stat()
        plt.figure()
        plt.plot(data1, label=f"КМР {kmr1.num}")
        plt.plot(data2, label=f"КМР {kmr2.num}")
        plt.legend()
        plt.title("Порівняння відсотків правильних відповідей")
        plt.xlabel("Номер питання")
        plt.ylabel("Відсоток")
        plt.savefig("comparison_avg.png")
        plt.close()


if __name__ == '__main__':
    print("--- Тести Завдання 4 ---")
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'marks2.lab11.csv')
    
    kmr1 = KmrWork(csv_path, 1)
    kmr1.read_csv()
    kmr1.file_info()
    
    kmr2 = KmrWork(csv_path, 2)
    kmr2.read_csv()
    
    print("Генерація статистики avg_plot() для kmr2...")
    avg_st = kmr2.avg_stat()
    kmr2.avg_plot(avg_st)
    
    print("Генерація статистики marks_plot() для kmr2...")
    mk_st = kmr2.marks_stat()
    kmr2.marks_plot(mk_st)
    
    print("Порівняння КМР...")
    KmrWork.compare_csv(kmr1, kmr2)
    KmrWork.compare_avg_plots(kmr1, kmr2)
    
    print("Завдання 4 виконано.")
