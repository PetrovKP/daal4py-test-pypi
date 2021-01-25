import dpctl
from dpctl import device_context, device_type

# Global runtime object inside dpctl
rt = dpctl

# Print metadata about the runtime
rt.dump()


queue = rt.get_current_queue()
print(dir(queue))


with device_context("opencl:cpu:0") as cpu_queue:
  print('aaa')  
