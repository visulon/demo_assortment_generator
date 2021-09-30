import streamlit as st
import pickle as pickle
import pandas as pd
import os


st.title("Assortment Generator")
st.write("----------------")
st.sidebar.write("""
    # Explore Different Algorithms
""")
st.sidebar.write("----------------")



classifier_name = st.sidebar.selectbox("Selet Classifier",
                                       ("CountVectorizer", "KNN","T-IDF"))


Assortment_name = st.text_input("Enter Assortment Name")


col1, col2, col3 = st.columns(3)



year = col1.selectbox("Year",
                    ('Select',"2020", "2021"))

season = col2.selectbox("Season",
                      ('Select','Fall', 'Summer', 'Holiday', 'Spring'))

channel = col3.selectbox("Channel",
                             ('Select','Retail', 'Wholesale', 'E-Commerce', 'Wholesale,Retail,E-Commerce', 'Retail,E-Commerce',
                              'Wholesale,E-Commerce', 'Wholesale,Retail'))



my_exp = st.expander("Main Material Content")
cotton = my_exp.checkbox("cotton")
Polyester = my_exp.checkbox("Polyester")
Elastane = my_exp.checkbox("Elastane")
Spandex = my_exp.checkbox("Spandex")
Lyocell = my_exp.checkbox("Lyocell")
Nylon = my_exp.checkbox("Nylon")
Lycra = my_exp.checkbox("Lycra")
Rayon = my_exp.checkbox("Rayon")



Product_Segmentation = st.selectbox("Product Segmentation",
                                    ('Select','Seasonal Key Items', 'Fashion', 'Core', 'CorePlus','Basics','Graphic'))

col4, col5,col6 = st.columns(3)

Business_Group = col4.selectbox("Business Group",
                              ('Select','Tommy Hilfiger', 'Lauren R Lauren','CK'))


Gender = col5.selectbox("Gender",
                      ('Select','Mens', 'Womens', 'Boys', 'Girls', 'Unisex'))

Department = col6.selectbox("Department",
                          ('Select','Knits', ' Sweaters', 'S/S Knits', 'Wovens ', ' S/S T-Shirts', ' Pants', 'T-Shirts', 'Outerwear',
                           'Dresses', 'Fleece', 'Heavy Wgt Knits', 'Shorts', 'L/S Wovens', 'S/S Wovens', 'Denim', 'NON DENIM',
                           'Swimwear', 'L/S Knits','Skirts', 'Hats', 'Bags ', 'L/S T-Shirts', 'ROMPERS', 'OW', 'Socks'))

Design_working_group = st.selectbox("Design Working Group",
                              ('Select','TH Kids', 'TH Mens', 'TH Womens', 'TH Accessories'))

submit = st.button('Recommend')

my_expander = st.sidebar.expander("Advance option")
season = my_expander.selectbox('Year',('Select','2019','2020','2021'))
Month = my_expander.selectbox('Month',('Select','January','February','March','April','May','August','September','October','November','December'))
user = my_expander.text_input("Created by")
my_expander.text('Sharing')
private = my_expander.checkbox("Private")
team = my_expander.checkbox("Team")
Color = my_expander.multiselect(' Color/Group Hue', 
      ['White/Natural 100-109', 'Black 001-009', 'Navy 410-419',
       'Red 600', 'Open White 110-199', 'Light/Pastel Grey 050-059',
       'RED', 'Unknown', 'MISC', 'MULTI', 'Open Blue 460-499', 'BLUE',
       'Dark Grey 021-029', 'Dark Blue 401-409', 'Bright Blue 430-439',
       'Open Green 340-399', 'Light/Pastel Brown 230-239', 'Grey 020',
       'Medium Blue 420-429', 'Light/Pastel Blue 450-459', 'Brown 200',
       'WHITE', 'Blue 400', 'Medium Grey 030-039', 'BLACK', 'Pink 650',
       'Light/Pastel Pink 680-689', 'Multi/Multi Packs 900-959',
       'Orange 800', 'YELLOW', 'PINK', 'GREY', 'NAVY',
       'Bright Green 321-330', 'Gold 710-719', 'Yellow 700',
       'Medium Green 310-320', 'Open Brown 240-249', 'ORANGE',
       'Dark Red 601-609', 'Open Beige 280-299', 'Open Pink 690-699',
       'BROWN', 'Green 300', 'Medium Orange 810-819',
       'Bright Orange 820-829', 'Light/Pastel Green 331-339',
       'Bright Yellow 730-739', 'PURPLE', 'GREEN', 'Open Grey 060-099',
       'BEIGE/KHAKI', 'Turquoise/Aqua 440-449', 'Open Red 640-649',
       'Bright Pink 670-679', 'Dark Beige 251-259',
       'Medium Brown 210-219', 'Dark Pink 651-659',
       'Light/Pastel Yellow 740-749', 'Medium Beige 260-269',
       'Dark Orange 801-809', 'Medium Yellow 720-729',
       'Medium Purple 510-519', 'Light/Pastel Orange 830-839',
       'Medium Pink 660-669', 'Dark Brown 201-209', 'Open Misc 970-998',
       'Dark Purple 501-509', 'Open Yellow 750-799',
       'Open Purple 540-599', 'Dark Green 301-309', 'Dark Yellow 701-709',
       'Beige/Khaki 250', 'Medium Red 610-619', 'Purple 500',
       'Light/Pastel Red 630-639', 'DENIM'])  


Size_Range_Offered = my_expander.multiselect('Size Range Offered', 
      ['XXXS-XXXXL','XS-XXXL','XXS-XL','M-XXL','XXS-XXL','No Size','One Size', '28-50', '0/3-24','28-42', '28-44', '00-28', '00-18',
        '2/3 to 8/10'])  
clicked = my_expander.button('Done')