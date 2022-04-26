from django.shortcuts import render, redirect
import json
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from .models import Battlefield

# Create your views here.
@csrf_exempt
def testPOST(request):
    context = {}
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        policy = {}
        for ally in data['Ally']:
            for target in data['Enemy']:
                policy[(ally['id'], target['id'])] = {'latlng': [ally['lat'], ally['lng']],
                                                      't_latlng': [target['lat'], target['lng']], 'missile': {}}

        for ally in data['Ally']:
            for target in data['Enemy']:
                for weapon in ally['Weapon']:
                    policy[(ally['id'], target['id'])]['missile'][weapon['id']] = {'type': weapon['type'], 'num': 0}
            for weapon in ally['Weapon']:
                for _ in range(int(weapon['num'])):
                    target = np.random.choice(data['Enemy'])
                    policy[(ally['id'], target['id'])]['missile'][weapon['id']]['num'] += 1

        Policy = []
        for key, value in policy.items():
            count = 0
            temp_val = value['missile'].copy()
            for wid, v in value['missile'].items():
                if v['num'] == 0:
                    temp_val.pop(wid, None)
                count += v['num']
            if count > 0:
                value['missile'] = temp_val
                value['ae_pair'] = key
                Policy.append(value)
        b = Battlefield(situation=data, policy=Policy)
        b.save()
        context = {'GeoJSON': json.dumps(data), 'Policy': json.dumps(Policy)}

    return redirect(f'../map/{b.id}')


def get_result(request, bid):
    context = {}
    b = Battlefield.objects.filter(id=bid)
    if b:
        b = b[0]
        context = {'GeoJSON': json.dumps(b.situation), 'Policy': json.dumps(b.policy)}
    return render(request, 'handleResult.html', context)