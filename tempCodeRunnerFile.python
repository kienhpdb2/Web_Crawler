import re
import requests
from bs4 import BeautifulSoup
import json


def scrape_careerlink_vn(page_number):
    url = f"https://www.topcv.vn/viec-lam-it?page={page_number}"
    job_data = []  # Danh sách để lưu thông tin công việc

    try:
        # Gửi yêu cầu GET đến trang web
        response = requests.get(url)
        response.raise_for_status()  # Nếu có lỗi, sẽ ném ra một exception

        # Parse HTML của trang web bằng BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Lấy tiêu đề công việc và thông tin chi tiết (đây chỉ là ví dụ, bạn cần điều chỉnh theo cấu trúc trang web)
        job_titles = soup.find_all('h3', class_="title")
        for title in job_titles:
            title.find_next_sibling('a')
            print(title.get('href'))
            print(type(title))
    
            job_info = {"Name": title.text.strip()}
            print(job_info["Name"])
            # Trích xuất đường link từ thuộc tính href
            
            print(job_link)
            # Mô tả job
            tmp_data = jobInfo(job_link,'div',"rich-text-content")
            mo_ta = BeautifulSoup(str(tmp_data[0]), "html.parser")
            mo_ta = mo_ta.get_text(strip=True)
            job_info["Mô tả công việc"] = mo_ta
            
            # Lấy thông tin mức lương
            tmp_data= jobInfo(job_link,'div',"d-flex align-items-center mb-2")
            luong = tmp_data[0]
            luong = BeautifulSoup(str(luong), "html.parser").span.get_text(strip=True)
            job_info["Mức lương"] = luong
            
            # Lấy thông tin kinh nghiệm
            job_info["Kinh nghiệm"] =  BeautifulSoup(str(tmp_data[1]), "html.parser").span.get_text(strip=True)
            # print( job_info["Kinh nghiệm"])
            #Kỹ năng
            tmp_data = jobInfo(job_link,'div',"raw-content rich-text-content")
            job_info["Kỹ năng"] = BeautifulSoup(str(tmp_data), "html.parser").get_text(strip=True)  
            job_info["Kỹ năng"] = job_info["Kỹ năng"].replace("[","").replace("]","")
            if(job_info["Kỹ năng"] == ""):
                        job_info["Kỹ năng"] = None
              
            #Phúc lợi
            tmp_data = jobInfo(job_link,'div',"job-benefit-item d-flex align-items-start mb-2" )
            job_info["Quyền lợi"] = BeautifulSoup(str(tmp_data), "html.parser").get_text(strip=True)  
            if (job_info["Quyền lợi"] == "[]"):
                response = requests.get(f"https://www.careerlink.vn{job_link}")
                response.raise_for_status()
                soup = BeautifulSoup(response.content, "html.parser")
                benefits_paragraph = soup.find('p', string='Quyền lợi được hưởng')
                if benefits_paragraph:
                    for item in benefits_paragraph.find_next_siblings('p'):
                        text = item.get_text(strip=True)
                        if text:
                            tmp_data.append(text)
                    job_info["Quyền lợi"] = BeautifulSoup(str(tmp_data), "html.parser").get_text(strip=True)  
                else :
                 benefits_paragraph = soup.find('p', string='Mức lương và phúc lợi')
                 if benefits_paragraph:
                    for item in benefits_paragraph.find_next_siblings('p'):
                        text = item.get_text(strip=True)
                        if text:
                            tmp_data.append(text)
                    job_info["Quyền lợi"] = BeautifulSoup(str(tmp_data), "html.parser").get_text(strip=True)
                 else:
                  benefits_paragraph = soup.find('p', string='Quyền lợi')
                  if benefits_paragraph:
                    for item in benefits_paragraph.find_next_siblings('p'):
                        text = item.get_text(strip=True)
                        if text:
                            tmp_data.append(text)
                    job_info["Quyền lợi"] = BeautifulSoup(str(tmp_data), "html.parser").get_text(strip=True)
                  else:
                    benefits_paragraph = soup.find('p', string='Phúc lợi')
                    if benefits_paragraph:
                        for item in benefits_paragraph.find_next_siblings('p'):
                            text = item.get_text(strip=True)
                            if text:
                                tmp_data.append(text)
                        job_info["Quyền lợi"] = BeautifulSoup(str(tmp_data), "html.parser").get_text(strip=True)
                    else:
                        benefits_paragraph = soup.find('p', string='QUYỀN LỢI')
                        if benefits_paragraph:
                            for item in benefits_paragraph.find_next_siblings('p'):
                                text = item.get_text(strip=True)
                                if text:
                                    tmp_data.append(text)
                            job_info["Quyền lợi"] = BeautifulSoup(str(tmp_data), "html.parser").get_text(strip=True)
                        else:
                         benefits_paragraph = soup.find('p', string='Allowance')
                         if benefits_paragraph:
                            for item in benefits_paragraph.find_next_siblings('p'):
                                text = item.get_text(strip=True)
                                if text:
                                    tmp_data.append(text)
                            job_info["Quyền lợi"] = BeautifulSoup(str(tmp_data), "html.parser").get_text(strip=True)
                         else:   
                          benefits_paragraph = soup.find('p', string='ALLOWANCE')
                          if benefits_paragraph:
                            for item in benefits_paragraph.find_next_siblings('p'):
                                text = item.get_text(strip=True)
                                if text:
                                    tmp_data.append(text)
                            job_info["Quyền lợi"] = BeautifulSoup(str(tmp_data), "html.parser").get_text(strip=True)
                          else:
                            benefits_paragraph = soup.find('p', string='PHÚC Lợi')
                            if benefits_paragraph:
                                for item in benefits_paragraph.find_next_siblings('p'):
                                    text = item.get_text(strip=True)
                                    if text:
                                        tmp_data.append(text)
                                job_info["Quyền lợi"] = BeautifulSoup(str(tmp_data), "html.parser").get_text(strip=True)                    
                            else:
                                keywords = ['quyền lợi', 'phúc lợi', 'nghỉ mát', 'du lịch', 'nghỉ dưỡng', 'tham quan', 'phụ cấp', 'thưởng', 'hưởng', 'tăng lương',
                                            'hằng năm','hằng tháng', 'hằng quý', 'hàng năm', 'hàng tháng', 'hàng quý', 'team building', 'teambuilding', 'trợ cấp',
                                            'Allowance','Bonus','event', 'Salary review','trip','travel','insurance','party','parties','tri ân','cảm ơn','lương tháng 13',
                                            'tháng lương 13','sinh nhật','hiểu hỉ','hiếu hỷ','13th salary','giải trí','nghỉ phép','thai sản','bảo hiểm','chăm sóc','review lương',
                                            'vacation','holiday','sick']
                                pattern = re.compile('|'.join(keywords), re.IGNORECASE)
                                matching_paragraphs = soup.find_all('p', text=pattern)
                                for paragraph in matching_paragraphs:
                                    tmp_data.append(paragraph.text)
                                job_info["Quyền lợi"] = BeautifulSoup(str(tmp_data), "html.parser").get_text(strip=True)  
                            
            job_info["Quyền lợi"] = job_info["Quyền lợi"].replace("[","").replace("]","")
            if(job_info["Quyền lợi"] == ""):
                        job_info["Quyền lợi"] = None
            print(job_info["Quyền lợi"])
            
            #Độ tuổi:
            
            tmp_data = jobInfo(job_link,'div',"job-summary-item d-block" )          
           
            try:
                 job_info["Độ tuổi"] = BeautifulSoup(str(tmp_data[5]), "html.parser").get_text(strip=True)  
                 if "Ngành nghề" in job_info["Độ tuổi"]:
                    job_info["Độ tuổi"] = BeautifulSoup(str(tmp_data[4]), "html.parser").get_text(strip=True)
                 if "Giới tính" in job_info["Độ tuổi"]:
                      job_info["Độ tuổi"] = "Tuổi"
            except IndexError:
                 job_info["Độ tuổi"] = "Tuổi"       
            job_info["Độ tuổi"] = job_info["Độ tuổi"].replace("Tuổi", "")
            if(job_info["Độ tuổi"] == ""):
                        job_info["Độ tuổi"] = None
            print( job_info["Độ tuổi"])   
            #Nơi làm việc
            job_info["Nơi làm việc"] = job_address(job_link)
            #Giới tính
            job_info["Giới tính"] = BeautifulSoup(str(tmp_data[3]), "html.parser").get_text(strip=True)  
            if "Học vấn" in job_info["Giới tính"]:
                    job_info["Giới tính"] = BeautifulSoup(str(tmp_data[4]), "html.parser").get_text(strip=True)     
            job_info["Giới tính"] = job_info["Giới tính"].replace("Giới tính", "")
            if(job_info["Giới tính"] == ""):
                        job_info["Giới tính"] = None
            #print( job_info["Giới tính"])   
            #Học vấn
            job_info["Học vấn"] = BeautifulSoup(str(tmp_data[2]), "html.parser").get_text(strip=True)  
            if "Cấp bậc" in job_info["Học vấn"]:
                    job_info["Học vấn"] = BeautifulSoup(str(tmp_data[3]), "html.parser").get_text(strip=True)     
            job_info["Học vấn"] = job_info["Học vấn"].replace("Học vấn", "")
            if(job_info["Học vấn"] == ""):
                        job_info["Học vấn"] = None
            #Loại công việc
            job_info["Loại công việc"] = BeautifulSoup(str(tmp_data[0]), "html.parser").get_text(strip=True)  
            if "Mã việc làm" in job_info["Loại công việc"]:
                    job_info["Loại công việc"] = BeautifulSoup(str(tmp_data[1]), "html.parser").get_text(strip=True)     
            job_info["Loại công việc"] = job_info["Loại công việc"].replace("Loại công việc", "")
            if(job_info["Loại công việc"] == ""):
                        job_info["Loại công việc"] = None
            #Cấp bậc
            job_info["Cấp bậc"] = BeautifulSoup(str(tmp_data[1]), "html.parser").get_text(strip=True)  
            if "Loại công việc" in job_info["Cấp bậc"]:
                    job_info["Cấp bậc"] = BeautifulSoup(str(tmp_data[2]), "html.parser").get_text(strip=True)     
            job_info["Cấp bậc"] = job_info["Cấp bậc"].replace("Cấp bậc", "")
            if(job_info["Cấp bậc"] == ""):
                        job_info["Cấp bậc"] = None           
                        
            job_data.append(job_info)

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")

    return job_data

def job_address(job_url):
    try:
        response = requests.get(f"https://www.careerlink.vn{job_url}")
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, "html.parser")
        location_spans = soup.find_all('span', class_="mr-1")
        locations = []
        for location_span in location_spans:
            # Sử dụng find_next_sibling để lấy thẻ <a> kế tiếp
            location_a = location_span.find_next_sibling('a')
            
            # Kiểm tra xem location_a có tồn tại không và lấy nội dung của cả thẻ <span> và <a>
            if location_a:
                location = f"{location_span.text.strip()}, {location_a.text.strip()}"
                location = location.replace(",,", ",")
                locations.append(location)
        return locations
    
        if not loactions :
            locations = soup.find_all('i', class_="cli-map-pin-line d-flex mr-2")
            print(locations)
            for location in locations : 
                location = location.find_next_sibling('i', class_="text-reset")
                location = f"{location.text.strip()}"
                locations.append(location)
        return locations
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
        

# Lấy dữ liệu từ 3 trang đầu tiên và lưu vào file JSON
all_job_data = []
for i in range(1, 4):
    page_job_data = scrape_careerlink_vn(i)
    all_job_data.extend(page_job_data)

# Lưu vào file JSON
with open('job_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_job_data, json_file, ensure_ascii=False, indent=2)
