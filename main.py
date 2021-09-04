
import time

from src import killer_weak
from src import killer_strong


def main():
  killer = killer_weak.KillerWeak(sec_per_monster=15)
  # killer = killer_strong.KillerStrong(sec_per_monster=35)
  killer.start()


if __name__ == "__main__":
  print("3...")
  time.sleep(0.5)
  print("2...")
  time.sleep(0.5)
  print("1...")
  time.sleep(0.5)
  print("satrted")
  main()



