# Fit list of bdata objects with function list
# Derek Fujimoto
# Nov 2018

import collections
import numpy as np
from bdata import bdata
from scipy.optimize import curve_fit
from tqdm import tqdm
from bfit.fitting.global_bdata_fitter import global_bdata_fitter

# ========================================================================== #
def fit_bdata(data,fn,omit=None,rebin=None,shared=None,hist_select='',
              xlims=None,asym_mode='c',fixed=None,**kwargs):
    """
        Fit combined asymetry from bdata.
    
        data:           list of bdata objects (or single object)    
    
        fn:             list of function handles to fit (or single which applies to all)
                        must specify inputs explicitly (do not do def fn(*par)!)
                        must have len(fn) = len(runs) if list
        
        omit:           list of strings of space-separated bin ranges to omit
        rebin:          list of rebinning of data prior to fitting. 
        
        shared:      list of bool to indicate which parameters are shared. 
                        True if shared
                        len = number of parameters.
        
        npar:           number of free parameters in each fitting function.
                        Set if number of parameters is not intuitable from 
                            function code.      
        
        hist_select:    string for selecting histograms to use in asym calc
        
        xlims:          list of 2-tuple for (low,high) bounds on fitting range 
                            based on x values
        
        asym_mode:      input for asymmetry calculation type 
                            c: combined helicity
                            h: split helicity
                            
                        For 2e mode, prefix with:
                            sl_: combined timebins using slopes
                            dif_: combined timebins using differences
                            raw_: raw time-resolved 
                            
                            ex: sl_c or raw_h or dif_c
        
        fixed:          list of booleans indicating if the paramter is to be 
                        fixed to p0 value (same length as p0). Returns best 
                        parameters in order presented, with the fixed 
                        parameters omitted. Can be a list of lists with one list 
                        for each run.
        
        kwargs:         keyword arguments for curve_fit. See curve_fit docs. 
        
        Returns: (par,std,cov,chi,gchi)
            par: array of best fit parameters
            std: array of best fit errors
            cov: 2D array, covariance matrix
            chi: array of chisquare of each fit
            gchi:global chisquared of fits
    """
    try:
        ndata = len(data)
    except TypeError:
        data = [data]
        ndata = 1
    
    # get fn
    if not isinstance(fn,collections.Iterable):
        fn = [fn]
    fn.extend([fn[-1] for i in range(ndata-len(fn))])
    
    # get number of parameters
    try:
        npar = len(kwargs['p0'])
    except KeyError:
        npar = fn[0].__code__.co_argcount-1
        kwargs['p0'] = np.ones(npar)
        if not npar: 
            raise RuntimeError('Unknown number of function arguments. '+\
                               'Define p0 to resolve.') from None
                               
    # get shared
    if shared is None:
        shared = np.zeros(npar,dtype=bool)

    # get omit
    if omit is None:
        omit = ['']*ndata
    elif len(omit) < ndata:
        omit = np.concatenate((omit,['']*(ndata-len(omit))))
        
    # get rebin
    if rebin is None:
        rebin = np.ones(ndata)
    elif type(rebin) is int:
        rebin = np.ones(ndata)*rebin
    elif len(rebin) < ndata:
        rebin = np.concatenate((rebin,np.ones(ndata-len(rebin))))
    rebin = np.asarray(rebin).astype(int)
        
    # fit globally -----------------------------------------------------------
    if any(shared) and ndata>1:
        print('Running shared parameter fitting...')
        g = global_bdata_fitter(data,fn,shared,xlims,
                                asym_mode=asym_mode,rebin=rebin,fixed=fixed)
        g.fit(**kwargs)
        gchi,chis = g.get_chi() # returns global chi, individual chi
        pars,covs,stds = g.get_par()
        
    # fit runs individually --------------------------------------------------
    else:
        
        # get bounds
        if 'bounds' in kwargs.keys():
            bounds = kwargs['bounds']
            del kwargs['bounds']
        else:
            bounds = [(-np.inf,np.inf)]*ndata 
            
        # check p0 dimensionality
        if len(np.asarray(kwargs['p0']).shape) < 2:
            p0 = [kwargs['p0']]*ndata
        else:
            p0 = kwargs['p0']
        
        # check xlims shape - should match number of runs
        if xlims is None:
            xlims = [None]*ndata
        elif len(np.asarray(xlims).shape) < 2:
            xlims = [xlims for i in range(ndata)]
        else:
            xlims = list(xlims)
            xlims.extend([xlims[-1] for i in range(ndata-len(xlims))])
        
        # check fixed shape
        if fixed is not None: 
            fixed = np.asarray(fixed)
            if len(fixed.shape) < 2:
                fixed = [fixed]*ndata
        else:
            fixed = [[False]*npar]*ndata
        
        pars = []
        covs = []
        chis = []
        stds = []
        gchi = 0.
        dof = 0.
        
        iter_obj = tqdm(zip(data,fn,omit,rebin,p0,bounds,xlims,fixed),
                        total=ndata,desc='Independent Fitting')
        for d,f,om,re,p,b,xl,fix in iter_obj:
            
            # get data for chisq calculations
            x,y,dy = _get_asym(d,asym_mode,rebin=re,omit=om)
            
            # get x limits
            if xl is None:  
                xl = [-np.inf,np.inf]
            else:
                if xl[0] is None: xl[0] = -np.inf
                if xl[1] is None: xl[1] = np.inf
            
            # get good data
            idx = (xl[0]<x)*(x<xl[1])*(dy!=0)
            x = x[idx]
            y = y[idx]
            dy = dy[idx]
            
            # trivial case: all parameters fixed
            if all(fix):
                lenp = len(p)
                s = np.full((lenp,lenp),np.nan)
                c = np.sum(np.square((y-f(x,*p))/dy))/len(y)
                
            # fit with free parameters
            else:            
                kwargs['p0'] = p
                kwargs['bounds'] = b
                p,s,c = _fit_single(d,f,om,re,hist_select,xlim=xl,
                                    asym_mode=asym_mode,fixed=fix,**kwargs)
            # outputs
            pars.append(p)
            covs.append(s)
            chis.append(c)
            stds.append(np.diag(s)**0.5)
            
            # get global chi             
            gchi += np.sum(np.square((y-f(x,*p))/dy))
            dof += len(x)-len(p)
        gchi /= dof
        
    pars = np.asarray(pars)
    covs = np.asarray(covs)
    stds = np.asarray(stds)
    chis = np.asarray(chis)
    
    # single data set fitting
    if ndata == 1:
        pars = pars[0]
        stds = stds[0]
        covs = covs[0]
        chis = chis[0]
    
    return(pars,stds,covs,chis,gchi)

# =========================================================================== #
def _fit_single(data,fn,omit='',rebin=1,hist_select='',xlim=None,asym_mode='c',
               fixed=None,**kwargs):
    """
        Fit combined asymetry from bdata.
    
        data:           bdata object

        fn:             function handle to fit
        
        omit:           string of space-separated bin ranges to omit
        rebin:          rebinning of data prior to fitting. 
        
        hist_select:    string for selecting histograms to use in asym calc
        
        xlim:           2-tuple for (low,high) bounds on fitting range based on 
                            x values
        
        asym_mode:      input for asymmetry calculation type 
                            c: combined helicity
                            h: split helicity
                            
                        For 2e mode, prefix with:
                            sl_: combined timebins using slopes
                            dif_: combined timebins using differences
                            raw_: raw time-resolved
                            
                            ex: sl_c or raw_h or dif_c
        
        fixed:          list of booleans indicating if the paramter is to be 
                        fixed to p0 value (same length as p0). Returns best 
                        parameters in order presented, with the fixed 
                        parameters omitted.
        
        kwargs:         keyword arguments for curve_fit. See curve_fit docs. 
        
        Returns: (par,cov,chi)
            par: best fit parameters
            cov: covariance matrix
            chi: chisquared of fit
    """
    
    # Get data input
    x,y,dy = _get_asym(data,asym_mode,rebin=rebin,omit=omit)
            
    # check for values with error == 0. Omit these values. 
    tag = dy != 0
    x = x[tag]
    y = y[tag]
    dy = dy[tag]
    
    # apply xlimits
    if xlim is not None:
        tag =(xlim[0]<x)*(x<xlim[1])
        x = x[tag]
        y = y[tag]
        dy = dy[tag]
    
    # p0
    if 'p0' not in kwargs:
        nargs = fn.__code__.co_argcount-1
        if not nargs: 
            raise RuntimeError('Unknown number of function arguments. '+\
                               'Define p0 to resolve.')
        kwargs['p0'] = np.ones(nargs)
    
    # fixed parameters
    did_fixed = False
    if fixed is not None and any(fixed):
        
        # save stuff for inflation
        did_fixed = True
        p0 = np.copy(kwargs['p0'])
        npar = len(p0)
        
        # dumb case: all values fixed: 
        if all(fixed):
            cov = np.full((npar,npar),np.nan)
            chi = np.sum(np.square((y-fn(x,*p0))/dy))/len(y)
            return (p0,cov,chi)
        
        # prep inputs
        fixed = np.asarray(fixed)
        if 'bounds' in kwargs:  bounds = kwargs['bounds']
        else:                   bounds = None
        
        # get fixed version
        fn,kwargs['p0'],bounds = _get_fixed_values(fixed,fn,kwargs['p0'],bounds)
        
        # modify fiting inputs
        if bounds is not None:  kwargs['bounds'] = bounds
        
    # Fit the function 
    par,cov = curve_fit(fn,x,y,sigma=dy,absolute_sigma=True,**kwargs)
    dof = len(y)-len(kwargs['p0'])
    
    # get chisquared
    chi = np.sum(np.square((y-fn(x,*par))/dy))/dof
    
    # inflate parameters with fixed values 
    if did_fixed:
        
        # inflate parameters
        par_inflated = np.zeros(npar)
        par_inflated[fixed] = p0[fixed]
        par_inflated[~fixed] = par
        par = par_inflated
        
        # inflate cov matrix with NaN
        nfixed_flat = np.concatenate(np.outer(~fixed,~fixed))
        c_inflated = np.full(npar**2,np.nan)
        c_inflated[nfixed_flat] = np.concatenate(cov)
        cov = c_inflated.reshape(npar,-1)
    
    return (par,cov,chi)
    
# =========================================================================== #
def _get_asym(data,asym_mode,**asym_kwargs):
    """
        Get asymmetry
        
        data = bdata object
        asym_mode: mode as described above
    """
    
    if asym_mode in ('c','p','n','sc','dc','sl_c','dif_c'):
        x,y,dy = data.asym(asym_mode,**asym_kwargs)
    elif asym_mode in ('h','sh','dh','sl_h','dif_h'):
        raise RuntimeError('Split helicity fitting not yet implemented')
    elif 'raw' in asym_mode:
        raise RuntimeError('2e Time-resolved fitting not yet implemented')

    return (x,y,dy)
    
# =========================================================================== #
def _get_fixed_values(fixed,fn,p0,bounds=None):
    """
        Get fixed function, p0, bounds
    """
    
    # save original inputs
    fn_orig = fn
    p0_orig = np.copy(p0)
    npar_orig = len(p0_orig)
            
    # index of fixed parameters
    idx = np.where(fixed)
    
    # make new fitting function with fixed parameter(s)
    def fn(x,*args):
        args_fixed = np.zeros(npar_orig)
        args_fixed[fixed] = p0_orig[fixed]
        args_fixed[~fixed] = args
        return fn_orig(x,*args_fixed)
    
    # make new p0
    p0 = np.asarray(p0_orig)[~fixed]
    
    # bounds
    if bounds is not None:
        try:
            bounds[0] = np.asarray(bounds[0])[~fixed]
            bounds[1] = np.asarray(bounds[1])[~fixed]
        except IndexError:
            pass
    
    return (fn,p0,bounds)
