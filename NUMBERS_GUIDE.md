# Using the Map with PNG Overlay Images

## The Solution: Transparent PNG Overlay

Instead of trying to place an image behind cells (which Excel can't do), we use a **transparent PNG overlay** that sits on top of the colored cells. The transparent areas of the PNG allow the colored universe cells to show through perfectly.

## How It Works

1. Create a PNG image with a transparent background (e.g., `floorplan.png`)
2. Place it in the same directory as the script
3. Run the script - it automatically adds the PNG as an overlay to `map.xlsx`
4. The PNG sits on top, but transparent areas show the colored cells below
5. Works in Excel, Google Sheets, and Numbers!

## Using in Different Applications

### Apple Numbers (macOS)

1. Open `map.xlsx` in Numbers
2. The colored grid and PNG overlay will import automatically
3. To adjust the overlay:
   - Click the overlay image to select it
   - Drag to reposition
   - Use corner handles to resize
   - Use Arrange menu to adjust layer order if needed
4. The colored cells will show through transparent areas of the PNG

### Microsoft Excel

1. Open `map.xlsx`
2. Right-click the overlay image to:
   - Move it
   - Resize it using corner handles
   - Format Picture → adjust transparency if needed
3. The image stays on top but transparent areas show the cells

### Google Sheets

1. Import `map.xlsx` into Google Sheets
2. The overlay image will import
3. Click to select and reposition as needed
4. Colored cells show through transparent areas

## Creating Your Transparent PNG

To create a floorplan overlay with transparency:

1. **Using Photoshop/GIMP/Pixelmator:**
   - Open your floorplan image
   - Delete or erase the background (make it transparent)
   - Save as PNG (PNG supports transparency)
   - Name it `floorplan.png`

2. **Using Preview (macOS):**
   - Open your image in Preview
   - Use Tools → Instant Alpha to remove background
   - Export as PNG

3. **Online Tools:**
   - Use remove.bg or similar tools to remove backgrounds
   - Download as PNG with transparency

## Locking the Image for Click-Through

To allow double-clicking cells underneath the image without selecting the image:

### In Apple Numbers:
1. Select the overlay image
2. Format sidebar → Arrange tab
3. Enable **"Lock"**
4. Now you can click through the image to select cells underneath!

### In Microsoft Excel:
1. Right-click the overlay image
2. Select **"Format Picture"** or **"Size and Properties"**
3. Under **Properties** tab, disable:
   - ☐ "Move and size with cells" (optional)
   - ☐ "Locked" (uncheck if sheet is protected, or...)
4. Alternative: Send image to a different layer
5. Or use Selection Pane (Home → Find & Select → Selection Pane) to hide/show the image

### In Google Sheets:
1. Google Sheets doesn't support image locking the same way
2. Alternative: Right-click image → "Put image behind grid" (if available)
3. Or temporarily hide the image when editing cells

## Tips

- **Positioning**: The overlay is positioned at cell B2 by default. You can move it after opening the file
- **Scaling**: You can resize the overlay to fit your grid perfectly
- **Opacity**: If the overlay is too strong, you can adjust its opacity in the spreadsheet app
- **Best for editing**: Apple Numbers has the best "lock and click-through" functionality

## Export Options

Once configured, you can export as:
- **PDF** - Perfect for printing with all colors and overlay intact
- **Excel/Numbers** - Share with others while preserving formatting
- **CSV** - Export just the data without formatting
- **Images** - Take screenshots or export as PNG/JPG for presentations

