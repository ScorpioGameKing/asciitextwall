# ---------------------------------------
# The following is am example automation
# script to for creating and setting the 
# generated image to a waypaper wallpaper
# - Scorpio
# ---------------------------------------
python main.py -t "Just Another $(date +%A)" -f "cosmic" -s 30 -w 100 -c "#ebdbb2" -b "#282828" -n 'test_name.png' -o '~/Pictures/Backgrounds/Static/Asciiwall/'
waypaper --wallpaper './test_name.png'