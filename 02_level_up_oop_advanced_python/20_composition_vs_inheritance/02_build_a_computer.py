class CPU:
    def __init__(self,brand,cores,clock_speed_ghz):
        self.brand=brand
        self.cores=cores
        self.clock_speed_ghz=clock_speed_ghz
    def benchmark(self):
        return self.cores * self.clock_speed_ghz
    def __str__(self):
        return(
            f"{self.brand}, {self.cores} cores @ "
            f"{self.clock_speed_ghz}GHz"
        )
class RAM:
    def __init__(self,size_gb,type):
        self.size_gb =size_gb
        self.type=type
    def is_sufficient(self,required_gb):
        return self.size_gb >= required_gb
    def __str__(self):
        return f"{self.size_gb}GB {self.type}"
class Storage:
    def __init__(self,size_gb,kind):
        self.size_gb =size_gb
        self.kind=kind
    def read_speed(self):
        if self.kind == "SSD":
            return 500      
        elif self.kind == "HDD":
            return 100
        else:
            return 0  
    def __str__(self):
        return f"{self.size_gb}GB {self.kind}"
class Computer:
    def __init__(self,name,cpu,ram,storage):
        self.name=name
        self.cpu=cpu
        self.ram=ram
        self.storage=storage
    def boot(self):
        if not all(
            component is not None
            for component in (self.cpu,self.ram,self.storage)
        ):
            print("Boot failed: Missing component!")
            return
        print(f"Booting {self.name}....")        
        print(f"CPU detected :{self.cpu}")
        print(f"Ram detected :{self.ram}")
        print(f"storage detected :{self.storage}")
        print("Boot successful!")
    def upgrade_ram(self,new_ram):
        self.ram=new_ram
    def upgrade_storage(self,new_storage):
        self.storage=new_storage
    def performance_score(self):
        return(
            self.cpu.benchmark()
            + self.ram.size_gb + self.storage.read_speed()
        )           
    def display_specs(self):
        print(f"=== {self.name} ===")
        print(
            f"CPU: {self.cpu} "
            f"(score: {self.cpu.benchmark()})"
        )
        print(f"RAM: {self.ram}")
        print(
            f"Storage: {self.storage} "
            f"(read: {self.storage.read_speed()} MB/s)"
        )
        print(f"Performance Score: {self.performance_score()}")
cpu1 = CPU("Intel i7", 8, 3.6)
ram1 = RAM(8, "DDR4")
storage1 = Storage(512, "SSD")
pc = Computer("Gaming PC", cpu1, ram1, storage1)
pc.boot()
print()
pc.display_specs()

print("\nUpgrading RAM to 32GB DDR5...\n")
pc.upgrade_ram(RAM(32, "DDR5"))
pc.name = "Gaming PC (upgraded)"
pc.display_specs()
print("\n=== CPU Aliasing Demonstration ===")
shared_cpu = CPU("AMD Ryzen 9", 12, 4.5)
pc1 = Computer(
    "Computer A",
    shared_cpu,
    RAM(16, "DDR5"),
    Storage(1000, "SSD")
)
pc2 = Computer(
    "Computer B",
    shared_cpu,
    RAM(32, "DDR5"),
    Storage(2000, "SSD")
)
print("Both computers share the same CPU:", pc1.cpu is pc2.cpu)
print("\nBefore changing CPU:")
print("Computer A CPU:", pc1.cpu)
print("Computer B CPU:", pc2.cpu)
shared_cpu.clock_speed_ghz = 5.0
print("\nAfter changing the shared CPU clock speed:")
print("Computer A CPU:", pc1.cpu)
print("Computer B CPU:", pc2.cpu)
print("Same CPU object:", pc1.cpu is pc2.cpu)
                 
"""Build a Computer
Multi-component composition with independent, swappable parts
Build a computer using composition. Create these component classes:

- CPU(brand, cores, clock_speed_ghz) — method: benchmark() returns cores × clock_speed as a score
- RAM(size_gb, type) — e.g., 16GB DDR5. Method: is_sufficient(required_gb) returns bool
- Storage(size_gb, kind) — kind is "SSD" or "HDD". Method: read_speed() returns 500 for SSD, 100 for HDD

Computer class:
- Attributes: name, cpu (CPU object), ram (RAM object), storage (Storage object)
- Methods:
  - boot() — checks all components exist, prints boot sequence with each component's info
  - upgrade_ram(new_ram) — replaces RAM with a new RAM object
  - upgrade_storage(new_storage) — replaces storage
  - performance_score() — combines CPU benchmark + RAM size + storage read speed into an overall score
  - display_specs() — prints all specs in a formatted way

Demonstrate:
1. Build a computer with specific components
2. Display specs and performance score
3. Upgrade RAM from 8GB to 32GB — show that only RAM changed, everything else stayed
4. Create the SAME CPU object and put it in two different computers — show they share the CPU (aliasing from Part 1!)

Example output:

=== Gaming PC ===
CPU: Intel i7, 8 cores @ 3.6GHz (score: 28.8)
RAM: 8GB DDR4
Storage: 512GB SSD (read: 500 MB/s)
Performance Score: 536.8

Upgrading RAM to 32GB DDR5...

=== Gaming PC (upgraded) ===
CPU: Intel i7, 8 cores @ 3.6GHz (score: 28.8)
RAM: 32GB DDR5
Storage: 512GB SSD (read: 500 MB/s)
Performance Score: 560.8
"""