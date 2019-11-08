import numpy as np
from pyevtk.hl import pointsToVTK, gridToVTK

def save_poits_to_vtk(df, xcol, ycol, zcol, flname):

    df = df.copy()

    x = np.array(df[xcol])
    y = np.array(df[ycol])
    z = np.array(df[zcol])
    
    dataframe_vars = list(df.drop(columns=[xcol,ycol,zcol])) 
    vardict = {}
    for var in dataframe_vars:
        vardict[var] = df[var].values

    pointsToVTK(flname, x, y, z, data=vardict)

def save_grids_to_vtk(df, grid, flname):

    df = df.copy()

    X = np.array([(grid['ox'] - grid['sx']/2 + x * grid['sx']) for x in range(grid['nx']+1)])
    Y = np.array([(grid['oy'] - grid['sy']/2 + x * grid['sy']) for x in range(grid['ny']+1)])
    Z = np.array([(grid['oz'] - grid['sz']/2 + x * grid['sz']) for x in range(grid['nz']+1)])

    dataframe_vars = df.columns
    vardict = {}
    for var in dataframe_vars:
        vardict[var] = df[var].values
        
    gridToVTK(flname, X, Y, Z, cellData=vardict)