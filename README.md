# Universe Map Generator

Generates a spreadsheet map with multiple "universes" arranged in a grid pattern.

## Output Files

- **map.csv** - CSV file for any spreadsheet application
- **map.xlsx** - Excel file with color-coded universes, includes transparent PNG overlay if `floorplan.png` exists

**Overlay Image Support:**
- Place a `floorplan.png` file (PNG with transparent background) in the directory
- The script will automatically add it as an overlay on top of the colored universe grid
- Transparent areas of the PNG allow the colored cells to show through
- Perfect for floorplans, layouts, or any reference image with transparency
- **Tip:** In Apple Numbers, lock the image (Format → Arrange → Lock) to click through it and select cells underneath
- See [NUMBERS_GUIDE.md](NUMBERS_GUIDE.md) for image locking instructions in different apps

## Structure

- **Grid**: 6 × 6 universes (36 total)
- **Each Universe**: 20 columns × 13 rows
- **Total Size**: 120 columns × 78 rows (plus headers)
- **Cell Format**: Three lines per cell
  ```
  N
  U#-B#
  [empty line]
  ```
  - N = Row number within universe (1-13)
  - U# = Universe number (U1-U36)
  - B# = Column number within universe (B1-B20)

## Universe Layout

```
U1   U2   U3   U4   U5   U6
U7   U8   U9   U10  U11  U12
U13  U14  U15  U16  U17  U18
U19  U20  U21  U22  U23  U24
U25  U26  U27  U28  U29  U30
U31  U32  U33  U34  U35  U36
```

**Color Coding** (in `map.xlsx`):
- Each universe has a distinct color strategically chosen to maximize contrast with neighboring universes
- Adjacent universes (horizontally and vertically) have visually different colors for easy identification
- Colors have **20% transparency** (80% opacity) 
- Note: `map_with_background.xlsx` has no cell colors (fully transparent) to show the background image

**Formatting**: 
- All cells are **square-shaped** (50pt height × 7.5 char width) with fixed dimensions for uniform grid appearance
- Light grey borders on all cells for clear visual separation
- Each data cell displays its information on three lines (row number, universe-band designation, and an empty line for spacing)
- Text is sized at 9pt to fit comfortably within the square cells
- Text alignment: **horizontally centered** and **vertically top-aligned** for consistent readability

**PNG Overlay Support**:
- If `floorplan.png` (transparent PNG) exists in the directory, it will be added as an overlay
- The PNG sits on top of the colored cells
- Transparent areas of the PNG allow the colored universe cells to show through
- Works perfectly in Excel, Google Sheets, and Numbers
- You can move/resize the overlay image in any spreadsheet application

## Usage

### Web GUI (Recommended)

Launch the web interface to customize your map visually:

```bash
./run_webapp.sh
```

Then open your browser to: **http://localhost:5000**

Features:
- 🎨 Visual interface for setting dimensions
- 📊 Live preview of grid size
- ⬇️ Direct Excel download
- 🔧 Customize rows, columns, and universe layout

### Command Line

#### Easy Way
```bash
./run.sh
```

#### Manual Way
```bash
# First time setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Generate files
python generate_map.py
```

## Using the Files

### Google Sheets Import

1. Open Google Sheets
2. File → Import → Upload
3. Select `map.xlsx`
4. Import location: "Replace spreadsheet"
5. Each universe will have its own distinct color
6. If you included a `floorplan.png`, it will appear as an overlay

### Apple Numbers (macOS) - Recommended

1. Open `map.xlsx` in Apple Numbers
2. The colored grid and any overlay image will import
3. **To lock the image for click-through:**
   - Select the overlay image
   - Format panel (right side) → Arrange tab
   - Check **"Lock"**
   - Now you can double-click cells underneath without selecting the image!
4. You can move/resize the overlay image before locking it

### Microsoft Excel

1. Open `map.xlsx`
2. The colored universe grid and any PNG overlay will display
3. Right-click the overlay image to move, resize, or adjust it

## Customization

Edit `generate_map.py` to modify:
- `COLS_PER_UNIVERSE` - Columns per universe (default: 20)
- `ROWS_PER_UNIVERSE` - Rows per universe (default: 13)
- `UNIVERSES_HORIZONTAL` - Universes left-to-right (default: 6)
- `UNIVERSES_VERTICAL` - Universes top-to-bottom (default: 6)
- `row_height` and `col_width` - Adjust cell dimensions (default: 50pt height, 7.5 char width for square cells)

