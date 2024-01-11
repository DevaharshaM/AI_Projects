# importing library

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Defining the network structure
model = BayesianNetwork([('Contestant', 'Host'), ('Prize', 'Host')])

# Defining the CPDs:
cpd_c = TabularCPD('Contestant', 3, [[1/3], [1/3], [1/3]])
cpd_p = TabularCPD('Prize', 3, [[1/3], [1/3], [1/3]])
cpd_h = TabularCPD('Host', 3, [[0, 0, 0, 0, 0.5, 1, 0, 1, 0.5],
                               [0.5, 0, 1, 0, 0, 0, 1, 0, 0.5],
                               [0.5, 1, 0, 1, 0.5, 0, 0, 0, 0]],
                  evidence=['Contestant', 'Prize'], evidence_card=[3, 3])

# Associating the CPDs with the network structure.
model.add_cpds(cpd_c, cpd_p, cpd_h)

infer = VariableElimination(model)
posterior = infer.query(variables=['Prize'], evidence={'Contestant': 0, 'Host': 2}, show_progress=False, joint=False)
print(posterior['Prize'])
