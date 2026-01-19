import{_ as l}from"./slidev/VClicks-DLD94jBU.js";import{b as r,o as u,w as s,g as t,e as m,v as d,x as f,C as o}from"./modules/vue-BjKabnyV.js";import{I as c}from"./slidev/center-mxZQ1lrj.js";import{u as p,f as _}from"./slidev/context-DbcbyBga.js";import{_ as v}from"./index-DayMp4VL.js";import"./modules/shiki-oSsGfnBi.js";const x={class:"relative flex flex-col justify-evenly h-96 mt-4"},g={__name:"slides.md__slidev_36",setup(k){const{$clicksContext:e,$frontmatter:i}=p();return e.setup(),(b,n)=>{const a=l;return u(),r(c,d(f(o(_)(o(i),35))),{default:s(()=>[n[1]||(n[1]=t("div",{class:"absolute inset-0 bg-gradient-to-bl from-stone-950/50 via-transparent to-neutral-900/40"},null,-1)),n[2]||(n[2]=t("h1",null,"Local Continuum Fitting",-1)),t("div",x,[m(a,null,{default:s(()=>[...n[0]||(n[0]=[t("div",{class:"card-locfit"},[t("span",{class:"dot-locfit"}),t("div",{class:"flex-1"},[t("div",{class:"mt-3 bg-gray-900/50 rounded px-4 py-2 font-mono text-sm"},[t("pre",{class:"text-gray-100"},`continuum_mask = np.ones(len(flux), dtype=bool) # Start: all points
 
for iteration in range(3):                      # Iterate
    # Fit linear continuum to current mask
    coeffs = np.polyfit(wavelength[continuum_mask], 
                        flux[continuum_mask], deg=1)
    continuum_fit = np.polyval(coeffs, wavelength)
    # Clip points >2σ below fit (absorption lines)
    residuals = flux - continuum_fit
    residual_std = np.std(residuals[continuum_mask])
    continuum_mask = (residuals > -2.0 * residual_std)
 
flux_normalized = flux / continuum_fit           # Now continuum ≈ 1
`)])])],-1)])]),_:1})]),n[3]||(n[3]=t("div",{class:"slide-number"},"36",-1))]),_:1},16)}}},P=v(g,[["__scopeId","data-v-469ce5dc"]]);export{P as default};
