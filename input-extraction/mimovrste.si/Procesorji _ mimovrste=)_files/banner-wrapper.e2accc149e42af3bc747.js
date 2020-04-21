(window.webpackJsonp=window.webpackJsonp||[]).push([[45,46,50,307,312],{1185:function(t,e,n){"use strict";var a=n(350),i=n(902),r=n(2),s=n(20),o=n(97),c=n(16),l={name:"DailyDeal",filters:{priceFormat:s.a,translate:r.a},components:{AddToCartButton:a.default,Timer:i.default},props:{isAvailable:{type:Boolean,default:!1},rrpSavePercent:{type:String|Number,required:!0},priceRrp:{type:String|Number,required:!0},mediaId:{type:String|Number,required:!0},variantId:{type:String|Number,required:!0},title:{type:String,required:!0},mainMenuUrlKey:{type:String,required:!0},urlKey:{type:String,required:!0},price:{type:String|Number,required:!0},endTime:{type:String|Number,required:!0},entityId:{type:String,required:!0},headline:{type:String,default:""},isTimestamp:{type:Boolean,default:!1}},data:function(){return{imgServer:this.$config.getValue("imgServer")}},computed:{content:function(){var t=this;return JSON.parse(Object(c.a)(this.$store.state.shopContent,"daily-deal-vue","[]")).find((function(e){return e.id===t.entityId}))||{headline:""}}},created:function(){o.a.getContent("daily-deal-vue")}},u=(n(1254),n(1)),d=Object(u.a)(l,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("a",{staticClass:"daily-deal-2",attrs:{href:"/"+t.mainMenuUrlKey+"/"+t.urlKey}},[n("div",{staticClass:"daily-deal-2__logo-countdown-container"},[n("div",{staticClass:"daily-deal-2__countdown"},[n("div",{staticClass:"daily-deal-2__offer-validity"},[t._v(t._s(t._f("translate")("offer_valid_to")))]),n("timer",{staticClass:"daily-deal-2__countdown-timer daily-deal-2__offer-validity",attrs:{"end-time":t.endTime,"is-timestamp":t.isTimestamp}})],1),t.rrpSavePercent?n("div",{staticClass:"label label--white daily-deal-2__discount-label"},[n("span",{staticClass:"label--round__inner"},[t._v("\n        -"+t._s(t.rrpSavePercent)+"%\n      ")])]):t._e()]),n("div",{staticClass:"daily-deal-2__container"},[n("div",{staticClass:"daily-deal-2__picture-container"},[n("div",{staticClass:"daily-deal-2__picture"},[n("span",{staticClass:"media"},[t.isAvailable?t._e():n("div",{staticClass:"daily-deal-2__sold-out"},[t._v(t._s(t._f("translate")("sold_out")))]),t.mediaId?n("img",{attrs:{src:t.imgServer+"/"+t.mediaId+"/278/138",alt:t.title}}):t._e()])])]),n("div",{staticClass:"daily-deal-2__product-info-container"},[n("div",{staticClass:"daily-deal-2__product-info"},[n("span",{staticClass:"daily-deal-2__product-title"},[t._v(t._s(t.title))]),n("div",{staticClass:"daily-deal-2__product-headline"},[t._v("\n          "+t._s(t.headline||t.content.headline)+"\n        ")]),n("div",{staticClass:"daily-deal-2__prices-button-container"},[n("div",{staticClass:"daily-deal-2__prices"},[t.priceRrp&&t.rrpSavePercent?n("div",{staticClass:"daily-deal-2__price-old"},[t._v("\n              "+t._s(t._f("priceFormat")(t.priceRrp))+"\n            ")]):t._e(),n("div",{staticClass:"daily-deal-2__price"},[t._v(t._s(t._f("priceFormat")(t.price)))])]),t.isAvailable?n("div",{staticClass:"daily-deal-2__add-to-cart"},[n("add-to-cart-button",{attrs:{product:{variantId:t.variantId}}})],1):t._e(),n("div",{staticClass:"daily-deal-2__flexible"})])])])])])}),[],!1,null,"5e030f52",null);e.a=d.exports},1187:function(t,e,n){"use strict";var a=n(12),i=n.n(a),r=n(6),s=i.a.extend({name:"Preview",components:{SvgImage:r.default},props:{title:{type:String,required:!0},image:{type:String,required:!0},url:{type:String,required:!0},isMallTv:{type:Boolean,required:!1,default:!0},utmSource:{type:String,default:null},utmMedium:{type:String,default:null},utmCampaign:{type:String,default:null},utmContent:{type:String,default:null}},computed:{utmQuery:function(){return[{key:"utm_source",value:this.utmSource},{key:"utm_medium",value:this.utmMedium},{key:"utm_campaign",value:this.utmCampaign},{key:"utm_content",value:this.utmContent}].filter((function(t){return!!t.value})).map((function(t){return"".concat(t.key,"=").concat(t.value)})).join("&")},urlWithUtmQuery:function(){return this.url+(this.url.match(/[?]/g)?"&":"?")+this.utmQuery}}}),o=(n(1256),n(1)),c=Object(o.a)(s,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("a",{staticClass:"tv-previews-item",attrs:{href:t.urlWithUtmQuery,target:"_blank"}},[n("div",{staticClass:"tv-previews-item__header"},[n("div",{staticClass:"content"},[n("div",{staticClass:"tv-previews-item__overlay"},[t.isMallTv?n("svg-image",{staticClass:"symbol-overlay-icon",attrs:{source:"iconMallTV",width:"33",height:"19"}}):t._e(),n("svg-image",{staticClass:"play-overlay-icon",attrs:{source:"iconVideoPlay",width:"20",height:"22"}})],1),n("img",{staticClass:"tv-previews-item__image lazyload",attrs:{"data-src":t.image,alt:t.title}})])]),n("div",{staticClass:"tv-previews-item__title"},[n("p",{staticClass:"line-clamp"},[t._v(t._s(t.title))])])])}),[],!1,null,"58152ee2",null);e.a=c.exports},1254:function(t,e,n){"use strict";var a=n(985);n.n(a).a},1255:function(t,e,n){},1256:function(t,e,n){"use strict";var a=n(986);n.n(a).a},1257:function(t,e,n){},1786:function(t,e,n){"use strict";var a=n(261),i=n.n(a),r=n(88),s=n(730),o=n(216),c=n(127);function l(t,e){var n=Object.keys(t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(t);e&&(a=a.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),n.push.apply(n,a)}return n}function u(t){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{};e%2?l(Object(n),!0).forEach((function(e){d(t,e,n[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(n)):l(Object(n)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(n,e))}))}return t}function d(t,e,n){return e in t?Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[e]=n,t}var b={Banners:"banner",CampaignBanners:"Campaign banners",Carousel:"Slider banner",DailyDealBanner:"Daily deal",SectionBanner:"Section banner",SlimBanner:"Slim banner",UspBanner:"Header banner USP",BannerFarm:"Banner farm"},m={bind:function(t,e,n){if(void 0!==e.value){var a=e.value,l=a.slideId,d=void 0===l?null:l,m=a.slidePosition,p=a.banner,f=p.id,v=p.pageId,h=p.bannerType,g=p.type,y=p.bannerSlides,_=p.gaTag,S=h||g,C=y&&y.length?y[m-1].gaTag:_,w="Banners"===S&&y.length?1===y.length?"Full banner":"1-".concat(y.length," ").concat(b[S]):b[S],T={id:c.a.getChannelFlag(),name:w,creative:C,position:m},O={slideId:d,bannerId:f,pageId:v};t.__bannerControlHitClickEL=function(t){window.dataLayer.push({event:"intPromoClick",ecommerce:{promoClick:{promotions:[T]}}}),n.context.$root.$store.dispatch(o.BANMAN_ACTIONS.PUSH_ANALYTICS_DATA,u({},O,{type:"click"}))},t.addEventListener("click",t.__bannerControlHitClickEL),t.__bannerControlImpressionScrollEL=Object(r.a)((function(){i()(t,{requiredVisibleElemPortion:.5})&&(n.context.$root.$store.dispatch(o.BANMAN_ACTIONS.PUSH_GOOGLE_ANALYTICS_DATA,{id:f,promotions:T}),n.context.$root.$store.dispatch(o.BANMAN_ACTIONS.PUSH_ANALYTICS_DATA,u({},O,{type:"impression"})),window.removeEventListener("scroll",t.__bannerControlImpressionScrollEL),window.removeEventListener("load",t.__bannerControlImpressionScrollEL))}),s.a),window.addEventListener("scroll",t.__bannerControlImpressionScrollEL),window.addEventListener("load",t.__bannerControlImpressionScrollEL)}},unbind:function(t){t.removeEventListener("click",t.__bannerControlHitClickEL),window.removeEventListener("scroll",t.__bannerControlImpressionScrollEL),window.removeEventListener("load",t.__bannerControlImpressionScrollEL)}};e.a={directives:{bannerControl:m},methods:{addBanmanAnalytics:function(t,e){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:0;return{slideId:t,banner:e,slidePosition:n+1}}}}},1816:function(t,e,n){var a=n(1852);"string"==typeof a&&(a=[[t.i,a,""]]),a.locals&&(t.exports=a.locals);(0,n(10).default)("82b0ef76",a,!0,{})},1817:function(t,e,n){var a=n(1857);"string"==typeof a&&(a=[[t.i,a,""]]),a.locals&&(t.exports=a.locals);(0,n(10).default)("773b9a18",a,!0,{})},1818:function(t,e,n){var a=n(1859);"string"==typeof a&&(a=[[t.i,a,""]]),a.locals&&(t.exports=a.locals);(0,n(10).default)("71511e96",a,!0,{})},1819:function(t,e,n){var a=n(1861);"string"==typeof a&&(a=[[t.i,a,""]]),a.locals&&(t.exports=a.locals);(0,n(10).default)("7d15f3e2",a,!0,{})},1820:function(t,e,n){var a=n(1863);"string"==typeof a&&(a=[[t.i,a,""]]),a.locals&&(t.exports=a.locals);(0,n(10).default)("5d68e834",a,!0,{})},1851:function(t,e,n){"use strict";var a=n(1816);n.n(a).a},1852:function(t,e,n){},1856:function(t,e,n){"use strict";var a=n(1817);n.n(a).a},1857:function(t,e,n){},1858:function(t,e,n){"use strict";var a=n(1818);n.n(a).a},1859:function(t,e,n){},1860:function(t,e,n){"use strict";var a=n(1819);n.n(a).a},1861:function(t,e,n){},1862:function(t,e,n){"use strict";var a=n(1820);n.n(a).a},1863:function(t,e,n){},1864:function(t,e,n){var a=n(1967);"string"==typeof a&&(a=[[t.i,a,""]]),a.locals&&(t.exports=a.locals);(0,n(10).default)("63482bb4",a,!0,{})},1865:function(t,e,n){var a=n(1969);"string"==typeof a&&(a=[[t.i,a,""]]),a.locals&&(t.exports=a.locals);(0,n(10).default)("3c4e4111",a,!0,{})},1866:function(t,e,n){var a=n(1971);"string"==typeof a&&(a=[[t.i,a,""]]),a.locals&&(t.exports=a.locals);(0,n(10).default)("0b93b578",a,!0,{})},1953:function(t,e,n){"use strict";n.r(e);var a=n(1786),i={name:"UspBanner",mixins:[a.a],props:{autoplay:{type:Boolean,default:!1},bannerData:{type:Object,required:!0,default:function(){return{}}},bannerAttributes:{type:Object,required:!1,default:function(){return{}}}},data:function(){return{uspBanner:this.bannerAttributes,imgServer:this.$config.getValue("imgServer")+"/"}},computed:{bgImageStyle:function(){var t="url('".concat(this.imgServer).concat(this.uspBanner.mediaId,"/").concat("250","')"),e=this.uspBanner,n=e.mediaId,a=e.bannerBackgroundRepeat,i=e.bannerBackgroundColor;return n&&a?"background-image: ".concat(t,";\n                background-color: ").concat(i,";\n                background-repeat: repeat;"):n?"background-image: ".concat(t,"; background-color: ").concat(i):"background-color: ".concat(i)},iconsStyle:function(){return"background-color: ".concat(this.uspBanner.iconsBackgroundColor)}},methods:{goToUrl:function(){window.location.href=this.uspBanner.button.url},getIconStyle:function(t){return t.mediaId?"background-image: url('".concat(this.imgServer).concat(t.mediaId,"/").concat("25/25","')"):""}}},r=(n(1862),n(1)),s=Object(r.a)(i,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return t.uspBanner?n("a",{directives:[{name:"banner-control",rawName:"v-banner-control",value:t.addBanmanAnalytics(null,t.bannerData),expression:"addBanmanAnalytics(null, bannerData)"}],staticClass:"bb-usp-banner__wrapper",style:t.bgImageStyle,on:{click:t.goToUrl}},[t.uspBanner.mediaId?n("div",{staticClass:"bb-usp-banner__image"}):t._e(),t._l(t.uspBanner.points,(function(e,a){return n("div",{key:a,staticClass:"bb-usp-banner__point-wrapper"},[n("div",{staticClass:"bb-usp-banner__point"},[n("div",{staticClass:"bb-usp-banner__icon-wrap",style:{backgroundColor:t.uspBanner.iconsBackgroundColor}},[n("div",{staticClass:"bb-usp-banner__icon",style:t.getIconStyle(e)})]),n("div",{staticClass:"bb-usp-banner__text-box",style:{color:t.uspBanner.pointTextColor}},[n("div",{staticClass:"bb-usp-banner__point-title"},[t._v(t._s(e.title))]),n("div",{staticClass:"bb-usp-banner__point-text"},[t._v(t._s(e.text))])])]),2===a?n("div",[t.uspBanner.button.text?n("button",{staticClass:"bb-usp-banner__button btn btn--small btn--primary",on:{click:t.goToUrl}},[t._v("\n        "+t._s(t.uspBanner.button.text)+"\n      ")]):t._e()]):t._e()])}))],2):t._e()}),[],!1,null,"068fa475",null);e.default=s.exports},1954:function(t,e,n){"use strict";n.r(e);var a=n(85),i=n(6),r=n(865),s=n(914),o=n(1786),c=n(88);function l(t,e){var n=Object.keys(t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(t);e&&(a=a.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),n.push.apply(n,a)}return n}function u(t){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{};e%2?l(Object(n),!0).forEach((function(e){d(t,e,n[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(n)):l(Object(n)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(n,e))}))}return t}function d(t,e,n){return e in t?Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[e]=n,t}var b={autoplayDuration:5e3,easing:"ease",loop:!0,draggable:!0},m={name:"BannerCarousel",components:{Carousel:r.a,SvgImage:i.default},directives:{CarouselClick:s.a},mixins:[o.a],props:{autoplay:{type:Boolean,default:!1},bannerData:{type:Object,required:!1,default:function(){return{}}},bannerAttributes:{type:Object,required:!1,default:function(){return{}}}},data:function(){return{slides:this.bannerData.bannerSlides,carouselOptions:u({},b,{},this.$config.getValue("carousel.carousel.config",!1),{autoplay:this.bannerAttributes.autoplay,imgBorderRadius:this.bannerAttributes.imgBorderRadius||0}),currentSlideIndex:0,imageResolution:"1200",imageResolutionMobile:"640",imgServer:this.$config.getValue("imgServer")+"/",slideHeight:0}},computed:{isMobile:function(){return this.$store.getters[a.GENERAL_GETTERS.IS_MOBILE]}},mounted:function(){var t=this;this.setWrapperHeightFromSlide(),window.addEventListener("resize",this.setHeightWithDebounce),this.carouselOptions.autoplay&&this.$refs.carousel.autoPlay(),this.$refs.carousel.$el.addEventListener("click",(function(e){return t.goToUrl(e)}))},beforeDestroy:function(){window.removeEventListener("resize",this.setHeightWithDebounce),this.$refs.carousel.$el.removeEventListener("click",this.goToUrl())},methods:{carouselChange:function(){this.currentSlideIndex=this.$refs.carousel.currentSlide},nextSlide:function(){this.$refs.carousel.next()},previousSlide:function(){this.$refs.carousel.prev()},goToSlide:function(t){this.$refs.carousel.goTo(t)},goToUrl:function(t){var e=parseInt(t.target.attributes.slide.value),n=t.target.attributes.url.value;e===this.currentSlideIndex?n&&(window.location.href=n):this.nextSlide()},bannerSrc:function(t){var e=t.mediaIdMobile||t.mediaId;return this.isMobile?"".concat(this.imgServer).concat(e,"/").concat(this.imageResolutionMobile):"".concat(this.imgServer).concat(t.mediaId,"/").concat(this.imageResolution)},setWrapperHeightFromSlide:function(){this.slideHeight=this.$refs.carousel.$el.querySelector(".bb-carousel__image-wrapper").offsetHeight},setHeightWithDebounce:Object(c.a)((function(){this.setWrapperHeightFromSlide()}),250)}},p=(n(1858),n(1860),n(1)),f=Object(p.a)(m,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"bb-carousel__wrapper"},[n("div",{staticClass:"bb-carousel__gradient"}),t.slides.length>1?n("div",[n("button",{staticClass:"bb-carousel__button",on:{click:function(e){return t.previousSlide()}}},[n("svg-image",{staticClass:"bb-carousel__arrow-left",attrs:{fallback:"arrow left",source:"iconArrow",width:"25",height:"25","fill-color":"#ffffff"}})],1),n("button",{staticClass:"bb-carousel__button bb-carousel__button--right",on:{click:function(e){return t.nextSlide()}}},[n("svg-image",{attrs:{fallback:"arrow right",source:"iconArrow",width:"25",height:"25","fill-color":"#ffffff"}})],1),n("div",{staticClass:"bb-carousel__slide-indicator-wrapper"},t._l(t.slides,(function(e,a){return n("button",{key:e.text+a,staticClass:"bb-carousel__slide-indicator-item",class:{"bb-carousel__slide-indicator-item--active":a===t.currentSlideIndex},on:{click:function(e){return t.goToSlide(a)}}})})),0)]):t._e(),n("div",{staticClass:"bb-carousel__slides",class:{"bb-carousel__slides--one":1===t.slides.length}},[n("carousel",t._b({ref:"carousel",staticClass:"bb-carousel",style:{height:t.slideHeight+"px"},on:{change:function(e){return t.carouselChange()}}},"carousel",t.carouselOptions,!1),t._l(t.slides,(function(e,a){return n("div",{directives:[{name:"carousel-click",rawName:"v-carousel-click"}],key:e.text+a,staticClass:"bb-carousel__image-wrapper"},[n("img",{directives:[{name:"banner-control",rawName:"v-banner-control",value:t.addBanmanAnalytics(e.id,t.bannerData,a),expression:"addBanmanAnalytics(slide.id, bannerData, index)"}],staticClass:"bb-carousel__image",style:{"border-radius":t.carouselOptions.imgBorderRadius+"px"},attrs:{src:t.bannerSrc(e),slide:a,url:e.url,alt:""}})])})),0)],1)])}),[],!1,null,"16f0a7d4",null);e.default=f.exports},1955:function(t,e,n){"use strict";n.r(e);var a=n(1786),i=n(85),r={name:"CampaignBanners",mixins:[a.a],props:{bannerData:{type:Object,default:function(){return{}}}},data:function(){return{banners:this.bannerData.bannerSlides,imageResolution:"1200",imageResolutionMobile:"640",imgServer:this.$config.getValue("imgServer")+"/"}},computed:{isMobile:function(){return this.$store.getters[i.GENERAL_GETTERS.IS_MOBILE]}},methods:{bannerStyle:function(t){if(1===this.banners.length)return"width: 100%"},bannerSrc:function(t){var e=t.mediaIdMobile||t.mediaId;return this.isMobile?"".concat(this.imgServer).concat(e,"/").concat(this.imageResolutionMobile):"".concat(this.imgServer).concat(t.mediaId,"/").concat(this.imageResolution)}}},s=(n(1856),n(1)),o=Object(s.a)(r,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"bb-campaign-banners__wrapper"},t._l(t.banners,(function(e,a){return n("a",{directives:[{name:"banner-control",rawName:"v-banner-control",value:t.addBanmanAnalytics(e.id,t.bannerData,a),expression:"addBanmanAnalytics(slide.id, bannerData, index)"}],key:a,staticClass:"bb-campaign-banner",style:t.bannerStyle(e),attrs:{href:e.url}},[n("img",{staticClass:"bb-campaign-banner_image",attrs:{src:t.bannerSrc(e)}})])})),0)}),[],!1,null,"586ee69b",null);e.default=o.exports},1956:function(t,e,n){"use strict";n.r(e);var a=n(830),i=n(6),r=n(1786),s=n(85),o={name:"Banners",components:{SvgImage:i.default},directives:{VideoBroadcast:a.a},mixins:[r.a],props:{bannerData:{type:Object,default:function(){return{}}}},data:function(){return{slides:this.bannerData.bannerSlides,imageResolution:"1200",imageResolutionMobile:"640",imgServer:this.$config.getValue("imgServer")+"/"}},computed:{isMobile:function(){return this.$store.getters[s.GENERAL_GETTERS.IS_MOBILE]}},methods:{bannerSrc:function(t){var e=t.mediaIdMobile||t.mediaId;return this.isMobile?"".concat(this.imgServer).concat(e,"/").concat(this.imageResolutionMobile):"".concat(this.imgServer).concat(t.mediaId,"/").concat(this.imageResolution)}}},c=(n(1851),n(1)),l=Object(c.a)(o,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"bb-banners__wrapper"},t._l(t.slides,(function(e,a){return n("div",{directives:[{name:"banner-control",rawName:"v-banner-control",value:t.addBanmanAnalytics(e.id,t.bannerData,a),expression:"addBanmanAnalytics(slide.id, bannerData, index)"}],key:a,staticClass:"bb-banner"},[e.video&&!e.urlNewWindow?n("a",{directives:[{name:"video-broadcast",rawName:"v-video-broadcast"}],attrs:{"data-video":e.video,href:"javascript:void(0)"}},[n("svg-image",{staticClass:"play-overlay-icon",attrs:{source:"iconVideoPlay",width:"20",height:"22"}}),n("img",{staticClass:"bb-banner-image",attrs:{src:t.bannerSrc(e)}})],1):n("a",{attrs:{href:e.url}},[n("img",{staticClass:"bb-banner-image",attrs:{src:t.bannerSrc(e)}}),n("div",{staticClass:"bb-banner-text"},[t._v(t._s(e.text))])])])})),0)}),[],!1,null,"711dddbb",null);e.default=l.exports},1966:function(t,e,n){"use strict";var a=n(1864);n.n(a).a},1967:function(t,e,n){},1968:function(t,e,n){"use strict";var a=n(1865);n.n(a).a},1969:function(t,e,n){},1970:function(t,e,n){"use strict";var a=n(1866);n.n(a).a},1971:function(t,e,n){},2133:function(t,e,n){"use strict";n.r(e);var a=n(1954),i=n(1953),r=n(1956),s=n(2125),o=n(1955),c=n(1786),l={name:"SlimBanner",mixins:[c.a],props:{bannerData:{type:Object,required:!1,default:function(){return{}}},bannerAttributes:{type:Object,required:!1,default:function(){return{}}}},data:function(){return{slimBanner:this.bannerData.bannerSlides[0],slimBannerAttrs:this.bannerAttributes,imageResolution:"1430",imgServer:this.$config.getValue("imgServer")+"/"}},methods:{bannerStyle:function(){var t="url('".concat(this.imgServer).concat(this.slimBanner.mediaId,"/").concat(this.imageResolution,"')");return"background-image: ".concat(t,";\n              border-radius: ").concat(this.slimBannerAttrs.borderRadius,";\n              background-size: ").concat(this.slimBannerAttrs.backgroundSize,";\n              background-position: ").concat(this.slimBannerAttrs.backgroundPosition,";")},goToUrl:function(){window.location.href=this.slimBanner.url}}},u=(n(1966),n(1)),d=Object(u.a)(l,(function(){var t=this.$createElement;return(this._self._c||t)("div",{directives:[{name:"banner-control",rawName:"v-banner-control",value:this.addBanmanAnalytics(this.slimBanner.id,this.bannerData),expression:"addBanmanAnalytics(slimBanner.id, bannerData)"}],staticClass:"slim-banner__wrapper",style:this.bannerStyle(),on:{click:this.goToUrl}})}),[],!1,null,"ef439124",null).exports,b=n(1185),m=n(3),p=n(16);function f(t,e,n,a,i,r,s){try{var o=t[r](s),c=o.value}catch(t){return void n(t)}o.done?e(c):Promise.resolve(c).then(a,i)}var v={name:"DailyDealBanner",components:{DailyDeal:b.a},mixins:[c.a],props:{bannerData:{type:Object,default:function(){return{}}},bannerAttributes:{type:Object,default:function(){return{}}}},data:function(){return{product:{}}},computed:{title:function(){return this.bannerAttributes.productTitle||this.product.title},isAvailable:function(){return Object(p.a)(this.product,"mainVariant.availability.isAvailable",!1)},validTo:function(){return new Date(this.bannerAttributes.validTo).getTime()}},created:function(){this.getProduct()},methods:{getProduct:function(){var t,e=this;return(t=regeneratorRuntime.mark((function t(){var n;return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,m.a.get("/api/product/findItem?articleId=".concat(e.bannerAttributes.productId)).catch((function(){console.error("Can't find product with id: ".concat(e.bannerAttributes.productId,"."))}));case 2:n=t.sent,e.product=Object(p.a)(n,"data.products[0]",{});case 4:case"end":return t.stop()}}),t)})),function(){var e=this,n=arguments;return new Promise((function(a,i){var r=t.apply(e,n);function s(t){f(r,a,i,s,o,"next",t)}function o(t){f(r,a,i,s,o,"throw",t)}s(void 0)}))})()}}},h=(n(1968),Object(u.a)(v,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return t.product.entityId?n("div",{staticClass:"column daily-deal-banner"},[n("div",{staticClass:"call--upper"},[n("h2",{staticClass:"call-head"},[t._v(t._s(t.bannerAttributes.header))])]),n("daily-deal",{directives:[{name:"banner-control",rawName:"v-banner-control",value:t.addBanmanAnalytics(null,t.bannerData),expression:"addBanmanAnalytics(null, bannerData)"}],attrs:{"end-time":t.validTo,"is-available":t.isAvailable,"rrp-save-percent":t.product.mainVariant.rrpSavePercent,"price-rrp":t.product.mainVariant.priceRrp,"media-id":t.product.mainVariant.mediaIdList[0],"variant-id":t.product.mainVariant.variantId,title:t.title,headline:t.bannerAttributes.productHeadline,"main-menu-url-key":t.product.mainMenuUrlKey,"url-key":t.product.urlKey,price:t.product.mainVariant.price,"entity-id":t.product.entityId,"is-timestamp":""}})],1):t._e()}),[],!1,null,null,null).exports),g=n(1187),y={name:"BannerFarm",components:{PreviewItem:g.a},mixins:[c.a],props:{bannerData:{type:Object,default:function(){return{}}},bannerAttributes:{type:Object,required:!1,default:function(){return{}}}},data:function(){var t=this.bannerData;return{title:t.title,bannerSlides:t.bannerSlides,imageResolution:"1200",imageResolutionMobile:"640",imgServer:this.$config.getValue("imgServer")+"/"}},computed:{main:function(){return this.bannerSlides[0]},slides:function(){return this.bannerSlides.slice(1)}},methods:{isMallTv:function(t){return"mallTvFeed"===t},slideSrc:function(t){if(this.isMallTv(t.type))return t.mediaUrl;var e=t.mediaIdMobile||t.mediaId;return this.isMobile?"".concat(this.imgServer).concat(e,"/").concat(this.imageResolutionMobile):"".concat(this.imgServer).concat(t.mediaId,"/").concat(this.imageResolution)}}},_=(n(1970),Object(u.a)(y,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"bb-banner-farm__wrapper",style:{backgroundColor:t.bannerAttributes.backgroundColor}},[n("div",{staticClass:"bb-banner-farm__title con-center call--upper"},[n("h2",{staticClass:"call-head"},[t._v(t._s(t.title))])]),n("div",{staticClass:"bb-banner-farm__content"},[n("div",{staticClass:"bb-banner-farm__main-slide"},[n("a",{directives:[{name:"banner-control",rawName:"v-banner-control",value:t.addBanmanAnalytics(t.main.id,t.bannerData,0),expression:"addBanmanAnalytics(main.id, bannerData, 0)"}],attrs:{href:t.main.url,target:"_blank"}},[n("img",{staticClass:"bb-banner-image",attrs:{src:t.slideSrc(t.main)}})])]),n("div",{staticClass:"bb-banner-farm__slides"},t._l(t.slides,(function(e,a){return n("preview-item",{directives:[{name:"banner-control",rawName:"v-banner-control",value:t.addBanmanAnalytics(e.id,t.bannerData,a+1),expression:"addBanmanAnalytics(slide.id, bannerData, index + 1)"}],key:a+"_"+e.title,attrs:{"is-mall-tv":t.isMallTv(e.type),title:e.title,image:t.slideSrc(e),url:e.url}})})),1)])])}),[],!1,null,null,null).exports);function S(t,e){var n=Object.keys(t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(t);e&&(a=a.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),n.push.apply(n,a)}return n}function C(t,e,n){return e in t?Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[e]=n,t}var w={components:{BrandCarousel:s.default,CampaignBanners:o.default,Banners:r.default,Carousel:a.default,UspBanner:i.default,SlimBanner:d,DailyDealBanner:h,BannerFarm:_},props:{position:{type:Number,default:null}},computed:{componentData:function(){var t=this,e=this.$store.state.banMan,n=e.pageId;return function(t){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{};e%2?S(Object(n),!0).forEach((function(e){C(t,e,n[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(n)):S(Object(n)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(n,e))}))}return t}({},e.banners.find((function(e){return t.position===e.position})),{pageId:n})}}},T=Object(u.a)(w,(function(){var t=this.$createElement,e=this._self._c||t;return this.componentData?e("div",[e(this.componentData.bannerType,{tag:"component",attrs:{"banner-data":this.componentData,"banner-attributes":this.componentData.bannerAttributes}})],1):this._e()}),[],!1,null,null,null);e.default=T.exports},229:function(t,e,n){"use strict";var a=n(483),i=n.n(a),r=n(238);e.a={template:i.a,components:{Spinner:r.a}}},307:function(t,e,n){"use strict";n.d(e,"a",(function(){return s}));var a=n(2),i=n(229),r=n(386),s={DEFAULT:"DEFAULT",TRIGGERED:"TRIGGERED",DONE:"DONE"},o={components:{ButtonLoader:i.a},filters:{translate:a.a},mixins:[r.a],props:{overrideClass:{type:String,required:!1,default:"btn--small btn--primary"},isBold:{type:Boolean,required:!1,default:!0},btnText:{type:String,required:!1,default:""},btnDoneText:{type:String,required:!1,default:""},btnState:{type:String,default:s.DEFAULT},customContent:{type:Boolean,default:!1},clickableMoreTimes:{type:Boolean,default:!1},btnClicked:{type:Function,required:!1,default:function(){}}},data:function(){return{BUTTON_STATES:s,buttonState:this.btnState}},computed:{isDone:function(){return this.buttonState===s.DONE},isTriggered:function(){return this.buttonState===s.TRIGGERED}},watch:{btnState:function(t){this.buttonState=t}},methods:{trigger:function(){(!this.isDone&&!this.isTriggered||this.clickableMoreTimes)&&(this.buttonState=s.TRIGGERED,this.btnClicked())}}},c=n(1),l=Object(c.a)(o,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("button",{staticClass:"btn btn--element btn--animate",class:[t.isTriggered&&!t.clickableMoreTimes&&"action--in-progress",t.isDone&&!t.clickableMoreTimes&&"action--done",t.isBold&&"con-bold",t.overrideClass],attrs:{type:"button"},on:{click:function(e){return e.preventDefault(),t.trigger()}}},[t.lazyLoaded?n("button-loader"):t._e(),t.customContent?t._t("customContent"):n("span",{staticClass:"btn-inner"},[t.isDone?n("span",{staticClass:"btn-inset--added"},[t._v(t._s(t._f("translate")(t.btnDoneText)))]):n("span",{staticClass:"btn-inset lay-block"},[t._v(t._s(t._f("translate")(t.btnText)))])])],2)}),[],!1,null,null,null);e.b=l.exports},350:function(t,e,n){"use strict";n.r(e);var a=n(5),i=n(2),r=n(229),s=n(484),o=n.n(s),c=n(307),l=n(475);function u(t,e){var n=Object.keys(t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(t);e&&(a=a.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),n.push.apply(n,a)}return n}function d(t,e,n){return e in t?Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[e]=n,t}e.default={template:o.a,props:{product:{type:Object,required:!0},amount:{type:Number,required:!1,default:1},overrideClass:{type:String,required:!1,default:"btn--small btn--primary"},bundles:{type:Object,required:!1},isBold:{type:Boolean,required:!1,default:!0},redirectUrl:{type:String},btnText:{type:String,required:!1,default:"cta_buy_now"},customContent:{type:Boolean,default:!1},clickableMoreTimes:{type:Boolean,default:!1},onButtonClick:{type:Function}},components:{ButtonLoader:r.a,ButtonWithLoader:c.b},filters:{translate:i.a},computed:{btnState:function(){return this.$store.getters[a.CART_GETTERS.IS_PRODUCT_IN_CART](this.product.variantId||this.product.bonusSetId)?c.a.DONE:c.a.DEFAULT}},methods:{add:function(){this.product.bundles=JSON.stringify(l.a.buildPayload(this.bundles));var t=function(t){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{};e%2?u(Object(n),!0).forEach((function(e){d(t,e,n[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(n)):u(Object(n)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(n,e))}))}return t}({},this.product,{amount:this.amount});this.$store.dispatch(a.CART_ACTIONS.ADD_ARTICLE,t),this.onButtonClick&&this.onButtonClick(),this.redirectUrl&&this.$store.dispatch(a.CART_ACTIONS.SET_REDIRECT_URL,this.redirectUrl)}}}},386:function(t,e,n){"use strict";e.a={data:function(){return{lazyLoaded:!1}},methods:{renderLazyParts:function(){this.lazyLoaded=!0}},mounted:function(){window.requestIdleCallback instanceof Function?requestIdleCallback(this.renderLazyParts):setTimeout(this.renderLazyParts,100)}}},475:function(t,e,n){"use strict";function a(t){return(a="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t})(t)}n.d(e,"a",(function(){return i}));var i={buildPayload:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};if("object"!==a(t))return{};if(!t||!Object.keys(t).length)return{};var e=Object.assign({},t),n={};for(var i in e)if(e.hasOwnProperty(i)){n[i]=[];var r=e[i],s=r.active,o=r.data;if(s&&o)for(var c in o)o.hasOwnProperty(c)&&o[c]&&n[i].push(c)}return n}}},483:function(t,e){t.exports='<div class="circle-spinner--wrapper">\n\t<spinner />\n</div>\n'},484:function(t,e){t.exports='\x3c!-- {{ \'cta_buy_now\' | translate }} --\x3e\n\x3c!-- {{ \'cta_added\' | translate }} --\x3e\n\x3c!--{{ \'deferred_payment_promobox_modal_button\' | translate }}--\x3e\n\n\n<button-with-loader\n    :is-bold="isBold"\n    class="btn btn--primary"\n    :btnState="btnState"\n    :btnClicked="add"\n    :customContent="true"\n    :overrideClass="overrideClass"\n    :clickableMoreTimes="clickableMoreTimes"\n>\n    <div class="btn-inner" slot="customContent">\n        <template v-if="!customContent">\n            <span class="btn-inset lay-block">\n                <slot name="icon" /> \x3c!-- there must be new line here to have correct space before text --\x3e\n                {{ btnText | translate }}\n            </span>\n            <span class="btn-inset--added">{{ \'cta_added\' | translate }}</span>\n        </template>\n        <slot v-else name="customContent" />\n    </div>\n</button-with-loader>\n'},531:function(t,e,n){"use strict";n.d(e,"a",(function(){return a})),n.d(e,"e",(function(){return i})),n.d(e,"d",(function(){return r})),n.d(e,"c",(function(){return s})),n.d(e,"b",(function(){return o}));var a="Not implemented yet",i="time-seconds",r="time-minutes",s="time-hours",o="time-days"},730:function(t,e,n){"use strict";n.d(e,"a",(function(){return a}));var a=1500},830:function(t,e,n){"use strict";var a=n(357);e.a={bind:function(t){t.__clickHandler=function(e){e.preventDefault();var n=t.getAttribute("data-video");a.a.play(n)},t.addEventListener("click",t.__clickHandler)},unbind:function(t){t.removeEventListener("click",t.__clickHandler)}}},902:function(t,e,n){"use strict";n.r(e);var a=n(2),i=n(176),r=n(531);function s(t,e,n){return e in t?Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[e]=n,t}var o={filters:{translate:a.a},props:{endTime:{type:String|Number,default:void 0},startTimeString:{type:String,default:void 0},endTimeString:{type:String,default:void 0},format:{type:String,default:""},inflection:{type:String,default:void 0},withDays:{type:String,default:void 0},withSeconds:{type:String,default:void 0},timerTitle:{type:String,default:void 0},isTimestamp:{type:Boolean,default:!1}},data:function(){return{secondsText:"",seconds:"",minutes:"",hours:"",minutesText:"",hoursText:"",days:"",daysText:"",daysActive:!1,intervalId:function(){},timerActive:!1,isEnding:!1,jsEndTime:"",isProductDetailBF:!1,withDaysData:!1}},computed:{containerClass:function(){var t;return s(t={"countdown-timer":!0},this.format,!0),s(t,"alert",this.isEnding),t},showInflectedTime:function(){return this.inflection&&this.timerActive}},created:function(){this.jsEndTime=this.isTimestamp?this.endTime:"".concat(this.endTime).concat("0").concat("0").concat("0"),this.isProductDetailBF=this.format&&"product-detail-bf"===this.format,this.withDaysData="true"===this.withDays||!0===this.withDays,this.initCountDown(),this.updateTimer()},methods:{initCountDown:function(){if(this.timerActive=!0,this.startTimeString){var t=this.getTimestamp(this.startTimeString);this.timerActive=!(this.getCurrentTime()<t)}this.endTimeString&&(this.jsEndTime=this.getTimestamp(this.endTimeString)),this.getCurrentTime()>this.jsEndTime&&(this.timerActive=!1),this.intervalId=setInterval(this.updateTimer,1e3),this.resolveInflection()},updateTimer:function(){var t=this.jsEndTime-this.getCurrentTime(),e=t/36e5;if(this.setActiveTimer(t),t<=0)return this.timerActive=!1,void clearInterval(this.intervalId);this.isProductDetailBF&&e<72&&(this.withDaysData=!1,this.daysActive=!1),this.withDaysData&&(this.daysActive=!0,this.days=this.getFormattedNumber(t/864e5,!1),"0"!==this.days&&"00"!==this.days||(this.daysActive=!1)),this.withDaysData&&(e%=24),this.hours=this.getFormattedNumber(e),this.minutes=this.getFormattedNumber(t/6e4%60),this.seconds=this.getFormattedNumber(t/1e3%60),this.resolveInflection()},getCurrentTime:function(){return(new Date).getTime()},getTimestamp:function(t){return new Date(t).getTime()},getFormattedNumber:function(t){var e=!(arguments.length>1&&void 0!==arguments[1])||arguments[1];return e&&t<10?"".concat("0").concat(Math.floor(t)).slice(-2):String(Math.floor(t)).slice(-3)},setActiveTimer:function(t){this.isEnding=t<6e4},resolveInflection:function(){"shorthand"!==this.inflection||this.isProductDetailBF?(this.daysActive&&(this.daysText=""===this.days?"":Object(i.a)(this.days,r.b)),this.hoursText=""===this.hours?"":Object(i.a)(this.hours,r.c),this.minutesText=""===this.minutes?"":Object(i.a)(this.minutes,r.d),this.secondsText=""===this.seconds?"":Object(i.a)(this.seconds,r.e)):(this.daysActive&&(this.daysText=Object(a.a)("days_shorthand")),this.hoursText=Object(a.a)("hours_shorthand"),this.minutesText=Object(a.a)("minutes_shorthand"),this.secondsText=Object(a.a)("seconds_shorthand"))}}},c=n(1),l=Object(c.a)(o,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return t.endTime?n("div",{class:t.containerClass},[n("span",{staticClass:"countdown-wrapper"},[t.timerTitle?n("h3",{staticClass:"countdown-timer-title"},[t._v(t._s(t._f("translate")(t.timerActive?t.timerTitle:"product-box-offer-ended")))]):t._e(),t.isProductDetailBF?[t.timerActive?n("span",{staticClass:"countdown-timer-time time-default"},[t.daysActive?n("span",[t._v("\n          "+t._s(t.days)+" "+t._s(t.daysText)+"\n        ")]):n("span",[t._v(t._s(t.hours)+":"+t._s(t.minutes)+":"+t._s(t.seconds))])]):t._e()]:[t.showInflectedTime?n("span",{staticClass:"countdown-timer-time time-inflection"},[t.daysActive?n("span",{staticClass:"time-value-day"},[n("span",{staticClass:"time-value"},[t._v(t._s(t.days))]),t._v(" "),n("span",{staticClass:"time-text"},[t._v(t._s(t.daysText))])]):t._e(),n("span",{staticClass:"time-value"},[t._v(t._s(t.hours))]),t._v(" "),n("span",{staticClass:"time-text"},[t._v(t._s(t.hoursText))]),n("span",{staticClass:"time-value"},[t._v(t._s(t.minutes))]),t._v(" "),n("span",{staticClass:"time-text"},[t._v(t._s(t.minutesText))]),!t.daysActive||t.withSeconds?n("span",{staticClass:"time-value-sec"},[n("span",{staticClass:"time-value"},[t._v(t._s(t.seconds))]),t._v(" "),n("span",{staticClass:"time-text"},[t._v(t._s(t.secondsText))])]):t._e()]):n("span",{staticClass:"countdown-timer-time time-default"},[t.daysActive?n("span",[t._v("\n          "+t._s(t.days)+":\n        ")]):t._e(),n("span",[t._v(t._s(t.hours)+":"+t._s(t.minutes))]),t.daysActive?t._e():n("span",[t._v(":"+t._s(t.seconds))])])]],2)]):t._e()}),[],!1,null,null,null);e.default=l.exports},985:function(t,e,n){var a=n(1255);"string"==typeof a&&(a=[[t.i,a,""]]),a.locals&&(t.exports=a.locals);(0,n(10).default)("7662f4af",a,!0,{})},986:function(t,e,n){var a=n(1257);"string"==typeof a&&(a=[[t.i,a,""]]),a.locals&&(t.exports=a.locals);(0,n(10).default)("736c3590",a,!0,{})}}]);
//# sourceMappingURL=banner-wrapper.e2accc149e42af3bc747.js.map