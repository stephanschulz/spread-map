# Web App Technical Notes

## Library Used

The web app uses **xlsx-js-style** - a fork of SheetJS that adds cell styling support.

- **Original SheetJS**: Free version doesn't support cell colors/styles
- **xlsx-js-style**: Community fork that adds styling to the free version
- **CDN**: `https://cdn.jsdelivr.net/npm/xlsx-js-style@1.2.0/dist/xlsx.bundle.js`

## Features Supported

✅ Cell background colors (36+ universe colors)
✅ Cell borders (light grey)  
✅ Text alignment (center horizontal, top vertical)
✅ Wrap text (for line breaks)
✅ Font sizing
✅ Bold headers
✅ Row heights
✅ Column widths

## Cell Format

Each data cell contains:
```
1
U1-B1

```

The line breaks (`\n`) are preserved in the Excel file with `wrapText: true`.

## Color Transparency

Colors are applied with 80% opacity (20% transparency) by blending with white:
- Original color RGB values
- Blended with white background: `rgb * 0.8 + 255 * 0.2`
- Converted back to hex for Excel

## Limitations

- Large grids (20×20 universes) may take 5-10 seconds to generate
- Browser may show "page unresponsive" warning for very large files
- File size grows quickly with many cells
- Styling is applied in JavaScript, not natively by Excel

## Browser Compatibility

Tested and working in:
- ✅ Chrome
- ✅ Safari  
- ✅ Firefox
- ✅ Edge

## Troubleshooting

### Colors Not Showing
- Make sure you're using the latest version of `index.html`
- Check browser console for errors (F12 / Cmd+Option+I)
- Try a smaller grid first (5×3 universes)

### Line Breaks Not Working
- Line breaks should appear automatically with wrapText enabled
- If not visible, manually adjust row height in Excel
- Or select cells and enable "Wrap Text" in Excel

### File Won't Download
- Check if popup blocker is enabled
- Some browsers may ask for download permission
- Try a different browser

## Performance Tips

- **Start small**: Test with 3×2 universes first
- **Increase gradually**: Add more universes as needed
- **Be patient**: Large grids (45+ universes) take time
- **Check preview**: See grid size before generating

