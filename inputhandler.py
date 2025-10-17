import threading
import time
import msvcrt

class InputHandler:
    def __init__(self):
        self.last_key = None
        self.running = True
        self.thread = threading.Thread(target=self._capture_input)
        self.thread.daemon = True
        self.thread.start()

    def _capture_input(self):
        try:
            while self.running:
                key = self._get_key()
                if key:
                    self.last_key = key
                time.sleep(0.01)
        except KeyboardInterrupt:
            self.running = False
    
    def _get_key(self):
        if msvcrt.kbhit():
            return msvcrt.getwch()
        else:
            return None
    
    def get_key(self):
        key = self.last_key
        self.last_key = None
        return key