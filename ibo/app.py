from flask import Flask
render_template_string
import json
app= Flask(__name__)
with open('veri.json','r',encoding='utf-8') as f:
    veri =json.load(f)
@app.route('/')
def ana_sayfa():
    kullanici = veri['hastalar'][0]
    aktivite =
    veri['aktivite'].get(kullanici['tanı'],'Genel hafif egzersiz')
    ilac__bilgileri = ''
    for ilac in kullanici['ilaclar']:
        bilgi=veri['ilaclar'].get(ilac,{})
        ilac__bilgileri += f"""
        <h4>{ilac}</h4>
        <p>Avantaj:
        {bilgi.get('avantaj','bilgi yok')}</p>
        <p>yan etki:
        {bilgi.get('yan_etki','bilgi yok')}</p>
 html = f"""
        <h1>sağlık uygulamamız başlıyor</h1>
        <hr>
        <h2>hasta:{kullanici['ad']}</h2>
        <p>tanı:{kullanici['tanı']}</p> 
        <p>onerilen aktivite:{aktivite}</p> 
        <h3>ilac bilgileri:</h3>
          {ilac__bilgileri}
        """
        return render_template_string(html)
        if__name__=="__main__":
          app.run(debug=True)
    