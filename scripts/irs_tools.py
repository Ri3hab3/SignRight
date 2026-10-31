"""Markup + JS for the five in-browser tools. No network calls, no storage, no libraries.

Each entry: name (WebApplication schema), desc, title (h2), intro, html.
The template wraps html in <div class="tool sr-tool"> so the AdSense excluded-area
selector `.sr-tool` covers every tool.
"""

PRIVACY = '<p class="privacy"><b>Runs in your browser.</b> Nothing you enter is sent anywhere, stored or tracked by this tool.</p>'

TOOLS = {}

# ------------------------------------------------------------------ FIRE countdown
TOOLS["fire_countdown"] = dict(
    name="IRS FIRE Shutdown Countdown",
    desc="Counts down to the last day to file through the IRS FIRE system (3 p.m. ET, 19 November 2026) and says whether FIRE can still be used today.",
    title="Countdown: can I still use FIRE?",
    intro="Live countdown to 3 p.m. Eastern Time on 19 November 2026, the IRS-announced last moment to file information returns through FIRE.",
    html=PRIVACY + """
<div id="fire-verdict" class="verdict" role="status" aria-live="polite">Calculating&hellip;</div>
<div class="count" aria-hidden="true">
  <div><b id="c-d">--</b><span>days</span></div><div><b id="c-h">--</b><span>hours</span></div>
  <div><b id="c-m">--</b><span>minutes</span></div><div><b id="c-s">--</b><span>seconds</span></div>
</div>
<p class="hint" id="fire-sub"></p>
<script>
(function(){
  var T=new Date('2026-11-19T15:00:00-05:00').getTime();
  var v=document.getElementById('fire-verdict'),sub=document.getElementById('fire-sub');
  var cd=document.getElementById('c-d'),ch=document.getElementById('c-h'),cm=document.getElementById('c-m'),cs=document.getElementById('c-s');
  function p(n){return n<10?'0'+n:''+n}
  function days(ms){return Math.floor(ms/86400000)}
  function left(ms){var d=days(ms);return d<1?'less than 1 day':d+' day'+(d===1?'':'s')}
  function tick(){
    var ms=T-Date.now(),open=ms>0;
    if(!open){ms=0}
    var s=Math.floor(ms/1000);
    cd.textContent=Math.floor(s/86400);ch.textContent=p(Math.floor(s%86400/3600));cm.textContent=p(Math.floor(s%3600/60));cs.textContent=p(s%60);
    var txt,cls;
    if(open){cls='verdict yes';txt='Yes. FIRE still accepts submissions until 3 p.m. ET on 19 November 2026 ('+left(T-Date.now())+' left).'}
    else{cls='verdict no';txt='No. FIRE stopped accepting submissions at 3 p.m. ET on 19 November 2026. File through IRIS.'}
    if(v.textContent!==txt){v.textContent=txt;v.className=cls}
    var now=Date.now(),a=new Date('2026-11-01T23:59:00-05:00').getTime(),b=new Date('2026-11-09T23:59:00-05:00').getTime();
    sub.textContent=(now>a?'The 1 Nov test-file window has closed. ':'Test files can still be sent until 1 Nov 2026. ')+(now>b?'The 9 Nov deadline for TCC application changes has passed.':'TCC application changes are allowed until 9 Nov 2026.');
    var st=document.querySelectorAll('[data-status]');
    for(var i=0;i<st.length;i++){var t=new Date(st[i].getAttribute('data-status')).getTime();st[i].textContent=t<now?'Passed':'In '+left(t-now)}
  }
  tick();document.addEventListener('DOMContentLoaded',tick);setInterval(tick,1000);
})();
</script>""",
)

# ------------------------------------------------------------------ TCC decision tree
TOOLS["tcc_tree"] = dict(
    name="FIRE TCC to IRIS TCC Decision Tree",
    desc="Three questions that tell a filer whether an existing FIRE Transmitter Control Code is enough for IRIS, and the next step.",
    title="3-question check: do I need a new TCC?",
    intro="Answer three questions. You get a verdict and your exact next step.",
    html=PRIVACY + """
<form id="tree" onsubmit="return false">
  <fieldset><legend>1. How do you file information returns today?</legend>
    <label class="opt"><input type="radio" name="q1" value="own"> <span>I upload files to FIRE myself, with my own FIRE TCC</span></label>
    <label class="opt"><input type="radio" name="q1" value="prov"> <span>Software or a service provider submits for me</span></label>
    <label class="opt"><input type="radio" name="q1" value="paper"> <span>I file on paper, or I haven&rsquo;t filed before</span></label>
  </fieldset>
  <fieldset><legend>2. Do you already have an IRIS TCC (starts with the letter D)?</legend>
    <label class="opt"><input type="radio" name="q2" value="y"> <span>Yes</span></label>
    <label class="opt"><input type="radio" name="q2" value="n"> <span>No</span></label>
    <label class="opt"><input type="radio" name="q2" value="u"> <span>Not sure</span></label>
  </fieldset>
  <fieldset><legend>3. Do you file 10 or more information returns a year, all form types combined?</legend>
    <label class="opt"><input type="radio" name="q3" value="y"> <span>Yes</span></label>
    <label class="opt"><input type="radio" name="q3" value="n"> <span>No, fewer than 10</span></label>
  </fieldset>
</form>
<div id="tree-out" class="verdict" role="status" aria-live="polite" hidden></div>
<script>
(function(){
  var f=document.getElementById('tree'),o=document.getElementById('tree-out');
  var APPLY='<a class="btn" href="https://www.irs.gov/tax-professionals/iris-application-for-tcc" target="_blank" rel="noopener">Start the IRIS Application for TCC</a> <a class="btn sec" href="/iris-tcc-application-guide">Check the timing</a>';
  function val(n){var e=f.querySelector('input[name='+n+']:checked');return e?e.value:null}
  function show(cls,head,body,extra){o.hidden=false;o.className='verdict '+cls;o.innerHTML='<b>'+head+'</b><br>'+body+(extra?'<div class="actions">'+extra+'</div>':'')}
  function run(){
    var a=val('q1'),b=val('q2'),c=val('q3');if(!a||!b||!c){o.hidden=true;return}
    if(b==='y'){show('yes','You already have what you need.','An IRIS TCC is the one that works in IRIS. Confirm your application shows &ldquo;Completed&rdquo;, then file your tax year 2026 returns through IRIS in 2027. FIRE closes 19 Nov 2026.','<a class="btn sec" href="/how-to-file-1099-through-iris">How to file through IRIS</a>');return}
    if(a==='own'){show('no','No. Your FIRE TCC will not work in IRIS.','The IRS tells current FIRE users to complete an IRIS Application for TCC. Next step: apply now.',APPLY);return}
    if(a==='prov'){show('mid','Probably not you, but ask your provider.','If a provider submits your returns, it is their TCC that matters. Ask whether they will submit through IRIS in 2027. If you want to file yourself in the free IRIS Taxpayer Portal you need your own IRIS TCC.',APPLY);return}
    if(c==='y'){show('mid','You must e-file, so you need a route to IRIS.','With 10 or more returns in total, e-filing is required. Either apply for an IRIS TCC to use the free Taxpayer Portal, or hire a provider that files through IRIS.',APPLY)}
    else{show('mid','No TCC is needed to file on paper.','With fewer than 10 returns you can still file on paper. An IRIS TCC is only needed if you want to e-file in the free Taxpayer Portal.',APPLY)}
  }
  f.addEventListener('change',run);
})();
</script>""",
)

# ------------------------------------------------------------------ threshold checker
TOOLS["threshold"] = dict(
    name="1099 Threshold Checker, Tax Year 2025 vs 2026",
    desc="Enter the amount paid to a contractor to see whether a Form 1099-NEC is required under the tax year 2025 ($600) and 2026 ($2,000) thresholds.",
    title="Is a 1099-NEC required? 2025 vs 2026",
    intro="Enter the total you paid one person for services in the year.",
    html=PRIVACY + """
<div class="row2">
  <div><label class="f" for="amt">Total paid to this person for services ($)</label>
  <input type="number" id="amt" inputmode="decimal" min="0" step="0.01" placeholder="e.g. 1500"></div>
  <div class="cb"><input type="checkbox" id="bw"><label for="bw">I withheld backup withholding from this person</label></div>
</div>
<div class="two" id="thr-out" aria-live="polite">
  <div class="verdict" id="r25"><b>Tax year 2025</b><br>Threshold: $600<br><span>Enter an amount</span></div>
  <div class="verdict" id="r26"><b>Tax year 2026</b><br>Threshold: $2,000<br><span>Enter an amount</span></div>
</div>
<p class="hint">Checks the dollar amount only. The kind of payment and who the payee is also matter. This tool is for payments for services (Form 1099-NEC).</p>
<script>
(function(){
  var a=document.getElementById('amt'),bw=document.getElementById('bw'),r25=document.getElementById('r25'),r26=document.getElementById('r26');
  function money(n){return '$'+n.toLocaleString('en-US',{minimumFractionDigits:0,maximumFractionDigits:2})}
  function one(el,limit,amt,b){
    var s=el.querySelector('span');
    if(b){el.className='verdict yes';s.textContent='1099-NEC required: you backup withheld, so the amount does not matter.';return}
    if(amt>=limit){el.className='verdict yes';s.textContent='1099-NEC required: '+money(amt)+' is at or above '+money(limit)+'.'}
    else{el.className='verdict no';s.textContent='Not required by amount: '+money(amt)+' is '+money(limit-amt)+' below '+money(limit)+'.'}
  }
  function run(){
    var raw=a.value;if(raw===''&&!bw.checked){r25.className=r26.className='verdict';r25.querySelector('span').textContent=r26.querySelector('span').textContent='Enter an amount';return}
    var n=parseFloat(raw);if(isNaN(n)||n<0)n=0;
    one(r25,600,n,bw.checked);one(r26,2000,n,bw.checked);
  }
  a.addEventListener('input',run);bw.addEventListener('change',run);
})();
</script>""",
)

# ------------------------------------------------------------------ deadlines + ics
TOOLS["deadlines"] = dict(
    name="1099 Deadline Calendar, 2027 Filing Season",
    desc="Lists 1099, W-2 and FIRE-to-IRIS deadlines for the 2027 filing season, highlights the next one, and downloads each as a calendar file.",
    title="Deadline calendar: your next date is highlighted",
    intro="The next upcoming deadline is highlighted using today&rsquo;s date. Each row downloads as a calendar file (.ics) with a reminder 7 days before.",
    html=PRIVACY + """
<div class="tblwrap"><table class="tbl" id="dl-table"><thead><tr><th scope="col">Date</th><th scope="col">What is due</th><th scope="col">Calendar</th></tr></thead><tbody></tbody></table></div>
<p class="hint" id="dl-note"></p>
<script>
(function(){
  var D=[
   ['2026-11-09','Last day to change IRIS/FIRE TCC applications (IR-2026-99)','TCC application changes close'],
   ['2026-11-19','FIRE stops accepting returns at 3 p.m. ET (IR-2026-99)','FIRE closes'],
   ['2027-02-01','Forms W-2 and 1099-NEC due (31 Jan is a Sunday). Recipient copies of most 1099s and 1098-VLI due','W-2 and 1099-NEC due'],
   ['2027-02-16','1099-MISC recipient copies when boxes 8 or 10 are used (15 Feb is a holiday)','1099-MISC boxes 8/10 recipient copy due'],
   ['2027-03-01','Paper filing with the IRS for 1099-MISC, 1099-K, 1099-R, 1098-VLI (28 Feb is a Sunday)','Paper 1099 filing due'],
   ['2027-03-31','Electronic filing with the IRS for 1099-MISC, 1099-K, 1099-R, 1098-VLI','E-filing of 1099s due']
  ];
  var tb=document.querySelector('#dl-table tbody'),next=-1,now=new Date(),today=Date.UTC(now.getFullYear(),now.getMonth(),now.getDate());
  function ts(s){var p=s.split('-');return Date.UTC(+p[0],+p[1]-1,+p[2])}
  for(var i=0;i<D.length;i++){if(ts(D[i][0])>=today){next=i;break}}
  function pretty(s){return new Date(ts(s)).toLocaleDateString('en-US',{timeZone:'UTC',weekday:'short',day:'numeric',month:'short',year:'numeric'})}
  function ymd(t){var d=new Date(t);return d.getUTCFullYear()+('0'+(d.getUTCMonth()+1)).slice(-2)+('0'+d.getUTCDate()).slice(-2)}
  function esc(s){return s.replace(/[\\\\;,]/g,function(c){return '\\\\'+c})}
  function ics(i){
    var t=ts(D[i][0]),stamp=new Date().toISOString().replace(/[-:]/g,'').replace(/\\.\\d{3}/,'');
    var L=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//SignRight//1099 Deadlines//EN','BEGIN:VEVENT','UID:'+D[i][0]+'-'+i+'@signright.io','DTSTAMP:'+stamp,
      'DTSTART;VALUE=DATE:'+ymd(t),'DTEND;VALUE=DATE:'+ymd(t+86400000),'SUMMARY:'+esc(D[i][2]),'DESCRIPTION:'+esc(D[i][1]+'. Source: IRS. Confirm on IRS.gov. https://signright.io/1099-deadlines-2027-filing-season'),
      'BEGIN:VALARM','TRIGGER:-P7D','ACTION:DISPLAY','DESCRIPTION:'+esc(D[i][2]),'END:VALARM','END:VEVENT','END:VCALENDAR'].join('\\r\\n');
    var a=document.createElement('a');a.href=URL.createObjectURL(new Blob([L],{type:'text/calendar'}));a.download='deadline-'+D[i][0]+'.ics';
    document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove()},500);
  }
  D.forEach(function(r,i){
    var tr=document.createElement('tr');if(i===next)tr.className='next';
    var c1=document.createElement('td');c1.textContent=pretty(r[0])+(i===next?' (next)':ts(r[0])<today?' (passed)':'');
    var c2=document.createElement('td');c2.textContent=r[1];
    var c3=document.createElement('td'),b=document.createElement('button');b.type='button';b.className='btn sec sm';b.textContent='Add to calendar';
    b.setAttribute('aria-label','Download calendar file for '+r[2]);b.addEventListener('click',function(){ics(i)});c3.appendChild(b);
    tr.appendChild(c1);tr.appendChild(c2);tr.appendChild(c3);tb.appendChild(tr);
  });
  document.getElementById('dl-note').textContent=next<0?'All dates in this table have passed. Check IRS.gov for the next filing season.':'Next deadline: '+pretty(D[next][0])+'.';
})();
</script>""",
)

# ------------------------------------------------------------------ TCC timing calculator
TOOLS["tcc_calc"] = dict(
    name="Will My IRIS TCC Arrive in Time? Calculator",
    desc="Works back from your target filing date using the IRS 45-day TCC processing window to give the last safe date to apply for an IRIS TCC.",
    title="Will my TCC arrive in time?",
    intro="Pick the date you want to file. The tool works back 45 days to your last safe application date.",
    html=PRIVACY + """
<label class="f" for="tgt">Target filing date</label>
<input type="date" id="tgt" value="2027-03-31">
<div class="quick">
  <button type="button" class="btn sec sm" data-d="2027-02-01">1 Feb 2027 (W-2, 1099-NEC)</button>
  <button type="button" class="btn sec sm" data-d="2027-03-31">31 Mar 2027 (e-filed 1099s)</button>
</div>
<fieldset class="inl"><legend>Count the 45 days as</legend>
  <label class="opt"><input type="radio" name="unit" value="bd" checked> <span>45 business days (cautious, Pub. 5903 / Pub. 1220)</span></label>
  <label class="opt"><input type="radio" name="unit" value="cd"> <span>45 calendar days (upper bound in the IRIS FAQs)</span></label>
</fieldset>
<div id="calc-out" class="verdict" role="status" aria-live="polite" hidden></div>
<p class="hint">Business days here = Monday to Friday except US federal holidays; the IRS does not define the term on these pages. The IRS FAQs say most applications finish within 24 hours, so this is a worst-case plan, not a forecast.</p>
<script>
(function(){
  var H={'2026-11-11':1,'2026-11-26':1,'2026-12-25':1,'2027-01-01':1,'2027-01-18':1,'2027-02-15':1,'2027-05-31':1};
  var t=document.getElementById('tgt'),o=document.getElementById('calc-out');
  function ts(s){var p=s.split('-');return Date.UTC(+p[0],+p[1]-1,+p[2])}
  function key(x){var d=new Date(x);return d.getUTCFullYear()+'-'+('0'+(d.getUTCMonth()+1)).slice(-2)+'-'+('0'+d.getUTCDate()).slice(-2)}
  function biz(x){var w=new Date(x).getUTCDay();return w!==0&&w!==6&&!H[key(x)]}
  function pretty(x){return new Date(x).toLocaleDateString('en-US',{timeZone:'UTC',weekday:'long',day:'numeric',month:'long',year:'numeric'})}
  function run(){
    if(!t.value){o.hidden=true;return}
    var unit=document.querySelector('input[name=unit]:checked').value,x=ts(t.value),n=0;
    if(unit==='cd'){x-=45*86400000}else{while(n<45){x-=86400000;if(biz(x))n++}}
    var now=new Date(),today=Date.UTC(now.getFullYear(),now.getMonth(),now.getDate()),left=Math.round((x-today)/86400000);
    o.hidden=false;
    if(left>=0){o.className='verdict yes';o.innerHTML='<b>Last safe date to apply: '+pretty(x)+'.</b><br>'+(left===0?'That is today.':'That is '+left+' day'+(left===1?'':'s')+' from today.')+' Apply earlier if you can.'}
    else{o.className='verdict no';o.innerHTML='<b>The cautious window has passed ('+pretty(x)+').</b><br>You are '+(-left)+' day'+(left===-1?'':'s')+' past it. The IRS says most applications finish within 24 hours but may take up to 45 days, so apply today and keep a provider as a backup.'}
  }
  t.addEventListener('input',run);
  document.querySelectorAll('input[name=unit]').forEach(function(e){e.addEventListener('change',run)});
  document.querySelectorAll('.quick button').forEach(function(b){b.addEventListener('click',function(){t.value=b.getAttribute('data-d');run()})});
  run();
})();
</script>""",
)
