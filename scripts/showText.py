import time
from freewili import FreeWili

def main():
    with FreeWili.find_first().expect("Failed to find a FreeWili") as fw:
        fw.open().expect("Failed to open FreeWili")
        
        fw.show_text_display(text= "Hello!")\
            .expect("Failed to show text")
        
        time.sleep(15)
        fw.show_text_display(text= "")
        fw.close()

if __name__ == "__main__":
    main()