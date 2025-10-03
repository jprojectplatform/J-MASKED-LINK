import tkinter as tk
from tkinter import ttk, messagebox
import requests
import validators
import webbrowser
import threading
from urllib.parse import quote
import time

class JMaskedLink:
    def __init__(self, root):
        self.root = root
        self.root.title("J Masked Link - Professional URL Masking Tool")
        self.root.geometry("1000x800")
        
        # Beautiful theme management
        self.dark_mode = True
        self.themes = {
            'dark': {
                'bg': '#0f0f23',
                'fg': '#e0e0e0',
                'accent': '#ff6b9d',
                'secondary': '#1a1a2e',
                'text_muted': '#a0a0c0',
                'success': '#4ecdc4',
                'error': '#ff6b6b',
                'warning': '#ffd166',
                'card_bg': '#16213e',
                'border': '#2d3047'
            },
            'light': {
                'bg': '#f8f9fa',
                'fg': '#2d3748',
                'accent': '#e53e3e',
                'secondary': '#ffffff',
                'text_muted': '#718096',
                'success': '#38a169',
                'error': '#e53e3e',
                'warning': '#d69e2e',
                'card_bg': '#ffffff',
                'border': '#e2e8f0'
            }
        }
        
        self.current_theme = self.themes['dark']
        self.root.configure(bg=self.current_theme['bg'])
        
        # Initialize dictionaries
        self.shortener_results = {}
        self.shortener_buttons = {}
        self.shortener_labels = {}
        self.shortener_status = {}
        
        self.create_widgets()
        self.setup_layout()
        self.apply_theme()
        
    def create_widgets(self):
        """Create all GUI widgets"""
        # Create main frame with scrollbar
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True)
        
        # Create canvas and scrollbar for entire app
        self.canvas = tk.Canvas(self.main_frame, bg=self.current_theme['bg'], highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Bind mouse wheel to scroll
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        
        # Header
        self.header_frame = ttk.Frame(self.scrollable_frame, padding="30")
        self.header_label = ttk.Label(self.header_frame, text="🔗 J MASKED LINK", 
                                     font=('Arial', 28, 'bold'))
        self.subheader_label = ttk.Label(self.header_frame, text="Professional URL Masking & Security Tool", 
                                        font=('Arial', 14))
        self.creator_label = ttk.Label(self.header_frame, text="Created by jh4ck3r • J Project Platform", 
                                      font=('Arial', 11))
        
        # Theme toggle button
        self.theme_btn = ttk.Button(self.header_frame, text="🌙 Dark Mode", 
                                   command=self.toggle_theme)
        
        # URL Input Section
        self.input_frame = ttk.LabelFrame(self.scrollable_frame, text="⚙️ URL CONFIGURATION", padding="25")
        
        self.phishing_label = ttk.Label(self.input_frame, text="🎯 Target URL:", font=('Arial', 11, 'bold'))
        self.phishing_entry = ttk.Entry(self.input_frame, width=80, font=('Arial', 10))
        
        self.custom_domain_label = ttk.Label(self.input_frame, text="🏷️ Custom Domain:", font=('Arial', 11, 'bold'))
        self.custom_domain_entry = ttk.Entry(self.input_frame, width=80, font=('Arial', 10))
        self.custom_domain_note = ttk.Label(self.input_frame, text="Example: gmail.com, facebook.com, microsoft.com", 
                                           font=('Arial', 9))
        
        self.keywords_label = ttk.Label(self.input_frame, text="🔑 Security Keywords:", font=('Arial', 11, 'bold'))
        self.keywords_entry = ttk.Entry(self.input_frame, width=80, font=('Arial', 10))
        self.keywords_note = ttk.Label(self.input_frame, text="Example: login, verify, security, update (separate with commas)", 
                                      font=('Arial', 9))
        
        # Control Buttons
        self.control_frame = ttk.Frame(self.scrollable_frame, padding="20")
        self.generate_btn = ttk.Button(self.control_frame, text="🚀 GENERATE MASKED URLS", 
                                      command=self.generate_all_masked_links)
        self.clear_btn = ttk.Button(self.control_frame, text="🗑️ CLEAR ALL", 
                                   command=self.clear_all)
        self.visit_btn = ttk.Button(self.control_frame, text="🌐 VISIT J PROJECT", 
                                   command=self.visit_website)
        
        # Progress Section
        self.progress_frame = ttk.LabelFrame(self.scrollable_frame, text="📊 GENERATION PROGRESS", padding="20")
        self.progress_label = ttk.Label(self.progress_frame, text="Ready to generate masked URLs...", font=('Arial', 10))
        self.progress = ttk.Progressbar(self.progress_frame, mode='indeterminate')
        
        # Results Section
        self.results_frame = ttk.LabelFrame(self.scrollable_frame, text="🎯 GENERATED MASKED URLS", padding="25")
        
        # Status Section
        self.status_frame = ttk.Frame(self.scrollable_frame, padding="15")
        self.status_label = ttk.Label(self.status_frame, text="✅ Ready to generate masked URLs...", font=('Arial', 10))
        
        # Footer
        self.footer_frame = ttk.Frame(self.scrollable_frame, padding="20")
        self.footer_label = ttk.Label(self.footer_frame, text="Enjoy With J Project Platform • Professional Security Tools", 
                                     font=('Arial', 11, 'bold'))
        
    def setup_layout(self):
        """Setup the layout of all widgets"""
        # Pack canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Header
        self.header_frame.pack(fill='x', pady=15)
        self.header_label.pack()
        self.subheader_label.pack(pady=8)
        self.creator_label.pack(pady=8)
        self.theme_btn.pack(pady=15)
        
        # URL Input Section
        self.input_frame.pack(fill='x', padx=30, pady=20)
        
        self.phishing_label.grid(row=0, column=0, sticky='w', pady=10)
        self.phishing_entry.grid(row=0, column=1, sticky='ew', pady=10, padx=(20, 0))
        
        self.custom_domain_label.grid(row=1, column=0, sticky='w', pady=10)
        self.custom_domain_entry.grid(row=1, column=1, sticky='ew', pady=10, padx=(20, 0))
        self.custom_domain_note.grid(row=2, column=1, sticky='w', padx=(20, 0))
        
        self.keywords_label.grid(row=3, column=0, sticky='w', pady=10)
        self.keywords_entry.grid(row=3, column=1, sticky='ew', pady=10, padx=(20, 0))
        self.keywords_note.grid(row=4, column=1, sticky='w', padx=(20, 0))
        
        self.input_frame.columnconfigure(1, weight=1)
        
        # Control Buttons
        self.control_frame.pack(fill='x', padx=30, pady=20)
        self.generate_btn.pack(side='left', padx=12)
        self.clear_btn.pack(side='left', padx=12)
        self.visit_btn.pack(side='right', padx=12)
        
        # Progress Section
        self.progress_frame.pack(fill='x', padx=30, pady=20)
        self.progress_label.pack(fill='x', pady=10)
        self.progress.pack(fill='x', pady=10)
        
        # Results Section
        self.results_frame.pack(fill='both', expand=True, padx=30, pady=20)
        
        # Status Section
        self.status_frame.pack(fill='x', padx=30, pady=15)
        self.status_label.pack()
        
        # Footer
        self.footer_frame.pack(fill='x', padx=30, pady=20)
        self.footer_label.pack()
        
        # Initialize shortener frames after layout is set
        self.initialize_shortener_frames()
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def toggle_theme(self):
        """Toggle between dark and light mode"""
        self.dark_mode = not self.dark_mode
        self.current_theme = self.themes['dark'] if self.dark_mode else self.themes['light']
        self.apply_theme()
        self.theme_btn.config(text="🌙 Dark Mode" if self.dark_mode else "☀️ Light Mode")
    
    def apply_theme(self):
        """Apply current theme to all widgets"""
        theme = self.current_theme
        
        # Configure root window
        self.root.configure(bg=theme['bg'])
        self.canvas.configure(bg=theme['bg'])
        
        # Configure styles with attractive colors
        style = ttk.Style()
        
        # Configure frame styles
        style.configure('TFrame', background=theme['bg'])
        style.configure('Card.TFrame', background=theme['card_bg'])
        
        # Configure label styles
        style.configure('TLabel', background=theme['bg'], foreground=theme['fg'], font=('Arial', 10))
        style.configure('Title.TLabel', background=theme['bg'], foreground=theme['accent'], font=('Arial', 12, 'bold'))
        style.configure('Accent.TLabel', background=theme['bg'], foreground=theme['accent'])
        
        # Configure button styles
        style.configure('TButton', 
                       background=theme['accent'], 
                       foreground=theme['bg' if self.dark_mode else 'secondary'],
                       font=('Arial', 10, 'bold'),
                       borderwidth=0,
                       focuscolor='none')
        style.map('TButton',
                 background=[('active', theme['success']),
                           ('pressed', theme['warning'])])
        
        # Configure entry styles
        style.configure('TEntry', 
                       fieldbackground=theme['card_bg'],
                       background=theme['card_bg'],
                       foreground=theme['fg'],
                       bordercolor=theme['border'],
                       lightcolor=theme['border'],
                       darkcolor=theme['border'])
        
        # Configure labelframe styles
        style.configure('TLabelFrame', 
                       background=theme['secondary'],
                       foreground=theme['accent'],
                       bordercolor=theme['border'],
                       lightcolor=theme['border'],
                       darkcolor=theme['border'])
        style.configure('TLabelFrame.Label', 
                       background=theme['secondary'],
                       foreground=theme['accent'],
                       font=('Arial', 11, 'bold'))
        
        # Configure scrollbar
        style.configure('Vertical.TScrollbar', 
                       background=theme['secondary'],
                       troughcolor=theme['bg'],
                       bordercolor=theme['border'],
                       arrowcolor=theme['accent'])
        
        # Configure progressbar
        style.configure('Horizontal.TProgressbar',
                       background=theme['accent'],
                       troughcolor=theme['secondary'],
                       bordercolor=theme['border'])
        
        # Update all widgets with new colors
        widgets = [
            (self.header_label, theme['accent']),
            (self.subheader_label, theme['text_muted']),
            (self.creator_label, theme['text_muted']),
            (self.phishing_label, theme['fg']),
            (self.custom_domain_label, theme['fg']),
            (self.keywords_label, theme['fg']),
            (self.custom_domain_note, theme['text_muted']),
            (self.keywords_note, theme['text_muted']),
            (self.progress_label, theme['fg']),
            (self.status_label, theme['fg']),
            (self.footer_label, theme['accent'])
        ]
        
        for widget, color in widgets:
            widget.configure(foreground=color)
        
        # Update result labels and status
        for key in self.shortener_labels:
            if key in self.shortener_results:
                self.shortener_labels[key].configure(foreground=theme['success'])
            else:
                self.shortener_labels[key].configure(foreground=theme['text_muted'])
            
            # Update status colors
            current_status = self.shortener_status[key].cget('text')
            if '✅' in current_status:
                self.shortener_status[key].configure(foreground=theme['success'])
            elif '❌' in current_status:
                self.shortener_status[key].configure(foreground=theme['error'])
            elif '🔄' in current_status:
                self.shortener_status[key].configure(foreground=theme['warning'])
            else:
                self.shortener_status[key].configure(foreground=theme['text_muted'])
    
    def initialize_shortener_frames(self):
        """Initialize frames for all shortener services"""
        shorteners = [
            ("TinyURL", "tinyurl", "🔗"),
            ("Is.gd", "isgd", "⚡"),
            ("V.gd", "vgd", "🚀"), 
            ("Da.gd", "dagd", "🔒"),
            ("Osdb", "osdb", "🌐"),
            ("T1p", "t1p", "📎"),
            ("Shorturl", "shorturl", "✂️"),
            ("U0", "u0", "🔐")
        ]
        
        # Create a grid for better organization
        grid_frame = ttk.Frame(self.results_frame, style='Card.TFrame')
        grid_frame.pack(fill='both', expand=True, padx=15, pady=15)
        
        for i, (name, key, icon) in enumerate(shorteners):
            row = i // 2  # 2 columns
            col = i % 2
            
            frame = ttk.LabelFrame(grid_frame, text=f" {icon} {name}", padding="15")
            frame.grid(row=row, column=col, padx=10, pady=8, sticky='nsew')
            frame.columnconfigure(0, weight=1)
            
            # Status label
            status_label = ttk.Label(frame, text="⏳ Waiting...", font=('Arial', 9))
            status_label.grid(row=0, column=0, sticky='w', pady=(0, 10))
            
            # Result label with attractive styling
            result_label = ttk.Label(frame, text="", wraplength=400, justify='left', 
                                   font=('Consolas', 9), background=self.current_theme['card_bg'],
                                   relief='solid', borderwidth=1, padding=10)
            result_label.grid(row=1, column=0, sticky='ew', pady=8)
            
            # Copy button with attractive styling
            btn = ttk.Button(frame, text="📋 COPY URL", 
                           command=lambda k=key: self.copy_shortener_result(k),
                           width=15)
            btn.grid(row=2, column=0, pady=8)
            btn.config(state='disabled')
            
            # Store references
            self.shortener_buttons[key] = btn
            self.shortener_labels[key] = result_label
            self.shortener_status[key] = status_label
        
        # Configure grid weights
        grid_frame.columnconfigure(0, weight=1)
        grid_frame.columnconfigure(1, weight=1)
        for i in range((len(shorteners) + 1) // 2):
            grid_frame.rowconfigure(i, weight=1)

    # ... (keep all the other methods exactly the same as before - validate_phishing_url, generate_all_masked_links, etc.)
    # The rest of your methods remain unchanged - just copy them from your previous code

    def validate_phishing_url(self, url):
        """Validate the phishing URL"""
        if not url:
            return False, "Target URL cannot be empty"
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        if not validators.url(url):
            return False, "Invalid URL format"
            
        return True, url
    
    def validate_custom_domain(self, domain):
        """Validate custom domain"""
        if not domain:
            return False, "Custom domain is required"
            
        # Remove http/https if present
        domain = domain.replace('https://', '').replace('http://', '').split('/')[0]
        
        if '.' not in domain:
            return False, "Invalid domain format. Use: gmail.com, facebook.com, etc."
            
        return True, domain
    
    def generate_all_masked_links(self):
        """Generate masked links using all services"""
        threading.Thread(target=self._generate_all_links_thread, daemon=True).start()
    
    def _generate_all_links_thread(self):
        """Thread function for generating all masked links"""
        try:
            self.update_status("🔄 Validating inputs...", "info")
            self.progress.start()
            self.generate_btn.config(state='disabled')
            
            # Get input values
            phishing_url = self.phishing_entry.get().strip()
            custom_domain = self.custom_domain_entry.get().strip()
            keywords = self.keywords_entry.get().strip()
            
            # Validate phishing URL
            is_valid, url_result = self.validate_phishing_url(phishing_url)
            if not is_valid:
                self.update_status(f"❌ Error: {url_result}", "error")
                messagebox.showerror("Validation Error", url_result)
                return
                
            phishing_url = url_result
            
            # Validate custom domain
            is_valid, domain_result = self.validate_custom_domain(custom_domain)
            if not is_valid:
                self.update_status(f"❌ Error: {domain_result}", "error")
                messagebox.showerror("Validation Error", domain_result)
                return
                
            custom_domain = domain_result
            
            # Validate keywords
            if not keywords:
                keywords = "login-verify-security"
            else:
                # Clean keywords
                keywords = '-'.join(k.strip().lower() for k in keywords.split(','))
                keywords = ''.join(c for c in keywords if c.isalnum() or c == '-')
            
            self.update_status("🚀 Generating masked URLs with all services...", "info")
            
            # Reset all shortener results
            self.shortener_results = {}
            for key in self.shortener_buttons.keys():
                self.shortener_buttons[key].config(state='disabled')
                self.shortener_labels[key].config(text="")
                self.shortener_status[key].config(text="⏳ Waiting...", foreground=self.current_theme['text_muted'])
            
            # Generate with all services
            services = [
                ("TinyURL", "tinyurl", self.shorten_tinyurl),
                ("Is.gd", "isgd", self.shorten_isgd),
                ("V.gd", "vgd", self.shorten_vgd),
                ("Da.gd", "dagd", self.shorten_dagd),
                ("Osdb", "osdb", self.shorten_osdb),
                ("T1p", "t1p", self.shorten_t1p),
                ("Shorturl", "shorturl", self.shorten_shorturl),
                ("U0", "u0", self.shorten_u0)
            ]
            
            for name, key, shortener_func in services:
                self.progress_label.config(text=f"Processing {name}...")
                self.update_shortener_status(key, "🔄 Processing...", "info")
                
                try:
                    # First shorten the URL
                    shortened_url = shortener_func(phishing_url)
                    if shortened_url:
                        # Create masked URL in the correct format
                        masked_url = self.create_masked_url(shortened_url, custom_domain, keywords, key)
                        self.shortener_results[key] = masked_url
                        self.shortener_labels[key].config(text=masked_url)
                        self.shortener_buttons[key].config(state='normal')
                        self.update_shortener_status(key, "✅ Success", "success")
                        # Update color for success
                        self.shortener_labels[key].configure(foreground=self.current_theme['success'])
                    else:
                        self.update_shortener_status(key, "❌ Failed", "error")
                        self.shortener_labels[key].config(text="Service unavailable")
                        self.shortener_labels[key].configure(foreground=self.current_theme['error'])
                except Exception as e:
                    self.update_shortener_status(key, f"❌ Error", "error")
                    self.shortener_labels[key].config(text=f"Error: {str(e)}")
                    self.shortener_labels[key].configure(foreground=self.current_theme['error'])
                
                time.sleep(1)  # Rate limiting
            
            self.progress.stop()
            self.generate_btn.config(state='normal')
            self.update_status("✅ All masked URLs generated successfully!", "success")
            self.progress_label.config(text="Generation completed!")
            
        except Exception as e:
            self.progress.stop()
            self.generate_btn.config(state='normal')
            self.update_status(f"❌ Error: {str(e)}", "error")
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
    
    def create_masked_url(self, shortened_url, custom_domain, keywords, service):
        """Create masked URL in the correct format"""
        # Extract the actual short code from the shortened URL
        if service == "tinyurl" and 'tinyurl.com/' in shortened_url:
            short_code = shortened_url.split('tinyurl.com/')[-1]
            return f"https://{custom_domain}-{keywords}@tinyurl.com/{short_code}"
        elif service == "isgd" and 'is.gd/' in shortened_url:
            short_code = shortened_url.split('is.gd/')[-1]
            return f"https://{custom_domain}-{keywords}@is.gd/{short_code}"
        elif service == "vgd" and 'v.gd/' in shortened_url:
            short_code = shortened_url.split('v.gd/')[-1]
            return f"https://{custom_domain}-{keywords}@v.gd/{short_code}"
        elif service == "dagd" and 'da.gd/' in shortened_url:
            short_code = shortened_url.split('da.gd/')[-1]
            return f"https://{custom_domain}-{keywords}@da.gd/{short_code}"
        elif service == "osdb" and 'osdb.link/' in shortened_url:
            short_code = shortened_url.split('osdb.link/')[-1]
            return f"https://{custom_domain}-{keywords}@osdb.link/{short_code}"
        elif service == "t1p" and 't1p.de/' in shortened_url:
            short_code = shortened_url.split('t1p.de/')[-1]
            return f"https://{custom_domain}-{keywords}@t1p.de/{short_code}"
        elif service == "shorturl" and 'shorturl.at/' in shortened_url:
            short_code = shortened_url.split('shorturl.at/')[-1]
            return f"https://{custom_domain}-{keywords}@shorturl.at/{short_code}"
        elif service == "u0" and 'u0.lt/' in shortened_url:
            short_code = shortened_url.split('u0.lt/')[-1]
            return f"https://{custom_domain}-{keywords}@u0.lt/{short_code}"
        else:
            # Fallback - use basic format
            return f"https://{custom_domain}-{keywords}@masked.url/redirect"
    
    # WORKING URL SHORTENER FUNCTIONS
    
    def shorten_tinyurl(self, url):
        """Shorten URL using TinyURL"""
        try:
            api_url = f"https://tinyurl.com/api-create.php?url={quote(url)}"
            response = requests.get(api_url, timeout=10)
            if response.status_code == 200 and response.text.startswith('http'):
                return response.text
            return None
        except:
            return None
    
    def shorten_isgd(self, url):
        """Shorten URL using Is.gd"""
        try:
            api_url = f"https://is.gd/create.php?format=simple&url={quote(url)}"
            response = requests.get(api_url, timeout=10)
            if response.status_code == 200 and response.text.startswith('http'):
                return response.text.strip()
            return None
        except:
            return None
    
    def shorten_vgd(self, url):
        """Shorten URL using V.gd"""
        try:
            api_url = f"https://v.gd/create.php?format=simple&url={quote(url)}"
            response = requests.get(api_url, timeout=10)
            if response.status_code == 200 and response.text.startswith('http'):
                return response.text.strip()
            return None
        except:
            return None
    
    def shorten_dagd(self, url):
        """Shorten URL using Da.gd"""
        try:
            api_url = "https://da.gd/s"
            payload = {"url": url}
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.post(api_url, data=payload, headers=headers, timeout=10)
            if response.status_code == 200 and response.text.startswith('http'):
                return response.text.strip()
            return None
        except:
            return None
    
    def shorten_osdb(self, url):
        """Shorten URL using Osdb.link"""
        try:
            api_url = "https://osdb.link/"
            payload = {"url": url}
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.post(api_url, data=payload, headers=headers, timeout=10)
            if response.status_code == 200 and response.text.startswith('http'):
                return response.text.strip()
            return None
        except:
            return None
    
    def shorten_t1p(self, url):
        """Shorten URL using T1p.de"""
        try:
            api_url = "https://t1p.de/api/urls"
            payload = {"url": url}
            headers = {'Content-Type': 'application/json'}
            response = requests.post(api_url, json=payload, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('short_url')
            return None
        except:
            return None
    
    def shorten_shorturl(self, url):
        """Shorten URL using Shorturl.at"""
        try:
            api_url = "https://shorturl.at/shortener.php"
            payload = {"u": url}
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.post(api_url, data=payload, headers=headers, timeout=10)
            if response.status_code == 200 and 'shorturl.at/' in response.text:
                # Extract the shortened URL from response
                return f"https://shorturl.at/{response.text.split('shorturl.at/')[-1].split('"')[0]}"
            return None
        except:
            return None
    
    def shorten_u0(self, url):
        """Shorten URL using U0.lt"""
        try:
            api_url = "https://u0.lt/api/urls"
            payload = {"url": url}
            headers = {'Content-Type': 'application/json'}
            response = requests.post(api_url, json=payload, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('short_url')
            return None
        except:
            return None
    
    def update_shortener_status(self, service, status, status_type="info"):
        """Update status for individual shortener service"""
        colors = {
            "info": self.current_theme['warning'],
            "success": self.current_theme['success'],
            "error": self.current_theme['error'],
            "warning": self.current_theme['warning']
        }
        color = colors.get(status_type, self.current_theme['text_muted'])
        self.shortener_status[service].config(text=status, foreground=color)
    
    def copy_shortener_result(self, service):
        """Copy specific shortener result to clipboard"""
        if service in self.shortener_results:
            result = self.shortener_results[service]
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            self.update_status(f"✅ {service.upper()} masked URL copied to clipboard!", "success")
            
            # Show temporary confirmation
            original_text = self.shortener_buttons[service].cget('text')
            self.shortener_buttons[service].config(text='✅ COPIED!')
            self.root.after(2000, lambda: self.shortener_buttons[service].config(text='📋 COPY URL'))
        else:
            messagebox.showwarning("Warning", "No result available to copy!")
    
    def clear_all(self):
        """Clear all input fields and results"""
        self.phishing_entry.delete(0, tk.END)
        self.custom_domain_entry.delete(0, tk.END)
        self.keywords_entry.delete(0, tk.END)
        
        # Clear all shortener results
        for key in self.shortener_buttons.keys():
            self.shortener_buttons[key].config(state='disabled')
            self.shortener_labels[key].config(text="")
            self.shortener_status[key].config(text="⏳ Waiting...", foreground=self.current_theme['text_muted'])
            self.shortener_labels[key].configure(foreground=self.current_theme['text_muted'])
        
        self.shortener_results = {}
        self.progress.stop()
        self.update_status("✅ All fields cleared. Ready to generate new URLs.", "success")
        self.progress_label.config(text="Ready to generate masked URLs...")
    
    def visit_website(self):
        """Visit J Project Platform website"""
        webbrowser.open("https://jprojectplatform.com")
    
    def update_status(self, message, status_type="info"):
        """Update status label with color coding"""
        colors = {
            "info": self.current_theme['warning'],
            "success": self.current_theme['success'],
            "error": self.current_theme['error'],
            "warning": self.current_theme['warning']
        }
        color = colors.get(status_type, self.current_theme['text_muted'])
        self.status_label.configure(text=message, foreground=color)

def main():
    root = tk.Tk()
    app = JMaskedLink(root)
    root.mainloop()

if __name__ == "__main__":
    main()