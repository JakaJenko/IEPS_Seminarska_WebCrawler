(window.webpackJsonp=window.webpackJsonp||[]).push([[44],{2146:function(e,t,n){"use strict";function r(e){if("undefined"==typeof Symbol||null==e[Symbol.iterator]){if(Array.isArray(e)||(e=function(e,t){if(!e)return;if("string"==typeof e)return o(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);"Object"===n&&e.constructor&&(n=e.constructor.name);if("Map"===n||"Set"===n)return Array.from(n);if("Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))return o(e,t)}(e))){var t=0,n=function(){};return{s:n,n:function(){return t>=e.length?{done:!0}:{done:!1,value:e[t++]}},e:function(e){throw e},f:n}}throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}var r,a,i=!0,c=!1;return{s:function(){r=e[Symbol.iterator]()},n:function(){var e=r.next();return i=e.done,e},e:function(e){c=!0,a=e},f:function(){try{i||null==r.return||r.return()}finally{if(c)throw a}}}}function o(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){c(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function c(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}n.r(t);var u={data:function(){return{imgServer:this.$config.getValue("imgServer")+"/",headerStyle:{maxWidth:"1460px",margin:"0 auto"},wrapperStyle:i({maxWidth:"1460px"},this.$config.getValue("campaignConfig")?{margin:"0 auto"}:{padding:"0 15px"}),footStyle:{maxWidth:"1460px"}}},computed:{backgroundBanner:function(){return this.$store.state.banMan.backgroundBanner},pageStyle:function(){return i({},this.backgroundBanner.backgroundImage&&{backgroundImage:"url('".concat(this.imgServer).concat(this.backgroundBanner.backgroundImage,"')")},{backgroundColor:this.backgroundBanner.backgroundColor||"#fff",backgroundRepeat:"repeat",backgroundPosition:"center top"})},containerStyle:function(){return i({},this.backgroundBanner.skyscraperImage&&{backgroundImage:"url('".concat(this.imgServer).concat(this.backgroundBanner.skyscraperImage,"')")},{backgroundRepeat:"no-repeat",backgroundColor:"transparent",backgroundPosition:"center top"})}},watch:{backgroundBanner:{immediate:!0,handler:function(e){e.id&&this.setStyles()}}},methods:{setStyles:function(){var e=this,t=document.querySelector("body"),n=document.getElementById("app"),o=document.getElementById("header"),a=document.querySelector(".header-banner-wrap"),i=document.querySelector(".main-wrapper"),c=document.getElementsByClassName("foot");this.setElementStyles(t,this.pageStyle),this.backgroundBanner.url&&t.addEventListener("click",(function(t){"app-content"!==t.target.id&&"app"!==t.target.id&&"FOOTER"!==t.target.nodeName||(window.location.href="".concat(window.location.origin,"/").concat(e.backgroundBanner.url.replace(/^\//g,"")))})),this.setElementStyles(n,this.containerStyle),this.setElementStyles(o,this.headerStyle),this.setElementStyles(a,this.headerStyle),this.setElementStyles(i,this.wrapperStyle);var u,l=r(c);try{for(l.s();!(u=l.n()).done;){var s=u.value;this.setElementStyles(s,this.footStyle)}}catch(e){l.e(e)}finally{l.f()}},setElementStyles:function(e,t){e&&Object.keys(t).forEach((function(n){e.style[n]=t[n]}))}},render:function(e){return e()}},l=n(1),s=Object(l.a)(u,void 0,void 0,!1,null,null,null);t.default=s.exports}}]);
//# sourceMappingURL=background-banner.e7ed1333ca53b45b2f20.js.map