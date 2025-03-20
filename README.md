# Analytics-app

This is the repository for the analytics pipeline. As a sidenote, some of our analytics pipeline is already covered with the use of the Firebase Analytics and Performance connections made with the front end apps, that allow us to visualize some important data about our users location, devices, loading times in screens, etc. However, this repository covers the extraction, processing and visualization using Microsoft's PowerBI tool of some of the data that could be useful for us or 3-rd parties.

# Project structure
```bash
Analytics-app/  
│── .gitignore  
│── README.md  
│── Dashboard.pbix  # Power BI file  
│── Dashboard.pdf  # PDF version of the dashboard  
│── analysis.py  # Python script for analysis  
│── database.py  # Database connection script  
│── main.py  # Main script  
│── transformed_posts_data.csv  # Processed data file for posts  
```
Note: A .env with URL and TOKEN is needed for the connection with the postgreSQL database hosted in Supabase.


# Generated Dashboard example
![image](https://github.com/user-attachments/assets/3c272795-9fc9-460d-a560-ba37a35c0f66)


# Some other analytics data extracted with Firebase Analytics 
## Authentication with Firebase auth
![image](https://github.com/user-attachments/assets/2957b2e1-1283-498c-a762-e0fb64957d76)


## Performance information with Firebase performance
![image](https://github.com/user-attachments/assets/f1968765-3229-41e2-86a4-9cc6e8b887a6)
![image](https://github.com/user-attachments/assets/d41d88d7-7681-4b95-b5ce-0e9ae0b0e22b)


## Firebase Analytics dashboard for user's locations
![image](https://github.com/user-attachments/assets/595ef7ec-b0a7-4bd3-b1c8-715fdf060cd5)

## Firebase Analytics dashboard with user's devices
![image](https://github.com/user-attachments/assets/59156e66-df80-4701-8950-42dbea1c45c2)
<p align="center">
    <img src="https://github.com/user-attachments/assets/1a87259d-9adf-47a9-b3e6-a3c5d3b4d0b9" width="45%">
    <img src="https://github.com/user-attachments/assets/fd35e1fc-a042-4bec-aa90-846ea70b15ee" width="45%">
</p>
