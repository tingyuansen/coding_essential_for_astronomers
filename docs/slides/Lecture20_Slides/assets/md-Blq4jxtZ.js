import{_ as i}from"./slidev/VClicks-D0vFe29O.js";import{b as l,o as m,w as t,g as e,e as p,v as _,x as d,C as r}from"./modules/vue-BjKabnyV.js";import{I as u}from"./slidev/center-vDeyfPKN.js";import{u as c,f}from"./slidev/context-Chpw6kDm.js";import{_ as k}from"./index-0ZbdpQjY.js";import"./modules/shiki-oSsGfnBi.js";const x={class:"relative flex flex-col justify-evenly h-96 mt-8"},v={__name:"slides.md__slidev_29",setup(g){const{$clicksContext:a,$frontmatter:n}=c();return a.setup(),(y,s)=>{const o=i;return m(),l(u,_(d(r(f)(r(n),28))),{default:t(()=>[s[1]||(s[1]=e("div",{class:"absolute inset-0 bg-gradient-to-bl from-rose-950/50 via-transparent to-pink-950/40"},null,-1)),s[2]||(s[2]=e("h1",null,"Implementation",-1)),e("div",x,[p(o,null,{default:t(()=>[...s[0]||(s[0]=[e("div",{class:"card-apcode"},[e("span",{class:"dot-apcode"}),e("div",{class:"flex-1"},[e("div",{class:"mt-2 bg-gray-900/50 rounded px-4 py-2 font-mono text-base"},[e("pre",{class:"text-gray-100"},`# Create coordinate grids centered on star
Y, X = np.ogrid[:img_size, :img_size]
dist = np.sqrt((X - x_center)**2 + (Y - y_center)**2)
 
# Create masks
aperture_mask = dist <= aperture_radius
sky_mask = (dist >= sky_inner) & (dist <= sky_outer)
 
# Estimate sky from annulus and measure flux
sky_level = np.median(image[sky_mask])
aperture_sum = np.sum(image[aperture_mask])
n_aperture_pixels = np.sum(aperture_mask)
flux = aperture_sum - sky_level * n_aperture_pixels
`)])])],-1)])]),_:1})]),s[3]||(s[3]=e("div",{class:"slide-number"},"28",-1))]),_:1},16)}}},j=k(v,[["__scopeId","data-v-3dac130b"]]);export{j as default};
