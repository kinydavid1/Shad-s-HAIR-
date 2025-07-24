#!/data/data/com.termux/files/usr/bin/bash

IP="10.255.170.127"
CHEMINS=(
"/video"
"/stream"
"/live"
"/mjpeg"
"/video.cgi"
"/cgi-bin/video.cgi"
"/snapshot.jpg"
"/admin"
"/login"
)

echo "🔍 Scan de chemins sur $IP"

for CHEMIN in "${CHEMINS[@]}"; do
  echo -n "➡️ $CHEMIN ... "
  HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://$IP$CHEMIN)
  if [[ "$HTTP_CODE" == "200" ]]; then
    echo "✅ Trouvé (200 OK)"
  elif [[ "$HTTP_CODE" == "401" ]]; then
    echo "🔐 Protégé par mot de passe (401 Unauthorized)"
  elif [[ "$HTTP_CODE" == "403" ]]; then
    echo "⛔ Accès interdit (403 Forbidden)"
  elif [[ "$HTTP_CODE" == "302" || "$HTTP_CODE" == "301" ]]; then
    echo "🔀 Redirigé ($HTTP_CODE)"
  else
    echo "❌ $HTTP_CODE"
  fi
done
