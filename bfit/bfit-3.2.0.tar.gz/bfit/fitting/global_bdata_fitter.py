# Fit set of run combined asymmetry globally 
# Derek Fujimoto
# Nov 2018

from bfit.fitting.global_fitter import global_fitter
import bdata as bd
import numpy as np
import collections

# =========================================================================== #
class global_bdata_fitter(global_fitter):
    
    # ======================================================================= #
    def __init__(self,data,fn,shared,xlims=None,rebin=1,asym_mode='c',fixed=None):
        """
            data:       list of bdata objects
            
            fn:         list of function handles to fit (or single which applies to all)
                        must specify inputs explicitly (do not do def fn(*par)!)
                        must have len(fn) = len(runs) if list
                        
            shared:     list of bool to indicate which parameters are shared. 
                        True if shared
                        len = number of parameters.
                        
            xlims:      list of 2-tuples for (low,high) bounds on fitting range 
                            based on x values. If list is not depth 2, use this 
                            range on all runs.
            
            rebin:      rebinning factor on fitting and drawing data
            
            fixed:      list of booleans indicating if the paramter is to be 
                        fixed to p0 value (same length as p0). Returns best 
                        parameters in order presented, with the fixed 
                        parameters omitted.
            
            asym_mode:  asymmetry type to calculate and fit
        """
        
        # check input type
        if type(data) in (bd.bdata,bd.bjoined):
            data = [data]
        ndata = len(data)
        
        # Set rebin
        if not isinstance(rebin,collections.Iterable):
            rebin = [rebin]*ndata
        
        # Get asymmetry
        asym = np.asarray([d.asym(asym_mode,rebin=re) for d,re in zip(data,rebin)])
        
        # split into x,y,dy data sets
        x = asym[:,0]
        y = asym[:,1]
        dy = asym[:,2]
        
        # select subrange
        if xlims is not None:
            
            # check depth
            if len(np.array(xlims).shape) < 2:
                xlims = [xlims]*ndata
                            
            # initialize new inputs
            xnew = []
            ynew = []
            dynew = []
            
            # select subrange
            for i,xl in enumerate(xlims):
                tag = (xl[0]<x[i])*(x[i]<xl[1])
                xnew.append(x[i][tag])
                ynew.append(y[i][tag])
                dynew.append(dy[i][tag])
            
            # new arrays
            x = np.array(xnew)
            y = np.array(ynew)
            dy = np.array(dynew)
            
        # intialize
        super(global_bdata_fitter,self).__init__(x,y,dy,fn,shared,fixed)
