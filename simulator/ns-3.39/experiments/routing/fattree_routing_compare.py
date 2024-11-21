import subprocess
import csv
import os
import matplotlib.pyplot as plt

parameter_ks = [4, 6, 8, 10, 20, 30]

with open('fattree_routing_compare_output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['k', 'Global Routing/s', 'BFS Routing/s'])

    for k in parameter_ks:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        print(current_directory)
        # topo_target_directory = '/home/v-wenkaili/Simulation_Experiments/experiments/inputs/topo/'
        generator = "gen_Fattree_topo.py"
        cmd = 'python3 %s -k %d' % (generator, k)
        print(cmd)
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd=current_directory)

        topo_file = 'Fattree_%d' % (k)
        cmd = '../../ns3 build fattree-with-global-routing'
        subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        cmd = '../../ns3 run \"fattree-with-global-routing --tp=%s\"' % (os.path.join(current_directory, topo_file))
        print(cmd)
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        output = result.stdout.strip().split()

        print(output)

        writer.writerow(output)