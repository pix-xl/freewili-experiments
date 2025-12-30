from freewili import FreeWili

def main():
    devices = FreeWili.find_all()
    print(f"Found {len(devices)} FreeWili(s)\n")
    
    for i, fw in enumerate(devices, start= 1):
        print(f"{i}. {fw}")
        print(f"    main:       {fw.main}")
        print(f"    display:    {fw.display}")
        print(f"    fpga:       {fw.fpga}")
        print("\n")
    
if __name__ == "__main__":
    main()