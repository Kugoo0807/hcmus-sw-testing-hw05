import csv
import sys
import json
import math

def calculate_percentile(data, percentile):
    if not data:
        return 0
    data.sort()
    k = (len(data) - 1) * percentile
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return data[int(k)]
    d0 = data[int(f)] * (c - k)
    d1 = data[int(c)] * (k - f)
    return round(d0 + d1)

def analyze(file_path):
    endpoints = {}
    total_start = sys.maxsize
    total_end = 0
    total_reqs = 0
    total_errors = 0
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ts = int(row['timeStamp'])
            elapsed = int(row['elapsed'])
            label = row['label']
            success = row['success'].lower() == 'true'
            
            end_time = ts + elapsed
            if ts < total_start: total_start = ts
            if end_time > total_end: total_end = end_time
            
            if label not in endpoints:
                endpoints[label] = {'reqs': 0, 'errors': 0, 'latencies': [], 'start': sys.maxsize, 'end': 0}
            
            ep = endpoints[label]
            ep['reqs'] += 1
            if not success:
                ep['errors'] += 1
                total_errors += 1
            ep['latencies'].append(elapsed)
            
            if ts < ep['start']: ep['start'] = ts
            if end_time > ep['end']: ep['end'] = end_time
            total_reqs += 1

    results = {}
    for label, data in endpoints.items():
        if data['reqs'] == 0: continue
        time_span_sec = (data['end'] - data['start']) / 1000.0
        rps = data['reqs'] / time_span_sec if time_span_sec > 0 else data['reqs']
        avg_lat = sum(data['latencies']) / data['reqs']
        p90 = calculate_percentile(data['latencies'], 0.90)
        p95 = calculate_percentile(data['latencies'], 0.95)
        err_rate = (data['errors'] / data['reqs']) * 100
        
        results[label] = {
            'RPS': round(rps, 2),
            'Avg': round(avg_lat, 2),
            'P90': p90,
            'P95': p95,
            'ErrRate': round(err_rate, 2),
            'TotalReqs': data['reqs']
        }
    
    overall_span = (total_end - total_start) / 1000.0 if total_start != sys.maxsize else 0
    overall_rps = total_reqs / overall_span if overall_span > 0 else total_reqs
    overall_err = (total_errors / total_reqs) * 100 if total_reqs > 0 else 0
    
    return {
        'overall': {
            'RPS': round(overall_rps, 2),
            'ErrRate': round(overall_err, 2),
            'TotalReqs': total_reqs,
            'DurationSecs': round(overall_span, 2)
        },
        'endpoints': results
    }

files = [
    r"c:\Users\KUGOO\OneDrive - VNU-HCMUS\Documents\HỌC\IT\25_HKIII\Kiểm thử phần mềm\HW05\23127212_Load.jtl",
    r"c:\Users\KUGOO\OneDrive - VNU-HCMUS\Documents\HỌC\IT\25_HKIII\Kiểm thử phần mềm\HW05\23127212_Spike.jtl",
    r"c:\Users\KUGOO\OneDrive - VNU-HCMUS\Documents\HỌC\IT\25_HKIII\Kiểm thử phần mềm\HW05\23127212_Stress.jtl"
]

output = {}
for file in files:
    name = file.split('\\')[-1].replace('.jtl', '')
    try:
        output[name] = analyze(file)
    except Exception as e:
        output[name] = {"error": str(e)}

print(json.dumps(output, indent=2))
