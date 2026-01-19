import{_ as l}from"./slidev/VClicks-Bf7_7t06.js";import{b as i,o as p,w as t,g as s,e as d,ac as m,v as u,x as _,C as o}from"./modules/vue-BjKabnyV.js";import{I as c}from"./slidev/center-BaVTJz7O.js";import{u as f,f as x}from"./slidev/context-CwExy7w2.js";import{_ as b}from"./index-C4hBybjX.js";import"./modules/shiki-oSsGfnBi.js";const v={class:"relative flex flex-col justify-evenly h-96 mt-8"},g={__name:"slides.md__slidev_31",setup(y){const{$clicksContext:r,$frontmatter:a}=f();return r.setup(),(B,e)=>{const n=l;return p(),i(c,u(_(o(x)(o(a),30))),{default:t(()=>[e[1]||(e[1]=s("div",{class:"absolute inset-0 bg-gradient-to-bl from-cyan-950/50 via-transparent to-teal-950/40"},null,-1)),e[2]||(e[2]=s("h1",null,"Using BLS in Python",-1)),s("div",v,[d(n,null,{default:t(()=>[...e[0]||(e[0]=[s("div",{class:"card-blscode"},[s("span",{class:"dot-blscode"}),s("div",{class:"flex-1"},[s("span",null,[s("strong",null,"The tool:"),m(" astropy.timeseries.BoxLeastSquares")]),s("div",{class:"mt-2 bg-gray-900/50 rounded px-4 py-2 font-mono text-base"},[s("pre",{class:"text-gray-100"},`from astropy.timeseries import BoxLeastSquares
 
# Initialize BLS with time series data
bls = BoxLeastSquares(times, flux)
periods = np.linspace(1.0, 10.0, 5000)
 
# Run BLS - returns power spectrum
bls_result = bls.power(periods, duration=0.12)
 
# Find best period
best_period = periods[np.argmax(bls_result.power)]
`)])])],-1)])]),_:1})]),e[3]||(e[3]=s("div",{class:"slide-number"},"31",-1))]),_:1},16)}}},P=b(g,[["__scopeId","data-v-a3827f56"]]);export{P as default};
