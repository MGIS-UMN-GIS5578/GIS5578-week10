def argument_parser():
    """   return arguments   """
    import argparse
    parser = argparse.ArgumentParser(description= "A function for buffering shapefiles")    
    parser.add_argument("--infile", required =True, help="The full path for the infile", dest="infile")    
    parser.add_argument("--distance", required =True, help="Buffer distance in units", dest="distance")    
    parser.add_argument("--units", required =True, help="Distance unit", dest="units")    
    parser.add_argument("--outfile", required =True, help="The full path for the outfile", dest="outfile")
    
    return parser

def main(inShapefile, dist, units, outShapefile):
    import arcpy
    distance_with_unit = "%s %s" % (dist, units)
    arcpy.Buffer_analysis(inShapefile, outShapefile, distance_with_unit, "FULL", "ROUND", "LIST")


if __name__ == '__main__':
    args = argument_parser().parse_args()
    main(args.infile, args.distance, args.units, args.outfile)
