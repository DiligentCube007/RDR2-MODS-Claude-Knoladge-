"""Small helpers for editing RDR2 timecycle files (w_*.xml) the way this project does it.

Timecycle layout: <cycle name=... regions="2"> <region name="GLOBAL"> ...keys... </region> <region name="URBAN"> ...
Each key is one line: <key_name> v00 v01 ... v12</key_name>  (13 time-of-day columns).
GLOBAL = wilderness, URBAN = towns. Edit GLOBAL and/or URBAN explicitly - they are independent.
Files are CRLF; some are UTF-8 with BOM -> always open with encoding='utf-8', newline='' and write back the same way.
"""
import re

def regions(text):
    """Split a timecycle file into [GLOBAL part, URBAN part] (URBAN part starts at '<region name="URBAN"')."""
    i = text.find('<region name="URBAN"')
    return [text[:i], text[i:]]

def get(part, key):
    """Return (match, [13 floats]) for a key inside one region part, or (None, None)."""
    m = re.search(r'(<%s>)([-0-9.\s]+)(</%s>)' % (key, key), part)
    return (m, [float(x) for x in m.group(2).split()]) if m else (None, None)

def put(part, key, values):
    """Replace a key's 13 values inside one region part (keeps the line format)."""
    m, _ = get(part, key)
    fmt = lambda v: f'{v:.4f}' if abs(v) >= 0.01 or v == 0 else f'{v:.6f}'
    return part[:m.start()] + m.group(1) + ' ' + ' '.join(fmt(v) for v in values) + m.group(3) + part[m.end():]

def rows(part):
    """All numeric keys of one region part -> {key: [floats]}."""
    return {m.group(1): [float(x) for x in m.group(2).split()]
            for m in re.finditer(r'<([a-z0-9_]+)>([-0-9.\s]+)</\1>', part)}

def to_vanilla(active_path, vanilla_path, keys, regions_to_fix=('GLOBAL', 'URBAN')):
    """Return the text of active_path with `keys` set to the vanilla file's values in the given regions."""
    t = open(active_path, encoding='utf-8', newline='').read()
    v = open(vanilla_path, encoding='utf-8', newline='').read()
    out = []
    for name, a, b in zip(('GLOBAL', 'URBAN'), regions(t), regions(v)):
        if name in regions_to_fix:
            for k in keys:
                _, vv = get(b, k)
                if vv is not None and get(a, k)[0] is not None:
                    a = put(a, k, vv)
        out.append(a)
    return ''.join(out)

# The 11 'fog noise / localized fog' keys = THE mist plane fix (option 15):
FOG_NOISE_FIX_KEYS = [
    'local_atmosphere_voxel_noise_min', 'local_atmosphere_voxel_noise_max', 'local_atmosphere_voxel_noise_scale_mult_z',
    'local_atmosphere_voxel_detail_wind_vertical_speed', 'local_atmosphere_voxel_distribution_blend',
    'local_atmosphere_localized_fog_density_mult', 'local_atmosphere_localized_fog_density_mult_raymarch',
    'local_atmosphere_localized_fog_noise_bounds_x', 'local_atmosphere_localized_fog_noise_bounds_y',
    'local_atmosphere_localized_fog_wind_velocity', 'local_atmosphere_localized_fog_height_offset']
