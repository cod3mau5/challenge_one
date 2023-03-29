import scrapy
import json


class DepartmentsSpider(scrapy.Spider):
    name = 'departments'


    def start_requests(self):

        yield scrapy.Request(
            url="https://super.walmart.com.mx/orchestra/graphql/header",
            method='POST',
            headers={
                'authority': 'super.walmart.com.mx',
                'accept': 'application/json',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,es-US;q=0.7,es-MX;q=0.6,es;q=0.5',
                'content-type': 'application/json',
                'cookie': '_uetvid=5e4c48c0a4f211ed8915a9ff9ee0d545; _fbp=fb.2.1675559639242.230673172; _clck=1hl9br8|1|f8v|0; cto_bundle=UUbGtF9NdDJObDZnM281RFhCVFRESWc2UGU5JTJCVyUyQmxidHFNZDdnT25ZYzR6NU53OGtrdXFvV0RoRjFYJTJGaVNZQlRIa3N6ZUM1aVRiNFE5YnJGYnZrYjJ6VzVkUmVHJTJCUElBQk9NZUlLNDVVNDhMN2ZPTzI5WkRxZnBOZEFxSkh1a3hSYW9ScDZuTlk2T3lMdU11SERtUHU1OVEzZyUzRCUzRA; FPID=FPID2.3.ZTAuRCOmTFSjgjZqVc0FewoBEkemcVWv0mdKCVUn9P4%3D.1675559639; _ga=GA1.3.2049529318.1675559639; __gads=ID=b451f5727e7b9975:T=1675559672:S=ALNI_MbvXd30-KUshjxQAdbmpL_vv4A1Lw; _ga_9C15BZ4SZ5=GS1.1.1675631014.2.0.1675631014.60.0.0; _ga_RZERZ9LC4J=GS1.1.1675631014.2.0.1675631014.60.0.0; ACID=40814db2-7bbe-4813-ad93-971354ade5bd; wmt.c=0; vtc=So2zKmx3AdEVLL-T0bjczs; TS01bab4a0=01938a701098159b641696f99482bc8c1f498f818fb96a83a96f50a86d693f8a448bba9856bd8038ac1c1e2c2e04f56c66967c4cfa; pxcts=de2c8233-c8ff-11ed-9fc4-70527a5a6b59; _pxvid=de2c738c-c8ff-11ed-9fc4-70527a5a6b59; adblocked=false; cartId=dea0cfd0-c8ff-11ed-89a8-014325fcdf30; cartType=OD; QuantumMetricUserID=61e5005bdc702b5d6203c6acafe31762; locDataV3=eyJmdWxmaWxsbWVudE9wdGlvbiI6IlBJQ0tVUCIsIm1hcmtldFR5cGUiOiJPRCIsInBpY2t1cFN0b3JlIjp7ImFjY2Vzc1BvaW50SWQiOiIxY2VlZWUwMC1lODljLTQ4OWQtYTU3Zi02N2MwYzA0ZmQ0MzUiLCJhY2Nlc3NUeXBlIjoiUElDS1VQX0lOU1RPUkUiLCJhZGRyZXNzTGluZU9uZSI6IkNhbHphZGEgZGUgR3VhZGFsdXBlICM0MzEiLCJjaXR5IjoiVmFsbGUgZGUgTcOpeGljbyIsImNvdW50cnlDb2RlIjoiTVgiLCJmdWxmaWxsbWVudE9wdGlvbiI6IlBJQ0tVUCIsImZ1bGZpbGxtZW50VHlwZSI6IklOU1RPUkVfUElDS1VQIiwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjE5LjQ3MjEwMywibG9uZ2l0dWRlIjotOTkuMTIwNzA3fSwicG9zdGFsQ29kZSI6IjA3ODQwIiwiZGlzcGxheU5hbWUiOiJXTSBUZXBleWFjIiwic3RhdGVPclByb3ZpbmNlQ29kZSI6IkNpdWRhZCBEZSBNZXhpY28iLCJzdG9yZUlkIjoiMDAwMDAwMjM0NSIsInN0b3JlSHJzIjp7InN0YXJ0IjoiMDowMGFtIiwiZW5kIjoiMTE6NTlwbSJ9LCJpbnN0b3JlUGlja3VwSWQiOiIxY2VlZWUwMC1lODljLTQ4OWQtYTU3Zi02N2MwYzA0ZmQ0MzUifSwic2hpcHBpbmciOnsicG9zdGFsQ29kZSI6IjA3ODQwIiwiY2l0eSI6IlZhbGxlIGRlIE3DqXhpY28iLCJzdGF0ZU9yUHJvdmluY2VDb2RlIjoiQ2l1ZGFkIERlIE1leGljbyIsImNvdW50cnlDb2RlIjoiTVgiLCJsYXRpdHVkZSI6MTkuNDcyMTAzLCJsb25naXR1ZGUiOi05OS4xMjA3MDcsImlzUG9Cb3giOmZhbHNlLCJpc0Fwb0ZwbyI6ZmFsc2V9LCJkZWxpdmVyeVN0b3JlIjp7ImFjY2Vzc1BvaW50SWQiOiI3MGJlNDNhMC00OTkwLTRhNzUtYWZmZS02MGNjZDc2YzA4YjAiLCJhZGRyZXNzTGluZU9uZSI6IkNhbHphZGEgZGUgR3VhZGFsdXBlICM0MzEiLCJhY2Nlc3NUeXBlIjoiREVMSVZFUlkiLCJjaXR5IjoiVmFsbGUgZGUgTcOpeGljbyIsImNvdW50cnlDb2RlIjoiTVgiLCJkaXNwbGF5TmFtZSI6IlRlcGV5YWMgRGVsaXZlcnkiLCJwb3N0YWxDb2RlIjoiMDc4NDAiLCJzdGF0ZU9yUHJvdmluY2VDb2RlIjoiQ2l1ZGFkIERlIE1leGljbyIsInN0b3JlSWQiOiIwMDAwMDAyMzQ1In0sImlzRGVmYXVsdFN0b3JlIjp0cnVlLCJpc0V4cGxpY2l0SW50ZW50IjpmYWxzZSwicmVmcmVzaEF0IjoxNjc5NTc0NTU3MzY3LCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6NDA4MTRkYjItN2JiZS00ODEzLWFkOTMtOTcxMzU0YWRlNWJkIn0%3D; hasLocData=1; bstc=bsMo4zKx8gnyisVhGHjch4; xpa=IdKDE; exp-ck=1; _astc=2d34fdc6a99befaf860c33490c286761; dimensionData=663; xpm=1%2B1679552957%2BSo2zKmx3AdEVLL-T0bjczs~%2B0; __gpi=UID=0000093c87a58518:T=1675559672:RT=1679552960:S=ALNI_MZy7j80NsHA_Ab5fJOJhofKnN2EZw; QuantumMetricSessionID=a5309b6a908be4a40adbcca95f99a718; TS01f4281b=01c5a4e2f91533bdec1dc381a78a00348628db883e223759aa65825be746e32b9198ab9f37494d6f431f34c2e0a2193f3f76e5165f; TS01c7b722=01c5a4e2f91533bdec1dc381a78a00348628db883e223759aa65825be746e32b9198ab9f37494d6f431f34c2e0a2193f3f76e5165f; TS0183c1de=01c5a4e2f91533bdec1dc381a78a00348628db883e223759aa65825be746e32b9198ab9f37494d6f431f34c2e0a2193f3f76e5165f; TS0e68bea5027=08cb8c7367ab20007eec92d1fcc751b98b25922046446b3964a342eea315b2c7a75b487a34cb6ebe087a39f0ac113000020978ca07f718c4cc26cb9e3a62464e5b7c669b8c6a0d84a88954543ad34e17c6c23ca7b4ce5b22199a046cc45f919e; TS014f2e15=01938a70105556d123cbc938c03f745425acd144c1d12ec4fff45d058f8cd96406733c4aac25d70508b6806c88447913005a32e594; TS017cb12c=01938a70105556d123cbc938c03f745425acd144c1d12ec4fff45d058f8cd96406733c4aac25d70508b6806c88447913005a32e594; TS0138c7d0=01938a70105556d123cbc938c03f745425acd144c1d12ec4fff45d058f8cd96406733c4aac25d70508b6806c88447913005a32e594; akavpau_vp_super=1679553736~id=074475c24257bc6b00e2fd91a9c24f89; _px3=d783483b0f3e98e703b42ea701a54336998b224a1bfccabb6b800fb0c220d48d:OiXzNSpSdUGVAlUfsxjXVicHS0jwECZRIIZBFUJYUzdpsKvneSA+Zlc9nrvBTFNXhxJ3Q9A7Gl2sb28GwkeE8Q==:1000:0P4Jkh7nl+qlrlqhRn0dK6XVz/u/tOaZBGGKj04O4RvstND7yGQAARFPLg0TVbr4AIaLXVZ9BGeTOkKMC5jMMnG1RllBPjeshvfw/28uqS+gNayuKaTKUKw9Ns3zseZfVbqWDvI6zTlX6Z/GROAL6ZsPCLhollFxf7K/zmfweq11ngLbxH2I5IDyVV6WqYEKGcSRSa5bsSFvPq3OxEYzoA==; _pxde=e8059cb132cb7728de33c34c842b52bbdf5f6004fe3978e31d0409603ec72167:eyJ0aW1lc3RhbXAiOjE2Nzk1NTM1NTM3NTJ9; TS0138c7d0=01538efd7c80e9c58ec4ee33d18840c699c30fef8bbebaf6659fcb8838925bb842e2406fa2e12b2a6fb7f5379e15c59878ca043b7e; TS017cb12c=01538efd7c80e9c58ec4ee33d18840c699c30fef8bbebaf6659fcb8838925bb842e2406fa2e12b2a6fb7f5379e15c59878ca043b7e; bstc=bsMo4zKx8gnyisVhGHjch4; exp-ck=1; vtc=So2zKmx3AdEVLL-T0bjczs; xpa=IdKDE; xpm=1%2B1679557615%2BSo2zKmx3AdEVLL-T0bjczs~%2B0; TS014f2e15=01538efd7c9cfa50789ff36d5d1aacb7cf4d545f30fb7e7bdb94bdaa9c0015e0bd19b61c629addb37d8f74d52330c274ad4bfda5f9; akavpau_vp_super=1679558445~id=6de02f4976d7be1aeef7f3c74b537a60',
                'device_profile_ref_id': '0QU3gXs4CHN7pxsh8Br67ZuHtgmppsYDviJl',
                'origin': 'https://super.walmart.com.mx',
                'referer': 'https://super.walmart.com.mx/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'traceparent': '00-1b47dfb802c846044a5f77095fc45759-6c2e6fccbf1e5e4f-00',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'wm_consumer.banner': 'GR',
                'wm_mp': 'true',
                'wm_page_url': 'https://super.walmart.com.mx/',
                'wm_qos.correlation_id': 'p9uKEmWGU_fdsRADJzb8N02bt5bg6PGTk4Cs',
                'x-apollo-operation-name': 'Header',
                'x-enable-server-timing': '1',
                'x-latency-trace': '1',
                'x-o-bu': 'WALMART-MX',
                'x-o-ccm': 'server',
                'x-o-correlation-id': 'p9uKEmWGU_fdsRADJzb8N02bt5bg6PGTk4Cs',
                'x-o-gql-query': 'query Header',
                'x-o-mart': 'B2C',
                'x-o-platform': 'rweb',
                'x-o-platform-version': 'main-1.26.1-90b166',
                'x-o-segment': 'oaoh'
            },
            body=json.dumps({
                "query": "query Header( $globalHeaderTempoParams:JSON $tenant:String! $pageType:String! ){contentLayout( channel:\"WWW\" pageType:$pageType tenant:$tenant version:\"v1\" ){modules(p13n:{}tempo:$globalHeaderTempoParams){name type moduleId matchedTrigger{zone}configs{...on EnricherModuleConfigsV1{zoneV1}...GlobalAlertBar...GlobalHeaderHamburgerNav...GlobalHeaderMenu}}}}fragment GlobalHeaderHamburgerNav on TempoWM_GLASSWWWGlobalHamburgerNavConfigs{subCategory{subLinks{link{linkText title clickThrough{value}uid}icon}}}fragment GlobalHeaderMenu on TempoWM_GLASSWWWGlobalHeaderMenuConfigs{allCategoriesLink{linkText title clickThrough{value}uid}departments{name cta{linkText title clickThrough{value}uid}heading description image{alt assetId assetName clickThrough{value}height src title width size contentType uid}subCategoryGroup{subCategoryHeading subCategoryLinksGroup{subCategoryLink{linkText title clickThrough{value}uid}openInNewTab}}}}fragment GlobalAlertBar on TempoWM_GLASSWWWGlobalAlertBarConfigsV1{athenaEnabled alertBarV1{iconName text link{linkText title clickThrough{value}uid}backgroundColor messageColor showCloseButton}}",
                "variables": {
                    "globalHeaderTempoParams": {
                    "params": [
                        {
                        "key": "zone",
                        "value": "alertBar"
                        },
                        {
                        "key": "zone",
                        "value": "hamburgerNav"
                        },
                        {
                        "key": "zone",
                        "value": "departmentsMenu"
                        },
                        {
                        "key": "zone",
                        "value": "servicesMenu"
                        }
                    ]
                    },
                    "tenant": "MX_GLASS",
                    "pageType": "global_header"
                }
            }),
            callback=self.parse,
        )

    def parse(self, response):

        baseUrl="https://super.walmart.com.mx"
        res= json.loads(response.body)
        departments=res["data"]["contentLayout"]["modules"][0]["configs"]["departments"]

        
        for department in departments:
            # first level
            departmentName=department["subCategoryGroup"][0]["subCategoryHeading"]
            
            departmentUrl=None
            categories=[]

            categorieInfo={
                "name":departmentName,
                "url":departmentUrl,
                "subcategories":[]
            }

            links=department["subCategoryGroup"][0]["subCategoryLinksGroup"]
            for link in links:
                if "Ver todo" in link["subCategoryLink"]["linkText"] or "Ver todo" in link["subCategoryLink"]["title"]:
                    departmentUrl=baseUrl+link["subCategoryLink"]["clickThrough"]["value"]
                elif "Temporadas" in departmentName:
                    departmentUrl=baseUrl+"/content/temporadas/"
                elif "Novedades" in departmentName:
                    departmentUrl=baseUrl+"/content/lo-mas-nuevo/"


                subcategorieInfo={
                        "name":link["subCategoryLink"]["title"],
                        "url":baseUrl+link["subCategoryLink"]["clickThrough"]["value"]
                }
                categorieInfo["subcategories"].append(subcategorieInfo)
                categorieInfo["url"]=departmentUrl
            

            categories.append(categorieInfo)
            
                          

            yield {
                "department":departmentName,
                "url":departmentUrl,

                    "categories":categories
            }
    
