import os
import json
import urllib
from geojson import Point, Feature, FeatureCollection, dump

url = "https://www.datos.gov.co/resource/gt2j-8ykr.json?departamento=Valle%20del%20Cauca"
response = urllib.urlopen(url)
data = json.loads(response.read())


#input_json = "covid19.json";
imput_geojson = "valle_cauca_municipios_centroids.geojson";
output_geojson = "covid19_vc.geojson";

#with open(input_json) as f:
#    data = json.load(f)
  
with open(imput_geojson) as f2:
    data2 = json.load(f2)

features = []
    
for p in data:
    print('id_caso: ' + p['id_de_caso'])
    print('fecha_notifica: ' + p['fecha_de_notificaci_n'])
    print('codigo_divipola: ' + p['codigo_divipola'])
    print('ciudad_ubicacion: ' + p['ciudad_de_ubicaci_n'])
    print('departamento: ' + p['departamento'])
    print('atencion: ' + p['atenci_n'])
    print('edad: ' + p['edad'])
    print('sexo: ' + p['sexo'])
    print('tipo: ' + p['tipo'])
    print('estado: ' + p['estado'])
    print('pais_procedencia: ' + p['pa_s_de_procedencia'])
    print('fis: ' + p['fis'])
    print('fecha_de_muerte: ' + p['fecha_de_muerte'])
    print('fecha_diagnostico: ' + p['fecha_diagnostico'])
    print('fecha_recuperado: ' + p['fecha_recuperado'])
    print('fecha_reporte_web: ' + p['fecha_reporte_web'])
    
    propuerties_ = {'id_caso' : p['id_de_caso'],
    'fecha_notifica': p['fecha_de_notificaci_n'],
    'codigo_divipola': p['codigo_divipola'],
    'ciudad_ubicacion': p['ciudad_de_ubicaci_n'],
    'departamento': p['departamento'],
    'atencion' : p['atenci_n'],
    'edad': p['edad'],
    'sexo': p['sexo'],
    'tipo':p['tipo'],
    'estado':p['estado'],
    'pais_procedencia':p['pa_s_de_procedencia'],
    'fis':p['fis'],
    'fecha_de_muerte':p['fecha_de_muerte'],
    'fecha_diagnostico' :p['fecha_diagnostico'],
    'fecha_recuperado':p['fecha_recuperado'],
    'fecha_reporte_web':p['fecha_reporte_web']};
    
    for feature2 in data2['features']:
        if p['codigo_divipola'] == feature2['properties']['cod_munici'] :
            print('nom_munici: ' + feature2['properties']['nom_munici'])
            print('lon: ' + str(feature2['geometry']['coordinates'][0]))
            print('lat: ' + str(feature2['geometry']['coordinates'][1]))
            
            point = Point((feature2['geometry']['coordinates'][0], feature2['geometry']['coordinates'][1]))
            features.append(Feature(geometry=point, properties=propuerties_))
    print('------------------------------------------------')
    

feature_collection = FeatureCollection(features)
with open(output_geojson, 'w') as f:
   dump(feature_collection, f)

print('Done!!');

