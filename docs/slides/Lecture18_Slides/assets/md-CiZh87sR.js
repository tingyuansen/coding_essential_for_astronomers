import{_ as l}from"./slidev/VClicks-Bq9VFcGX.js";import{b as p,o as d,w as t,g as e,e as m,ac as a,v as c,x as f,C as n}from"./modules/vue-BjKabnyV.js";import{I as u}from"./slidev/center-jiu19geR.js";import{u as _,f as v}from"./slidev/context-DnQc23GN.js";import{_ as g}from"./index-BzdcdtSK.js";import"./modules/shiki-oSsGfnBi.js";const x={class:"relative flex flex-col justify-evenly h-96 mt-8"},b={__name:"slides.md__slidev_19",setup(y){const{$clicksContext:i,$frontmatter:o}=_();return i.setup(),(h,s)=>{const r=l;return d(),p(u,c(f(n(v)(n(o),18))),{default:t(()=>[s[1]||(s[1]=e("div",{class:"absolute inset-0 bg-gradient-to-tr from-fuchsia-950/50 via-transparent to-pink-950/40"},null,-1)),s[2]||(s[2]=e("h1",null,"Fitting the Sinusoidal Model",-1)),e("div",x,[m(r,null,{default:t(()=>[...s[0]||(s[0]=[e("div",{class:"card-sinfit"},[e("span",{class:"dot-sinfit"}),e("div",{class:"flex-1"},[e("div",{class:"mt-2 bg-gray-900/50 rounded px-4 py-2 font-mono text-lg"},[e("pre",{class:"text-gray-100"},`def sinusoidal_model(t, mean, amp, freq, phase):
    return mean + amp * np.sin(2*np.pi*freq*t + phase)
`),e("br"),e("pre",{class:"text-gray-100"},`p0 = [initial_mean, initial_amp, initial_freq, 0]
popt, pcov = curve_fit(
    sinusoidal_model,        # The model function to fit
    observation_times,       # Independent variable (x data)
    observed_brightness,     # Dependent variable (y data)
    p0=p0,                   # Initial parameter guesses
    sigma=brightness_errors  # Uncertainties in measurements
)`)])])],-1),e("div",{class:"card-sinfit"},[e("span",{class:"dot-sinfit"}),e("span",null,[a("The "),e("code",null,"p0"),a(" parameter passes initial guesses to help convergence")])],-1)])]),_:1})]),s[3]||(s[3]=e("div",{class:"slide-number"},"19",-1))]),_:1},16)}}},N=g(b,[["__scopeId","data-v-afc37601"]]);export{N as default};
