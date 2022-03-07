from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


data = { 
        "1":
            {
            "id": "1",
            "project": "One Vanderbilt",
            "image": "https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iBevWpMV5RgU/v0/1200x-1.jpg",
            "alttext": "One Vanderbilt",
            "category":"Office Space",
            "neighborhood": "Midtown Manhattan",
            "address": "1 Vanderbilt Ave, New York, NY 10017",
            "cost": "3310000000",
            "costClean": "$3.31 Billion",
            "completed": {"year": "2020","month":"September","day":"14"},
            "completedClean":"September 14, 2020",
            "summary": "One Vanderbilt is a Class A office building developed between 2016 and 2020. It is 93 stories tall and offers observation deck views and large office spaces. Its largest tennant is TD Bank and its principal developer was SL Green Realty Corp.",
            "financiers": ["Wells Fargo","The Bank of New York Mellon","JP Morgan Chase","Toronto-Dominion Bank", "Bank of China","Landesbank Baden-Württemberg"],
            "developers": ["SL Green Realty Corp", "Hines", "NPS"],
            "contractors": ["Navillus Tile"],
            "sqft": "1750212",
            "sqftClean": "1,750,000"
            },
        "2":
            {
            "id": "2",
            "project": "South Bronx Industrial Site",
            "image": "https://s14.therealdeal.com/trd/up/2019/01/1200-980-E.-149th-St-turnbrudge.jpg",
            "alttext": "Central Park Tower",
            "category":"Industrial Development",
            "neighborhood": "South Bronx",
            "address": "980 East 149th Street",
            "cost": "381000000",
            "costClean": "$381 Million",
            "completed": {"year": "","month":"","day":""},
            "completedClean":"N/A",
            "summary": "As e-commerce and grocery delivery services boom, Turnbridge Equities scooped up a South Bronx industrial site that could hold up to 890,000 square feet of warehouse space.The firm paid $56.2 million for the 10-acre industrial development site at 980 East 149th Street, Crain’s reported. ACORE Capital financed the acquisition with a mortgage and mezzanine loan totaling $43.6 million. Dune Real Estate and Turnbridge partnered to begin development on a 1.2 million-square-foot industrial complex after securing $381 million in financing from KKR",
            "financiers": ["ACORE Capital, KKR"],
            "developers": ["Turnbridge Equities", "Dune Real Estate"],
            "contractors": [],
            "sqft": "12000000",
            "sqftClean": "12,000,000"
            },
        "3":
            {
            "id": "3",
            "project": "The Alexander at Rego Park",
            "image": "https://cdn-img-feed.streeteasy.com/nyc/image/53/435547453.jpg",
            "alttext": "Central Park Tower",
            "category":"Residential Apartments",
            "neighborhood": "Rego Park",
            "address": "61-55 Junction Boulevard, Rego Park, NY",
            "cost": "550000000",
            "costClean": "$550 Million",
            "completed": {"year": "2016","month":"","day":""},
            "completedClean":"2016",
            "summary": "At the center of it all, The Alexander in Rego Park is a new level of sophistication, style and comfort located above Rego Center. Featuring a 24-hour concierge, on-site parking and an array of amenities including a lounge with a kitchen and fireplace, private state-of-the-art fitness center, both indoor and outdoor children's playgrounds, bicycle storage and an outdoor landscaped terrace with seating, cabanas and barbeque area. Offering expansive views from the bridges to the beaches, each apartment has white oak floors, 9-foot ceilings and substantial storage. This LEED-certified, 27 story, 312 unit luxury rental building enjoys easy access to a roster of nationally recognized retailers and dining options below at the area's premier shopping destination and subway service to Manhattan one block away. The Alexander is situated near several of Queen's most popular attractions, including the Queens Botanical Garden, the Queens Museum, Flushing Meadows-Corona Park, Citi Field and the National Tennis Center.",
            "financiers": [],
            "developers": ["Vornado Realty Trust"],
            "contractors": [],
            "sqft": "600000",
            "sqftClean": "600,000"
            },
        "4":
            {
            "id": "4",
            "project": "One World Trade Center",
            "image": "https://aecom.com/wp-content/uploads/2015/10/1WTC_Credit-Michael-Mahesh-PANYNJ.jpg",
            "alttext": "Central Park Tower",
            "category":"Office Space",
            "neighborhood": "Downtown Manhattan",
            "address": "285 Fulton St, New York, NY",
            "cost": "3900000000",
            "costClean": "$3.9 Billion",
            "completed": {"year": "2014","month":"November","day":"3"},
            "completedClean":"September 14, 2020",
            "summary": "One World Trade Center (also known as One World Trade, One WTC, and formerly Freedom Tower) is the main building of the rebuilt World Trade Center complex in Lower Manhattan, New York City. One WTC is the tallest building in the United States, the tallest building in the Western Hemisphere, and the seventh-tallest in the world. The supertall structure has the same name as the North Tower of the original World Trade Center, which was destroyed in the terrorist attacks of September 11, 2001. The new skyscraper stands on the northwest corner of the 16-acre (6.5 ha) World Trade Center site, on the site of the original 6 World Trade Center. The building is bounded by West Street to the west, Vesey Street to the north, Fulton Street to the south, and Washington Street to the east.",
            "financiers": ["Port Authority of New York and New Jersey","Larry Silverstein"],
            "developers": ["Silverstein Properties","Port Authority of New York and New Jersey","Skidmore Owings & Merrill"],
            "contractors": ["Tishman Construction"],
            "sqft": "3501000",
            "sqftClean": "3,500,000"
            },
        "5":
            {
            "id": "5",
            "project": "432 Park Avenue",
            "image": "https://newyorkyimby.com/wp-content/uploads/2016/11/432-Park-Avenue-Tower-Looking-South-DBOX.jpg",
            "alttext": "432 Park Avenue, New York, NY",
            "category":"Luxury Apartments",
            "neighborhood": "Midtown East",
            "address": "432 Park Avenue",
            "cost": "1250000000",
            "costClean": "$1.25 Billion",
            "completed": {"year":"2015","month":"December","day":"23"},
            "completedClean":"December 23, 2015",
            "summary": "432 Park Avenue is a residential skyscraper at 57th Street and Park Avenue in Midtown Manhattan in New York City, overlooking Central Park. The 1,396-foot-tall (425.5 m) tower was developed by CIM Group and Harry B. Macklowe and designed by Rafael Viñoly. A part of Billionaires' Row, 432 Park Avenue has some of the most expensive residences in the city, with the median unit selling for tens of millions of dollars.",
            "financiers": ["CIM Group","Citigroup","Pacific Northwest Bank","The Children's Investment Fund Management"],
            "developers": ["CIM Group","Macklowe Properties"],
            "contractors": [],
            "sqft": "412637",
            "sqftClean": "412,637"
            },
        "6":
            {
            "id": "6",
            "project": "111 West 57th Street",
            "image": "https://images.adsttc.com/media/images/5dc1/57e4/3312/fd7c/7e00/0817/large_jpg/111W57__Hugh_Ferriss_Image_FINAL_JDS.jpg?1572951990",
            "alttext": "Central Park Tower",
            "category":"Luxury Apartments",
            "neighborhood": "Midtown East",
            "address": "111 West 57th Street, New York, NY",
            "cost": "2000000000",
            "costClean": "$2 Billion",
            "completed": {"year": "2021","month":"","day":""},
            "completedClean":"2021",
            "summary": "111 West 57th Street, also known as Steinway Tower, is a supertall residential skyscraper in the Midtown Manhattan neighborhood of New York City. Developed by JDS Development Group and Property Markets Group, it is situated along Billionaires' Row on the north side of 57th Street near Sixth Avenue. The main portion of the building is an 84-story, 1,428-foot (435-meter) tower designed by SHoP Architects and completed in 2021.",
            "financiers": ["Annaly Capital Management","AmBase Corporation","American International Group","Apollo Global Management","Quatar Investment Authority"],
            "developers": ["JDS Development Group","Property Markets Group"],
            "contractors": [],
            "sqft": "",
            "sqftClean": "N/A"
            },
        "7":
            {
            "id": "7",
            "project": "Central Park Tower",
            "image": "https://cdn-img-feed.streeteasy.com/nyc/image/14/435222014.jpg",
            "alttext": "Central Park Tower and a view of central park",
            "category":"Luxury Apartments",
            "neighborhood": "Columbus Circle",
            "address": "225 West 57th Street, New York, NY",
            "cost": "3000000000",
            "costClean": "$3 Billion",
            "completed": {"year": "2021","month":"","day":""},
            "completedClean":"2021",
            "summary": "Central Park Tower, also known as the Nordstrom Tower, is a residential supertall skyscraper at 225 West 57th Street in the Midtown Manhattan neighborhood of New York City, along Billionaires' Row. Designed by Adrian Smith + Gordon Gill Architecture, the building rises 1,550 feet (472 m) with 98 above-ground stories and three basement stories, although the top story is numbered 136. Central Park Tower is the second-tallest building in New York City, the United States, and the Western Hemisphere; the 14th tallest building in the world; the tallest primarily residential building in the world; and the tallest building outside Asia by roof height.",
            "financiers": ["The Blackstone Group","HSBC","Tel Aviv Stock Exchange","Shanghai Municipal Investment Group","JP Morgan Chase"],
            "developers": ["Extell Development Company"],
            "contractors": ["Lendlease"],
            "sqft": "1285308",
            "sqftClean": "1,285,308"
            },
        "8":
            {
            "id": "8",
            "project": "Trump Tower",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Trump_Tower_%287181836700%29_%28cropped%29.jpg/500px-Trump_Tower_%287181836700%29_%28cropped%29.jpg",
            "alttext": "Central Park Tower",
            "category":"Residential and Retail",
            "neighborhood": "Midtown East",
            "address":"721 Fifth Avenue Manhattan, New York, NY",
            "cost": "300000000",
            "costClean": "$300 Million",
            "completed": {"year": "1983","month":"November","day":"30"},
            "completedClean":"November 30, 1983",
            "summary": "Trump Tower is a 58-floor, 664-foot-tall (202 m) mixed-use skyscraper at 721–725 Fifth Avenue in the Midtown Manhattan neighborhood of New York City, between 56th and 57th Streets. It serves as the headquarters for the Trump Organization. Additionally, it houses the penthouse condominium residence of businessman, real estate developer, and former U.S. president Donald Trump, who developed the building and named it after himself.",
            "financiers": [],
            "developers": ["Donald Trump"],
            "contractors": ["HRR Construction"],
            "sqft": "300000",
            "sqftClean": "300,000"
            },
        "9":
            {
            "id": "9",
            "project": "8 Spruce Street",
            "image": "https://miro.medium.com/max/1400/1*-I_bZ0F8mJAYsZKE9MOEfA.jpeg",
            "alttext": "Central Park Tower",
            "category":"Residential and Retail",
            "neighborhood": "Financial District",
            "address": "8 Spruce Street",
            "cost": "875000000",
            "costClean": "$875 Million",
            "completed": {"year": "2011","month":"February","day":""},
            "completedClean":"2011",
            "summary": "8 Spruce Street, previously known as the Beekman Tower and New York by Gehry,[4] is a 76-story skyscraper designed by architect Frank Gehry at 8 Spruce Street in the Financial District of Manhattan, New York City. 8 Spruce Street is one of the tallest residential towers in the world, and it was the tallest residential tower in the Western Hemisphere at the time of opening in February 2011.",
            "financiers": [],
            "developers": ["Forest City Ratner"],
            "contractors": ["Kreisler Borg Florman"],
            "sqft": "1100000",
            "sqftClean": "110,000"
            },
        "10":
            {
            "id": "10",
            "project": "56 Leonard Street",
            "image": "https://blog.architizer.com/wp-content/uploads/9.jpg",
            "alttext": "Central Park Tower",
            "category":"Residential",
            "neighborhood": "Tribeca",
            "address": "56 Leonard Street",
            "cost": "500000000",
            "costClean": "$500 Million",
            "completed": {"year": "2017","month":"","day":""},
            "completedClean":"2017",
            "summary": "56 Leonard Street (known colloquially as the Jenga Building or Jenga Tower) is an 821-foot-tall (250 m), 57-story skyscraper on Leonard Street in the neighborhood of Tribeca in Manhattan, New York, United States. The building was designed by the Swiss architecture firm Herzog & de Meuron, which describes the building as \"houses stacked in the sky.\" It is the tallest structure in Tribeca.",
            "financiers": ["Bank of America"],
            "developers": ["Alexico Group"],
            "contractors": [],
            "sqft": "500000",
            "sqftClean": "500,000"
            }                 
        }


@app.route('/')
def home():
    #select featured items
    featured = []
    featured.append(data["1"]) 
    featured.append(data["9"])
    featured.append(data["3"])
    featured.append(data["4"])

    return render_template("home.html", featured = featured)


@app.route('/search', methods = ["GET","POST"])
def search():

    searchTerm = request.args.get("input")
    lowerTerm = searchTerm.lower()
    if lowerTerm is None:
        lowerTerm = ""

    results = []
    for key, val in data.items():
        append = False
        if lowerTerm in val["project"].lower():
            results.append({"project":val})
        elif lowerTerm in val["neighborhood"].lower():
            results.append({"neighborhood":val})
        else:
            for developer in val["developers"]:
                if lowerTerm in developer.lower():
                    results.append({"developers":val})
                    append = True
                    break
            if not append:
                for financier in val["financiers"]:
                    if lowerTerm in financier.lower():
                        results.append({"financiers":val})
                        append = True
                        break
            if not append:
                for contractor in val["contractors"]:
                    if lowerTerm in contractor.lower():
                        results.append({"contractors":val})
                        append = True
                        break

    return render_template("searchresult.html", search = searchTerm, results = results)

@app.route('/searchval/<searchVal>')
def searchval(searchVal = None):
    lowerTerm = searchVal.lower()
    if lowerTerm is None:
        lowerTerm = ""

    results = []
    for key, val in data.items():
        append = False
        if lowerTerm in val["project"].lower():
            results.append({"project":val})
        elif lowerTerm in val["neighborhood"].lower():
            results.append({"neighborhood":val})
        else:
            for developer in val["developers"]:
                if lowerTerm in developer.lower():
                    results.append({"developers":val})
                    append = True
                    break
            if not append:
                for financier in val["financiers"]:
                    if lowerTerm in financier.lower():
                        results.append({"financiers":val})
                        append = True
                        break
            if not append:
                for contractor in val["contractors"]:
                    if lowerTerm in contractor.lower():
                        results.append({"contractors":val})
                        append = True
                        break

    return render_template("searchresult.html", search = searchVal, results = results)

'''
@app.route("/get_featured", methods = ["GET","POST"])
def get_featured():
    nums = request.get_json()
    first = nums["1"]
    second = nums["2"]
    third = nums["3"]

    featured = []
    featured.append(data[first])
    featured.append(data[second])
    featured.append(data[third])
    return jsonify(featured = featured)
'''

@app.route('/view/<id>')
def view(id):
    result = data[id]
    address = result["address"]

    embedCode = address.replace(" ","+")

    return render_template("view.html", result = result, embedCode = embedCode)


if __name__ == '__main__':
    app.run(debug = True)