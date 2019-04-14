
#####################################
Coleta dos seguidores evolutioncoffee
#####################################

Descrição
**********

Para coletar os dados utilizei o site https://phantombuster.com, o site oferece uma conta free com algumas limitações,
oferece também algumas libs para Web scraping, como por exemplo: https://github.com/phantombuster/nickjs e ainda
a geração automatica de um agente para alguns casos, como por exemplo a coleta de seguidores de usuários instagram.
Com as libs citadas pode-se criar um "Custom api agent" para qualquer site, em função do senso de urgencia, optei
por criar um agent automático, já que oferecem essa opção para coleta de seguidores no Instagram.

O agente gerado automaticamente (Instagram Follower Collector) pode ser acionado via linguagem de programação ou via comando curl, novamente em
função do senso de urgencia e por ser uma conta free com limitações optei pelo Curl, nessa opcao, quando o comando
é executado, a coleta é feita, é gerado 2 arquivos como resultado, um .csv e outro .json, e então é retornado os
dados da execução, incluindo os endereços para download dos arquivos


Comando para fazer a coleta via curl:
*************************************

.. code-block::

    curl https://phantombuster.com/api/v1/agent/87372/launch --data "{\"output\":\"result-object\",\"argument\":{\"sessionCookie\":\"1524004563%3AHrGuUBkeLgsWaX%3A20\",\"spreadsheetUrl\":\"https://www.instagram.com/evolutioncoffee/\",\"numberofProfilesperLaunch\":10,\"csvName\":\"followers_evolution\"}}" --header "Content-Type: application/json" --header "X-Phantombuster-Key-1: 2DdDSOpKMYjvRC9gvOhAmWjXP4yRW1b0"


Resultado
*********

O resultado deverá informar o endereço (para download) dos arquivos gerados (.csv e .json.), algo como:

.. code-block::

    {
      "status": "success",
      "message": "Agent finished (success)",
      "data": {
        "containerId": 55595396,
        "executionTime": 90,
        "exitCode": 0,
        "resultObject": {
          "csvURL": "https://phantombuster.s3.amazonaws.com/JFGl2h7LwrA/nWtYoxzanRN2LFCNyyC9Aw/followers_evolution.csv",
          "jsonUrl": "https://phantombuster.s3.amazonaws.com/JFGl2h7LwrA/nWtYoxzanRN2LFCNyyC9Aw/followers_evolution.json"
        }
      }
    }


