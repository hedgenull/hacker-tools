import threading

# DO NOT RUN THIS UNLESS YOU WANT YOUR COMPUTER TO DIE!

def cpu_bane():
  while True:
    t = threading.Thread(target=cpu_bane)
    t.start()
