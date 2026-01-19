import{b as n,o as r,w as i,g as t,v as d,x as p,C as s}from"./modules/vue-BjKabnyV.js";import{I as l}from"./slidev/center-vDeyfPKN.js";import{u as c,f as _}from"./slidev/context-Chpw6kDm.js";import{_ as u}from"./index-0ZbdpQjY.js";import"./modules/shiki-oSsGfnBi.js";const f={__name:"slides.md__slidev_33",setup(m){const{$clicksContext:a,$frontmatter:o}=c();return a.setup(),(v,e)=>(r(),n(l,d(p(s(_)(s(o),32))),{default:i(()=>[...e[0]||(e[0]=[t("div",{class:"absolute inset-0 bg-gradient-to-bl from-purple-950/50 via-transparent to-fuchsia-950/40"},null,-1),t("h1",null,"PSF Fitting: Implementation",-1),t("div",{class:"relative flex flex-col justify-evenly h-96 mt-8"},[t("div",{class:"card-psfcode"},[t("span",{class:"dot-psfcode"}),t("div",{class:"flex-1"},[t("div",{class:"mt-2 bg-gray-900/50 rounded px-4 py-2 font-mono text-base"},[t("pre",{class:"text-gray-100"},`def gaussian_2d(coords, x0, y0, A, sigma, b):
    x, y = coords
    return b + A * np.exp(-((x-x0)**2 + (y-y0)**2) / (2*sigma**2))
 
# Flatten 2D data for curve_fit
x_grid, y_grid = np.meshgrid(np.arange(cutout.shape[1]),
                              np.arange(cutout.shape[0]))
coords = np.vstack([x_grid.ravel() + x_min, y_grid.ravel() + y_min])
data_flat = cutout.ravel()
 
# Initial guess and fit (use peak detection position directly)
p0 = [x_detected, y_detected, peak_value, psf_sigma, 0.0]
popt, pcov = curve_fit(gaussian_2d, coords, data_flat, p0=p0)
`)])])])],-1),t("div",{class:"slide-number"},"32",-1)])]),_:1},16))}},k=u(f,[["__scopeId","data-v-6816d3c6"]]);export{k as default};
