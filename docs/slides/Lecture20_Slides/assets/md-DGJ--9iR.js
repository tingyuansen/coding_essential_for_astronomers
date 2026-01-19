import{_ as r}from"./slidev/VClicks-D0vFe29O.js";import{b as l,o as m,w as t,g as e,e as d,v as p,x as _,C as o}from"./modules/vue-BjKabnyV.js";import{I as c}from"./slidev/center-vDeyfPKN.js";import{u,f}from"./slidev/context-Chpw6kDm.js";import{_ as g}from"./index-0ZbdpQjY.js";import"./modules/shiki-oSsGfnBi.js";const x={class:"relative flex flex-col justify-evenly h-96 mt-8"},b={__name:"slides.md__slidev_24",setup(v){const{$clicksContext:a,$frontmatter:n}=u();return a.setup(),(y,s)=>{const i=r;return m(),l(c,p(_(o(f)(o(n),23))),{default:t(()=>[s[1]||(s[1]=e("div",{class:"absolute inset-0 bg-gradient-to-bl from-amber-950/50 via-transparent to-orange-950/40"},null,-1)),s[2]||(s[2]=e("h1",null,"Source Detection: Implementation",-1)),e("div",x,[d(i,null,{default:t(()=>[...s[0]||(s[0]=[e("div",{class:"card-detectcode"},[e("span",{class:"dot-detectcode"}),e("div",{class:"flex-1"},[e("div",{class:"mt-2 bg-gray-900/50 rounded px-4 py-2 font-mono text-base"},[e("pre",{class:"text-gray-100"},`from scipy import ndimage
 
# Apply maximum filter - each pixel becomes max of neighborhood
max_filtered = ndimage.maximum_filter(image_bgsub, size=5)
is_peak = (image_bgsub == max_filtered)
 
# Apply threshold: signal > 5σ
threshold = 5 * bg_std
is_significant = image_bgsub > threshold
 
# Sources are significant peaks
sources = is_peak & is_significant
y_sources, x_sources = np.where(sources)
`)])])],-1)])]),_:1})]),s[3]||(s[3]=e("div",{class:"slide-number"},"24",-1))]),_:1},16)}}},P=g(b,[["__scopeId","data-v-abae741d"]]);export{P as default};
