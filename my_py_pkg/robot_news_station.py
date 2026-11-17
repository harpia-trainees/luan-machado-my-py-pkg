#!/usr/bin/env python3
# Indica que o arquivo deve ser executado utilizando Python 3.

import rclpy
# Importa a biblioteca cliente do ROS 2 para Python.

from rclpy.node import Node
# Importa a classe Node, utilizada para criar nós ROS 2.

from example_interfaces.msg import String
# Importa o tipo de mensagem String, que será publicado no Topic.


class RobotNewsStationNode(Node):
    # Cria uma classe própria que herda da classe Node.
    # Esse Node será responsável por publicar notícias.

    def __init__(self):
        # Construtor da classe. É executado quando criamos o objeto.

        super().__init__("robot_news_station")
        # Inicializa a classe Node (classe-pai).
        # Define "robot_news_station" como o nome deste Node.

        self.robot_name = "R2-D2"
        # Define o nome do robô que será usado nas mensagens publicadas.

        self.publisher_ = self.create_publisher(String, "robot_news", 10)
        # Cria um Publisher.
        # String: tipo de mensagem que será publicada.
        # "robot_news": nome do Topic utilizado para comunicação.
        # 10: profundidade da fila (history depth).

        self.timer_ = self.create_timer(0.5, self.publish_news)
        # Cria um Timer que chama publish_news a cada 0.5 segundo.
        # Isso faz com que o Node publique mensagens periodicamente.

        self.get_logger().info("Robot News Station has been started.")
        # Exibe uma mensagem informativa no terminal indicando
        # que o Node foi iniciado.


    def publish_news(self):
        # Método responsável por publicar as mensagens.

        msg = String()
        # Cria uma nova mensagem do tipo String.

        msg.data = "Hi, this is " + self.robot_name + " bringing you the latest news!"
        # Define o conteúdo da mensagem.
        # O campo data armazena o texto que será enviado.

        self.publisher_.publish(msg)
        # Publica a mensagem no Topic "robot_news".
        # Os Subscribers inscritos nesse Topic poderão recebê-la.


def main(args=None):
    # Função principal do programa.

    rclpy.init(args=args)
    # Inicializa o contexto ROS 2.

    node = RobotNewsStationNode()
    # Cria uma instância do nosso Node.
    # Nesse momento, o construtor __init__ é executado.

    rclpy.spin(node)
    # Mantém o Node ativo e permite que o executor processe eventos.
    # É por meio dele que o Timer consegue chamar publish_news.
    # O programa permanece executando até ser interrompido.

    rclpy.shutdown()
    # Encerra o contexto ROS 2 após o término do spin.


if __name__ == "__main__":
    # Verifica se o arquivo está sendo executado diretamente.

    main()
    # Chama a função principal.