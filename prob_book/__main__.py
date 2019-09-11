from ipykernel.kernelapp import IPKernelApp
from . import kernel

IPKernelApp.launch_instance(kernel_class=kernel.StatKernel)