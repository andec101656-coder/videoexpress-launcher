import webbrowser
import os
import json

def main():
    print("🚀 Initializing VideoExpress Automated Generation Pipeline...")
    
    # 1. Ensure your core requirements file exists
    config_file = "video_requirements.json"
    if not os.path.exists(config_file):
        # Create your new, expanded default layout with options
        default_setup = {
            "1_SELECT_ASPECT_RATIO": "16:9",
            "AVAILABLE_ASPECT_RATIOS": ["16:9", "9:16", "1:1", "--ar 2.39:1"],

            "2_SET_TARGET_DURATION": "2 Minutes",
            "AVAILABLE_DURATIONS": ["2 Minutes (15 scenes)", "3 Minutes (22 scenes)", "5 Minutes (37 scenes)"],

            "3_CHOOSE_VISUAL_TYPE": "Human / Photorealistic",
            "AVAILABLE_VISUAL_TYPES": ["Human / Photorealistic", "2D Animation (1990s Anime)", "3D Animation (Pixar CGI)"],

            "4_YOUR_CREATIVE_CONCEPT": "Enter your story, setting, and character descriptions here."
        }
        
        # Save it nicely spaced out so it's easy to read in Notepad
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(default_setup, f, indent=4)
        print(f"📄 Created fresh {config_file} with selection layouts!")

    # 2. Trigger the automated web application gate sequence
    print("📋 System instructions loaded. Merging visual and audio tracks...")
    target_url = "https://app.videoexpress.ai/"
    
    print(f"🌐 Opening VideoExpress in your automation-enabled browser...")
    webbrowser.open(target_url)

if __name__ == "__main__":
    main()
