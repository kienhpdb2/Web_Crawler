import argparse
import json
import requests
from bs4 import BeautifulSoup, NavigableString, Tag


def setup_file(filename, is_append):
    if is_append:
        mod = "a+"
        bra = ']'
    else:
        mod = "w"
        bra = '['
    with open(filename, mod) as f:
        f.writelines(bra)


def write_file(filename, data, deli):
    with open(filename, "a+") as f:
        f.writelines(deli)
        json.dump(data, f, indent=2, ensure_ascii=False)


def add_contents(contents, data):
    for header in contents.find_all('h3'):
        nextNode = header
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, NavigableString):
                # print (nextNode.strip())
                pass
            if isinstance(nextNode, Tag):
                if nextNode.name == "h3":
                    break
                # print (nextNode.get_text(strip=True).strip())
                data[header.text] = nextNode.get_text(strip=True).strip()


def get_list_link(start, end):
    links = []
    for i in range(start, end + 1):
        links.append(
            f"https://www.careerlink.vn/vieclam/list?category_ids=130%2C19&page={i}")
    return links


def get_titles(list_link):
    titles = []
    for link in list_link:
        response = requests.get(link)
        print(response.content)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find_all('a', class_="job-link clickable-outside")
        for tit in title:
            titles.append(tit)

    return titles



def get_links_company(titles):
    links_company = []
    for link_company in titles:
        link = link_company['href']
        links_company.append(link)
    return links_company


def crawl_contents(filename, links_company):

    setup_file(filename, False)
    deli = ""

    for link in links_company:
        news = requests.get(f"https://www.careerlink.vn{link}")
        soup = BeautifulSoup(news.content, "html.parser")
        names_obj = soup.find('h1', class_="job-title mb-0")
        if names_obj == None:
            continue
        names = names_obj.text
        data = {}
        data['name'] = names
        job_description= soup.find(id="section-job-description")
        job_skill= soup.find(id="section-job-skills")
        job_contact= soup.find(id="section-job-contact-information")
        job_des = job_description.find("div", class_="rich-text-content")
        data['mô tả công việc']= job_des.get_text(strip= True)
        skill = job_skill.find("div", class_="rich-text-content")
        data['kinh nghiệm']= skill.get_text(strip=True)
        content = job_contact.find("ul", class_="list-unstyled contact-person rounded-lg p-3 m-0")
        li_elements = content.select("ul.list-unstyled li")
        contact_array=[]
        for li in li_elements:
            text_content = li.get_text(strip=True)
            contact_array.append(text_content)
        data['thông tin liên hệ']= contact_array
        write_file(filename, data, deli)
        deli = ",\n"
        print(data)
    setup_file(filename, True)


if __name__ == "_main_":
    # create parser
    print("Parsing Args")
    parser = argparse.ArgumentParser()
    parser.add_argument("start")
    parser.add_argument("end")
    args = parser.parse_args()

    print("Start crawling from ", args.start, " to ", args.end)
    # data = read_data(args.data_file_name)
    links = get_list_link(int(args.start), int(args.end))
    print("get list link")
    title = get_titles(links)
    print(title)
    links_company = get_links_company(title)
    print(links_company)
    filename = "recruit_" + args.start + "_" + args.end + ".json"
    crawl_contents(filename, links_company)