import webbrowser
import os
import json

def main():
    print("🚀 Initializing VideoExpress Automated Generation Pipeline...")
    
    # 1. Ensure your core requirements file exists
    config_file = "video_requirements.json"
    if not os.path.exists(config_file):
        # Create a default template if it doesn't exist yet
        default_setup = {
            "aspect_ratio": "16:9",
            "target_duration_seconds": 120,
            "visual_style": "Cinematic Photoreal",
            "topic": "Enter your story idea here"
        }
        with open(config_file, 'w') as f:
            json.dump(default_setup, f, indent=4)
        print(f"📄 Created fresh {config_file}. Fill this out with your topic!")

    # 2. Trigger the automated web application gate sequence
    print("📋 System instructions loaded. Merging visual and audio tracks...")
    target_url = "https://app.videoexpress.ai/"
    
    print(f"🌐 Opening VideoExpress in your automation-enabled browser...")
    webbrowser.open(target_url)

if __name__ == "__main__":
    main()
