Este programa converte um chat exportado do Telegram para o formato do Whatsapp, para que o Telegram possa importá-lo posteriormente.

Para que o programa funcione, siga os passos abaixo:

1 – Exporte o chat através Telegram Desktop;
2 - Vá até o local de exportação: Telegram Desktop/ChatExport_'date'/
3 – Faça uma cópia do arquivo result.json
4 - Certifique-se de que os arquivos converter.py e result.json estejam na mesma pasta
5 - Execute o converter.py
6 – O programa pedirá o nome do contato da primeira mensagem. Ele pode ser encontrado abrindo o arquivo result.json e procurando pela 11ª linha, como algo como '"from": "contact_name", '
7 – O programa irá pedir o id do contato da primeira mensagem. Ele pode ser encontrado abrindo o arquivo result.json e procurando pela 12ª linha, como algo como '"from_id": "contact_id", '
8 – Faça o mesmo para o segundo contato (você) conforme o programa pede
9 – Aguarde até o programa terminar e gerar um arquivo whatsapp.txt
10 - Renomeie o arquivo whatsapp.txt para "Conversa do WhatsApp com [nome do seu contato].txt", sem as aspas e sem os colchetes
11 - Se você deseja importar as fotos, vídeos e áudios do chat do Telegram original, siga para o passo 13. Senão, continue no 12
12 - Envie o arquivo .txt para seu telefone e compartilhe com o Telegram, e depois selecione o contato que deseja importar o chat
13 - Por causa de algum bug (provavelmente do Telegram), é necessário salvar todos os arquivos de fotos, vídeos e áudios numa pasta de drive (no meu caso, Google Drive) para que o Telegram reconheça os arquivos de mídia, e a partir dessa pasta na nuvem, compartilhar os arquivos do seu telefone para o Telegram.

Se ficou alguma dúvida, sinta-se à vontade para deixar algum comentário nesse post do GitHub :)
