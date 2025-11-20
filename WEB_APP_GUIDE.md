# Universe Map Generator - Web App Guide

## Quick Start

1. **Start the server:**
   ```bash
   ./run_webapp.sh
   ```
   Or manually:
   ```bash
   source venv/bin/activate
   python app.py
   ```

2. **Open in browser:**
   - Navigate to: **http://localhost:5000**
   - The page should open automatically

3. **Configure your map:**
   - Set **Columns per universe** (1-50)
   - Set **Rows per universe** (1-50)
   - Set **Horizontal universes** (1-10)
   - Set **Vertical universes** (1-10)

4. **Preview & Generate:**
   - Click **"Preview"** to see the grid dimensions
   - Click **"Generate Excel"** to download your file

## Features

### 🎨 Visual Interface
- Clean, modern design
- Intuitive form controls
- Real-time input validation

### 📊 Live Preview
- See total grid size before generating
- Preview total universes
- Check dimensions before download

### ⬇️ Instant Download
- Generate Excel files on demand
- Custom filename: `universe_map.xlsx`
- No need to save files manually

### 🎯 Smart Defaults
- Pre-filled with sensible defaults
- Based on your last successful configuration
- Easy to adjust on the fly

## How It Works

### Universe Dimensions
- **Columns**: Number of columns in each individual universe (B1, B2, B3, ...)
- **Rows**: Number of rows in each individual universe (1, 2, 3, ...)

### Universe Grid Layout
- **Horizontal**: How many universes to place left-to-right
- **Vertical**: How many universes to place top-to-bottom
- **Total Universes** = Horizontal × Vertical

### Example
If you set:
- Columns per universe: 20
- Rows per universe: 13
- Horizontal universes: 6
- Vertical universes: 6

You get:
- **36 total universes** (6×6)
- **120 data columns** (20×6)
- **78 data rows** (13×6)
- Each universe labeled U1 through U36

## Output File

The generated Excel file includes:
- ✅ Square cells with fixed dimensions
- ✅ Color-coded universes with high contrast
- ✅ Light grey borders on all cells
- ✅ Headers (C1, C2, ... and R1, R2, ...)
- ✅ Cell labels showing row number and universe-column (e.g., "1\nU1-B1")

## Stopping the Server

Press **Ctrl+C** in the terminal to stop the server.

## Troubleshooting

### Port Already in Use
If port 5000 is already taken:
1. Edit `app.py`
2. Change `app.run(debug=True, port=5000)` to another port (e.g., 5001)
3. Restart the server

### Browser Doesn't Open
Manually navigate to: **http://localhost:5000**

### Generation Fails
- Check that all values are within valid ranges (1-50 for dimensions, 1-10 for universe counts)
- Ensure virtual environment is activated
- Check terminal for error messages

## Advanced Usage

### API Endpoints

The web app exposes these endpoints:

#### GET `/`
- Returns the main HTML interface

#### POST `/preview`
- Parameters: `cols`, `rows`, `universes_h`, `universes_v`
- Returns: JSON with preview information

#### POST `/generate`
- Parameters: `cols`, `rows`, `universes_h`, `universes_v`
- Returns: Excel file download

### Customization

Edit `app.py` to:
- Change default values
- Modify color schemes
- Adjust cell dimensions
- Add new features

Edit `templates/index.html` to:
- Change UI design
- Modify form layout
- Add new input fields

## Tips

1. **Start with Preview**: Always preview first to check dimensions
2. **Reasonable Sizes**: Very large grids (e.g., 10×10 universes with 50×50 cells) may be slow to generate
3. **Browser Compatibility**: Works best in Chrome, Firefox, Safari, Edge
4. **Save Configurations**: Take note of settings that work well for your use case

## Future Enhancements

Potential features to add:
- Background image upload through web interface
- Color scheme customization
- Save/load configurations
- Multiple file format exports (CSV, PDF)
- Grid preview visualization
- Preset templates

