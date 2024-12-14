class AppUI(ctk.CTk):
    """Encapsulates UI functionality for interview assistant"""
    global_vars: TranscriptionGlobals
    ui_filename: str = None

    def create_ui_components(self, config: dict):
        """Create all UI components"""
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.title("Interview Assistant")
        self.configure(bg='#252422')
        self.geometry("1200x800")

        # Frame for the main content
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.create_menus()

        # Left side: SelectableTextComponent
        self.transcript_text: SelectableText = SelectableText(self.main_frame)
        self.transcript_text.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        self.transcript_text.set_callbacks(self.global_vars.convo.on_convo_select)

        # Right side
        self.right_frame = ctk.CTkFrame(self.main_frame)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # LLM Response textbox
        self.min_response_textbox_width = 300
        self.response_textbox = ctk.CTkTextbox(self.right_frame, self.min_response_textbox_width,
                                               font=("Arial", UI_FONT_SIZE),
                                               text_color='#639cdc',
                                               wrap="word")
        self.response_textbox.pack(fill="both", expand=True)
        self.response_textbox.insert("0.0", prompts.INITIAL_RESPONSE)

        # Bottom Frame for buttons
        self.bottom_frame = ctk.CTkFrame(self, border_color="white", border_width=2)
        self.bottom_frame.pack(side="bottom", fill="both", pady=10)

        response_enabled = bool(config['General']['continuous_response'])
        b_text = "Suggest Responses Continuously" if not response_enabled else "Do Not Suggest Responses Continuously"
        self.continuous_response_button = ctk.CTkButton(self.bottom_frame, text=b_text)
        self.continuous_response_button.grid(row=0, column=4, padx=10, pady=3, sticky="nsew")
        self.continuous_response_button.configure(command=self.freeze_unfreeze)

        self.response_now_button = ctk.CTkButton(self.bottom_frame, text="Suggest Response Now")
        self.response_now_button.grid(row=1, column=4, padx=10, pady=3, sticky="nsew")
        self.response_now_button.configure(command=self.get_response_now)

        self.read_response_now_button = ctk.CTkButton(self.bottom_frame, text="Suggest Response and Read")
        self.read_response_now_button.grid(row=2, column=4, padx=10, pady=3, sticky="nsew")
        self.read_response_now_button.configure(command=self.update_response_ui_and_read_now)

        self.summarize_button = ctk.CTkButton(self.bottom_frame, text="Summarize")
        self.summarize_button.grid(row=3, column=4, padx=10, pady=3, sticky="nsew")
        self.summarize_button.configure(command=self.summarize)

        # Continuous LLM Response label and slider
        self.update_interval_slider_label = ctk.CTkLabel(self.bottom_frame, text="", font=("Arial", 12),
                                                         text_color="#FFFCF2")
        self.update_interval_slider_label.grid(row=0, column=0, columnspan=4, padx=10, pady=3, sticky="nsew")
        self.update_interval_slider = ctk.CTkSlider(self.bottom_frame, from_=1, to=30, width=300,
                                                    number_of_steps=29)
        self.update_interval_slider.set(config['General']['llm_response_interval'])
        self.update_interval_slider.grid(row=1, column=0, columnspan=4, padx=10, pady=3, sticky="nsew")
        self.update_interval_slider.configure(command=self.update_interval_slider_value)