import argparse

def gen_Fattree(args):
    k = args.k_port
    k_half = k // 2
    core_switch_num = k_half ** 2
    aggr_switch_num = k_half * k
    edge_switch_num = k_half * k
    servers = edge_switch_num * k_half

    switch_nodes = (int) (core_switch_num + aggr_switch_num + edge_switch_num)
    nodes = (int) (servers + switch_nodes)
    links = (int) (aggr_switch_num * k + servers)

    file_name = "Fattree_"+str(k)
    with open(file_name, 'w') as f:
        print(file_name)
        first_line = str(nodes)+" "+str(switch_nodes)+" "+str(links)
        f.write(first_line)
        f.write('\n')

        sec_line = ""
        nnodes = nodes - switch_nodes
        for i in range(nnodes, nodes):
            sec_line += str(i) + " "
        f.write(sec_line)
        f.write('\n')

        curr_node_id = servers
        core_switch = list(range(curr_node_id, curr_node_id + core_switch_num))
        curr_node_id += core_switch_num
        aggr_switch = list(range(curr_node_id, curr_node_id + aggr_switch_num))
        curr_node_id += aggr_switch_num
        edge_switch = list(range(curr_node_id, curr_node_id + edge_switch_num))
        curr_node_id += edge_switch_num

        for i in range(aggr_switch_num):
            r = i % k_half
            for j in range(k_half):
                line = str(aggr_switch[i])+" "+str(core_switch[r*k_half+j])+" "+args.switch_bandwidth+" "+args.latency+" "+args.error_rate
                f.write(line)
                f.write('\n')

        for i in range(edge_switch_num):
            pod = i // k_half
            for j in range(k_half):
                line = str(edge_switch[i])+" "+str(aggr_switch[pod*k_half+j])+" "+args.switch_bandwidth+" "+args.latency+" "+args.error_rate
                f.write(line)
                f.write('\n')

        for i in range(0, edge_switch_num):
            for j in range(0, k_half):
                line = str(i*k_half+j)+" "+str(edge_switch[i])+" "+args.bandwidth+" "+args.latency+" "+args.error_rate
                f.write(line)
                f.write('\n')

def main():
    parser = argparse.ArgumentParser(description="Python script for generate the Fattree network topo")
    parser.add_argument('-l','--latency',type=str,default='0.0005ms',help='nic latency,default 0.0005ms')
    parser.add_argument('-bw','--bandwidth',type=str,default='100Gbps',help='nic to asw bandwitch,default 100Gbps')
    parser.add_argument('-swbw','--switch_bandwidth',type=str,default='400Gbps',help='fattree switch bandwitch,default 400Gbps')
    parser.add_argument('-er','--error_rate',type=str,default='0',help='error_rate,default 0')
    parser.add_argument('-k', '--k_port',type=int,default='4',help='pod num,default 4,must be even')
    args = parser.parse_args()
    gen_Fattree(args)

if __name__ == '__main__':
    main()