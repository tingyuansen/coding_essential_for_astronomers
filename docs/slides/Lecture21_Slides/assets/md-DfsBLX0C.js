import{_ as p}from"./slidev/VClicks-DLD94jBU.js";import{b as l,o as c,w as o,g as t,e as d,ac as e,v as m,x as _,C as a}from"./modules/vue-BjKabnyV.js";import{I as f}from"./slidev/center-mxZQ1lrj.js";import{u,f as v}from"./slidev/context-DbcbyBga.js";import{_ as g}from"./index-DayMp4VL.js";import"./modules/shiki-oSsGfnBi.js";const x={class:"relative flex flex-col justify-evenly h-96 mt-4"},y={__name:"slides.md__slidev_27",setup(b){const{$clicksContext:n,$frontmatter:r}=u();return n.setup(),(k,s)=>{const i=p;return c(),l(f,m(_(a(v)(a(r),26))),{default:o(()=>[s[1]||(s[1]=t("div",{class:"absolute inset-0 bg-gradient-to-tr from-indigo-950/50 via-transparent to-violet-950/40"},null,-1)),s[2]||(s[2]=t("h1",null,"Fitting with curve_fit",-1)),t("div",x,[d(i,null,{default:o(()=>[...s[0]||(s[0]=[t("div",{class:"card-curvefit"},[t("span",{class:"dot-curvefit"}),t("div",{class:"flex-1"},[t("div",{class:"mt-3 bg-gray-900/50 rounded px-4 py-2 font-mono text-sm"},[t("pre",{class:"text-gray-100"},[e(`from scipy import optimize
 
`),t("span",{class:"text-gray-400"},"# Initial guesses"),e(`
p0 = [1.0, 0.3, 500.0, 0.015, 0.005]       
 
`),t("span",{class:"text-gray-400"},"# Minimize χ²"),e(`
`),t("span",{class:"text-gray-400"},"popt: best-fit parameters"),e(`
popt, pcov = optimize.curve_fit(           
    voigt_line, wavelength, flux_observed, p0=p0, sigma=noise)
 
`),t("span",{class:"text-gray-400"},"# Uncertainties"),e(`
perr = np.sqrt(np.diag(pcov))              `)])])])],-1)])]),_:1})]),s[3]||(s[3]=t("div",{class:"slide-number"},"27",-1))]),_:1},16)}}},P=g(y,[["__scopeId","data-v-5906c42b"]]);export{P as default};
