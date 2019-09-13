from ipykernel.kernelbase import Kernel
from prob_book.parsing import parser
from prob_book.plotting.plot import JupyterPlot

class StatKernel(Kernel):
    implementation = "stat_kernel"
    implementation_version = "0.1"
    banner = "Stat Analysis Kernel"
    language_info = {
        "name":"Stat",
        "mimetype":"text/plain",
    }
    use_kernel_is_complete = False

    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):
        parser.CLIENT = "jupyter"
        if not silent:
            code_lines = code.split("\n")
            for l in code_lines:
                output = parser.parse(l)
                if output == None:
                    stream_content = {"name":"stdout","text":""}
                    self.send_response(self.iopub_socket, "stream", stream_content)
                if type(output) == JupyterPlot:
                    self.send_response(self.iopub_socket,"display_data",output.msg_content)
                else:
                    stream_content = {"name": "stdout", "text": str("{}\n".format(output))}
                    self.send_response(self.iopub_socket,"stream",stream_content)


        return {"status":"ok",
                "execution_count":self.execution_count,
                "payload":[],
                "user_expressions":[]
                }

def main():
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=StatKernel)
