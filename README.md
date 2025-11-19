# Universe Map Generator

Generates a spreadsheet map with multiple "universes" arranged in a grid pattern.

## Output Files

- **map.csv** - CSV file for any spreadsheet application
- **map.xlsx** - Excel file with color-coded universes (ready for Google Sheets import)

## Structure

- **Grid**: 6 × 6 universes (36 total)
- **Each Universe**: 15 columns × 20 rows
- **Total Size**: 90 columns × 120 rows (plus headers)
- **Cell Format**: `NN-U#-B#` (e.g., `01-U1-B1`)
  - NN = Row number within universe (01-20)
  - U# = Universe number (U1-U36)
  - B# = Band number (B1, B2, or B3 - cycles per column)

## Universe Layout

```
U1   U2   U3   U4   U5   U6
U7   U8   U9   U10  U11  U12
U13  U14  U15  U16  U17  U18
U19  U20  U21  U22  U23  U24
U25  U26  U27  U28  U29  U30
U31  U32  U33  U34  U35  U36
```

**Color Coding**: Each universe has a distinct color strategically chosen to maximize contrast with neighboring universes. Adjacent universes (horizontally and vertically) have visually different colors for easy identification.

## Usage

### Easy Way
```bash
./run.sh
```

### Manual Way
```bash
# First time setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Generate files
python generate_map.py
```

## Google Sheets Import

1. Open Google Sheets
2. File → Import → Upload
3. Select `map.xlsx`
4. Import location: "Replace spreadsheet"
5. Each universe will have its own distinct color!

## Customization

Edit `generate_map.py` to modify:
- `COLS_PER_UNIVERSE` - Columns per universe (default: 15)
- `ROWS_PER_UNIVERSE` - Rows per universe (default: 20)
- `UNIVERSES_HORIZONTAL` - Universes left-to-right (default: 6)
- `UNIVERSES_VERTICAL` - Universes top-to-bottom (default: 6)

