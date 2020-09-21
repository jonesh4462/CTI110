<!DOCTYPE html>
<!-- saved from url=(0077)https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/12 -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="X-UA-Compatible" content="IE=11">
    <title>1.12. zyLab training: Basics</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="https://learn.zybooks.com/assets/favicon.ico">

    
<meta name="zybooks-web/config/environment" content="%7B%22environment%22%3A%22production%22%2C%22locationType%22%3A%22auto%22%2C%22modulePrefix%22%3A%22zybooks-web%22%2C%22rootURL%22%3A%22%2F%22%2C%22EmberENV%22%3A%7B%22FEATURES%22%3A%7B%7D%2C%22EXTEND_PROTOTYPES%22%3Atrue%7D%2C%22APP%22%3A%7B%22AUTHORS_ONLY%22%3Afalse%2C%22BUILDKEY%22%3A%22dad37ff3-9e0d-fb6b-46aa-ed7b892e520b%22%2C%22CLOUDSEARCH_ENDPOINT%22%3A%22https%3A%2F%2Foqsgv0xbv7.execute-api.us-west-2.amazonaws.com%2Fproduction%22%2C%22DISABLE_EVENTS%22%3Afalse%2C%22EVENTS_API_TARGET%22%3A%22v1%2Fstream%22%2C%22EVENTS_API_HOST%22%3A%22https%3A%2F%2Fzyevents.zybooks.com%2F%22%2C%22ACCESS_DEV%22%3Afalse%2C%22ADMIN_URL%22%3A%22https%3A%2F%2Fadmin.zybooks.com%22%2C%22NEW_RELIC_LICENSE_KEY%22%3A%2245d36ecda8%22%2C%22NEW_RELIC_APP_ID%22%3A%2287357829%22%2C%22SALES_URL%22%3A%22https%3A%2F%2Fsales.zybooks.com%22%2C%22API_HOST%22%3A%22https%3A%2F%2Fzyserver.zybooks.com%2Fv1%2F%22%2C%22WEBINAR_URL%22%3A%22https%3A%2F%2Fzoom.us%2Fwebinar%2Fregister%2FWN_W-XikM7mSu6gP21XOXoH-g%22%2C%22ZYBOOKS_URL%22%3A%22learn.zybooks.com%22%2C%22ZYSERVER2_API_HOST%22%3A%22https%3A%2F%2Fzyserver2.zybooks.com%2Fv1%2F%22%2C%22ZYSERVER2_DR_API_HOST%22%3A%22https%3A%2F%2Fzyserver2.zybooks.com%2Fv1%2F%22%2C%22TERMINAL_SOCKET_URL%22%3A%22wss%3A%2F%2Fzyterminal.zybooks.com%2Fws%22%2C%22SESSION_KEY_SUFFIX%22%3A%225%22%2C%22WHAT_IS_ZYBOOK_VIDEO_URL%22%3A%22https%3A%2F%2Fvimeo.com%2F285133146%2F48bc90afb5%22%7D%2C%22contentSecurityPolicy%22%3A%7B%22connect-src%22%3A%22&#39;self&#39;%20www.google-analytics.com%20https%3A%2F%2Ffonts.googleapis.com%20https%3A%2F%2F*.nr-data.net%20https%3A%2F%2Fzyserver.zybooks.com%2Fv1%2F%22%2C%22default-src%22%3A%22&#39;none&#39;%22%2C%22font-src%22%3A%22&#39;self&#39;%20fonts.gstatic.com%20%22%2C%22img-src%22%3A%22&#39;self&#39;%20http%3A%2F%2Fupload.wikimedia.org.com%2F%20https%3A%2F%2F*.nr-data.net%22%2C%22media-src%22%3A%22&#39;self&#39;%22%2C%22script-src%22%3A%22&#39;self&#39;%20&#39;unsafe-inline&#39;%20&#39;unsafe-eval&#39;%20http%3A%2F%2F*.newrelic.com%20https%3A%2F%2F*.nr-data.net%20http%3A%2F%2F*.nr-data.net%22%2C%22style-src%22%3A%22&#39;self&#39;%20&#39;unsafe-inline&#39;%20https%3A%2F%2Ffonts.googleapis.com%22%7D%2C%22intercom%22%3A%7B%22appId%22%3A%22jac28hwh%22%2C%22enabled%22%3Atrue%2C%22userProperties%22%3A%7B%22createdAtProp%22%3A%22createdAt%22%2C%22emailProp%22%3A%22email%22%2C%22nameProp%22%3A%22name%22%2C%22userHashProp%22%3A%22hash%22%2C%22userIdProp%22%3A%22id%22%7D%7D%2C%22metricsAdapters%22%3A%5B%7B%22name%22%3A%22GoogleAnalytics%22%2C%22environments%22%3A%5B%22development%22%2C%22staging%22%2C%22production%22%5D%2C%22config%22%3A%7B%22id%22%3A%22UA-43181201-3%22%2C%22debug%22%3Afalse%2C%22trace%22%3Afalse%2C%22sendHitTask%22%3Atrue%2C%22require%22%3A%5B%22ecommerce%22%5D%7D%7D%5D%2C%22stripe%22%3A%7B%22publishableKey%22%3A%22pk_live_6WfpM1NZl9sSnKivV9WvGD2H%22%7D%2C%22moment%22%3A%7B%22includeTimezone%22%3A%22subset%22%7D%2C%22ember-froala-editor%22%3A%7B%22key%22%3A%22vA2A6A6D6E5E3iB3B9B6B5C2C4G5H3I3H3C-22NGNb1IODMGYNSFKV%3D%3D%22%7D%2C%22exportApplicationGlobal%22%3Afalse%2C%22ember-websockets%22%3A%7B%22socketIO%22%3Afalse%7D%2C%22resourceHost%22%3A%22https%3A%2F%2Fzytools.zybooks.com%2FzyBooks2%2F%22%2C%22staticResourceHost%22%3A%22https%3A%2F%2Fstatic-resources.zybooks.com%2F%22%2C%22imageHost%22%3A%22https%3A%2F%2Fzytools.zybooks.com%2FzyAuthor%2F%22%2C%22zydeHost%22%3A%22http%3A%2F%2Fzyde2.zyante.com%22%2C%22terminalSocketUrl%22%3A%22wss%3A%2F%2Fzyterminal.dev.kube.zybooks.com%2Fws%22%7D">
    
                <script type="text/javascript" async="" src="./P1LAB1_JonesHydeia_files/ecommerce.js.download"></script><script async="" src="./P1LAB1_JonesHydeia_files/analytics.js.download"></script><script type="text/javascript" src="./P1LAB1_JonesHydeia_files/45d36ecda8"></script><script src="./P1LAB1_JonesHydeia_files/nr-spa-1071.min.js.download"></script><script type="text/javascript" async="" src="./P1LAB1_JonesHydeia_files/jac28hwh"></script><script type="text/javascript">
window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var o=e[n]={exports:{}};t[n][0].call(o.exports,function(e){var o=t[n][1][e];return r(o||e)},o,o.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(t,e,n){function r(t){try{c.console&&console.log(t)}catch(e){}}var o,i=t("ee"),a=t(20),c={};try{o=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(c.console=!0,o.indexOf("dev")!==-1&&(c.dev=!0),o.indexOf("nr_dev")!==-1&&(c.nrDev=!0))}catch(s){}c.nrDev&&i.on("internal-error",function(t){r(t.stack)}),c.dev&&i.on("fn-err",function(t,e,n){r(n.stack)}),c.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(c,function(t,e){return t}).join(", ")))},{}],2:[function(t,e,n){function r(t,e,n,r,c){try{h?h-=1:o(c||new UncaughtException(t,e,n),!0)}catch(f){try{i("ierr",[f,s.now(),!0])}catch(d){}}return"function"==typeof u&&u.apply(this,a(arguments))}function UncaughtException(t,e,n){this.message=t||"Uncaught error with no additional information",this.sourceURL=e,this.line=n}function o(t,e){var n=e?null:s.now();i("err",[t,n])}var i=t("handle"),a=t(21),c=t("ee"),s=t("loader"),f=t("gos"),u=window.onerror,d=!1,p="nr@seenError",h=0;s.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(l){"stack"in l&&(t(13),t(12),"addEventListener"in window&&t(6),s.xhrWrappable&&t(14),d=!0)}c.on("fn-start",function(t,e,n){d&&(h+=1)}),c.on("fn-err",function(t,e,n){d&&!n[p]&&(f(n,p,function(){return!0}),this.thrown=!0,o(n))}),c.on("fn-end",function(){d&&!this.thrown&&h>0&&(h-=1)}),c.on("internal-error",function(t){i("ierr",[t,s.now(),!0])})},{}],3:[function(t,e,n){t("loader").features.ins=!0},{}],4:[function(t,e,n){function r(){M++,S=y.hash,this[u]=b.now()}function o(){M--,y.hash!==S&&i(0,!0);var t=b.now();this[l]=~~this[l]+t-this[u],this[d]=t}function i(t,e){E.emit("newURL",[""+y,e])}function a(t,e){t.on(e,function(){this[e]=b.now()})}var c="-start",s="-end",f="-body",u="fn"+c,d="fn"+s,p="cb"+c,h="cb"+s,l="jsTime",m="fetch",v="addEventListener",w=window,y=w.location,b=t("loader");if(w[v]&&b.xhrWrappable){var g=t(10),x=t(11),E=t(8),P=t(6),O=t(13),R=t(7),T=t(14),L=t(9),j=t("ee"),N=j.get("tracer");t(15),b.features.spa=!0;var S,M=0;j.on(u,r),j.on(p,r),j.on(d,o),j.on(h,o),j.buffer([u,d,"xhr-done","xhr-resolved"]),P.buffer([u]),O.buffer(["setTimeout"+s,"clearTimeout"+c,u]),T.buffer([u,"new-xhr","send-xhr"+c]),R.buffer([m+c,m+"-done",m+f+c,m+f+s]),E.buffer(["newURL"]),g.buffer([u]),x.buffer(["propagate",p,h,"executor-err","resolve"+c]),N.buffer([u,"no-"+u]),L.buffer(["new-jsonp","cb-start","jsonp-error","jsonp-end"]),a(T,"send-xhr"+c),a(j,"xhr-resolved"),a(j,"xhr-done"),a(R,m+c),a(R,m+"-done"),a(L,"new-jsonp"),a(L,"jsonp-end"),a(L,"cb-start"),E.on("pushState-end",i),E.on("replaceState-end",i),w[v]("hashchange",i,!0),w[v]("load",i,!0),w[v]("popstate",function(){i(0,M>1)},!0)}},{}],5:[function(t,e,n){function r(t){}if(window.performance&&window.performance.timing&&window.performance.getEntriesByType){var o=t("ee"),i=t("handle"),a=t(13),c=t(12),s="learResourceTimings",f="addEventListener",u="resourcetimingbufferfull",d="bstResource",p="resource",h="-start",l="-end",m="fn"+h,v="fn"+l,w="bstTimer",y="pushState",b=t("loader");b.features.stn=!0,t(8);var g=NREUM.o.EV;o.on(m,function(t,e){var n=t[0];n instanceof g&&(this.bstStart=b.now())}),o.on(v,function(t,e){var n=t[0];n instanceof g&&i("bst",[n,e,this.bstStart,b.now()])}),a.on(m,function(t,e,n){this.bstStart=b.now(),this.bstType=n}),a.on(v,function(t,e){i(w,[e,this.bstStart,b.now(),this.bstType])}),c.on(m,function(){this.bstStart=b.now()}),c.on(v,function(t,e){i(w,[e,this.bstStart,b.now(),"requestAnimationFrame"])}),o.on(y+h,function(t){this.time=b.now(),this.startPath=location.pathname+location.hash}),o.on(y+l,function(t){i("bstHist",[location.pathname+location.hash,this.startPath,this.time])}),f in window.performance&&(window.performance["c"+s]?window.performance[f](u,function(t){i(d,[window.performance.getEntriesByType(p)]),window.performance["c"+s]()},!1):window.performance[f]("webkit"+u,function(t){i(d,[window.performance.getEntriesByType(p)]),window.performance["webkitC"+s]()},!1)),document[f]("scroll",r,{passive:!0}),document[f]("keypress",r,!1),document[f]("click",r,!1)}},{}],6:[function(t,e,n){function r(t){for(var e=t;e&&!e.hasOwnProperty(u);)e=Object.getPrototypeOf(e);e&&o(e)}function o(t){c.inPlace(t,[u,d],"-",i)}function i(t,e){return t[1]}var a=t("ee").get("events"),c=t(23)(a,!0),s=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";e.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(o(window),o(f.prototype)),a.on(u+"-start",function(t,e){var n=t[1],r=s(n,"nr@wrapped",function(){function t(){if("function"==typeof n.handleEvent)return n.handleEvent.apply(n,arguments)}var e={object:t,"function":n}[typeof n];return e?c(e,"fn-",null,e.name||"anonymous"):n});this.wrapped=t[1]=r}),a.on(d+"-start",function(t){t[1]=this.wrapped||t[1]})},{}],7:[function(t,e,n){function r(t,e,n){var r=t[e];"function"==typeof r&&(t[e]=function(){var t=r.apply(this,arguments);return o.emit(n+"start",arguments,t),t.then(function(e){return o.emit(n+"end",[null,e],t),e},function(e){throw o.emit(n+"end",[e],t),e})})}var o=t("ee").get("fetch"),i=t(20);e.exports=o;var a=window,c="fetch-",s=c+"body-",f=["arrayBuffer","blob","json","text","formData"],u=a.Request,d=a.Response,p=a.fetch,h="prototype";u&&d&&p&&(i(f,function(t,e){r(u[h],e,s),r(d[h],e,s)}),r(a,"fetch",c),o.on(c+"end",function(t,e){var n=this;e?e.clone().arrayBuffer().then(function(t){n.rxSize=t.byteLength,o.emit(c+"done",[null,e],n)}):o.emit(c+"done",[t],n)}))},{}],8:[function(t,e,n){var r=t("ee").get("history"),o=t(23)(r);e.exports=r,o.inPlace(window.history,["pushState","replaceState"],"-")},{}],9:[function(t,e,n){function r(t){function e(){s.emit("jsonp-end",[],p),t.removeEventListener("load",e,!1),t.removeEventListener("error",n,!1)}function n(){s.emit("jsonp-error",[],p),s.emit("jsonp-end",[],p),t.removeEventListener("load",e,!1),t.removeEventListener("error",n,!1)}var r=t&&"string"==typeof t.nodeName&&"script"===t.nodeName.toLowerCase();if(r){var o="function"==typeof t.addEventListener;if(o){var a=i(t.src);if(a){var u=c(a),d="function"==typeof u.parent[u.key];if(d){var p={};f.inPlace(u.parent,[u.key],"cb-",p),t.addEventListener("load",e,!1),t.addEventListener("error",n,!1),s.emit("new-jsonp",[t.src],p)}}}}}function o(){return"addEventListener"in window}function i(t){var e=t.match(u);return e?e[1]:null}function a(t,e){var n=t.match(p),r=n[1],o=n[3];return o?a(o,e[r]):e[r]}function c(t){var e=t.match(d);return e&&e.length>=3?{key:e[2],parent:a(e[1],window)}:{key:t,parent:window}}var s=t("ee").get("jsonp"),f=t(23)(s);if(e.exports=s,o()){var u=/[?&](?:callback|cb)=([^&#]+)/,d=/(.*).([^.]+)/,p=/^(w+)(.|$)(.*)$/,h=["appendChild","insertBefore","replaceChild"];f.inPlace(HTMLElement.prototype,h,"dom-"),f.inPlace(HTMLHeadElement.prototype,h,"dom-"),f.inPlace(HTMLBodyElement.prototype,h,"dom-"),s.on("dom-start",function(t){r(t[0])})}},{}],10:[function(t,e,n){var r=t("ee").get("mutation"),o=t(23)(r),i=NREUM.o.MO;e.exports=r,i&&(window.MutationObserver=function(t){return this instanceof i?new i(o(t,"fn-")):i.apply(this,arguments)},MutationObserver.prototype=i.prototype)},{}],11:[function(t,e,n){function r(t){var e=a.context(),n=c(t,"executor-",e),r=new f(n);return a.context(r).getCtx=function(){return e},a.emit("new-promise",[r,e],e),r}function o(t,e){return e}var i=t(23),a=t("ee").get("promise"),c=i(a),s=t(20),f=NREUM.o.PR;e.exports=a,f&&(window.Promise=r,["all","race"].forEach(function(t){var e=f[t];f[t]=function(n){function r(t){return function(){a.emit("propagate",[null,!o],i),o=o||!t}}var o=!1;s(n,function(e,n){Promise.resolve(n).then(r("all"===t),r(!1))});var i=e.apply(f,arguments),c=f.resolve(i);return c}}),["resolve","reject"].forEach(function(t){var e=f[t];f[t]=function(t){var n=e.apply(f,arguments);return t!==n&&a.emit("propagate",[t,!0],n),n}}),f.prototype["catch"]=function(t){return this.then(null,t)},f.prototype=Object.create(f.prototype,{constructor:{value:r}}),s(Object.getOwnPropertyNames(f),function(t,e){try{r[e]=f[e]}catch(n){}}),a.on("executor-start",function(t){t[0]=c(t[0],"resolve-",this),t[1]=c(t[1],"resolve-",this)}),a.on("executor-err",function(t,e,n){t[1](n)}),c.inPlace(f.prototype,["then"],"then-",o),a.on("then-start",function(t,e){this.promise=e,t[0]=c(t[0],"cb-",this),t[1]=c(t[1],"cb-",this)}),a.on("then-end",function(t,e,n){this.nextPromise=n;var r=this.promise;a.emit("propagate",[r,!0],n)}),a.on("cb-end",function(t,e,n){a.emit("propagate",[n,!0],this.nextPromise)}),a.on("propagate",function(t,e,n){this.getCtx&&!e||(this.getCtx=function(){if(t instanceof Promise)var e=a.context(t);return e&&e.getCtx?e.getCtx():this})}),r.toString=function(){return""+f})},{}],12:[function(t,e,n){var r=t("ee").get("raf"),o=t(23)(r),i="equestAnimationFrame";e.exports=r,o.inPlace(window,["r"+i,"mozR"+i,"webkitR"+i,"msR"+i],"raf-"),r.on("raf-start",function(t){t[0]=o(t[0],"fn-")})},{}],13:[function(t,e,n){function r(t,e,n){t[0]=a(t[0],"fn-",null,n)}function o(t,e,n){this.method=n,this.timerDuration=isNaN(t[1])?0:+t[1],t[0]=a(t[0],"fn-",this,n)}var i=t("ee").get("timer"),a=t(23)(i),c="setTimeout",s="setInterval",f="clearTimeout",u="-start",d="-";e.exports=i,a.inPlace(window,[c,"setImmediate"],c+d),a.inPlace(window,[s],s+d),a.inPlace(window,[f,"clearImmediate"],f+d),i.on(s+u,r),i.on(c+u,o)},{}],14:[function(t,e,n){function r(t,e){d.inPlace(e,["onreadystatechange"],"fn-",c)}function o(){var t=this,e=u.context(t);t.readyState>3&&!e.resolved&&(e.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,y,"fn-",c)}function i(t){b.push(t),l&&(x?x.then(a):v?v(a):(E=-E,P.data=E))}function a(){for(var t=0;t<b.length;t++)r([],b[t]);b.length&&(b=[])}function c(t,e){return e}function s(t,e){for(var n in t)e[n]=t[n];return e}t(6);var f=t("ee"),u=f.get("xhr"),d=t(23)(u),p=NREUM.o,h=p.XHR,l=p.MO,m=p.PR,v=p.SI,w="readystatechange",y=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],b=[];e.exports=u;var g=window.XMLHttpRequest=function(t){var e=new h(t);try{u.emit("new-xhr",[e],e),e.addEventListener(w,o,!1)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}return e};if(s(h,g),g.prototype=h.prototype,d.inPlace(g.prototype,["open","send"],"-xhr-",c),u.on("send-xhr-start",function(t,e){r(t,e),i(e)}),u.on("open-xhr-start",r),l){var x=m&&m.resolve();if(!v&&!m){var E=1,P=document.createTextNode(E);new l(a).observe(P,{characterData:!0})}}else f.on("fn-end",function(t){t[0]&&t[0].type===w||a()})},{}],15:[function(t,e,n){function r(t){var e=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<d;r++)t.removeEventListener(u[r],this.listener,!1);if(!e.aborted){if(n.duration=a.now()-this.startTime,4===t.readyState){e.status=t.status;var i=o(t,this.lastSize);if(i&&(n.rxSize=i),this.sameOrigin){var s=t.getResponseHeader("X-NewRelic-App-Data");s&&(e.cat=s.split(", ").pop())}}else e.status=0;n.cbTime=this.cbTime,f.emit("xhr-done",[t],t),c("xhr",[e,n,this.startTime])}}}function o(t,e){var n=t.responseType;if("json"===n&&null!==e)return e;var r="arraybuffer"===n||"blob"===n||"json"===n?t.response:t.responseText;return l(r)}function i(t,e){var n=s(e),r=t.params;r.host=n.hostname+":"+n.port,r.pathname=n.pathname,t.sameOrigin=n.sameOrigin}var a=t("loader");if(a.xhrWrappable){var c=t("handle"),s=t(16),f=t("ee"),u=["load","error","abort","timeout"],d=u.length,p=t("id"),h=t(19),l=t(18),m=window.XMLHttpRequest;a.features.xhr=!0,t(14),f.on("new-xhr",function(t){var e=this;e.totalCbs=0,e.called=0,e.cbTime=0,e.end=r,e.ended=!1,e.xhrGuids={},e.lastSize=null,h&&(h>34||h<10)||window.opera||t.addEventListener("progress",function(t){e.lastSize=t.loaded},!1)}),f.on("open-xhr-start",function(t){this.params={method:t[0]},i(this,t[1]),this.metrics={}}),f.on("open-xhr-end",function(t,e){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&e.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid)}),f.on("send-xhr-start",function(t,e){var n=this.metrics,r=t[0],o=this;if(n&&r){var i=l(r);i&&(n.txSize=i)}this.startTime=a.now(),this.listener=function(t){try{"abort"===t.type&&(o.params.aborted=!0),("load"!==t.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof e.onload))&&o.end(e)}catch(n){try{f.emit("internal-error",[n])}catch(r){}}};for(var c=0;c<d;c++)e.addEventListener(u[c],this.listener,!1)}),f.on("xhr-cb-time",function(t,e,n){this.cbTime+=t,e?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof n.onload||this.end(n)}),f.on("xhr-load-added",function(t,e){var n=""+p(t)+!!e;this.xhrGuids&&!this.xhrGuids[n]&&(this.xhrGuids[n]=!0,this.totalCbs+=1)}),f.on("xhr-load-removed",function(t,e){var n=""+p(t)+!!e;this.xhrGuids&&this.xhrGuids[n]&&(delete this.xhrGuids[n],this.totalCbs-=1)}),f.on("addEventListener-end",function(t,e){e instanceof m&&"load"===t[0]&&f.emit("xhr-load-added",[t[1],t[2]],e)}),f.on("removeEventListener-end",function(t,e){e instanceof m&&"load"===t[0]&&f.emit("xhr-load-removed",[t[1],t[2]],e)}),f.on("fn-start",function(t,e,n){e instanceof m&&("onload"===n&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=a.now()))}),f.on("fn-end",function(t,e){this.xhrCbStart&&f.emit("xhr-cb-time",[a.now()-this.xhrCbStart,this.onload,e],e)})}},{}],16:[function(t,e,n){e.exports=function(t){var e=document.createElement("a"),n=window.location,r={};e.href=t,r.port=e.port;var o=e.href.split("://");!r.port&&o[1]&&(r.port=o[1].split("/")[0].split("@").pop().split(":")[1]),r.port&&"0"!==r.port||(r.port="https"===o[0]?"443":"80"),r.hostname=e.hostname||n.hostname,r.pathname=e.pathname,r.protocol=o[0],"/"!==r.pathname.charAt(0)&&(r.pathname="/"+r.pathname);var i=!e.protocol||":"===e.protocol||e.protocol===n.protocol,a=e.hostname===document.domain&&e.port===n.port;return r.sameOrigin=i&&(!e.hostname||a),r}},{}],17:[function(t,e,n){function r(){}function o(t,e,n){return function(){return i(t,[f.now()].concat(c(arguments)),e?null:this,n),e?void 0:this}}var i=t("handle"),a=t(20),c=t(21),s=t("ee").get("tracer"),f=t("loader"),u=NREUM;"undefined"==typeof window.newrelic&&(newrelic=u);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],p="api-",h=p+"ixn-";a(d,function(t,e){u[e]=o(p+e,!0,"api")}),u.addPageAction=o(p+"addPageAction",!0),u.setCurrentRouteName=o(p+"routeName",!0),e.exports=newrelic,u.interaction=function(){return(new r).get()};var l=r.prototype={createTracer:function(t,e){var n={},r=this,o="function"==typeof e;return i(h+"tracer",[f.now(),t,n],r),function(){if(s.emit((o?"":"no-")+"fn-start",[f.now(),r,o],n),o)try{return e.apply(this,arguments)}catch(t){throw s.emit("fn-err",[arguments,this,t],n),t}finally{s.emit("fn-end",[f.now()],n)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){l[e]=o(h+e)}),newrelic.noticeError=function(t){"string"==typeof t&&(t=new Error(t)),i("err",[t,f.now()])}},{}],18:[function(t,e,n){e.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(e){return}}}},{}],19:[function(t,e,n){var r=0,o=navigator.userAgent.match(/Firefox[/s](d+.d+)/);o&&(r=+o[1]),e.exports=r},{}],20:[function(t,e,n){function r(t,e){var n=[],r="",i=0;for(r in t)o.call(t,r)&&(n[i]=e(r,t[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],21:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,o=n-e||0,i=Array(o<0?0:o);++r<o;)i[r]=t[e+r];return i}e.exports=r},{}],22:[function(t,e,n){e.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],23:[function(t,e,n){function r(t){return!(t&&t instanceof Function&&t.apply&&!t[a])}var o=t("ee"),i=t(21),a="nr@original",c=Object.prototype.hasOwnProperty,s=!1;e.exports=function(t,e){function n(t,e,n,o){function nrWrapper(){var r,a,c,s;try{a=this,r=i(arguments),c="function"==typeof n?n(r,a):n||{}}catch(f){p([f,"",[r,a,o],c])}u(e+"start",[r,a,o],c);try{return s=t.apply(a,r)}catch(d){throw u(e+"err",[r,a,d],c),d}finally{u(e+"end",[r,a,s],c)}}return r(t)?t:(e||(e=""),nrWrapper[a]=t,d(t,nrWrapper),nrWrapper)}function f(t,e,o,i){o||(o="");var a,c,s,f="-"===o.charAt(0);for(s=0;s<e.length;s++)c=e[s],a=t[c],r(a)||(t[c]=n(a,f?c+o:o,i,c))}function u(n,r,o){if(!s||e){var i=s;s=!0;try{t.emit(n,r,o,e)}catch(a){p([a,n,r,o])}s=i}}function d(t,e){if(Object.defineProperty&&Object.keys)try{var n=Object.keys(t);return n.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(r){p([r])}for(var o in t)c.call(t,o)&&(e[o]=t[o]);return e}function p(e){try{t.emit("internal-error",e)}catch(n){}}return t||(t=o),n.inPlace=f,n.flag=a,n}},{}],ee:[function(t,e,n){function r(){}function o(t){function e(t){return t&&t instanceof r?t:t?s(t,c,i):i()}function n(n,r,o,i){if(!p.aborted||i){t&&t(n,r,o);for(var a=e(o),c=l(n),s=c.length,f=0;f<s;f++)c[f].apply(a,r);var d=u[y[n]];return d&&d.push([b,n,r,a]),a}}function h(t,e){w[t]=l(t).concat(e)}function l(t){return w[t]||[]}function m(t){return d[t]=d[t]||o(n)}function v(t,e){f(t,function(t,n){e=e||"feature",y[n]=e,e in u||(u[e]=[])})}var w={},y={},b={on:h,emit:n,get:m,listeners:l,context:e,buffer:v,abort:a,aborted:!1};return b}function i(){return new r}function a(){(u.api||u.feature)&&(p.aborted=!0,u=p.backlog={})}var c="nr@context",s=t("gos"),f=t(20),u={},d={},p=e.exports=o();p.backlog=u},{}],gos:[function(t,e,n){function r(t,e,n){if(o.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return t[e]=r,r}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){o.buffer([t],r),o.emit(t,e,n)}var o=t("ee").get("handle");e.exports=r,r.ee=o},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,i,function(){return o++})}var o=1,i="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!x++){var t=g.info=NREUM.info,e=p.getElementsByTagName("script")[0];if(setTimeout(u.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&e))return u.abort();f(y,function(e,n){t[e]||(t[e]=n)}),s("mark",["onload",a()+g.offset],null,"api");var n=p.createElement("script");n.src="https://"+t.agent,e.parentNode.insertBefore(n,e)}}function o(){"complete"===p.readyState&&i()}function i(){s("mark",["domContent",a()+g.offset],null,"api")}function a(){return E.exists&&performance.now?Math.round(performance.now()):(c=Math.max((new Date).getTime(),c))-g.offset}var c=(new Date).getTime(),s=t("handle"),f=t(20),u=t("ee"),d=window,p=d.document,h="addEventListener",l="attachEvent",m=d.XMLHttpRequest,v=m&&m.prototype;NREUM.o={ST:setTimeout,SI:d.setImmediate,CT:clearTimeout,XHR:m,REQ:d.Request,EV:d.Event,PR:d.Promise,MO:d.MutationObserver};var w=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-spa-1071.min.js"},b=m&&v&&v[h]&&!/CriOS/.test(navigator.userAgent),g=e.exports={offset:c,now:a,origin:w,features:{},xhrWrappable:b};t(17),p[h]?(p[h]("DOMContentLoaded",i,!1),d[h]("load",r,!1)):(p[l]("onreadystatechange",o),d[l]("onload",r)),s("mark",["firstbyte",c],null,"api");var x=0,E=t(22)},{}]},{},["loader",2,15,5,3,4]);

            ;NREUM.info={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",licenseKey:"45d36ecda8",applicationID:"87357829",sa:1}
                </script>
            

    <link rel="stylesheet" href="./P1LAB1_JonesHydeia_files/vendor-2ef2ef625ea123bd9f6c5a70e70fc76f.css">
    <link rel="stylesheet" href="./P1LAB1_JonesHydeia_files/zybooks-web-1df6e58dbade11a2792c3d2960ca145e.css">
    <link href="./P1LAB1_JonesHydeia_files/css" rel="stylesheet" integrity="" crossorigin="anonymous">
    <link href="./P1LAB1_JonesHydeia_files/css(1)" rel="stylesheet">

    <script src="./P1LAB1_JonesHydeia_files/highlight.min.js.download"></script>
    <script type="text/javascript" src="./P1LAB1_JonesHydeia_files/MathJax.js.download" id="mathjax">
        MathJax.Hub.Register.MessageHook('Math Processing Error', message => {
            //  do something with the error.  message[2] is the Error object that records the problem.
            const error = message[2];

            console.error(error);

            try {
                newrelic.noticeError(error);
            }
            catch (err) {
                // Ignore
            }
        });
    </script>
    <script>
        MathJax.Hub.Queue([ 'setRenderer', MathJax.Hub, 'SVG' ]); // eslint-disable-line new-cap
    </script>

    <script src="./P1LAB1_JonesHydeia_files/vendor-239f93f559bcc3fa88c2d561c3525240.js.download"></script>
    <script src="./P1LAB1_JonesHydeia_files/zybooks-web-c83d026daa9c2857c767403848251999.js.download"></script>
    <script src="./P1LAB1_JonesHydeia_files/ace.js.download"></script><style id="ace_editor.css">.ace_editor {position: relative;overflow: hidden;font: 12px/normal 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'source-code-pro', monospace;direction: ltr;text-align: left;}.ace_scroller {position: absolute;overflow: hidden;top: 0;bottom: 0;background-color: inherit;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;cursor: text;}.ace_content {position: absolute;-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;min-width: 100%;}.ace_dragging .ace_scroller:before{position: absolute;top: 0;left: 0;right: 0;bottom: 0;content: '';background: rgba(250, 250, 250, 0.01);z-index: 1000;}.ace_dragging.ace_dark .ace_scroller:before{background: rgba(0, 0, 0, 0.01);}.ace_selecting, .ace_selecting * {cursor: text !important;}.ace_gutter {position: absolute;overflow : hidden;width: auto;top: 0;bottom: 0;left: 0;cursor: default;z-index: 4;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;}.ace_gutter-active-line {position: absolute;left: 0;right: 0;}.ace_scroller.ace_scroll-left {box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;}.ace_gutter-cell {padding-left: 19px;padding-right: 6px;background-repeat: no-repeat;}.ace_gutter-cell.ace_error {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: 2px center;}.ace_gutter-cell.ace_warning {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");background-position: 2px center;}.ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");background-position: 2px center;}.ace_dark .ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");}.ace_scrollbar {position: absolute;right: 0;bottom: 0;z-index: 6;}.ace_scrollbar-inner {position: absolute;cursor: text;left: 0;top: 0;}.ace_scrollbar-v{overflow-x: hidden;overflow-y: scroll;top: 0;}.ace_scrollbar-h {overflow-x: scroll;overflow-y: hidden;left: 0;}.ace_print-margin {position: absolute;height: 100%;}.ace_text-input {position: absolute;z-index: 0;width: 0.5em;height: 1em;opacity: 0;background: transparent;-moz-appearance: none;appearance: none;border: none;resize: none;outline: none;overflow: hidden;font: inherit;padding: 0 1px;margin: 0 -1px;text-indent: -1em;-ms-user-select: text;-moz-user-select: text;-webkit-user-select: text;user-select: text;white-space: pre!important;}.ace_text-input.ace_composition {background: inherit;color: inherit;z-index: 1000;opacity: 1;text-indent: 0;}.ace_layer {z-index: 1;position: absolute;overflow: hidden;word-wrap: normal;white-space: pre;height: 100%;width: 100%;-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;pointer-events: none;}.ace_gutter-layer {position: relative;width: auto;text-align: right;pointer-events: auto;}.ace_text-layer {font: inherit !important;}.ace_cjk {display: inline-block;text-align: center;}.ace_cursor-layer {z-index: 4;}.ace_cursor {z-index: 4;position: absolute;-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;border-left: 2px solid;transform: translatez(0);}.ace_slim-cursors .ace_cursor {border-left-width: 1px;}.ace_overwrite-cursors .ace_cursor {border-left-width: 0;border-bottom: 1px solid;}.ace_hidden-cursors .ace_cursor {opacity: 0.2;}.ace_smooth-blinking .ace_cursor {-webkit-transition: opacity 0.18s;transition: opacity 0.18s;}.ace_editor.ace_multiselect .ace_cursor {border-left-width: 1px;}.ace_marker-layer .ace_step, .ace_marker-layer .ace_stack {position: absolute;z-index: 3;}.ace_marker-layer .ace_selection {position: absolute;z-index: 5;}.ace_marker-layer .ace_bracket {position: absolute;z-index: 6;}.ace_marker-layer .ace_active-line {position: absolute;z-index: 2;}.ace_marker-layer .ace_selected-word {position: absolute;z-index: 4;-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;}.ace_line .ace_fold {-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;display: inline-block;height: 11px;margin-top: -2px;vertical-align: middle;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");background-repeat: no-repeat, repeat-x;background-position: center center, top left;color: transparent;border: 1px solid black;border-radius: 2px;cursor: pointer;pointer-events: auto;}.ace_dark .ace_fold {}.ace_fold:hover{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");}.ace_tooltip {background-color: #FFF;background-image: -webkit-linear-gradient(top, transparent, rgba(0, 0, 0, 0.1));background-image: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.1));border: 1px solid gray;border-radius: 1px;box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);color: black;max-width: 100%;padding: 3px 4px;position: fixed;z-index: 999999;-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;cursor: default;white-space: pre;word-wrap: break-word;line-height: normal;font-style: normal;font-weight: normal;letter-spacing: normal;pointer-events: none;}.ace_folding-enabled > .ace_gutter-cell {padding-right: 13px;}.ace_fold-widget {-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;margin: 0 -12px 0 1px;display: none;width: 11px;vertical-align: top;background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: center;border-radius: 3px;border: 1px solid transparent;cursor: pointer;}.ace_folding-enabled .ace_fold-widget {display: inline-block;   }.ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");}.ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");}.ace_fold-widget:hover {border: 1px solid rgba(0, 0, 0, 0.3);background-color: rgba(255, 255, 255, 0.2);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);}.ace_fold-widget:active {border: 1px solid rgba(0, 0, 0, 0.4);background-color: rgba(0, 0, 0, 0.05);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);}.ace_dark .ace_fold-widget {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");}.ace_dark .ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget:hover {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);background-color: rgba(255, 255, 255, 0.1);}.ace_dark .ace_fold-widget:active {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);}.ace_fold-widget.ace_invalid {background-color: #FFB4B4;border-color: #DE5555;}.ace_fade-fold-widgets .ace_fold-widget {-webkit-transition: opacity 0.4s ease 0.05s;transition: opacity 0.4s ease 0.05s;opacity: 0;}.ace_fade-fold-widgets:hover .ace_fold-widget {-webkit-transition: opacity 0.05s ease 0.05s;transition: opacity 0.05s ease 0.05s;opacity:1;}.ace_underline {text-decoration: underline;}.ace_bold {font-weight: bold;}.ace_nobold .ace_bold {font-weight: normal;}.ace_italic {font-style: italic;}.ace_error-marker {background-color: rgba(255, 0, 0,0.2);position: absolute;z-index: 9;}.ace_highlight-marker {background-color: rgba(255, 255, 0,0.2);position: absolute;z-index: 8;}.ace_br1 {border-top-left-radius    : 3px;}.ace_br2 {border-top-right-radius   : 3px;}.ace_br3 {border-top-left-radius    : 3px; border-top-right-radius:    3px;}.ace_br4 {border-bottom-right-radius: 3px;}.ace_br5 {border-top-left-radius    : 3px; border-bottom-right-radius: 3px;}.ace_br6 {border-top-right-radius   : 3px; border-bottom-right-radius: 3px;}.ace_br7 {border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px;}.ace_br8 {border-bottom-left-radius : 3px;}.ace_br9 {border-top-left-radius    : 3px; border-bottom-left-radius:  3px;}.ace_br10{border-top-right-radius   : 3px; border-bottom-left-radius:  3px;}.ace_br11{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-left-radius:  3px;}.ace_br12{border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br13{border-top-left-radius    : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br14{border-top-right-radius   : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br15{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;}
/*# sourceURL=ace/css/ace_editor.css */</style><style id="ace-tm">.ace-tm .ace_gutter {background: #f0f0f0;color: #333;}.ace-tm .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-tm .ace_fold {background-color: #6B72E6;}.ace-tm {background-color: #FFFFFF;color: black;}.ace-tm .ace_cursor {color: black;}.ace-tm .ace_invisible {color: rgb(191, 191, 191);}.ace-tm .ace_storage,.ace-tm .ace_keyword {color: blue;}.ace-tm .ace_constant {color: rgb(197, 6, 11);}.ace-tm .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-tm .ace_constant.ace_language {color: rgb(88, 92, 246);}.ace-tm .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-tm .ace_invalid {background-color: rgba(255, 0, 0, 0.1);color: red;}.ace-tm .ace_support.ace_function {color: rgb(60, 76, 114);}.ace-tm .ace_support.ace_constant {color: rgb(6, 150, 14);}.ace-tm .ace_support.ace_type,.ace-tm .ace_support.ace_class {color: rgb(109, 121, 222);}.ace-tm .ace_keyword.ace_operator {color: rgb(104, 118, 135);}.ace-tm .ace_string {color: rgb(3, 106, 7);}.ace-tm .ace_comment {color: rgb(76, 136, 107);}.ace-tm .ace_comment.ace_doc {color: rgb(0, 102, 255);}.ace-tm .ace_comment.ace_doc.ace_tag {color: rgb(128, 159, 191);}.ace-tm .ace_constant.ace_numeric {color: rgb(0, 0, 205);}.ace-tm .ace_variable {color: rgb(49, 132, 149);}.ace-tm .ace_xml-pe {color: rgb(104, 104, 91);}.ace-tm .ace_entity.ace_name.ace_function {color: #0000A2;}.ace-tm .ace_heading {color: rgb(12, 7, 255);}.ace-tm .ace_list {color:rgb(185, 6, 144);}.ace-tm .ace_meta.ace_tag {color:rgb(0, 22, 142);}.ace-tm .ace_string.ace_regex {color: rgb(255, 0, 0)}.ace-tm .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-tm.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px white;}.ace-tm .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-tm .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-tm .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-tm .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.07);}.ace-tm .ace_gutter-active-line {background-color : #dcdcdc;}.ace-tm .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-tm .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}
/*# sourceURL=ace/css/ace-tm */</style><style>    .error_widget_wrapper {        background: inherit;        color: inherit;        border:none    }    .error_widget {        border-top: solid 2px;        border-bottom: solid 2px;        margin: 5px 0;        padding: 10px 40px;        white-space: pre-wrap;    }    .error_widget.ace_error, .error_widget_arrow.ace_error{        border-color: #ff5a5a    }    .error_widget.ace_warning, .error_widget_arrow.ace_warning{        border-color: #F1D817    }    .error_widget.ace_info, .error_widget_arrow.ace_info{        border-color: #5a5a5a    }    .error_widget.ace_ok, .error_widget_arrow.ace_ok{        border-color: #5aaa5a    }    .error_widget_arrow {        position: absolute;        border: solid 5px;        border-top-color: transparent!important;        border-right-color: transparent!important;        border-left-color: transparent!important;        top: -5px;    }</style>
    <script src="./P1LAB1_JonesHydeia_files/string-diff.js.download"></script>

    <script src="./P1LAB1_JonesHydeia_files/zip.js.download"></script>
    <script src="./P1LAB1_JonesHydeia_files/zip-ext.js.download"></script>
    <script src="./P1LAB1_JonesHydeia_files/zip-fs.js.download"></script>
    <script src="./P1LAB1_JonesHydeia_files/mime-types.js.download"></script>
    <script src="./P1LAB1_JonesHydeia_files/deflate.js.download"></script>

    
  <style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MathJax_Preview .MJXf-math {color: inherit!important}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style></style><script src="./P1LAB1_JonesHydeia_files/theme-dreamweaver.js.download"></script><script src="./P1LAB1_JonesHydeia_files/mode-python.js.download"></script><style id="ace-dreamweaver">.ace-dreamweaver .ace_gutter {background: #e8e8e8;color: #333;}.ace-dreamweaver .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-dreamweaver {background-color: #FFFFFF;color: black;}.ace-dreamweaver .ace_fold {background-color: #757AD8;}.ace-dreamweaver .ace_cursor {color: black;}.ace-dreamweaver .ace_invisible {color: rgb(191, 191, 191);}.ace-dreamweaver .ace_storage,.ace-dreamweaver .ace_keyword {color: blue;}.ace-dreamweaver .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-dreamweaver .ace_constant.ace_language {color: rgb(88, 92, 246);}.ace-dreamweaver .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-dreamweaver .ace_invalid {background-color: rgb(153, 0, 0);color: white;}.ace-dreamweaver .ace_support.ace_function {color: rgb(60, 76, 114);}.ace-dreamweaver .ace_support.ace_constant {color: rgb(6, 150, 14);}.ace-dreamweaver .ace_support.ace_type,.ace-dreamweaver .ace_support.ace_class {color: #009;}.ace-dreamweaver .ace_support.ace_php_tag {color: #f00;}.ace-dreamweaver .ace_keyword.ace_operator {color: rgb(104, 118, 135);}.ace-dreamweaver .ace_string {color: #00F;}.ace-dreamweaver .ace_comment {color: rgb(76, 136, 107);}.ace-dreamweaver .ace_comment.ace_doc {color: rgb(0, 102, 255);}.ace-dreamweaver .ace_comment.ace_doc.ace_tag {color: rgb(128, 159, 191);}.ace-dreamweaver .ace_constant.ace_numeric {color: rgb(0, 0, 205);}.ace-dreamweaver .ace_variable {color: #06F}.ace-dreamweaver .ace_xml-pe {color: rgb(104, 104, 91);}.ace-dreamweaver .ace_entity.ace_name.ace_function {color: #00F;}.ace-dreamweaver .ace_heading {color: rgb(12, 7, 255);}.ace-dreamweaver .ace_list {color:rgb(185, 6, 144);}.ace-dreamweaver .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-dreamweaver .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-dreamweaver .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-dreamweaver .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-dreamweaver .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.07);}.ace-dreamweaver .ace_gutter-active-line {background-color : #DCDCDC;}.ace-dreamweaver .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-dreamweaver .ace_meta.ace_tag {color:#009;}.ace-dreamweaver .ace_meta.ace_tag.ace_anchor {color:#060;}.ace-dreamweaver .ace_meta.ace_tag.ace_form {color:#F90;}.ace-dreamweaver .ace_meta.ace_tag.ace_image {color:#909;}.ace-dreamweaver .ace_meta.ace_tag.ace_script {color:#900;}.ace-dreamweaver .ace_meta.ace_tag.ace_style {color:#909;}.ace-dreamweaver .ace_meta.ace_tag.ace_table {color:#099;}.ace-dreamweaver .ace_string.ace_regex {color: rgb(255, 0, 0)}.ace-dreamweaver .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}
/*# sourceURL=ace/css/ace-dreamweaver */</style></head>
  <body class="ember-application" style="overflow: auto;"><div id="MathJax_Message" style="display: none;"></div>
      <script type="text/javascript" src="./P1LAB1_JonesHydeia_files/saved_resource"></script>

      

      <div id="ember-basic-dropdown-wormhole"></div>

      <!--Comment out until we do maintenance on the platform-->
      <script src="./P1LAB1_JonesHydeia_files/script.js.download"></script><iframe src="./P1LAB1_JonesHydeia_files/frame.html" style="position: fixed; border: none; box-shadow: rgba(9, 20, 66, 0.25) 0px 20px 32px -8px; z-index: 9999; transition: left 1s ease 0s, bottom 1s ease 0s, right 1s ease 0s; height: 115px; width: 320px; left: -9999px; right: -9999px; bottom: calc(100% - 175px);"></iframe>
  

<iframe frameborder="0" allowtransparency="true" scrolling="no" name="__privateStripeMetricsController0" allowpaymentrequest="true" src="./P1LAB1_JonesHydeia_files/m-outer-6e6ed81584679d263bf5a2b0f15af9e1.html" aria-hidden="true" tabindex="-1" style="border: none !important; margin: 0px !important; padding: 0px !important; width: 1px !important; min-width: 100% !important; overflow: hidden !important; display: block !important; visibility: hidden !important; position: fixed !important; height: 1px !important; pointer-events: none !important; user-select: none !important;"></iframe><div class="ember-view" id="ember3"><header class="top-toolbar ">
    <div class="left-buttons">
        <div id="ember4" class="zb-breadcrumbs ember-view"><button id="ember5" class="menu-button  zb-button grey icon-button left ember-view">        <i aria-hidden="false" id="ember6" class="zb-icon grey material-icons med ember-view">        menu
</i>
<!----></button>

    <div class="logo">
            <img width="83px" height="22px" src="./P1LAB1_JonesHydeia_files/logo.svg" alt="zyBooks logo">
    </div>
        <ul class="bread-crumbs">
<!----><a href="https://learn.zybooks.com/library" id="ember22" class="ember-view">                    <li class="bread-crumb">My library</li>
</a>                    <span class="divider" aria-hidden="true">&gt;</span>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020" id="ember24" class="ember-view">                    <li class="bread-crumb">CTI 110: Web, Programming, Database Foundation home</li>
</a>                    <span class="divider" aria-hidden="true">&gt;</span>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/12" id="ember417" class="no-link-styling active ember-view">                    <li class="bread-crumb">1.12: zyLab training: Basics</li>
</a>        </ul>
</div>
    </div>
    <div class="right-buttons">
<!----><!----><a href="https://learn.zybooks.com/catalog" id="ember18" class="ember-view">                <button id="ember19" class="zb-button grey icon-button-with-title left ember-view">        <i aria-hidden="true" id="ember20" class="zb-icon grey material-icons med ember-view">        library_books
</i>
        <span class="title">zyBooks catalog</span>
</button>
</a>                <a class="zb-button help-button" href="http://support.zybooks.com/" target="_blank">
            <i id="ember7" class="zb-icon grey material-icons med ember-view">        help
</i>
                Help/FAQ
        </a>
<div id="ember8" class="zb-menu ember-view"><button id="ember9" class="toolbar-menu-toggle rl-dropdown-toggle ember-view" type="button">                    <i aria-hidden="true" id="ember10" class="zb-icon grey material-icons med ember-view">        account_circle
</i>
                    Hydeia Jones
                    <i aria-hidden="true" id="ember11" class="zb-icon grey material-icons med ember-view">        arrow_drop_down
</i>
</button>
<ul id="ember12" class="right-anchored rl-dropdown ember-view" style="display: none;">                    <li><button class="profile-button" type="button" data-ember-action="" data-ember-action-13="13">My profile</button></li>
                    <li><button class="signout-button" type="button" data-ember-action="" data-ember-action-14="14">Sign out</button></li>
</ul>
</div>    </div>
</header>

<!---->
<div class="route-container zybook-chapter-section-page  no-margin-left" role="main" aria-label="zybook page">
<!---->
    <nav id="ember15" class="hide-nav-menu zb-nav-menu ember-view"><ul class="level-1">
            <li class="flex-row">
                            <i id="ember419" class="item-bullet zb-icon grey material-icons med ember-view">        search
</i>
                                            <a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/content-explorer" id="ember420" class="ember-view">Search zyBook</a>
            </li>
            <li class="flex-row">
                    <button class="list-toggle" type="button" data-ember-action="" data-ember-action-422="422">
                        <div class="flex-row">
                                    <i id="ember423" class="item-bullet zb-icon grey material-icons med ember-view">        info
</i>
                                                            <span class="list-toggle-title ">About this Material</span>
                        </div>
                    </button>
            </li>
            <li>
                <button class="list-toggle" type="button" data-ember-action="" data-ember-action-425="425">
                    <div class="list-toggle">
                        <div class="flex-row">
                                    <span class="item-bullet">1)</span>
                            <span class="list-toggle-title ">Introduction to Python 3</span>
                        </div>
<!---->                            <i id="ember426" class="zb-icon grey material-icons med ember-view">        expand_less
</i>
                    </div>
                </button>

                    <ul class="level-2">
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/1" id="ember490" class="ember-view">                                            <span class="item-bullet">1.1</span>
                                    <span>Programming (general)</span>
                                    <div class="section-labels">
<!----><!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/2" id="ember492" class="ember-view">                                            <span class="item-bullet">1.2</span>
                                    <span>Programming using Python</span>
                                    <div class="section-labels">
<!----><!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/3" id="ember494" class="ember-view">                                            <span class="item-bullet">1.3</span>
                                    <span>Input/Output</span>
                                    <div class="section-labels">
<!----><!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/4" id="ember496" class="ember-view">                                            <span class="item-bullet">1.4</span>
                                    <span>Errors</span>
                                    <div class="section-labels">
<!----><!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/5" id="ember498" class="ember-view">                                            <span class="item-bullet">1.5</span>
                                    <span>Development environment</span>
                                    <div class="section-labels">
<!----><!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/6" id="ember500" class="ember-view">                                            <span class="item-bullet">1.6</span>
                                    <span>Computers and programs (general)</span>
                                    <div class="section-labels">
<!----><!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/7" id="ember502" class="ember-view">                                            <span class="item-bullet">1.7</span>
                                    <span>Computer tour</span>
                                    <div class="section-labels">
<!----><!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/8" id="ember504" class="ember-view">                                            <span class="item-bullet">1.8</span>
                                    <span>Language history</span>
                                    <div class="section-labels">
<!----><!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/9" id="ember506" class="ember-view">                                            <span class="item-bullet">1.9</span>
                                    <span>Why whitespace matters</span>
                                    <div class="section-labels">
<!----><!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/10" id="ember508" class="ember-view">                                            <span class="item-bullet">1.10</span>
                                    <span>Python example: Salary calculation</span>
                                    <div class="section-labels">
<!----><!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/11" id="ember510" class="ember-view">                                            <span class="item-bullet">1.11</span>
                                    <span>Additional practice: Output art</span>
                                    <div class="section-labels">
<!----><!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/12" id="ember512" class="active ember-view">                                            <span class="item-bullet">1.12</span>
                                    <span>zyLab training: Basics</span>
                                    <div class="section-labels">
                                            <span class="nav-item-label-lab">Lab</span>
<!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/13" id="ember514" class="ember-view">                                            <span class="item-bullet">1.13</span>
                                    <span>zyLab training: Interleaved input / output</span>
                                    <div class="section-labels">
                                            <span class="nav-item-label-lab">Lab</span>
<!---->                                            <span class="nav-item-label-hidden">Hidden</span>
<!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/14" id="ember516" class="ember-view">                                            <span class="item-bullet">1.14</span>
                                    <span>LAB: Formatted output: Hello World!</span>
                                    <div class="section-labels">
                                            <span class="nav-item-label-lab">Lab</span>
<!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/15" id="ember518" class="ember-view">                                            <span class="item-bullet">1.15</span>
                                    <span>LAB: Formatted output: No parking sign</span>
                                    <div class="section-labels">
                                            <span class="nav-item-label-lab">Lab</span>
<!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/16" id="ember520" class="ember-view">                                            <span class="item-bullet">1.16</span>
                                    <span>LAB: Input: Welcome message</span>
                                    <div class="section-labels">
                                            <span class="nav-item-label-lab">Lab</span>
<!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/17" id="ember522" class="ember-view">                                            <span class="item-bullet">1.17</span>
                                    <span>LAB: Input: Mad Lib</span>
                                    <div class="section-labels">
                                            <span class="nav-item-label-lab">Lab</span>
<!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/18" id="ember524" class="ember-view">                                            <span class="item-bullet">1.18</span>
                                    <span>LAB: Warm up: Hello world</span>
                                    <div class="section-labels">
                                            <span class="nav-item-label-lab">Lab</span>
<!---->                                            <span class="nav-item-label-hidden">Hidden</span>
<!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/19" id="ember526" class="ember-view">                                            <span class="item-bullet">1.19</span>
                                    <span>LAB: Warm up: Basic output with variables</span>
                                    <div class="section-labels">
                                            <span class="nav-item-label-lab">Lab</span>
<!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/20" id="ember528" class="ember-view">                                            <span class="item-bullet">1.20</span>
                                    <span>LAB*: Program: ASCII art</span>
                                    <div class="section-labels">
                                            <span class="nav-item-label-lab">Lab</span>
<!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/21" id="ember530" class="ember-view">                                            <span class="item-bullet">1.21</span>
                                    <span>P1HW2 Basic Math</span>
                                    <div class="section-labels">
                                            <span class="nav-item-label-lab">Lab</span>
<!----><!----><!---->                                    </div>
</a>                            </li>
                            <li>
<a target="_blank" href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/print" id="ember531" class="ember-view">                                            <i id="ember532" class="item-bullet zb-icon grey material-icons med ember-view">        print
</i>
                                                                            <span>Print chapter</span>
                                    <div class="section-labels">
<!----><!----><!----><!---->                                    </div>
</a>                            </li>
                    </ul>
            </li>
            <li>
                <button class="list-toggle" type="button" data-ember-action="" data-ember-action-428="428">
                    <div class="list-toggle">
                        <div class="flex-row">
                                    <span class="item-bullet">2)</span>
                            <span class="list-toggle-title ">Variables and Expressions</span>
                        </div>
<!---->                            <i id="ember429" class="zb-icon grey material-icons med ember-view">        expand_more
</i>
                    </div>
                </button>

<!---->            </li>
            <li>
                <button class="list-toggle" type="button" data-ember-action="" data-ember-action-431="431">
                    <div class="list-toggle">
                        <div class="flex-row">
                                    <span class="item-bullet">3)</span>
                            <span class="list-toggle-title ">Types</span>
                        </div>
<!---->                            <i id="ember432" class="zb-icon grey material-icons med ember-view">        expand_more
</i>
                    </div>
                </button>

<!---->            </li>
            <li>
                <button class="list-toggle" type="button" data-ember-action="" data-ember-action-434="434">
                    <div class="list-toggle">
                        <div class="flex-row">
                                    <span class="item-bullet">4)</span>
                            <span class="list-toggle-title ">Branching</span>
                        </div>
<!---->                            <i id="ember435" class="zb-icon grey material-icons med ember-view">        expand_more
</i>
                    </div>
                </button>

<!---->            </li>
            <li>
                <button class="list-toggle" type="button" data-ember-action="" data-ember-action-437="437">
                    <div class="list-toggle">
                        <div class="flex-row">
                                    <span class="item-bullet">5)</span>
                            <span class="list-toggle-title ">Loops</span>
                        </div>
<!---->                            <i id="ember438" class="zb-icon grey material-icons med ember-view">        expand_more
</i>
                    </div>
                </button>

<!---->            </li>
            <li>
                <button class="list-toggle" type="button" data-ember-action="" data-ember-action-440="440">
                    <div class="list-toggle">
                        <div class="flex-row">
                                    <span class="item-bullet">6)</span>
                            <span class="list-toggle-title ">Functions</span>
                        </div>
<!---->                            <i id="ember441" class="zb-icon grey material-icons med ember-view">        expand_more
</i>
                    </div>
                </button>

<!---->            </li>
            <li>
                <button class="list-toggle" type="button" data-ember-action="" data-ember-action-443="443">
                    <div class="list-toggle">
                        <div class="flex-row">
                                    <span class="item-bullet">7)</span>
                            <span class="list-toggle-title ">Introduction to Web Programming</span>
                        </div>
<!---->                            <i id="ember444" class="zb-icon grey material-icons med ember-view">        expand_more
</i>
                    </div>
                </button>

<!---->            </li>
            <li>
                <button class="list-toggle" type="button" data-ember-action="" data-ember-action-446="446">
                    <div class="list-toggle">
                        <div class="flex-row">
                                    <span class="item-bullet">8)</span>
                            <span class="list-toggle-title ">HTML</span>
                        </div>
<!---->                            <i id="ember447" class="zb-icon grey material-icons med ember-view">        expand_more
</i>
                    </div>
                </button>

<!---->            </li>
            <li>
                <button class="list-toggle" type="button" data-ember-action="" data-ember-action-449="449">
                    <div class="list-toggle">
                        <div class="flex-row">
                                    <span class="item-bullet">9)</span>
                            <span class="list-toggle-title ">More HTML</span>
                        </div>
<!---->                            <i id="ember450" class="zb-icon grey material-icons med ember-view">        expand_more
</i>
                    </div>
                </button>

<!---->            </li>
            <li>
                <button class="list-toggle" type="button" data-ember-action="" data-ember-action-452="452">
                    <div class="list-toggle">
                        <div class="flex-row">
                                    <span class="item-bullet">10)</span>
                            <span class="list-toggle-title ">Basic CSS</span>
                        </div>
<!---->                            <i id="ember453" class="zb-icon grey material-icons med ember-view">        expand_more
</i>
                    </div>
                </button>

<!---->            </li>
            <li>
                <button class="list-toggle" type="button" data-ember-action="" data-ember-action-455="455">
                    <div class="list-toggle">
                        <div class="flex-row">
<!---->                            <span class="list-toggle-title margin-for-bullet">Unused</span>
                        </div>
<!---->                            <i id="ember456" class="zb-icon grey material-icons med ember-view">        expand_more
</i>
                    </div>
                </button>

<!---->            </li>
</ul>
</nav>

    <section class="section-container">
<!---->        <nav class="section-nav" aria-label="previous section">
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/11" id="ember457" class="nav-link ember-view">                <i id="ember458" class="zb-icon secondary material-icons sm ember-view">        arrow_upward
</i>
                <span class="nav-text previous ">1.11 Additional practice: Output art</span>
</a>    </nav>

<div role="main" aria-label="section content">
<!---->
<!---->
<!---->
<!---->
<!---->
    <article id="ember459" class="zybook-section zb-card ember-view"><div class="zb-card-content">
    <!----><!---->    <div class="section-header-row">
        <h1 class="zybook-section-title">1.12 zyLab training: Basics</h1>

            <div class="section-action-container">
<!---->
<!----><!----><!----><!---->
<!---->            </div>
    </div>

<!---->
<!---->
<!---->
<!---->
                    <div id="ember461" class="content-resource markdown-content-resource ember-view"><div id="ember462" class="ember-view"><p>While the zyLab platform can be used without training, a bit of training may help some students avoid common issues. </p>
<p>The assignment is to get an integer from input, and output that integer squared, ending with newline. (Note: This assignment is configured to have students programming directly in the zyBook. Instructors may instead require students to upload a file). Below is a program that's been nearly completed for you. </p>
<ol>
<li>Click "Run program".  The output is wrong. Sometimes a program lacking input will produce wrong output (as in this case), or no output. Remember to always pre-enter needed input.</li>
<li>Type 2 in the input box, then click "Run program", and note the output is 4.</li>
<li>Type 3 in the input box instead, run, and note the output is 6. </li>
</ol>
<p>When students are done developing their program, they can submit the program for automated grading. </p>
<ol>
<li>Click the "Submit mode" tab</li>
<li>Click "Submit for grading". </li>
<li>The first test case failed (as did all test cases, but focus on the first test case first). The highlighted arrow symbol means an ending newline was expected but is missing from your program's output. </li>
</ol>
<p>Matching output exactly, even whitespace, is often required. Change the program to output an ending newline. </p>
<ol>
<li>Click on "Develop mode", and change the output statement to output a newline: <code>print(userNumSquared)</code>. Type 2 in the input box and run. </li>
<li>Click on "Submit mode", click "Submit for grading", and observe that now the first test case passes and 1 point was earned.</li>
</ol>
<p>The last two test cases failed, due to a bug, yielding only 1 of 3 possible points. Fix that bug. </p>
<ol>
<li>Click on "Develop mode", change the program to use * rather than +, and try running with input 2 (output is 4) and 3 (output is now 9, not 6 as before). </li>
<li>Click on "Submit mode" again, and click "Submit for grading". Observe that all test cases are passed, and you've earned 3 of 3 points.</li>
</ol>
</div>
</div>
        
<!---->            <div content_resource_id="42297505" id="ember464" class="interactive-activity-container programming-submission-content-resource lab large ember-view"><div class="activity-title-bar" data-ember-action="" data-ember-action-465="465">
    <div class="activity-type" aria-label="labactivity">lab activity</div>
    <div class="activity-description">
            <div class="activity-title">1.12.1: zyLab training: Basics</div>
<!---->            <div class="title-bar-chevron-container">
<!---->
                    <span class="lab-score">0 / 3</span>
<!---->                        <div aria-label="Activity not completed" id="ember466" class="zb-chevron title-bar-chevron grey large outline ember-view">
</div>
            </div>
    </div>
</div>
<div class="activity-payload">
<!---->
    <div id="ember467" class="content-resource programming-submission-payload ember-view">    <div id="ember468" class="download-files ember-view"><!----></div>

    <div id="ember469" class="zylab-inline-editor ember-view"><div class="inline-editor-header">
<!----><!---->        <div id="ember470" class="inline-editor-filename zb-truncate-text ember-view">main.py
</div>
            <button id="ember549" class="load-default-template-button zb-button primary ember-view"><!---->        <span class="title">Load default template...</span>
</button>
</div>

<div id="ember472" class="ace-editor-container ember-view ui-resizable">    <div id="ace-editor" class="ace-editor resizable ace_editor ace-dreamweaver"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14px; width: 6.59781px; left: 37px; top: 66px;"></textarea><div class="ace_gutter"><div class="ace_layer ace_gutter-layer" style="margin-top: 10px; height: 328px; width: 33px;"><div class="ace_gutter-cell " style="height: 14px;">1</div><div class="ace_gutter-cell " style="height: 14px;">2</div><div class="ace_gutter-cell " style="height: 14px;">3</div><div class="ace_gutter-cell " style="height: 14px;">4</div><div class="ace_gutter-cell " style="height: 14px;">5</div></div><div class="ace_gutter-active-line" style="top: 66px; height: 14px;"></div></div><div class="ace_scroller" style="left: 33px; right: 0px; bottom: 0px;"><div class="ace_content" style="margin-top: 10px; width: 913px; height: 328px; margin-left: 0px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 531.825px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"><div class="ace_active-line" style="height:14px;top:56px;left:0;right:0;"></div></div><div class="ace_layer ace_text-layer" style="padding: 0px 4px;"><div class="ace_line" style="height:14px"><span class="ace_identifier">userNum</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_support ace_function">int</span><span class="ace_paren ace_lparen">(</span><span class="ace_support ace_function">input</span><span class="ace_paren ace_lparen">(</span><span class="ace_paren ace_rparen">))</span></div><div class="ace_line" style="height:14px"><span class="ace_identifier">userNumSquared</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_identifier">userNum</span> <span class="ace_keyword ace_operator">+</span> <span class="ace_identifier">userNum</span>   <span class="ace_comment"># Bug here; fix it when instructed</span></div><div class="ace_line" style="height:14px">   </div><div class="ace_line" style="height:14px"><span class="ace_keyword">print</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">userNumSquared</span>, <span class="ace_identifier">end</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">' '</span><span class="ace_paren ace_rparen">)</span>       <span class="ace_comment"># Output formatting issue here; fix it when instructed</span></div><div class="ace_line" style="height:14px"></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor" style="left: 4px; top: 56px; width: 6.59781px; height: 14px;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 0px;"><div class="ace_scrollbar-inner" style="width: 22px; height: 90px;"></div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 22px; left: 33px; right: 0px;"><div class="ace_scrollbar-inner" style="height: 22px; width: 946px;"></div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div>
<!----><div class="ui-resizable-handle ui-resizable-e" style="z-index: 90;"></div><div class="ui-resizable-handle ui-resizable-s" style="z-index: 90;"></div><div class="ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se" style="z-index: 90;"></div></div>

<!----></div>

    <div class="develop-submit-control-container">
        <div id="ember473" class="zb-segmented-control secondary ember-view">    <button id="ember475" class="first  zb-button secondary ember-view"><!---->        <span class="title">Develop mode</span>
</button>
    <button id="ember477" class="last selected  zb-button secondary ember-view"><!---->        <span class="title">Submit mode</span>
</button>
</div>
        <div class="develop-submit-instructions">When done developing your program, press the <span class="primary-font-bold">Submit for grading</span> button below. This will submit your program for auto-grading.</div>
    </div>

<div class="submit-container">
    <div class="submission-row">
        <button id="ember544" class="submit-button zb-button primary raised ember-view"><!---->        <span class="title">Submit for grading</span>
</button>

<!---->
<!---->
        <div class="submission-cap-throttle-container">
<!----><!---->        </div>
    </div>

<!---->
<!---->
        <div id="ember545" class="zylab-signature ember-view"><div class="signature-header">
    <span>Signature of your work</span>
    <button id="ember546" class="zb-button secondary thin-title no-padding ember-view"><!---->        <span class="title">What is this?</span>
</button>
</div>
<div class="code-block-styling">9/14.. <span class="day-of-week">M</span>- <span class="day-of-week">M</span>-|0 ..9/21</div>

<!----></div>
    <div id="ember547" class="latest-submission zb-card ember-view"><div class="zb-card-content">
            <div class="latest-submission-header">
            <span>Latest submission - 12:25 AM on 09/21/20</span>
                <div class="flex-row">
<!---->                    <div class="total-score error">
                        Total score: 0 / 3
                    </div>
                </div>
        </div>
            <div id="ember550" class="zylab-submission-result ember-view"><!---->
<div class="submission-result-controls">
    <div class="hide-tests-container">
            <div id="ember551" class="zb-checkbox blue label-present right ember-view"><input aria-label="Only show failing tests" type="checkbox" value="false">
<label aria-hidden="true">Only show failing tests</label>
</div>
<!---->    </div>
        <button id="ember552" class="download-submission-button zb-button zb-download-button secondary ember-view"><!---->        <span class="title">Download this submission</span>


<a id="submissions-download-link-ember552" download="" href="https://s3-us-west-2.amazonaws.com/zyante-programming-submissions/2625940f-4bd3-4765-9d78-3dc9f3578d63.zip"></a>
</button>
</div>

<!---->            <div id="ember554" class="test-result allow-expand ember-view"><div class="test-header" data-ember-action="" data-ember-action-555="555">
    <div class="test-title-container">
<!---->        <span>1: Compare output</span>

            <i id="ember556" class="expand-button zb-icon grey material-icons med ember-view">        keyboard_arrow_up
</i>
    </div>
        <span class="test-score">0 / 1</span>
</div>
    <div id="ember557" class="expected-output-test-result ember-view"><!---->
<!---->            <div class="output-differs">
                Output is nearly correct; but whitespace differs. See highlights below.
                    <button id="ember571" class="zb-button secondary thin-title ember-view"><!---->        <span class="title">Special character legend</span>
</button>
            </div>
                <div class="test-result-row">
                    <div class="result-row-description">Input</div>
                    <div class="programming-code-output no-wrap" data-test-selector="test-input">2</div>
                </div>
<!---->                        <div class="test-result-row">
                            <div class="result-row-description">Your output</div>
                                <div class="programming-code-output no-wrap">4<span class="string-diff-highlight "> </span></div>
                        </div>
                        <div class="test-result-row">
                            <div data-test-selector="expected-output" class="result-row-description">Expected output</div>
                                <div class="programming-code-output no-wrap">4<span class="string-diff-highlight newline">
</span></div>
                        </div>
<!----><!----></div>
</div>
            <div id="ember560" class="test-result allow-expand ember-view"><div class="test-header" data-ember-action="" data-ember-action-561="561">
    <div class="test-title-container">
<!---->        <span>2: Compare output</span>

            <i id="ember562" class="expand-button zb-icon grey material-icons med ember-view">        keyboard_arrow_up
</i>
    </div>
        <span class="test-score">0 / 1</span>
</div>
    <div id="ember563" class="expected-output-test-result ember-view"><!---->
<!---->            <div class="output-differs">
                Output differs. See highlights below.
                    <button id="ember572" class="zb-button secondary thin-title ember-view"><!---->        <span class="title">Special character legend</span>
</button>
            </div>
                <div class="test-result-row">
                    <div class="result-row-description">Input</div>
                    <div class="programming-code-output no-wrap" data-test-selector="test-input">12</div>
                </div>
<!---->                        <div class="test-result-row">
                            <div class="result-row-description">Your output</div>
                                <div class="programming-code-output no-wrap"><span class="string-diff-highlight ">2</span>4<span class="string-diff-highlight "> </span></div>
                        </div>
                        <div class="test-result-row">
                            <div data-test-selector="expected-output" class="result-row-description">Expected output</div>
                                <div class="programming-code-output no-wrap"><span class="string-diff-highlight ">1</span>4<span class="string-diff-highlight ">4</span><span class="string-diff-highlight newline">
</span></div>
                        </div>
<!----><!----></div>
</div>
            <div id="ember566" class="test-result allow-expand ember-view"><div class="test-header" data-ember-action="" data-ember-action-567="567">
    <div class="test-title-container">
<!---->        <span>3: Compare output</span>

            <i id="ember568" class="expand-button zb-icon grey material-icons med ember-view">        keyboard_arrow_up
</i>
    </div>
        <span class="test-score">0 / 1</span>
</div>
    <div id="ember569" class="expected-output-test-result ember-view"><!---->
<!---->            <div class="output-differs">
                Output differs. See highlights below.
                    <button id="ember573" class="zb-button secondary thin-title ember-view"><!---->        <span class="title">Special character legend</span>
</button>
            </div>
                <div class="test-result-row">
                    <div class="result-row-description">Input</div>
                    <div class="programming-code-output no-wrap" data-test-selector="test-input">-5</div>
                </div>
<!---->                        <div class="test-result-row">
                            <div class="result-row-description">Your output</div>
                                <div class="programming-code-output no-wrap"><span class="string-diff-highlight ">-</span><span class="string-diff-highlight ">1</span><span class="string-diff-highlight ">0</span><span class="string-diff-highlight "> </span></div>
                        </div>
                        <div class="test-result-row">
                            <div data-test-selector="expected-output" class="result-row-description">Expected output</div>
                                <div class="programming-code-output no-wrap"><span class="string-diff-highlight ">2</span><span class="string-diff-highlight ">5</span><span class="string-diff-highlight newline">
</span></div>
                        </div>
<!----><!----></div>
</div>
</div>

</div>
</div>

<!----></div>


<!---->
<!---->
<!----></div>
</div>

    <div id="ember485" class="zb-feedback ember-view">    <div class="feedback-control-row">

<!---->
<!---->
            <button id="ember486" class="expand-feedback-button zb-button secondary ember-view"><!---->        <span class="title">Feedback?</span>
</button>
    </div>

<!----></div>
</div>

<!---->

<!---->
<!---->
</div>
</article>
<!---->
<!---->
<!---->
<!---->
<!---->
<!---->

<!---->
<!----></div>

<!---->
    <nav class="section-nav next" aria-label="next section">
<a href="https://learn.zybooks.com/zybook/FAYTECHCCCTI110Fall2020/chapter/1/section/13" id="ember487" class="nav-link ember-view">                <i id="ember488" class="zb-icon secondary material-icons sm ember-view">        arrow_downward
</i>
                <span class="nav-text next ">1.13 zyLab training: Interleaved input / output</span>
</a>    </nav>

<!---->
<!---->
<!---->
<!---->
</section>


<!---->
<!---->
<!---->
<!---->

<!----></div>
</div><iframe id="intercom-frame" style="position: absolute !important; opacity: 0 !important; width: 1px !important; height: 1px !important; top: 0 !important; left: 0 !important; border: none !important; display: block !important; z-index: -1 !important; pointer-events: none;" aria-hidden="true" tabindex="-1" title="Intercom" src="./P1LAB1_JonesHydeia_files/saved_resource.html"></iframe><div id="dom_ruler-text_measurer" style="position: absolute; left: -10010px; top: -10px; width: 10000px; height: 0px; overflow: hidden; visibility: hidden;"><div style=""></div></div></body></html>