import json
import csv

def save_movies(data, filename="movies.json"):
    """
    Lưu dữ liệu vào file JSON.
    
    :param data: Dữ liệu cần lưu (kiểu dictionary hoặc list).
    :param filename: Tên file JSON (mặc định là 'movies.json').
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Dữ liệu đã được lưu vào file {filename}")

def save_to_csv(data, filename="movies.csv"):
    """
    Lưu dữ liệu vào file CSV.
    
    :param data: Dữ liệu cần lưu (kiểu list của dictionaries).
    :param filename: Tên file CSV (mặc định là 'movies.csv').
    """
    if not data:
        print("Không có dữ liệu để lưu.")
        return

    # Lấy tên các cột từ keys của dictionary đầu tiên
    fieldnames = data[0].keys()

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Ghi tiêu đề cột
        writer.writerows(data)  # Ghi dữ liệu
    print(f"Dữ liệu đã được lưu vào file {filename}")

def save_espisodes(data, filename="episode.json"):
    """
    Lưu dữ liệu vào file JSON.
    
    :param data: Dữ liệu cần lưu (kiểu dictionary hoặc list).
    :param filename: Tên file JSON (mặc định là 'episode.json').
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Dữ liệu đã được lưu vào file {filename}")