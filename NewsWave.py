import tkinter
import customtkinter
import requests  

class NewsWave(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("NEWSWAVE")
        self.geometry("900x550")
        self.minsize(800,450)

        # Create a 1x1 grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create the sidebar and tabview
        self.create_sidebar()
        self.create_tabview()

    def create_sidebar(self):
        sidebar = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        sidebar.grid(row=0, column=0, rowspan=1, sticky="nsew")
        sidebar.grid_rowconfigure(4, weight=1)

        logo_label = customtkinter.CTkLabel(sidebar, text="NEWSWAVE", font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        appearance_mode_label = customtkinter.CTkLabel(sidebar, text="Appearance Mode:", anchor="w")
        appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        appearance_mode_optionmenu = customtkinter.CTkOptionMenu(sidebar, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        scaling_label = customtkinter.CTkLabel(sidebar, text="UI Scaling:", anchor="w")
        scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        scaling_optionmenu = customtkinter.CTkOptionMenu(sidebar, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        scaling_optionmenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    def create_tabview(self):
        tabview = customtkinter.CTkTabview(self, width=0)
        tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        tab_labels = ["Trending", "Business", "Sports News"]
        for label in tab_labels:
            self.add_scrollable_tab(tabview,label) 

    def content(self,tab_label):
        if "Trending" in tab_label:
            query_params = {"source": "bbc-news","sortBy": "top","apiKey": "4dbc17e007ab436fb66416009dfb59a8"}
            main_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
            res = requests.get(main_url, params=query_params)
            open_bbc_page = res.json()
            article = open_bbc_page["articles"]
            result = []
            result = [f"{i + 1}. {article['title']}" for i, article in enumerate(article)]
            return result
        elif "Sports News" in tab_label:
            params = {'q': 'sports','source': ("BBC Sport"),'sortBy': 'top','language': 'en','category': 'sports','country': 'in'}
            headers = {'X-Api-Key': '4dbc17e007ab436fb66416009dfb59a8'}
            url = 'https://newsapi.org/v2/top-headlines'
            response = requests.get(url, params=params, headers=headers)
            data = response.json()
            article = data["articles"] 
            result = []
            result = [f"{i + 1}. {article['title']}" for i, article in enumerate(article)]
            return result
        else:
            params = {'q': 'business','source': ("BBC news"),'sortBy': 'top','language': 'en','category': 'business','country': 'in'}
            headers = {'X-Api-Key': '4dbc17e007ab436fb66416009dfb59a8'}
            url = 'https://newsapi.org/v2/top-headlines'
            response = requests.get(url, params=params, headers=headers)
            data = response.json()
            article = data["articles"] 
            result = []
            result = [f"{i + 1}. {article['title']}" for i, article in enumerate(article)]
            return result

    def add_scrollable_tab(self, tabview, label):
        tab = tabview.add(label)
        scrollable_frame = customtkinter.CTkScrollableFrame(tab)
        scrollable_frame.pack(fill=tkinter.BOTH,padx=10,pady=10,expand=1)
        Label1 = customtkinter.CTkLabel(scrollable_frame, text="\n".join(self.content(label)), font=customtkinter.CTkFont(size=20, weight="bold"))
        Label1.pack(padx=10,pady=10, anchor="w")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = NewsWave()
    app.mainloop() 