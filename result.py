from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService(
    channel='ibm_quantum',
    instance='ibm-q/open/main',
    token='c081244015953bec2b34c29829f3e6e3f902b2e7ccde427f6dacfbab0c1843991b7fcec06c45867ae8d0ba801fa6da7cb6d717b517f27930509c62d13863beef'
)
job = service.job('cxgqezkgcckg008sfcvg')
job_result = job.result()


print(job_result)
# To get counts for a particular pub result, use 
#
# pub_result = job_result[<idx>].data.<classical register>.get_counts()
#
# where <idx> is the index of the pub and <classical register> is the name of the classical register. 
# You can use circuit.cregs to find the name of the classical registers.