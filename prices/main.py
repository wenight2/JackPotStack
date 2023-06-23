import requests
import json
import sys

# with open('conf.json', 'r') as source:
#     json_data = json.load(source)
# urls = json_data['urls']

# with open ('product.json', 'r') as p_source:
#     product_data = p_source.read()
# all_poducts = json.loads(product_data)

#print(all_poducts)

urls_json = { 
    "urls": [ 
        "https://www.arukereso.hu/processzor-c3139/intel/core-i5-13600k-3-5ghz-14-core-box-p864861552/",
        "https://www.arukereso.hu/processzor-c3139/intel/core-i7-13700k-3-4ghz-16-core-box-p864865917/",
        "https://www.arukereso.hu/videokartya-c3142/asus/tuf-gaming-geforce-rtx-4070-12g-gddr6x-oc-tuf-rtx4070-o12g-gaming-p949211577/",
        "https://belso-ssd-meghajto.arukereso.hu/corsair/mp600-pro-lpx-1tb-m-2-pcie-nvme-cssd-f1000gbmp600plp-p763397892/",
        "https://belso-ssd-meghajto.arukereso.hu/kingston/nv2-2tb-m-2-snv2s-2000g-p861081282/",
        "https://www.arukereso.hu/alaplap-c3128/asus/rog-strix-b760-f-gaming-wifi-p908525874/",
        "https://www.arukereso.hu/memoria-modul-c3577/corsair/vengeance-rgb-32gb-2x16gb-ddr5-5600mhz-cmh32gx5m2b5600c36k-p883958631/"
    ]
}

all_poducts = {   "p864861552": "i5-13600k", 
    "p864865917": "i7-13700k", 
    "p949211577": "ASUS TUF Gaming GeForce RTX 4070 12G GDDR6X OC",
    "p763397892": "Corsair MP600 PRO LPX 1TB M.2 PCIe NVMe (CSSD-F1000GBMP600PLP)",
    "p861081282": "Kingston NV2 2TB M.2 (SNV2S/2000G)",
    "p908525874": "ASUS Rog Strix B760-F Gaming WIFI Alaplap",
    "p883958631": "Corsair VENGEANCE RGB 32GB (2x16GB) DDR5 5600MHz CMH32GX5M2B5600C36K"
}


# urls = json(urls_json)

prices = []
sum_p = 0

for url in urls_json["urls"]:
    for product in all_poducts:
        if product in url:
            name = all_poducts[product]
            response = requests.get(url, timeout=15)
            lowest = '<span class="price" itemprop="lowPrice" content="'
            lines = response.text.splitlines()
            for line in lines:   
                if lowest in line:
                    #print(line)
                    start_marker = ">"
                    end_marker = "<"
                    # Find the index of the start marker
                    start_index = line.find(start_marker)
                    if start_index != -1:
                        # Find the index of the end marker, starting from the index after the start marker
                        end_index = line.find(end_marker, start_index + len(start_marker))
                        if end_index != -1:
                            # Extract the desired substring between the start and end markers
                            extracted_text = line[start_index + len(start_marker):end_index]
                            print(name + ": " + extracted_text)
                            #prices.append(int(extracted_text))

# for item_price in prices:
#     sum_P = sum + item_price
# print(sum_p)



    



