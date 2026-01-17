# import moudel and other files for using their functions
import threading
import Controlers_Server
import Screen_Server

def main():
    
    t1 = threading.Thread(target=Controlers_Server.main, daemon=True)
    t2 = threading.Thread(target=Screen_Server.main, daemon=True)

    t1.start()
    t2.start()

    # keep main alive
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()