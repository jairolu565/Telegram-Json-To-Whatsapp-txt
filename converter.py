import json
from datetime import datetime

# Função para converter a data e hora para o formato desejado
def format_date(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')
    return date_object.strftime('%d/%m/%Y %H:%M')

# Solicitar nomes e IDs dos participantes da conversa
participant1_name = input("Digite o nome do primeiro participante da conversa: ")
participant1_id = input(f"Digite o ID de usuário do {participant1_name}: ")
participant2_name = input("Digite o nome do segundo participante da conversa: ")
participant2_id = input(f"Digite o ID de usuário do {participant2_name}: ")

# Mapeamento de IDs para nomes de remetentes
sender_names = {
    participant1_id: participant1_name,
    participant2_id: participant2_name
}

# Carregar o arquivo JSON
with open('telegram.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Acessar a lista de mensagens
messages = data.get('messages', [])

# Abrir o arquivo de saída para gravação
with open('whatsapp.txt', 'w', encoding='utf-8') as output_file:
    # Loop através das mensagens e gravar no arquivo "whatsapp.txt"
    for message in messages:
        date = format_date(message['date'])
        sender_id = message.get('from_id', 'Remetente Desconhecido')
        sender_name = sender_names.get(sender_id, sender_id)
        
        # Verificar se a mensagem é uma foto
        if 'photo' in message:
            photo_filename = message['photo'].split('/')[-1]  # Obtém apenas o nome do arquivo
            formatted_message = f"{date} - {sender_name}: {photo_filename} (arquivo anexado)"
        # Verificar se a mensagem é um vídeo
        elif 'file' in message and message['file'].endswith('.mp4'):
            video_filename = message['file'].split('/')[-1]  # Obtém apenas o nome do arquivo
            formatted_message = f"{date} - {sender_name}: ‎{video_filename} (arquivo anexado)"
        # Verificar se a mensagem é um áudio
        elif 'file' in message and message.get('media_type') == 'voice_message':
            audio_filename = message['file'].split('/')[-1]  # Obtém apenas o nome do arquivo
            formatted_message = f"{date} - {sender_name}: ‎{audio_filename} (arquivo anexado)"
        else:
            text = message.get('text', 'Mensagem sem texto')
            formatted_message = f"{date} - {sender_name}: {text}"
        
        output_file.write(formatted_message + '\n')

print("Conteúdo convertido e gravado em 'whatsapp.txt'.")
