#!/usr/bin/env python3
"""
Generate a CSV map with multiple universes arranged in a grid.
Each universe is 15 columns x 20 rows.
"""

import csv

# Configuration
COLS_PER_UNIVERSE = 15
ROWS_PER_UNIVERSE = 20
UNIVERSES_HORIZONTAL = 6  # U1 through U6 (original + 5 to the right)
UNIVERSES_VERTICAL = 6    # 6 rows of universes (original + 5 downward)

def generate_cell_label(row_in_universe, col_in_universe, universe_num):
    """
    Generate a cell label in the format: NN-U#-B#
    row_in_universe: 1-20
    col_in_universe: 0-14
    universe_num: 1-36
    """
    # Row number with zero padding (01-20)
    row_label = f"{row_in_universe:02d}"
    
    # Universe label (U1, U2, etc.)
    universe_label = f"U{universe_num}"
    
    # B label cycles through B1, B2, B3 for each column
    b_num = (col_in_universe % 3) + 1
    b_label = f"B{b_num}"
    
    return f"{row_label}-{universe_label}-{b_label}"

def generate_map():
    """Generate the complete map with all universes."""
    total_rows = ROWS_PER_UNIVERSE * UNIVERSES_VERTICAL
    total_cols = COLS_PER_UNIVERSE * UNIVERSES_HORIZONTAL
    
    # Create the grid
    grid = []
    
    # Add header row with column labels (C1, C2, C3, ...)
    header_row = ['']  # Empty cell at top-left corner
    for col_idx in range(total_cols):
        header_row.append(f"C{col_idx + 1}")
    grid.append(header_row)
    
    for row_idx in range(total_rows):
        row_data = []
        
        # Add row label at the beginning (R1, R2, R3, ...)
        row_data.append(f"R{row_idx + 1}")
        
        # Determine which universe row we're in (0-5)
        universe_row = row_idx // ROWS_PER_UNIVERSE
        # Row within the current universe (1-20)
        row_in_universe = (row_idx % ROWS_PER_UNIVERSE) + 1
        
        for col_idx in range(total_cols):
            # Determine which universe column we're in (0-5)
            universe_col = col_idx // COLS_PER_UNIVERSE
            # Column within the current universe (0-14)
            col_in_universe = col_idx % COLS_PER_UNIVERSE
            
            # Calculate universe number (1-36)
            # Universe numbering goes left to right, then top to bottom
            universe_num = (universe_row * UNIVERSES_HORIZONTAL) + universe_col + 1
            
            # Generate the cell label
            cell_label = generate_cell_label(row_in_universe, col_in_universe, universe_num)
            row_data.append(cell_label)
        
        grid.append(row_data)
    
    return grid

def save_to_csv(grid, filename='map.csv'):
    """Save the grid to a CSV file."""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(grid)
    print(f"Generated {filename}")
    print(f"  Total size: {len(grid)} rows x {len(grid[0])} columns (including headers)")
    print(f"  Universes: {UNIVERSES_HORIZONTAL} x {UNIVERSES_VERTICAL} = {UNIVERSES_HORIZONTAL * UNIVERSES_VERTICAL} total")

if __name__ == '__main__':
    grid = generate_map()
    save_to_csv(grid)

