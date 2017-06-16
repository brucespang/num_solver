import numpy as np
import scipy.optimize
import networkx as nx

def num_links(R):
    return R.shape[0]

def num_flows(R):
    return R.shape[1]

def remove_extra_constraints(R, capacity):
    min_R = []
    min_capacity = []
    x0 = [1. for _ in range(num_flows(R))]
    for i,v in enumerate(R):
        res = scipy.optimize.minimize(lambda x: np.dot(-v, x), x0,
                                      jac=lambda x: -v,
                                      bounds=[(0., None) for _ in range(num_flows(R))],
                                      constraints=[{'type': 'ineq','fun': lambda x: capacity - np.dot(R, x)}])

        x = res.x

        if np.abs(np.dot(v,x) - capacity[i]) < 0.0001:
            min_R.append(v)
            min_capacity.append(capacity[i])

    return np.array(min_R), np.array(min_capacity)

def get_topology(filename):
    return nx.read_edgelist(filename, create_using=nx.DiGraph())

def get_routing_matrix_and_capacity(g, flows):
    capacity = np.array([parse_bw(g.get_edge_data(l[0], l[1])['bw']) for l in g.edges()])

    flow_paths = [set(zip(f, f[1:])) for f in flows]
    R = [[int(edge in path) for path in flow_paths] for edge in g.edges()]

    return np.array(R), capacity

def subflow_matrix(flows):
    flow_and_route_to_id = {}
    for flow,routes in enumerate(flows):
        for rid,_ in enumerate(routes):
            flow_and_route_to_id[(flow, rid)] = len(flow_and_route_to_id)

    num_routes = len(flow_and_route_to_id)
    H = []
    for flow,routes in enumerate(flows):
        row = [0 for _ in range(num_routes)]
        for rid,_ in enumerate(routes):
            row[flow_and_route_to_id[(flow,rid)]] = 1
        H.append(row)
    return np.array(H)


def parse_bw(bw):
    if 'Mbps' in bw:
        return float(bw.replace('Mbps', ''))
    elif 'Gbps' in bw:
        return 1000*float(bw.replace('Gbps', ''))
    elif 'Kbps' in bw:
        return float(bw.replace('Kbps', ''))/1000
    else:
        raise Exception("Unknown bandwidth format %s, allowed units are %%f(Gbps|Mbps|Kbps)"%(bw))
