import requests
from bs4 import BeautifulSoup
import json
def job_address(job_url):
    try:
        response = requests.get(f"https://www.careerlink.vn{job_url}")
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, "html.parser")
        location_span = soup.find('span', class_="mr-1")
        if location_span:
            # Sử dụng find_next_sibling để lấy thẻ <a> kế tiếp
            location_a = location_span.find_next_sibling('a')
            
            # Kiểm tra xem location_a có tồn tại không và lấy nội dung của cả thẻ <span> và <a>
            if location_a:
                location = f"{location_span.text.strip()}, {location_a.text.strip()}"
                location = location.replace(",,", ",")
                return location
        else:
             location = "Nhật Bản"
             return location
         
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        
def jobInfo(job_url: str, tag: str, class_name: str)->[]:
    try:
        response = requests.get(f"https://www.careerlink.vn{job_url}")
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        info_span = soup.find_all(tag, class_= class_name)
        return info_span
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        


def scrape_careerlink_vn(page_number):
    url = f"https://www.careerlink.vn/vieclam/list?category_ids=130%2C19&page={page_number}"
    job_data = []  # Danh sách để lưu thông tin công việc

    try:
        # Gửi yêu cầu GET đến trang web
        response = requests.get(url)
        response.raise_for_status()  # Nếu có lỗi, sẽ ném ra một exception

        # Parse HTML của trang web bằng BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Lấy tiêu đề công việc và thông tin chi tiết (đây chỉ là ví dụ, bạn cần điều chỉnh theo cấu trúc trang web)
        job_titles = soup.find_all('a', class_="job-link clickable-outside")
        for title in job_titles:
            job_info = {"Tiêu đề công việc": title.text.strip()}

            # Trích xuất đường link từ thuộc tính href
            job_link = title['href']

            # Truy cập vào link chi tiết công việc để lấy thông tin địa điểm
            job_info["Địa điểm công việc"] = job_address(job_link)
            #if(job_info["Địa điểm công việc"]  == null):
             
            # Lấy thông tin mức lương
            tmp_data= jobInfo(job_link,'div',"d-flex align-items-center mb-2")
            luong = tmp_data[0]
            luong = BeautifulSoup(str(luong), "html.parser").span.get_text(strip=True)
            job_info["Mức lương"] = luong
            
            # Lấy thông tin kinh nghiệm
            job_info["Kinh nghiệm"] =  BeautifulSoup(str(tmp_data[1]), "html.parser").span.get_text(strip=True)
            print( job_info["Kinh nghiệm"])
            job_data.append(job_info)

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")

    return job_data

# Lấy dữ liệu từ 3 trang đầu tiên và lưu vào file JSON
all_job_data = []
for i in range(1, 4):
    page_job_data = scrape_careerlink_vn(i)
    all_job_data.extend(page_job_data)

# Lưu vào file JSON
with open('job_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_job_data, json_file, ensure_ascii=False, indent=2)
