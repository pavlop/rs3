
import time

from src import killer_weak


def main():
  killer = killer_weak.KillerWeak(sec_per_monster=13)
  killer.start()

if __name__ == "__main__":
  print("3...")
  time.sleep(0.3)
  print("2...")
  time.sleep(0.3)
  print("1...")
  time.sleep(0.3)
  print("satrted")
  main()



