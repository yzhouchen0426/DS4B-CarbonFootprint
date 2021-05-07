import streamlit as st

st.title("Food Carbon Footprint")
st.subheader("DS4B Final Project")
st.text('Yan Zhou Chen, Britnie Nguyen, Angeline Utomo, and JoJo Zhang')
st.text('Spring 2021')

import pandas as pd
from PIL import Image

st.markdown("We often underestimate the greenhouse gas (GHG) emissions associated with the food production chain when in reality, food production contributes 26% of the global GHG emissions. Using datasets from Hannah Ritchie and Max Roser's *Our World in Data* documentation (https://ourworldindata.org/environmental-impacts-of-food), we aim to visualize GHG emissions associated with different food groups across stages of the food production chain. We hope that the visualizations and food-associated GHG calculator we are providing can help to empower consumers to make more sustainable decisions when it comes to their diets.")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")


#----------------------------JoJo----------------------------------------------------------------------------------------------------------------------------------
        
import streamlit.components.v1 as components
df = pd.read_csv("co2_emission.csv")

food_ghg_map = """<script type='text/javascript' src='https://prod-useast-b.online.tableau.com/javascripts/api/viz_v1.js'></script><div 
class='tableauPlaceholder' style='width: 1000px; height: 850px;'><object class='tableauViz' width='1000' height='850' style='display:none;'><param name='host_url' 
value='https%3A%2F%2Fprod-useast-b.online.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='&#47;t&#47;dsbfinal' /><param 
name='name' value='Food_GHG_1990-2015_by_tonnes&#47;Dashboard1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='showAppBanner' value='false' /
></object></div>
"""

total_co2_map = """<script type='text/javascript' src='https://prod-useast-b.online.tableau.com/javascripts/api/viz_v1.js'>
</script><div class='tableauPlaceholder' style='width: 1000px; height: 850px;'><object class='tableauViz' width='1000' height='850' style='display:none;'>
<param name='host_url' value='https%3A%2F%2Fprod-useast-b.online.tableau.com%2F' /> <param name='embed_code_version' value='3' /> 
<param name='site_root' value='&#47;t&#47;dsbfinal' /><param name='name' value='Total_CO2_Map&#47;Dashboard1' /><param name='tabs' 
value='yes' /><param name='toolbar' value='yes' /><param name='showAppBanner' value='false' /></object></div>"""

co2_stacked = """<script type='text/javascript' src='https://prod-useast-b.online.tableau.com/javascripts/api/viz_v1.js'></script><div class='tableauPlaceholder'style='width: 1280px; height: 563px;'><object class='tableauViz' 
width='1280' height='563' style='display:none;'><param name='host_url' value='https%3A%2F%2Fprod-useast-b.online.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='&#47;t&#47;dsbfinal' />
<param name='name'
value='StackedBarsCombined&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='showAppBanner' value='false' /></object></div>"""

consumption_map = """<script type='text/javascript' src='https://prod-useast-b.online.tableau.com/javascripts/api/viz_v1.js'></script><div class='tableauPlaceholder' 
style='width: 1280px; height: 563px;'><object class='tableauViz' width='1280' height='563' style='display:none;'><param name='host_url' value='https%3A%2F%2Fprod-useast-b.
online.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='&#47;t&#47;dsbfinal' /><param name='name' value='DataScienceforBiote
chnology&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='showAppBanner' value='false' /></object></div>"""

st.header("Visualizing GHG Emissions")

st.markdown("Total CO2 Emissions Annually")
components.html(total_co2_map, width = 900, height = 500, scrolling = True)
st.markdown("How does this compare to GHG emissions from food production?")
components.html(food_ghg_map, width = 900, height = 500, scrolling = True)
st.markdown("For a clearer comparison...")
components.html(co2_stacked, width = 900, height = 500, scrolling = True)
st.markdown("Total CO2 Emissions Annually Based On Consumption")
components.html(consumption_map, width = 900, height = 500, scrolling = True)
#---------------------------YAN----------------------------
st.markdown(" ")
st.header("GHG Emission by Food groups and Production Stages")
                     
df = pd.read_csv("GHG avg by food groups.csv")
avg_ghg = df.pop('Avg GHG (kg CO2 equivalent/ kg product)')
df = df.dropna()

grouped_df = df.groupby(by=['Food group']).mean()
grouped_df = grouped_df.sort_values(by = 'Total GHG (kg CO2 equivalent/ kg product)', ascending = False)
st.write(grouped_df)
col1, col2 = st.beta_columns(2)
with col1:
        image = Image.open('food_production_chain.jpeg')
        st.image(image, use_column_width = True)
        
with col2:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        rm_total = grouped_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
        new_grouped_df = grouped_df
        f = new_grouped_df.plot.bar(stacked = True)
        st.pyplot()
        
st.markdown("- Production: land use change (think deforestation), animal feed (GHG coming from production of food for livestock), and farm (think methane emissions from cows and rice, gases produced by breakdown of manure, etc.)")
st.markdown("- Processing: emission to convert agricultural products to final food products")
st.markdown("- Transport, packaging, and retail")
st.markdown("GHG emission is quantified in CO2 equivalent, as GHGs such as methane and nitrous oxide are significantly more powerful than CO2 in their global warming potentials (standardization to CO2's global warming potential).")
st.markdown(" ")            
            
st.header("What food products are in each food group?")

col1, col2 = st.beta_columns(2)
with col1:
        selected_metrics = st.selectbox(label = '',options=['Plant starch','Plant protein','Animal protein','Vegetable','Fruit','Dairy','Other'],key = "1")
        col1.header(selected_metrics)
        if selected_metrics == 'Plant starch':
          food_group = 'Plant starch'
          food_df = df[df['Food group'] == food_group]
          food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df = food_df.set_index('Food product')
          fig = food_df.plot.bar(stacked = True)
          st.pyplot()

        if selected_metrics == 'Plant protein':
          food_group = 'Plant protein'
          food_df = df[df['Food group'] == food_group]
          food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df = food_df.set_index('Food product')
          fig = food_df.plot.bar(stacked = True)
          st.pyplot()

        if selected_metrics == 'Animal protein':
          food_group = 'Animal protein'
          food_df = df[df['Food group'] == food_group]
          food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df = food_df.set_index('Food product')
          fig = food_df.plot.bar(stacked = True)
          st.pyplot()

        if selected_metrics == 'Vegetable':
          food_group = 'Vegetable'
          food_df = df[df['Food group'] == food_group]
          food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df = food_df.set_index('Food product')
          fig = food_df.plot.bar(stacked = True)
          st.pyplot()


        if selected_metrics == 'Fruit':
          food_group =  'Fruit'
          food_df = df[df['Food group'] == food_group]
          food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df = food_df.set_index('Food product')
          fig = food_df.plot.bar(stacked = True)
          st.pyplot()

        if selected_metrics == 'Dairy':
          food_group = 'Dairy'
          food_df = df[df['Food group'] == food_group]
          food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df = food_df.set_index('Food product')
          fig = food_df.plot.bar(stacked = True)
          st.pyplot()

        if selected_metrics == 'Other':
          food_group = 'Miscellaneous'
          food_df = df[df['Food group'] == food_group]
          food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df = food_df.set_index('Food product')
          fig = food_df.plot.bar(stacked = True)
          st.pyplot()
        
        
with col2:       
        selected_metrics_2 = st.selectbox(label = '',options=['Plant starch','Plant protein','Animal protein','Vegetable','Fruit','Dairy','Other'], key = "2")
        col2.header(selected_metrics_2)
       

        if selected_metrics_2 == 'Plant starch':
          food_group_2 = 'Plant starch'
          food_df_2 = df[df['Food group'] == food_group_2]
          food_df_2.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df_2 = food_df_2.set_index('Food product')
          fig = food_df_2.plot.bar(stacked = True)
          st.pyplot()

        if selected_metrics_2 == 'Plant protein':
          food_group_2 = 'Plant protein'
          food_df_2 = df[df['Food group'] == food_group_2]
          food_df_2.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df_2 = food_df_2.set_index('Food product')
          fig = food_df_2.plot.bar(stacked = True)
          st.pyplot()

        if selected_metrics_2 == 'Animal protein':
          food_group_2 = 'Animal protein'
          food_df_2 = df[df['Food group'] == food_group_2]
          food_df_2.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df_2 = food_df_2.set_index('Food product')
          fig = food_df_2.plot.bar(stacked = True)
          st.pyplot()

        if selected_metrics_2 == 'Vegetable':
          food_group_2 = 'Vegetable'
          food_df_2 = df[df['Food group'] == food_group_2]
          food_df_2.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df_2 = food_df_2.set_index('Food product')
          fig = food_df_2.plot.bar(stacked = True)
          st.pyplot()


        if selected_metrics_2 == 'Fruit':
          food_group_2 =  'Fruit'
          food_df_2 = df[df['Food group'] == food_group_2]
          food_df_2.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df_2 = food_df_2.set_index('Food product')
          fig = food_df_2.plot.bar(stacked = True)
          st.pyplot()

        if selected_metrics_2 == 'Dairy':
          food_group_2 = 'Dairy'
          food_df_2 = df[df['Food group'] == food_group_2]
          food_df_2.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df_2 = food_df_2.set_index('Food product')
          fig = food_df_2.plot.bar(stacked = True)
          st.pyplot()

        if selected_metrics_2 == 'Other':
          food_group_2 = 'Miscellaneous'
          food_df_2 = df[df['Food group'] == food_group_2]
          food_df_2.pop('Total GHG (kg CO2 equivalent/ kg product)')
          food_df_2 = food_df_2.set_index('Food product')
          fig = food_df_2.plot.bar(stacked = True)
          st.pyplot()
                
st.header("How does each food group contribute to different production stages?")
st.markdown(" ")
col1, col2 = st.beta_columns(2)
with col1:
        stage = st.selectbox(label = '',options=['Land use', 'Animal Feed', 'Farm','Processing','Transport', 'Packging','Retail'])
        st.subheader(stage)
        if stage == 'Land use':
                stage = 'Land use change'
                fig = new_grouped_df.plot.bar(y = 'Land use change')
                st.pyplot()
        if stage == 'Animal Feed':
                fig = new_grouped_df.plot.bar(y = 'Animal Feed')
                st.pyplot()
        if stage == 'Farm':
                fig = new_grouped_df.plot.bar(y = 'Farm')
                st.pyplot()
        if stage == 'Processing':
                fig = new_grouped_df.plot.bar(y = 'Processing')
                st.pyplot()
        if stage == 'Transport':
                fig = new_grouped_df.plot.bar(y = 'Transport')
                st.pyplot()
        if stage == 'Packging':
                fig = new_grouped_df.plot.bar(y = 'Packging')
                st.pyplot()
        if stage == 'Retail':
                fig = new_grouped_df.plot.bar(y = 'Retail')
                st.pyplot()
with col2:
        food_group_ = st.selectbox(label = '', options = ['Plant starch','Plant protein','Animal protein','Vegetable','Fruit','Dairy','Other'], key = "3")
        col2.subheader(food_group_)
        
        if food_group_ == 'Plant starch':
          food_df_3 = df[df['Food group'] == food_group_]
          food_df_3 = food_df_3.set_index('Food product')
          fig = food_df_3.plot.bar(y = stage, color = 'green')
          st.pyplot()
        if food_group_ == 'Plant protein':
          food_df_3 = df[df['Food group'] == food_group_]
          food_df_3 = food_df_3.set_index('Food product')
          fig = food_df_3.plot.bar(y = stage,color = 'green')
          st.pyplot()
        if food_group_ == 'Animal protein':
          food_df_3 = df[df['Food group'] == food_group_]
          food_df_3 = food_df_3.set_index('Food product')
          fig = food_df_3.plot.bar(y = stage,color = 'green')
          st.pyplot()
        if food_group_ == 'Vegetable':
          food_df_3 = df[df['Food group'] == food_group_]
          food_df_3 = food_df_3.set_index('Food product')
          fig = food_df_3.plot.bar(y = stage,color = 'green')
          st.pyplot()
        if food_group_ == 'Fruit':
          food_df_3 = df[df['Food group'] == food_group_]
          food_df_3 = food_df_3.set_index('Food product')
          fig = food_df_3.plot.bar(y = stage,color = 'green')
          st.pyplot()
        if food_group_ == 'Dairy':
          food_df_3 = df[df['Food group'] == food_group_]
          food_df_3 = food_df_3.set_index('Food product')
          fig = food_df_3.plot.bar(y = stage,color = 'green')
          st.pyplot()
        if food_group_ == 'Other':
          food_df_3 = df[df['Food group'] == 'Miscellaneous']
          food_df_3 = food_df_3.set_index('Food product')
          fig = food_df_3.plot.bar(y = stage,color = 'green')
          st.pyplot()
        
#---------------------------ANGIE----------------------------
st.markdown(" ")
st.header("Your turn! How much GHG does your meal contribute?")

# Make food_dict a global variable so my functions can have access to it
global food_dict

food_dict = {'Wheat & Rye': 1.4,
'Cornmeal': 1.1,
'Barley': 1.1,
'Oatmeal': 1.6,
'Rice': 4,
'Potatoes': 0.3,
'Cassava': 0.9,
'Other Pulses': 1.6,
'Peas': 0.8,
'Nuts': 0.2,
'Groundnuts': 2.4,
'Soymilk': 1,
'Tofu': 3,
'Beef': 59.6,
'Lamb & Mutton': 24.5,
'Pork': 7.2,
'Poultry': 6.1,
'Eggs': 4.5,
'Fish (farmed)': 5.1,
'Shrimps (farmed)': 11.8, 
'Tomatoes': 1.4,
'Onions & Leeks': 0.3,
'Root Vegetables': 0.3,
'Cabbages': 0.4,
'Other Vegetables': 0.5,
'Citrus Fruits': 0.3,
'Bananas': 0.8,
'Apples': 0.3,
'Berries & Grapes': 1.1,
'Other Fruits': 0.7,
'Milk': 2.8,
'Cheese': 21.2, 
'Wine': 1.4,             
'Coffee': 16.5,
'Dark Chocolate': 18.7,
'Cane Sugar': 2.6,
'Beet Sugar': 1.4,
'Soybean Oil': 6,
'Palm Oil': 7.6,
'Sunflower Oil': 3.5,
'Rapeseed Oil': 3.7,
'Olive Oil': 6,
'Average plant starch': 1.5,
'Average plant protein': 1.5,
'Average animal protein': 17,
'Average vegetable': 0.6,
'Average fruit': 0.6,
'Average plant oils': 5.4,
}


save_list = st.multiselect('Which food items are included in your meal? You can select multiple items here', list(food_dict))
st.markdown(" ")


st.subheader("Use the following conversion cheat sheet to help you estimate the mass of your food items in grams:")
st.markdown(" ")
"""- 1 cup of uncooked rice/ beans = 200g
- 1 cup of uncooked pasta = 100g
- 1 medium-sized potato = 150g
- 1 slice of bread = 25g
- 1 egg = 50g
- A palm-sized portion of meat = 85g
- 1 cup of raw non-leafy vegetables = 160g
- 1 cup of raw leafy vegetables = 80g
- A handful of berries/ 1 banana/ 1 apple/ 1 orange = 80g
- 1/3 cup of nuts = 50g
- 1 cup of milk = 240g
- 1 tbsp of ground coffee = 5g
"""
st.markdown(" ")


mass_list = []
x = 0
for item in save_list:
  st.write(save_list[x])
  mass = st.number_input('How many grams of this item did you consume?', key = str(x))
  mass_list.append(mass)
  x += 1  
st.markdown(" ")
  
  
def getGHG(save_list, mass_list):
  ghg_list = []
  for idx,save in enumerate(save_list):  
    ghg_amount = food_dict[save]

    ghg_calculator = ghg_amount *mass_list[idx]
    ghg_list.append(ghg_calculator)
    
  return ghg_list

st.markdown("""
<style>
.med-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

ghg_list = getGHG(save_list,mass_list)
total_ghg = sum(ghg_list)
st.markdown(f'<p class="med-font">These food items contributed {int(total_ghg)} g CO2 equivalent</p>', unsafe_allow_html=True)


import matplotlib.pyplot as plt
import numpy as np

def func(pct, allvals):
    absolute = int(round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
  
textprops = {"fontsize": 8}  
st.subheader("Your food GHG breakdown:")
fig = plt.pie(ghg_list, explode=None, labels=save_list, colors=None, autopct=lambda pct: func(pct, ghg_list), shadow=False, radius=1, textprops=textprops)
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)


st.markdown(" ")
st.header("Takeaways:")
st.markdown("- Overall trends for emissions from food production map pretty well to those for total GHG emissions")
st.markdown("- Transport, packaging, and retail do not contribute as much GHG as the pre-farming and farming stages")
st.markdown("- Livestocks, especially cows raised for beef, produce so much more GHG compared to crops. It is estimated that going from current diets to diets that exclude animal products would reduce food's GHG emissions by 49% (Poore and Nemecek 2018).")
st.markdown("- We have only visualized the GHG aspect of food's environmental impact. Check out (https://ourworldindata.org/environmental-impacts-of-food) for visualizations on other impacts such as water use and eutrophication!")

st.markdown(" ")
st.subheader("We would like to thank all of the researchers who contributed to the following documentations. The datasets used to build the visualizations on this page were taken from Hannah Ritchie and Max Roser's page, where data from many other researchers including Poore and Nemecek is compiled, visualized, and analyzed.")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown("- Hannah Ritchie and Max Roser (2020) - 'Environmental impacts of food production'. Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/environmental-impacts-of-food' [Online Resource]")
st.markdown("- Poore, J., & Nemecek, T. (2018). Reducing food’s environmental impacts through producers and consumers. Science, 360(6392), 987-992.")
