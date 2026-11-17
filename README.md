# ROS 2 Jazzy — Comunicação entre Nodes com Python

Este repositório registra, em ordem cronológica, o desenvolvimento do curso de ROS 2.

O desenvolvimento foi realizado com ROS 2 Jazzy em um container Docker, utilizando o VS Code para edição dos arquivos e terminais separados.

## 1. Criação do pacote Python

O pacote `my_py_pkg` foi criado no workspace ROS 2 com o sistema de build `ament_python` e a dependência inicial `rclpy`.

```bash
cd /ros2_ws/src
ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
```

![Criação do pacote my_py_pkg](images/01-criacao-do-pacote.jpg)

## 2. Criação do primeiro Node

Foi criado o arquivo `my_first_node.py` no módulo Python interno do pacote. Nesse primeiro exemplo, foi implementado um Node mínimo para acompanhar sua inicialização e execução.

![Criação do arquivo Python](images/02-criacao-do-arquivo-python.jpg)

O executável `my_first_node_executable` foi registrado no `setup.py`.

![Primeiro código e configuração do pacote](images/03-primeiro-codigo-e-configuracao.jpg)

Após a compilação do pacote, o primeiro Node foi executado. A saída no terminal registra as mensagens produzidas durante a execução.

![Compilação inicial](images/04-compilacao-inicial.jpg)

![Execução do primeiro Node](images/05-execucao-do-primeiro-node.jpg)

## 3. Implementação do Publisher

Foi criado o arquivo `robot_news_station.py`, responsável pela publicação periódica de mensagens.

![Criação do arquivo do Publisher](images/06-criacao-do-publisher.jpg)

A implementação utiliza a classe `RobotNewsStationNode`, que herda de `Node`. O Publisher foi configurado com as seguintes características:

| Elemento | Configuração |
|---|---|
| Nome do Node | `robot_news_station` |
| Tipo de mensagem | `example_interfaces/msg/String` |
| Topic | `robot_news` |
| Profundidade da fila | `10` |
| Timer | `0,5 segundo` (aproximadamente 2 Hz) |
| Método de publicação | `publish_news()` |

O Timer agenda o método `publish_news()` a cada 0,5 segundo. A cada chamada, uma mensagem `String` é criada, seu campo `data` recebe o texto `Hello` e a mensagem é publicada no Topic `robot_news`.

![Implementação do RobotNewsStationNode](images/07-implementacao-do-publisher.jpg)

Como o Publisher utiliza o tipo `String` de `example_interfaces`, essa dependência foi declarada no `package.xml`.

![Dependência example_interfaces no package.xml](images/08-dependencia-no-package-xml.jpg)

O executável `robot_news_station_executable` foi adicionado ao `setup.py`, mantendo também o executável do primeiro Node.

![Registro do Publisher no setup.py](images/09-registro-do-publisher-no-setup.jpg)

Após essa alteração, o pacote foi recompilado.

## 4. Implementação do Subscriber

Em seguida, foi criado o arquivo `smartphone.py`, contendo a classe `SmartphoneNode`.

![Criação do arquivo smartphone.py](images/10-criacao-do-subscriber.jpg)

O Subscriber foi configurado para receber mensagens do tipo `String` no mesmo Topic `robot_news` utilizado pelo Publisher. O método `callback_receive_news()` trata as mensagens recebidas e exibe seu conteúdo no terminal.

O executável `smartphone_executable` também foi registrado no `setup.py`. Com isso, o pacote passou a contar com três executáveis: `my_first_node_executable`, `robot_news_station_executable` e `smartphone_executable`.

![Registro dos três executáveis no setup.py](images/11-registro-dos-tres-executaveis.jpg)

O pacote foi recompilado após o registro do Subscriber.

![Compilação com os três executáveis](images/12-compilacao-com-os-tres-executaveis.jpg)

## 5. Comunicação entre Publisher e Subscriber

O Publisher `robot_news_station` e o Subscriber `smartphone` foram executados simultaneamente em terminais separados. O Publisher passou a publicar mensagens periodicamente, enquanto o Subscriber recebia e exibia o conteúdo recebido pelo Topic `robot_news`.

![Publisher e Subscriber em execução](images/13-publisher-e-subscriber-em-execucao.jpg)

## 6. Visualização da comunicação com rqt_graph

Com os dois Nodes em execução, foi utilizado o `rqt_graph` para visualizar a comunicação estabelecida entre eles. Durante a inicialização, o terminal exibiu avisos relacionados ao acesso gráfico e ao driver AMD; a janela do `rqt_graph` foi aberta mesmo com esses avisos.

![Execução do rqt_graph junto aos processos](images/14-rqt-graph-e-processos.jpg)

O grafo apresentou o fluxo entre o Publisher, o Topic e o Subscriber:

```text
/robot_news_station  →  /robot_news  →  /smartphone
       Publisher            Topic          Subscriber
```

![Grafo inicial no rqt_graph](images/15-grafo-inicial-no-rqt-graph.jpg)

## 7. Execução simultânea de múltiplos Nodes e remapeamento

Na etapa seguinte, foram iniciadas seis instâncias simultâneas: três Publishers e três Subscribers. O argumento `__node` foi utilizado para atribuir nomes diferentes às instâncias. Além disso, o terceiro Publisher e o terceiro Subscriber foram direcionados para o Topic `robot_news_2`.

![Execução simultânea de múltiplos Nodes e remapeamento](images/16-execucao-multipla-de-nodes-e-remapeamento.jpg)

**Publishers:**

```bash
ros2 run my_py_pkg robot_news_station_executable --ros-args -r __node:=robot_1
ros2 run my_py_pkg robot_news_station_executable --ros-args -r __node:=robot_2
ros2 run my_py_pkg robot_news_station_executable --ros-args -r __node:=robot_3 -r robot_news:=robot_news_2
```

**Subscribers:**

```bash
ros2 run my_py_pkg smartphone_executable --ros-args -r __node:=smartphone_1
ros2 run my_py_pkg smartphone_executable --ros-args -r __node:=smartphone_2
ros2 run my_py_pkg smartphone_executable --ros-args -r __node:=smartphone_3 -r robot_news:=robot_news_2
```

O remapeamento `__node` altera o nome de cada instância sem modificar o código Python. O remapeamento `robot_news:=robot_news_2` altera o Topic utilizado pelos dois Nodes da terceira dupla.

A comunicação ficou organizada em dois grupos:

```text
 robot_1 ──────┐                         ┌──── smartphone_1
               ├──── /robot_news ────────┤
 robot_2 ──────┘                         └──── smartphone_2

 robot_3 ─────────── /robot_news_2 ─────────── smartphone_3
```

Os dois Publishers conectados a `/robot_news` publicam no mesmo canal, e os dois Subscribers inscritos nesse Topic podem receber mensagens de ambos. Já `/robot_news_2` é utilizado pela terceira dupla, mantendo esse fluxo separado do primeiro.

![Grafo dos Nodes e tópicos remapeados no rqt_graph](images/17-rqt-graph-com-remapeamento.jpg)

## Atualização do registro

Este README será atualizado até o fim do curso de ROS 2, incorporando os próximos conteúdos estudados, atividades práticas e registros do desenvolvimento.
