from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import os
from datetime import datetime
import urllib.request

class OfflineCacheApp(App):
    def build(self):
        # Ensure storage folders and files exist
        if not os.path.exists("cached_videos"):
            os.makedirs("cached_videos")
        if not os.path.exists("cache.txt"):
            with open("cache.txt", "w") as f:
                pass

        # Outer AnchorLayout to center everything perfectly on the mobile screen
        root_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        # Inner vertical container with fixed width/height for clean spacing
        layout = BoxLayout(
            orientation='vertical', 
            padding=20, 
            spacing=15, 
            size_hint=(0.95, None), 
            height=520
        )
        
        # Status / Title Header
        self.status_label = Label(
            text="Offline Internet & Video Cacher", 
            font_size=18, 
            size_hint_y=None, 
            height=50,
            halign='center', 
            valign='middle'
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        layout.add_widget(self.status_label)

        # Text input box for notes, URLs, or media links
        self.user_input = TextInput(
            hint_text="Type note, web URL, or video link...", 
            size_hint_y=None, 
            height=52,
            multiline=False,
            font_size=15
        )
        layout.add_widget(self.user_input)

        # Button 1: Save Note
        btn_note = Button(
            text="Save Custom Note", 
            size_hint_y=None, 
            height=50, 
            background_color=(0.1, 0.6, 0.8, 1),
            font_size=15
        )
        btn_note.bind(on_press=self.save_note_action)
        layout.add_widget(btn_note)

        # Button 2: Download & Cache Web Page
        btn_web = Button(
            text="Cache Web Page (HTML)", 
            size_hint_y=None, 
            height=50, 
            background_color=(0.2, 0.7, 0.3, 1),
            font_size=15
        )
        btn_web.bind(on_press=self.save_web_action)
        layout.add_widget(btn_web)

        # Button 3: Download Video / File
        btn_video = Button(
            text="Download Video/File to Folder", 
            size_hint_y=None, 
            height=50, 
            background_color=(0.9, 0.4, 0.1, 1),
            font_size=15
        )
        btn_video.bind(on_press=self.save_video_action)
        layout.add_widget(btn_video)

        # Button 4: View Cache Status
        btn_read = Button(
            text="View Cache Status", 
            size_hint_y=None, 
            height=50, 
            background_color=(0.5, 0.3, 0.8, 1),
            font_size=15
        )
        btn_read.bind(on_press=self.view_logs_action)
        layout.add_widget(btn_read)

        root_layout.add_widget(layout)
        return root_layout

    def save_note_action(self, instance):
        data = self.user_input.text.strip()
        if data:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("cache.txt", "a") as f:
                f.write(f"[{current_time}] [NOTE] {data}\n")
            self.status_label.text = "Note saved successfully!"
            self.user_input.text = ""
        else:
            self.status_label.text = "Please type something first."

    def save_web_action(self, instance):
        url = self.user_input.text.strip()
        if url:
            self.status_label.text = "Downloading web page..."
            try:
                with urllib.request.urlopen(url, timeout=5) as response:
                    html_text = response.read().decode('utf-8', errors='ignore')
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    page_snippet = html_text[:300].replace("\n", " ")
                    with open("cache.txt", "a") as f:
                        f.write(f"[{current_time}] [WEB CACHE: {url}] {page_snippet}...\n")
                    self.status_label.text = "Web page cached successfully!"
                    self.user_input.text = ""
            except Exception as e:
                self.status_label.text = "Error: Check URL or connection."
        else:
            self.status_label.text = "Please paste a web URL first."

    def save_video_action(self, instance):
        url = self.user_input.text.strip()
        if url:
            self.status_label.text = "Downloading video/file..."
            try:
                # Extract filename or generate a timestamp-based filename
                filename = url.split("/")[-1].split("?")[0]
                if not filename or "." not in filename:
                    filename = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
                
                filepath = os.path.join("cached_videos", filename)
                urllib.request.urlretrieve(url, filepath)
                
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("cache.txt", "a") as f:
                    f.write(f"[{current_time}] [VIDEO CACHE] Saved {filename}\n")
                
                self.status_label.text = f"Saved: {filename}"
                self.user_input.text = ""
            except Exception as e:
                self.status_label.text = "Download failed. Check direct link."
        else:
            self.status_label.text = "Please paste a direct video/file URL."

    def view_logs_action(self, instance):
        try:
            with open("cache.txt", "r") as f:
                content = f.read().strip()
                lines = content.split("\n") if content else []
                video_count = len(os.listdir("cached_videos"))
                if not content and video_count == 0:
                    self.status_label.text = "Cache is currently empty."
                else:
                    self.status_label.text = f"Logs: {len(lines)} items | Videos: {video_count}"
        except FileNotFoundError:
            self.status_label.text = "No cache records found yet."

if __name__ == '__main__':
    OfflineCacheApp().run()
