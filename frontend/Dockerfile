# Use a imagem nginx como base
FROM nginx

# Copie os arquivos de configuração do Nginx para dentro do contêiner
COPY nginx.conf /etc/nginx/nginx.conf

# Copie os arquivos estáticos do frontend para dentro do diretório raiz do servidor Nginx
COPY index.html /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/

# Exponha a porta 80 para permitir acesso ao servidor Nginx
EXPOSE 80

# Inicie o servidor Nginx quando o contêiner for iniciado
CMD ["nginx", "-g", "daemon off;"]

