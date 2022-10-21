import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('I love Labrodar dogs')

streamlit.header('Available dog breeds')
streamlit.text('We love puppies')
streamlit.text('Dogs eat lot of food')
streamlit.text('We have to take them out periodically')

streamlit.title('🥣 🥗 🐔 🥑🍞 adding emojis')

streamlit.header('🥣 🥗 🐔 🥑🍞 adding emojis')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Add user to pick the friuts they want in the smoothies
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display the table on the page
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")


#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + 'kiwi')
#streamlit.text(fruityvice_response.json())
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit_error('Please select a fruit to get information')
    else:
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        # write your own comment -what does the next line do? 
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        # write your own comment - what does this do?
        streamlit.dataframe(fruityvice_normalized)

except URLError as e:
streamlit.error()

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("my fruit load list contains")
streamlit.dataframe(my_data_rows)


fruit_choice = streamlit.text_input('What fruit you would like to add?','Jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)

my_cur.execute("insert into fruit_load_list values ('From Streamlit')")
