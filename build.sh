# Clean anything left by previous build
rm -rf build/AsciiTextWall/

# Setup dir
mkdir build/AsciiTextWall

# Build as a standalone executable
python -m nuitka --mode=onefile --output-filename=AsciiTextWall --no-deployment-flag=self-execution --python-flag=no_asserts --python-flag=no_docstrings --python-flag=no_site main.py

# Move build and resources into the executable directory
mv AsciiTextWall build/AsciiTextWall/AsciiTextWall

# Final Clean up
rm -rf main.build
rm -rf main.dist
rm -rf main.onefile-build