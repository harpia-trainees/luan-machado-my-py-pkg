#!/usr/bin/env python3
# Indica ao sistema que este arquivo deve ser executado usando Python 3.

import rclpy
# Importa a biblioteca cliente do ROS 2 para Python.
# Ela fornece funções como init(), spin() e shutdown().

from rclpy.node import Node
# Importa a classe Node, que representa um nó no ROS 2.


#def main(args=None):
    # Função principal do programa.
    # args permite receber argumentos passados ao ROS 2.

#    rclpy.init(args=args)
    # Inicializa o contexto do ROS 2.
    # Deve ser chamada antes de criar qualquer Node.

#    node = Node("my_first_node")
    # Cria uma instância da classe Node diretamente.
    # "my_first_node" é o nome que identificará este nó no ROS 2.

#    node.get_logger().info("Hello ROS2")
    # Obtém o sistema de logs do Node e exibe uma mensagem informativa.
    # A mensagem aparecerá no terminal.

#    rclpy.spin(node)
    # Mantém o Node em execução.
    # Permite que ele processe eventos e callbacks.
    # O programa permanece aqui até receber uma interrupção, como Ctrl+C.

#    node.destroy_node()
    # Destrói o Node e libera os recursos associados a ele.

#    rclpy.shutdown()
    # Encerra o contexto do ROS 2.


#if __name__ == "__main__":
    # Verifica se este arquivo está sendo executado diretamente,
    # e não sendo importado como módulo por outro arquivo.

#    main()
    # Executa a função principal.

# Do jeito acima, o código não cria um nó personalizado, apenas instanciaria a classe Node diretamente. 
# Para criar um nó personalizado, é necessário definir uma nova classe que herde de Node e implemente 
# funcionalidades específicas. Abaixo está a implementação de um nó personalizado chamado MyFirstNode.

class MyFirstNode(Node):
    # Define uma nova classe chamada MyFirstNode que herda da classe Node.
    # Esta classe representa um nó personalizado no ROS 2.

    def __init__(self):
        # Construtor da classe MyFirstNode.
        # Inicializa a instância do nó.

        super().__init__("my_first_node")
        # Chama o construtor da classe base Node.
        # "my_first_node" é o nome do nó.

        self.counter = 0

        self.get_logger().info("Hello ROS2")
        # Obtém o sistema de logs do Node e exibe uma mensagem informativa.
        # A mensagem aparecerá no terminal.

        self.create_timer(1.0, self.timer_callback)
        # Cria um timer que chama o método timer_callback a cada 1 segundo.
    
    def timer_callback(self):
        # Define um método chamado timer_callback.
        # Este método será chamado periodicamente pelo timer.

        self.get_logger().info("Hello " + str(self.counter))
        # Obtém o sistema de logs do Node e exibe uma mensagem informativa
        # indicando que o callback do timer foi acionado.

        self.counter += 1
        # Incrementa o contador a cada vez que o callback do timer é chamado.

def main(args=None):
    # Função principal do programa.
    # args permite receber argumentos passados ao ROS 2.

    rclpy.init(args=args)
    # Inicializa o contexto do ROS 2.
    # Deve ser chamada antes de criar qualquer Node.

    node = MyFirstNode()
    # Cria uma instância da classe MyFirstNode.
    # Isso inicializa o nó e configura o timer.

    rclpy.spin(node)
    # Mantém o Node em execução.
    # Permite que ele processe eventos e callbacks.
    # O programa permanece aqui até receber uma interrupção, como Ctrl+C.

    rclpy.shutdown()
    # Encerra o contexto do ROS 2.

if __name__ == "__main__":
    # Verifica se este arquivo está sendo executado diretamente,
    # e não sendo importado como módulo por outro arquivo.

    main()
    # Executa a função principal.