# import moudel and files
import threading
import Controlers_Client
import Screen_Client

def main():
    
    t1 = threading.Thread(target=Controlers_Client.main, daemon=True)
    t2 = threading.Thread(target=Screen_Client.main, daemon=True)

    t1.start()
    t2.start()

    # keep main alive
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()