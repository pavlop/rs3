
import time

from src import killer


def main():
  killer.KillerScript(sec_per_monster=15).start()

if __name__ == "__main__":
  print("3...")
  time.sleep(0.5)
  print("2...")
  time.sleep(0.5)
  print("1...")
  time.sleep(0.5)
  print("satrted")
  main()



