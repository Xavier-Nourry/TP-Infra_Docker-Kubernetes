# TP-Infra_Docker-Kubernetes
Dans le cadre de ce tp j'ai choisi d'implémenter une petite application web en Flask dont le but est de fournir 
des propositions d'activités diverses. Pour se faire je fais appelle à l'API <a href="https://www.boredapi.com/">'The Bored API'</a>. L'application consiste en une page html simple délivrant l'activité courante et toutes les
activités ayant déjà été proposées. Le fait de garder en mémoire les anciennes activités est permi par l'utilisation
d'une base de données mariadb.
L'application fonctionne avec deux conteneurs, l'un pour l'application web et l'autre pour la base de données.
Pour la base de données comme pour l'application web, les images docker sont générées à partir de dockerfiles dédiés. Ces images sont disponibles sur dockerhub <a href="https://hub.docker.com/search?q=nourryx&type=image">ici</a> (pour permettre le pull des images à Kubernetes).

L'application complète peut être construitre et exécutée via la lecture du fichier 'docker-compose.yaml' présent à la racine du projet via la commande 'docker-compose up --build'. Le site est alors accessible en <a href="http://127.0.0.1:5000">'127.0.0.1:5000'</a>, à noté que le site peut parfois prendre du temps à répondre ou planter si l'API n'est pas accessible.

Du côté de docker tout fonctionne correctement et les données en base sont persistantes grâce à l'utilisation d'un volume docker dédié. Cependant je ne peux pas présenter l'équivalent en Kubernetes car je n'ai pas pu tester l'exécution de l'application pour cause de pc trop peu puissant pour exécuter minikube.