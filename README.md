# RL-Machine-Learning

Inteligencia artificial avanzada que recolecta todo tipo de información del juego y va entrenando por sí sola, el código es totalmente automático, es decir al cerrar el programa automáticamente escribirá lo que ha aprendido en un replay_loader.py, este código está adaptado para cualquier tipo de modo de juego y cualquier tipo de instancia modificada dentro de él.
## Cómo usarlo

-Instala las dependencias con pip install -r requirements.txt.

Ejecuta rl_training.py para entrenar al agente.

Ejecuta rl_game.py para jugar con el agente entrenado.


## Authors

- [@0xfvck](https://github.com/0xfvck)


## Información adicional

rl_training.py: Entrena al agente usando PPO.

rl_game.py: El juego interactúa con el agente entrenado.

agent_nn.py: Define la red neuronal del agente.

rewards_terminal_obs.py: Define las reglas del juego.

replay_loader.py: Carga datos de partidas previas para iniciar la simulación.
