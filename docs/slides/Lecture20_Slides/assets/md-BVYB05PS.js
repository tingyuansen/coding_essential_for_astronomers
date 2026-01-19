import{_ as p}from"./slidev/VClicks-D0vFe29O.js";import{b as d,o as l,w as a,g as t,e as r,v as m,x as _,C as s}from"./modules/vue-BjKabnyV.js";import{I as c}from"./slidev/center-vDeyfPKN.js";import{u as f,f as u}from"./slidev/context-Chpw6kDm.js";import{_ as g}from"./index-0ZbdpQjY.js";import"./modules/shiki-oSsGfnBi.js";const v={class:"relative flex flex-col justify-evenly h-96 mt-8"},x={__name:"slides.md__slidev_22",setup(b){const{$clicksContext:n,$frontmatter:o}=f();return n.setup(),(y,e)=>{const i=p;return l(),d(c,m(_(s(u)(s(o),21))),{default:a(()=>[e[1]||(e[1]=t("div",{class:"absolute inset-0 bg-gradient-to-bl from-amber-950/50 via-transparent to-orange-950/40"},null,-1)),e[2]||(e[2]=t("h1",null,"Sigma Clipping: Implementation",-1)),t("div",v,[r(i,null,{default:a(()=>[...e[0]||(e[0]=[t("div",{class:"card-sigcode"},[t("span",{class:"dot-sigcode"}),t("div",{class:"flex-1"},[t("div",{class:"mt-2 bg-gray-900/50 rounded px-4 py-2 font-mono text-base"},[t("pre",{class:"text-gray-100"},`# Sigma-clipped statistics
clipped_data = image_noisy.flatten().copy()
 
for iteration in range(5):
    mean = np.mean(clipped_data)
    std = np.std(clipped_data)
     
    # Keep only pixels within 3σ of mean
    mask = np.abs(clipped_data - mean) < 3 * std
    clipped_data = clipped_data[mask]
 
bg_mean = np.mean(clipped_data)
bg_std = np.std(clipped_data)
`)])])],-1)])]),_:1})]),e[3]||(e[3]=t("div",{class:"slide-number"},"22",-1))]),_:1},16)}}},S=g(x,[["__scopeId","data-v-040a000e"]]);export{S as default};
