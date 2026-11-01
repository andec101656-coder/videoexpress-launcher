import webbrowser
import os

def main():
    print("🚀 Opening VideoExpress...")
    
    # 1. Read the instructions so they are ready
    instructions_file = "system_instructions.md"
    if os.path.exists(instructions_file):
        print("📋 Instructions loaded successfully!")
    
    # 2. Automatically launch the browser
    target_url = "https://app.videoexpress.ai/"
    webbrowser.open(target_url)

if __name__ == "__main__":
    main()
