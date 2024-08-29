import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titel der App
st.title("Test")

# CSV-Datei importieren
df = pd.read_csv('Testdatei.csv', sep=';')

# Konvertiere die Medaillenzahlen in numerische Werte
df['Gold'] = pd.to_numeric(df['Gold'], errors='coerce')
df['Silver'] = pd.to_numeric(df['Silver'], errors='coerce')
df['Bronze'] = pd.to_numeric(df['Bronze'], errors='coerce')

# Konvertiere die NOC-Spalte zu String, um sicherzustellen, dass sie korrekt angezeigt wird
df['NOC'] = df['NOC'].astype(str)

# Zeige nur die ersten 10 Länder an
top_10_df = df.head(10)

# Prüfe, ob die Schweiz in den Top 10 ist, und füge sie hinzu, wenn nicht
switzerland_df = df[df['NOC'].str.contains('Switzerland', case=False)]
if not switzerland_df.empty and 'Switzerland' not in top_10_df['NOC'].values:
    top_10_df = pd.concat([top_10_df, switzerland_df])

# Tabelle in Streamlit anzeigen (Top 10 + Switzerland)
st.write("Tabellarische Darstellung der CSV-Datei (Top 10 + Switzerland):")
st.dataframe(top_10_df)

# Diagramm erstellen
fig, ax = plt.subplots(figsize=(10, 8))

# Balkendiagramm für Gold, Silber und Bronze
ax.bar(top_10_df['NOC'], top_10_df['Gold'], label='Gold', color='gold')
ax.bar(top_10_df['NOC'], top_10_df['Silver'], bottom=top_10_df['Gold'], label='Silver', color='silver')
ax.bar(top_10_df['NOC'], top_10_df['Bronze'], bottom=top_10_df['Gold']+top_10_df['Silver'], label='Bronze', color='#cd7f32')

# Achsenbeschriftungen und Titel
ax.set_xlabel('Countries')
ax.set_ylabel('Number of Medals')
ax.set_title('Medal Count by Country (Top 10 + Switzerland)')
ax.legend()

# Drehe die x-Achsenbeschriftungen für bessere Lesbarkeit
plt.xticks(rotation=90)

# Diagramm in Streamlit anzeigen
st.pyplot(fig)


# Display Text
st.header('Display Text')
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

import streamlit as st

# Display interactive widgets
st.title('Display Interactive Widgets')

# Verschiedene Widgets erstellen
button_clicked = st.button('Hit me')
checkbox_checked = st.checkbox('Check me out')
radio_selected = st.radio('Pick one:', ['nose', 'ear'])
selectbox_selected = st.selectbox('Select', [1, 2, 3])
multiselect_selected = st.multiselect('Multiselect', [1, 2, 3])
slider_value = st.slider('Slide me', min_value=0, max_value=10)
select_slider_value = st.select_slider('Slide to select', options=[1, '2'])
text_input_value = st.text_input('Enter some text')
number_input_value = st.number_input('Enter a number')
text_area_value = st.text_area('Area for textual entry')
date_input_value = st.date_input('Date input')
time_input_value = st.time_input('Time entry')
file_uploaded = st.file_uploader('File uploader')
download_clicked = st.download_button('On the dl', 'Download data')
camera_input_value = st.camera_input("一二三,茄子!")
color_picker_value = st.color_picker('Pick a color')

# Use widgets' returned values in variables
num_iterations = int(st.number_input('Num:'))
for i in range(num_iterations):
    st.write(f"Iteration {i + 1}")


# Use the slider value
my_slider_val = st.slider('Quinn Mallory', 1, 88)
st.write('Selected slider value:', my_slider_val)


#Display Data
st.title('Display data')
st.dataframe(df)
st.table(df.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
st.metric(label="Temp", value="273 K", delta="1.2 K")


# Insert containers separated into tabs
st.title('Insert containers separated into tabs')

# Tabs erstellen
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

# Inhalt in den Tabs anzeigen
tab1.write("This is Tab 1")
tab2.write("This is Tab 2")

# You can also use "with" notation:
with tab1:
    selected_value = st.radio('Select one:', [1, 2])

# Optional: Den ausgewählten Wert aus dem Radio-Button anzeigen
st.write(f'You selected: {selected_value}')

# Sidebar erstellen
st.sidebar.title("Themenauswahl")

# Themen in der Sidebar
thema = st.sidebar.selectbox(
    "Wähle ein Thema:",
    ["Kunstturnen", "Rhythmische Gymnastik", "Trampolin"]
)

# Unterthemen für Kunstturnen
if thema == "Kunstturnen":
    unterthema = st.sidebar.radio("Wähle eine Disziplin:", ["GAM", "GAF"])
    st.write(f"Du hast {unterthema} im Bereich {thema} gewählt.")

elif thema == "Rhythmische Gymnastik":
    st.write("Du hast Rhythmische Gymnastik gewählt.")
    
elif thema == "Trampolin":
    st.write("Du hast Trampolin gewählt.")

# Hauptinhalt je nach Auswahl anzeigen
st.title(f"Ausgewähltes Thema: {thema}")