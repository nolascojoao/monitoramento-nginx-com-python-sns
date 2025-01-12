# Monitoramento do Nginx com Python + Boto3 + AWS SNS 🔔


Script em **Python** para monitorar o status do servidor **Nginx**. 


Sempre que o status do servidor mudar, o script envia notificações por e-mail utilizando o **AWS SNS**.


---


## Pré-requisitos ⚙️


1. **AWS CLI**: Instalado e configurado com credenciais apropriadas.


2. **Python 3 e Boto3**: Instalados no servidor.


3. **Tópico AWS SNS**: Um tópico SNS já deve ter sido criado na AWS para envio de notificações.


---


## Instruções de Configuração 🛠️


### 1. Configure o Script


> Edite o script `nginx_monitor.py` para substituir `ARN_DO_TÓPICO_SNS` pelo ARN do seu Tópico SNS da AWS.
```python
topic_arn = 'ARN_DO_TÓPICO_SNS'
```


### 2. Crie um Serviço systemd


> Para que o script rode como um serviço.


1. Crie um arquivo de unidade systemd:
   ```bash
   sudo nano /etc/systemd/system/nginx-monitor.service
   ```

   
2. Adicione a seguinte configuração:


> Altere /caminho/para/nginx_monitor.py para o caminho absoluto onde o seu script Python está localizado.
   ```ini
   [Unit]
   Description=Serviço de Monitoramento do Nginx
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /caminho/para/nginx_monitor.py
   Restart=always
   User=ubuntu

   [Install]
   WantedBy=multi-user.target
   ```

   
4. Salve e saia do arquivo.


### 3. Inicie e Habilite o Serviço


> Execute os seguintes comandos para iniciar e habilitar o serviço:
```bash
sudo systemctl daemon-reload
sudo systemctl start nginx-monitor.service
sudo systemctl enable nginx-monitor.service
```

### 4. Teste a Configuração


> Pare e inicie o servidor Nginx para disparar notificações:
```bash
sudo systemctl stop nginx
sudo systemctl start nginx
```


> Você deverá receber um e-mail similar ao seguinte:
```
Assunto: Nginx Server Status
Corpo: {"status": "DOWN", "server": "EC2 Nginx Server"}
```


---



## Exemplo de Alerta por E-mail para Nginx Ativo e Inativo 📧


<div align="center">
  <img src="https://github.com/user-attachments/assets/e5c6ed2f-4a7b-4388-8be7-965bd4541187"/>
</div>


<div align="center">
  <img src="https://github.com/user-attachments/assets/db8151e0-e740-4ee4-b034-3dfdbe470c8a"/>
</div>
