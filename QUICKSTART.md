# Quick Start - Universe Map Generator

## 🚀 Easiest Way (Web GUI)

### Open the Web App

**Option 1:** Double-click `index.html`

**Option 2:** From terminal:
```bash
open index.html
```

**Option 3:** Drag `index.html` into your browser

### That's It!

The web interface will open with:
- **Left Panel**: Compact controls for customizing your map
- **Main Area**: Large visual preview showing the colored universe grid
- Changes update **instantly** as you type!

Features:
- ✅ **Large visual grid preview** - fills the main screen
- ✅ Color-coded universes (easy to see the layout)
- ✅ Live stats (updates as you type)
- ✅ Compact controls on the left
- ✅ Instant Excel generation

No server, no Python, no installation needed!

## 📊 How to Use

1. **Adjust settings** in the form:
   - Columns per universe (1-50)
   - Rows per universe (1-50)  
   - Horizontal universes (1-20)
   - Vertical universes (1-20)

2. **See live preview** updating in real-time

3. **Click "Generate & Download Excel"** to get your file

## 🎯 Example Configurations

### Small Grid (for testing)
- Columns: 10, Rows: 5
- Horizontal: 3, Vertical: 2
- Result: 6 universes, 30×10 grid

### Medium Grid (default)
- Columns: 20, Rows: 10
- Horizontal: 9, Vertical: 5  
- Result: 45 universes, 180×50 grid

### Large Grid (for venues)
- Columns: 20, Rows: 13
- Horizontal: 10, Vertical: 8
- Result: 80 universes, 200×104 grid

## 📁 Generated File

The Excel file includes:
- ✅ Square cells with fixed dimensions
- ✅ Color-coded universes (36+ distinct colors)
- ✅ Light grey borders
- ✅ Headers (C1, C2... and R1, R2...)
- ✅ Cell labels (row number + universe-column ID)

## 💡 Tips

- **Larger numbers = bigger file**: 20×20 universes may take a few seconds
- **Preview updates instantly**: See your grid size before generating
- **All offline**: Works without internet once page is loaded
- **Privacy**: All processing happens in your browser, nothing uploaded

## 🔧 For Advanced Users

If you need command-line generation or want to include overlay images, see the main [README.md](README.md).

