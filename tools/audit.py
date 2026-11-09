# Consistency audit for the Vestigia + Rain Particles Fix + RW setup. Run: python3 tools/audit.py  (from anywhere)
import os, re, glob, hashlib, xml.etree.ElementTree as E
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V='Vestigia'; A=f'{V}/active'; OPT=f'{V}/variants/00 - COMPATIBLE OPTIONS (use these)'
h=lambda p: hashlib.md5(open(p,'rb').read()).hexdigest()
issues=[]; ok=[]
def rep(cond, good, bad): (ok.append(good) if cond else issues.append(bad))
# 1 XML validity
bad=[]
for p in glob.glob(f'{A}/*/*.xml')+glob.glob(f'{OPT}/**/*.xml',recursive=True)+['Vestigia - Rain Sheets (Optional)/weather.xml',f'{V}/install.xml']:
    try: E.parse(p)
    except Exception as e: bad.append(p)
rep(not bad, 'All XML files parse', f'Broken XML: {bad}')
# 2 install.xml references
t=open(f'{V}/install.xml').read()
miss=[fp for fp in re.findall(r'<FilePath>([^<]*)',t) if not os.path.exists(f'{V}/{fp}')]
issues.append(f'install.xml references {len(miss)} files not in the repo (should exist on your PC): {", ".join(os.path.basename(m) for m in miss)}') if miss else ok.append('install.xml: all files present')
# timecycle helpers
def regions(p):
    s=open(p,encoding='utf-8').read(); i=s.find('name="URBAN"'); return s[:i], s[i:]
def row(g,k):
    m=re.search(r'<%s>([-0-9.\s]+)</%s>'%(k,k),g); return m.group(1).split() if m else None
RAINY=['w_drizzle','w_rain','w_shower','w_shower_finale2','w_shower_guama','w_shower_mp_pred','w_sleet','w_hail','w_hurricane','w_thunder','w_thunderstorm','w_thunderstorm_mp_pred','w_thunderstorm_nativeson3']
B=['local_atmosphere_voxel_noise_min','local_atmosphere_voxel_noise_max','local_atmosphere_voxel_noise_scale_mult_z','local_atmosphere_voxel_detail_wind_vertical_speed','local_atmosphere_voxel_distribution_blend','local_atmosphere_localized_fog_density_mult','local_atmosphere_localized_fog_density_mult_raymarch','local_atmosphere_localized_fog_noise_bounds_x','local_atmosphere_localized_fog_noise_bounds_y','local_atmosphere_localized_fog_wind_velocity','local_atmosphere_localized_fog_height_offset']
# 3 fog noise fix (GLOBAL) in all rainy
nf=[]; urb=[]
for f in RAINY:
    g,u=regions(f'{A}/ess/{f}.xml'); vg,vu=regions(f'{V}/timecycle vanila/{f}.xml')
    if any(row(g,k)!=row(vg,k) for k in B): nf.append(f)
    if row(u,'local_atmosphere_voxel_noise_max')!=row(vu,'local_atmosphere_voxel_noise_max'): urb.append(f"{f}({' '.join(row(u,'local_atmosphere_voxel_noise_min')[:1])}/{' '.join(row(u,'local_atmosphere_voxel_noise_max')[:1])} vs vanilla {row(vu,'local_atmosphere_voxel_noise_min')[0]}/{row(vu,'local_atmosphere_voxel_noise_max')[0]})")
rep(not nf,'Fog-noise fix: present in all 13 rainy timecycles (wilderness)',f'Fog-noise fix MISSING in: {nf}')
if urb: issues.append(f'Fog-noise fix only in wilderness (GLOBAL); TOWN region (URBAN) still has Vestigia noise in {len(urb)} rainy files, e.g. {urb[0]} -> plane may show in towns')
# 4 haze colour fix
haze_ok=[];haze_no=[]
for f in RAINY:
    g,_=regions(f'{A}/ess/{f}.xml'); b=row(g,'local_atmosphere_fill_ambient_light_color_b'); r=row(g,'local_atmosphere_fill_ambient_light_color_r')
    (haze_ok if abs(float(b[6])-float(r[6]))<0.12 or float(b[6])>0.9 else haze_no).append(f)
issues.append(f'Less-blue haze fix: in {len(haze_ok)} rainy weathers, NOT in {haze_no} (these keep Vestigia deep-blue haze)') if haze_no else ok.append('Less-blue haze fix in all rainy weathers')
# 5 weather.xml fog switch / density map vs vanilla
VW=open('Vestigia/vanilla reference/weather.xml').read(); AW=open(f'{A}/ess/weather.xml').read()
def wv(t,n):
    m=re.search(r'<Name>%s</Name>\s*<ShortName>'%n,t); nx=re.search(r'<Name>[A-Za-z0-9_]+</Name>\s*<ShortName>',t[m.end():]); b=t[m.start():m.end()+nx.start() if nx else len(t)]
    vs=b.find('<Variations>'); head=b if vs<0 else b[:vs]
    return re.search(r'<Fog value="([^"]*)"',head).group(1), re.findall(r'<LocalizedDensityMap>([^<]*)',b)[-1] if re.findall(r'<LocalizedDensityMap>([^<]*)',b) else '-'
diffw=[]
for n in ['DRIZZLE','RAIN','SHOWER','THUNDER','THUNDERSTORM','HURRICANE','HAIL','SLEET']:
    a=wv(AW,n); v=wv(VW,n)
    if a!=v: diffw.append(f'{n}: Fog {a[0][:3]} map {a[1].replace("localized_density_map_","")} (vanilla Fog {v[0][:3]} map {v[1].replace("localized_density_map_","")})')
issues.append('weather.xml rainy weathers differing from vanilla: '+'; '.join(diffw)) if diffw else ok.append('weather.xml rainy weathers match vanilla fog switch/shape')
# 6 add-on weather.xml = Vestigia weather.xml + sheet only
AD=open('Vestigia - Rain Sheets (Optional)/weather.xml').read()
stripped=re.sub(r'    <Item>\s*<Name>THUNDER_SHEET</Name>.*?</Item>\r?\n','',AD,count=1,flags=re.S)
stripped=re.sub(r'(<Name>THUNDERSTORM</Name>.*?<SheetSettingName>)THUNDER_SHEET','\\1-',stripped,count=1,flags=re.S)
rep(stripped==AW,'Rain Sheets add-on weather.xml = Vestigia weather.xml + sheet only (in sync)','Rain Sheets add-on weather.xml is OUT OF SYNC with Vestigia weather.xml')
# 7 particles consistency
P=lambda s:f'{A}/{s}.xml'
pairs=[('str/shower_render_ground','ess/rainstorm_render_ground'),('str/shower_emitter_drop','ess/rainstorm_emitter_drop'),('str/shower_emitter_ground','ess/rainstorm_emitter_ground'),('str/hurricane_render_ground','ess/thunder_render_ground'),('str/hurricane_emitter_ground','ess/thunder_emitter_ground'),('str/drizzle_emitter_ground','ess/rainstorm_emitter_ground')]
pb=[f'{a} != {b}' for a,b in pairs if h(P(a))!=h(P(b))]
def keyset(p): return dict(re.findall(r'<(\w+) value="([^"]*)"',open(p).read()))
dr=[k for k,v in keyset(P('str/shower_render_drop')).items() if keyset(P('ess/rainstorm_render_drop')).get(k)!=v]+[k for k,v in keyset(P('str/hurricane_render_drop')).items() if keyset(P('ess/thunder_render_drop')).get(k)!=v]
rep(not pb and not dr,'Particles: Shower = Rain files, Hurricane = Thunderstorm files (look identical, wind tweaks only in emitter)',f'Particle mismatch: {pb} {dr}')
# 8 visualsettings sync
rep(h(f'{A}/ess/visualsettings.dat')==h('RW Release 10004 20 2026-10-26T06-42Z zhfBtEA9f/lml/Sauvy/Sauvy - RW Grass Sway/visualsettings.dat'),'visualsettings.dat identical in Vestigia and RW Grass Sway','visualsettings.dat differs between Vestigia and RW Grass Sway')
# 9 option "current/installed" copies match active
stale=[]
for d in glob.glob(f'{OPT}/*/0 - current*')+glob.glob(f'{OPT}/*/0 - default*')+glob.glob(f'{OPT}/15*/1 - rainy*')+glob.glob(f'{OPT}/20*/1 - *'):
    for p in glob.glob(f'{d}/**/*.*',recursive=True):
        b=os.path.basename(p)
        if b.endswith(('.txt','.md')): continue
        if '20 - drizzle' in d:
            tgt=f'{A}/ess/weather.xml' if 'active-ess' in p else 'Vestigia - Rain Sheets (Optional)/weather.xml'
        elif b=='install.xml': tgt=f'{V}/install.xml'
        else:
            tgt=f'{A}/str/{b}' if '/str/' in p.replace(d,'') else (f'{A}/ess/{b}' if os.path.exists(f'{A}/ess/{b}') else f'{A}/wea/{b}')
        if os.path.exists(tgt) and h(p)!=h(tgt): stale.append(p.replace(OPT+'/',''))
rep(not stale,"All options' '0 - current/installed' copies match the installed files",f"STALE '0 - current' copies (don't match installed): {stale}")
print('OK:'); [print('  +',x) for x in ok]
print('\nINCONSISTENCIES / NOTES:'); [print('  !',x) for x in issues]
