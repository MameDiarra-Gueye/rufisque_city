from django.http import HttpResponse

def accueil(request):
    html = """
    <html><body style="text-align:center; font-family:Arial; background-color:#fff8e7; margin:0; padding:0;">
    <div style="background-color:#e67e22; color:white; padding:40px 20px;">
    <h1 style="font-size:40px; margin:0;">Bienvenue a Rufisque</h1>
    <p style="font-size:18px;">Decouvrez la ville, son histoire, ses marches et ses plages !</p>
    </div>
    <p style="margin-top:20px;">
    <a href="/histoire/">Histoire</a> |
    <a href="/marches/">Marches</a> |
    <a href="/plages/">Plages</a> |
    <a href="/decouvrir/">Decouvrir</a> |
    <a href="/contact/">Contact</a>
    </p>
    <img src="https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=800" width="600" style="border-radius:10px;">
    <p style="max-width:600px; margin:20px auto;">Rufisque est une ville chaleureuse au Senegal. Venez visiter ses quartiers, gouter sa cuisine et rencontrer ses habitants.</p>
    <p><a href="/decouvrir/" style="background:#e67e22; color:white; padding:10px 20px; border-radius:5px; text-decoration:none;">Decouvrir Rufisque</a></p>
    </body></html>
    """
    return HttpResponse(html)

def histoire(request):
    html = """
    <html><body style="text-align:center; font-family:Arial; background-color:#fdebd0; margin:0; padding:20px;">
    <h1 style="color:#7e5109;">L'Histoire de Rufisque</h1>
    <p>Une des plus anciennes villes du Senegal, entre mer et commerce.</p>
    <p>
    <a href="/">Accueil</a> |
    <a href="/marches/">Marches</a> |
    <a href="/plages/">Plages</a> |
    <a href="/decouvrir/">Decouvrir</a> |
    <a href="/contact/">Contact</a>
    </p>
    <img src="https://images.unsplash.com/photo-1509099863732-ef4bff19e808?w=600" width="300" style="border-radius:10px; margin:5px;">
    <img src="https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600" width="300" style="border-radius:10px; margin:5px;">
    <img src="https://images.unsplash.com/photo-1533900298318-6b8da08a523e?w=600" width="300" style="border-radius:10px; margin:5px;">
    <p style="margin-top:20px; max-width:600px; margin-left:auto; margin-right:auto;">Rufisque etait un grand port de commerce. Ses vieilles maisons, ses rues et son marche racontent encore son passe.</p>
    <p><a href="/">Retour accueil</a></p>
    </body></html>
    """
    return HttpResponse(html)

def marches(request):
    html = """
    <html><body style="text-align:center; font-family:Arial; background-color:#fff2cc; margin:0; padding:20px;">
    <h1 style="color:#b7791f;">Les Marches de Rufisque</h1>
    <p>Epices, tissus, poissons, fruits... tout est colore et vivant !</p>
    <p>
    <a href="/">Accueil</a> |
    <a href="/histoire/">Histoire</a> |
    <a href="/plages/">Plages</a> |
    <a href="/decouvrir/">Decouvrir</a> |
    <a href="/contact/">Contact</a>
    </p>
    <img src="https://images.unsplash.com/photo-1533900298318-6b8da08a523e?w=600" width="300" style="border-radius:10px; margin:5px;">
    <img src="https://images.unsplash.com/photo-1488459716781-31db52582fe9?w=600" width="300" style="border-radius:10px; margin:5px;">
    <img src="https://images.unsplash.com/photo-1578916171728-46686eac8d58?w=600" width="300" style="border-radius:10px; margin:5px;">
    <p style="margin-top:20px;">Venez negocier, gouter et decouvrir les couleurs du marche de Rufisque !</p>
    <p><a href="/">Retour accueil</a></p>
    </body></html>
    """
    return HttpResponse(html)

def plages(request):
    html = """
    <html><body style="text-align:center; font-family:Arial; background-color:#e0f7ff; margin:0; padding:20px;">
    <h1 style="color:#0077b6;">Les Plages de Rufisque</h1>
    <p>Du sable, de la mer, et des pirogues de pecheurs.</p>
    <p>
    <a href="/">Accueil</a> |
    <a href="/histoire/">Histoire</a> |
    <a href="/marches/">Marches</a> |
    <a href="/decouvrir/">Decouvrir</a> |
    <a href="/contact/">Contact</a>
    </p>
    <img src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600" width="300" style="border-radius:10px; margin:5px;">
    <img src="https://images.unsplash.com/photo-1519046904884-53103b34b206?w=600" width="300" style="border-radius:10px; margin:5px;">
    <img src="https://images.unsplash.com/photo-1502680390469-be75c86b636f?w=600" width="300" style="border-radius:10px; margin:5px;">
    <p style="margin-top:20px;">Venez profiter du soleil et de la brise de l'ocean a Rufisque !</p>
    <p><a href="/">Retour accueil</a></p>
    </body></html>
    """
    return HttpResponse(html)

def contact(request):
    html = """
    <html><body style="text-align:center; font-family:Arial; background-color:#e8f5e9; margin:0; padding:20px;">
    <h1 style="color:#2e7d32;">Contactez-nous</h1>
    <p>Une question sur Rufisque ? Ecrivez-nous !</p>
    <p>
    <a href="/">Accueil</a> |
    <a href="/histoire/">Histoire</a> |
    <a href="/marches/">Marches</a> |
    <a href="/plages/">Plages</a> |
    <a href="/decouvrir/">Decouvrir</a>
    </p>
    <div style="background:white; width:320px; margin:20px auto; padding:20px; border-radius:10px; text-align:left;">
    <p><b>Adresse :</b> Rufisque, Dakar, Senegal</p>
    <p><b>Telephone :</b> +221 78 474 10 84 </p>
    <p><b>Email :</b> contact@rufisque.sn</p>
    <p><b>Horaires :</b> Lundi - Samedi, 8h - 18h</p>
    </div>
    <img src="https://images.unsplash.com/photo-1521791136064-7986c2920216?w=600" width="300" style="border-radius:10px; margin:5px;">
    <p style="margin-top:20px;">On vous repondra tres vite !</p>
    <p><a href="/">Retour accueil</a></p>
    </body></html>
    """
    return HttpResponse(html)

def decouvrir(request):
    html = """
    <html><body style="text-align:center; font-family:Arial; background-color:#fff8e7; margin:0; padding:20px;">
    <h1 style="color:#d35400;">Decouvrir Rufisque</h1>
    <p>Une ville pleine d'histoire, de couleurs et de vie.</p>
    <p>
    <a href="/">Accueil</a> |
    <a href="/histoire/">Histoire</a> |
    <a href="/marches/">Marches</a> |
    <a href="/plages/">Plages</a> |
    <a href="/contact/">Contact</a>
    </p>
    <img src="https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600" width="300" style="border-radius:10px; margin:5px;">
    <img src="https://images.unsplash.com/photo-1533900298318-6b8da08a523e?w=600" width="300" style="border-radius:10px; margin:5px;">
    <img src="https://images.unsplash.com/photo-1523805009345-7448845a9e53?w=600" width="300" style="border-radius:10px; margin:5px;">
    <p style="margin-top:20px;">Visitez les quartiers, rencontrez les habitants, gouter la cuisine locale !</p>
    <p><a href="/">Retour accueil</a></p>
    </body></html>
    """
    return HttpResponse(html)