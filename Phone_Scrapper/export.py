import csv

def save_to_file(phones):
  file = open("phones.csv",mode="w")
  writer = csv.writer(file)
  writer.writerow(["기종", "디스플레이 크기","AP","램", "용량", "후면 카메라", "전면 카메라", "배터리", "충전 속도", "무게", "두께"]) 
  for phone in phones:
    if(phone == None):
        continue
    else:
        writer.writerow(phone.values())
  return