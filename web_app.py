import streamlit as st
from scraper import scrape_kayak_flights
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def streamlit_app():
    st.set_page_config(page_title="Airport Scraper", page_icon="", layout="centered")
        
    tab1, tab2, tab3 = st.tabs(["scraping bot", "mongodb exploration", "analysis"])
        
    with tab1:
        st.title("✈️ Flight Scraper Tool")

        #Predefined Airport Options
        airport_options = ["CAI", "DXB", "DOH", "JED", "RUH", "DMM", "IST", "LHR", "CDG","HBE","HKG"]

        #User Input
        st.subheader("Choose origin Airports")
        origin_city = st.selectbox(
            "Select one Arrival Airports", 
            options=airport_options    
        )

        st.subheader("🛫 Choose destination Airports")
        destination_city = st.selectbox(
            "Select one  Initial Airports",
            options=airport_options,
            
        )

        initial_date = st.date_input("Initial Date")
        
        return_date = st.date_input("Return Date")


        # ====== Scraping Section ======
        if st.button("🚀 Start Scraping"):
            with st.spinner("Starting the scraping process..."):
                scraped_data= scrape_kayak_flights(
                    origin=origin_city,
                    destination=destination_city,
                    depart_date=initial_date.strftime("%Y-%m-%d"),
                    return_date = return_date.strftime("%Y-%m-%d")
                )
                
                # Show results
                df = pd.DataFrame(scraped_data)
                st.subheader("Flights Found")
                st.dataframe(df)

                # Offer download
                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button("⬇Download Results as CSV", csv, "scraped_flights.csv", "text/csv")


    with tab2:
        st.subheader("MongoDB Data")
        
        
        num = st.slider("Select number of showed data", 10,1000)
        
        # Fetch data from MongoDB
        # we will use local data so we can host the streamlit application
        data = pd.read_csv(r"Data/data.csv")
        
        df_mongo = data
        st.dataframe(df_mongo.head(num)) 

    with tab3:
        # st.subheader("Data Analysis")
        # # datapreprocessing
        # df_mongo['airlines'] = df_mongo['airlines'].astype(str)
        # df_mongo['duration'] = df_mongo['duration'].apply(convert_to_minutes)        
        # df_mongo['price'] = df_mongo['price'].apply(convert_to_usd)
        # df_mongo['stops'] = df_mongo['stops'].apply(convert_to_int)
        # st.dataframe(df_mongo.describe())
        
        st.subheader("data visualization")
        
        #first chart
        st.write("Top 10 Average Price per Destinations")
        top_destinations = df_mongo["destination"].value_counts().head(10).index
        top_avg_price_per_dest = df_mongo[df_mongo["destination"].isin(top_destinations)].groupby("destination")['price'].mean().sort_values(ascending = False)
        st.bar_chart(top_avg_price_per_dest)
        st.write("Some destinations (like SGN and TBS) have relatively lower average prices compared to others.\n " \
        "Prices vary significantly by location, likely due to distance or airline competition.")
        
        #second chart
        st.write("Top 10 Average Price per airline")
        top_destinations = df_mongo["airlines"].value_counts().head(10).index
        top_avg_price_per_dest_air = df_mongo[df_mongo["airlines"].isin(top_destinations)].groupby("airlines")['price'].mean().sort_values(ascending = False)
        st.bar_chart(top_avg_price_per_dest_air)
        st.write("Airlines like lberia and flydubai show higher average ticket prices.\n" \
        " Budget carriers like Pegasus and Air Arabia offer lower average prices.")
        
        ####
        
        st.write("Most Affordable Destinations from HBE")
        cheapest_destinations = df_mongo.groupby(['origin', 'destination'])['price'].min().reset_index()

        origin_city = 'HBE'
        cheapest_from_origin = cheapest_destinations[cheapest_destinations['origin'] == origin_city]

        cheapest_from_origin = cheapest_from_origin.sort_values('price', ascending=True)

        fig, ax = plt.subplots(figsize=(12, 6))

        sns.barplot(
            x='price',
            y='destination',
            data=cheapest_from_origin,
            palette='viridis',
            ax=ax
        )

        ax.set_title(f'Most Affordable Destinations from {origin_city}', fontsize=16)
        ax.set_xlabel('Price')
        ax.set_ylabel('Destination')
        ax.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()

        # Display in Streamlit
        st.pyplot(fig)
        st.write("The visualization above shows — destinations like Jeddah, Dubai, and Istanbul are the most.\n" \
        "`affordable from HBE(Borg El Arab).")

        #third chart

        correlation_matrix = df_mongo[["price", "stops", "duration"]].corr()
        fig, ax = plt.subplots(figsize=(6, 4))  # Create a Matplotlib figure and axes
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax) 
        ax.set_title("Correlation Matrix") 
        st.pyplot(fig, use_container_width = True ) 
        
        #fourth chart
        st.write("Average price per stop")
        avg_price_per_stop = df_mongo[["stops", "price"]].groupby("stops")['price'].mean()
        st.bar_chart(avg_price_per_stop)
        st.write("increasing the number of stops will increase the price \n but that also indicates that the distination is further away")

        #fifth chart
        st.write("price vs duration")
        df_scater=df_mongo[["price","duration"]]
        st.scatter_chart(df_scater, x="price", y="duration")

streamlit_app()