import{_ as l}from"./slidev/VClicks-Bf7_7t06.js";import{b as d,o as p,w as a,g as t,e as u,ac as e,v as f,x as _,C as n}from"./modules/vue-BjKabnyV.js";import{I as m}from"./slidev/center-BaVTJz7O.js";import{u as c,f as v}from"./slidev/context-CwExy7w2.js";import{_ as g}from"./index-C4hBybjX.js";import"./modules/shiki-oSsGfnBi.js";const x={class:"relative flex flex-col justify-evenly h-96 mt-8"},b={__name:"slides.md__slidev_16",setup(k){const{$clicksContext:o,$frontmatter:r}=c();return o.setup(),(y,s)=>{const i=l;return p(),d(m,f(_(n(v)(n(r),15))),{default:a(()=>[s[1]||(s[1]=t("div",{class:"absolute inset-0 bg-gradient-to-bl from-pink-950/50 via-transparent to-rose-950/40"},null,-1)),s[2]||(s[2]=t("h1",null,"Fitting the Trapezoidal Model",-1)),t("div",x,[u(i,null,{default:a(()=>[...s[0]||(s[0]=[t("div",{class:"card-fit"},[t("span",{class:"dot-fit"}),t("span",null,[t("strong",null,"Four fitted parameters:"),e(" t₀ (transit center), δ (depth), T"),t("sub",null,"total"),e(" (duration), t"),t("sub",null,"ingress"),e(" (ingress time)")])],-1),t("div",{class:"card-fit"},[t("span",{class:"dot-fit"}),t("div",{class:"flex-1"},[t("span",null,[t("strong",null,"The workflow:")]),t("div",{class:"mt-2 bg-gray-900/50 rounded px-4 py-2 font-mono text-base"},[t("pre",{class:"text-gray-100"},`# Define trapezoidal model
def trapezoidal_transit(t, t0, depth, duration, ingress_dur):
    # returns flux values
 
# Fit to data
popt, pcov = curve_fit(trapezoidal_transit, times, flux, 
                       p0=initial_guess, sigma=uncertainties)
 
# Extract fitted observables
t0, depth, T_total, t_ingress = popt
`)])])],-1)])]),_:1})]),s[3]||(s[3]=t("div",{class:"slide-number"},"16",-1))]),_:1},16)}}},I=g(b,[["__scopeId","data-v-8cf672e5"]]);export{I as default};
