#!/usr/bin/env python3
# Indica que o arquivo deve ser executado utilizando Python 3.

import rclpy
# Importa a biblioteca cliente do ROS 2 para Python.

from rclpy.node import Node
# Importa a classe Node, utilizada para criar nós ROS 2.

from example_interfaces.msg import String
# Importa o tipo de mensagem String, que será publicado no Topic.


class SmartphoneNode(Node):
    # Cria uma classe própria que herda da classe Node.
    # Esse Node será responsável por publicar notícias.

    def __init__(self):
        # Construtor da classe. É executado quando criamos o objeto.

        super().__init__("smartphone")
        # Inicializa a classe Node (classe-pai).
        # Define "smartphone" como o nome deste Node.

        self.subscriber_ = self.create_subscription(String, "robot_news", self.callback_robot_news, 10)
        # Cria um Subscriber.
        # String: tipo de mensagem que será recebida.
        # "robot_news": nome do Topic utilizado para comunicação.
        # 10: profundidade da fila (history depth).

        self.get_logger().info("Smartphone has been started.")
        # Exibe uma mensagem informativa no terminal indicando
        # que o Node foi iniciado.


    def callback_robot_news(self, msg):
        # Método chamado sempre que uma nova mensagem é recebida no Topic "robot_news".

        self.get_logger().info("Received news: " + msg.data)
        # Exibe a mensagem recebida no terminal.
        # msg.data contém o conteúdo da mensagem do tipo String.


def main(args=None):
    # Função principal do programa.

    rclpy.init(args=args)
    # Inicializa o contexto ROS 2.

    node = SmartphoneNode()
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