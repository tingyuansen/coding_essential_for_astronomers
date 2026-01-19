import{_ as i}from"./slidev/VClicks-Bf7_7t06.js";import{b as l,o as d,w as e,g as s,e as p,v as m,x as u,C as a}from"./modules/vue-BjKabnyV.js";import{I as c}from"./slidev/center-BaVTJz7O.js";import{u as _,f}from"./slidev/context-CwExy7w2.js";import{_ as v}from"./index-C4hBybjX.js";import"./modules/shiki-oSsGfnBi.js";const g={class:"relative flex flex-col justify-evenly h-96 mt-8"},x={__name:"slides.md__slidev_18",setup(b){const{$clicksContext:r,$frontmatter:o}=_();return r.setup(),(k,t)=>{const n=i;return d(),l(c,m(u(a(f)(a(o),17))),{default:e(()=>[t[1]||(t[1]=s("div",{class:"absolute inset-0 bg-gradient-to-tr from-pink-950/50 via-transparent to-rose-950/40"},null,-1)),t[2]||(t[2]=s("h1",null,"Avoiding Local Minima",-1)),s("div",g,[p(n,null,{default:e(()=>[...t[0]||(t[0]=[s("div",{class:"card-restart"},[s("span",{class:"dot-restart"}),s("span",null,"Gradient-based optimizers can get stuck in local minima with poor initial guesses")],-1),s("div",{class:"card-restart"},[s("span",{class:"dot-restart"}),s("div",{class:"flex-1"},[s("span",null,[s("strong",null,"Try multiple random initial guesses, keep the fit with lowest χ²")]),s("div",{class:"mt-2 bg-gray-900/50 rounded px-4 py-2 font-mono text-base"},[s("pre",{class:"text-gray-100"},`results = []
for i in range(20):  # Try 20 random starts
    p0_random = generate_random_guess()
    popt, pcov = curve_fit(model, times, flux, p0=p0_random)
    chi2 = calculate_chi_squared(popt)
    results.append({'params': popt, 'chi2': chi2})
 
# Pick result with lowest chi-squared
best = min(results, key=lambda r: r['chi2'])
`)])])],-1)])]),_:1})]),t[3]||(t[3]=s("div",{class:"slide-number"},"18",-1))]),_:1},16)}}},I=v(x,[["__scopeId","data-v-4d17b515"]]);export{I as default};
