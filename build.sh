# Clean anything left by previous build
rm -rf build/AsciiTextWall/
rm -rf build/AsciiTextWall/res

# Setup dir
mkdir build/AsciiTextWall

# Build as a standalone executable
python -m nuitka --mode=onefile --no-deployment-flag=self-execution --product-name=AsciiTextWall --output-filename=AsciiTextWall main.py

# Move build and resources into the executable directory
mv AsciiTextWall build/AsciiTextWall/AsciiTextWall
cp -r res build/AsciiTextWall/

# Final Clean up
rm -rf main.build
rm -rf main.dist
rm -rf main.onefile-build