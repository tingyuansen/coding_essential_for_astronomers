import{b as r,o as n,w as i,g as s,v as l,x as d,C as e}from"./modules/vue-BjKabnyV.js";import{I as u}from"./slidev/center-vDeyfPKN.js";import{u as c,f as m}from"./slidev/context-Chpw6kDm.js";import{_ as p}from"./index-0ZbdpQjY.js";import"./modules/shiki-oSsGfnBi.js";const _={__name:"slides.md__slidev_37",setup(x){const{$clicksContext:o,$frontmatter:a}=c();return o.setup(),(f,t)=>(n(),r(u,l(d(e(m)(e(a),36))),{default:i(()=>[...t[0]||(t[0]=[s("div",{class:"absolute inset-0 bg-gradient-to-bl from-violet-950/50 via-transparent to-purple-950/40"},null,-1),s("div",{class:"relative flex flex-col justify-evenly h-full mt-8"},[s("div",{class:"card-multicode"},[s("span",{class:"dot-multicode"}),s("div",{class:"flex-1"},[s("span",null,[s("strong",null,"Building the multi-source model:")]),s("div",{class:"mt-2 bg-gray-900/50 rounded px-4 py-2 font-mono text-base"},[s("pre",{class:"text-gray-100"},`def multi_gaussian_2d(coords, x1, y1, A1, x2, y2, A2, 
                      x3, y3, A3, sigma, background):
    x, y = coords
    result = background
    # Sum contributions from all stars
    for xi, yi, Ai in [(x1,y1,A1), (x2,y2,A2), (x3,y3,A3)]:
        result += Ai * np.exp(-((x-xi)**2 + (y-yi)**2) / (2*sigma**2))
    return result
 
# Initial guesses from detected positions
p0 = [x1_det, y1_det, A1_guess, x2_det, y2_det, A2_guess,
      x3_det, y3_det, A3_guess, psf_sigma, 0.0]
 
# Fit all sources simultaneously
popt, pcov = curve_fit(multi_gaussian_2d, coords, data, p0=p0)
`)])])])],-1),s("div",{class:"slide-number"},"38",-1)])]),_:1},16))}},k=p(_,[["__scopeId","data-v-a38c8d7b"]]);export{k as default};
