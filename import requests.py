import requests
from bs4 import BeautifulSoup

def scrape_careerlink_vn(page_number):
    url = f"https://www.careerlink.vn/vieclam/list?category_ids=130%2C19&page={page_number}"

    try:
        # Gửi yêu cầu GET đến trang web
        response = requests.get(url)
        response.raise_for_status()  # Nếu có lỗi, sẽ ném ra một exception

        # Parse HTML của trang web bằng BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Lấy tiêu đề công việc (đây chỉ là ví dụ, bạn cần điều chỉnh theo cấu trúc trang web)
        job_titles = soup.find_all('a', class_="job-link clickable-outside")
        for title in job_titles:
            print("Tiêu đề công việc:", title.text.strip())

            # Trích xuất đường link từ thuộc tính href
            job_link = title['href']
            
            # Truy cập vào link chi tiết công việc để lấy thông tin địa điểm
            scrape_job_details(job_link)

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")

def scrape_job_details(job_url):
    try:
        # Gửi yêu cầu GET đến trang web chi tiết công việc
        response = requests.get(f"https://www.careerlink.vn{job_url}")
        response.raise_for_status()  # Nếu có lỗi, sẽ ném ra một exception

        # Parse HTML của trang web chi tiết công việc bằng BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Lấy thông tin địa điểm công việc (đây chỉ là ví dụ, bạn cần điều chỉnh theo cấu trúc trang web)
        location_span = soup.find('span', class_="mr-1")
        if location_span:
            # Sử dụng find_next_sibling để lấy thẻ <a> kế tiếp
            location_a = location_span.find_next_sibling('a')
            # Kiểm tra xem location_a có tồn tại không và lấy nội dung của cả thẻ <span> và <a>
            if location_a:
                location = f"{location_span.text.strip()}, {location_a}"
                location.replace(",,",",")
                print("Địa điểm công việc:", location)

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")

# Ví dụ: Lấy dữ liệu từ 3 trang đầu tiên
for i in range(1, 2):
    scrape_careerlink_vn(i)
