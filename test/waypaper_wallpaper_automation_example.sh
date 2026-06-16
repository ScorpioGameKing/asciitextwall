# ---------------------------------------
# The following is am example automation
# script to for creating and setting the 
# generated image to a waypaper wallpaper
# ---------------------------------------
python main.py -t "Just Another $(date +%A)" -f "random" -s 30 -w 100 -c "#ebdbb2" -b "#282828" -n 'day_of_week.png' -o '~/Pictures/Backgrounds/Static/Asciiwall/' -mf '/usr/share/fonts/TTF/AgaveNerdFontMono-Regular.ttf'
waypaper --wallpaper './day_of_week.png'