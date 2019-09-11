from ipykernel.kernelbase import Kernel
from prob_book.parsing import parser

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
        if not silent:
            stream_content = {"name":"stdout","text":parser.parse(code)}
            self.send_response(self.iopub_socket,"stream",stream_content)

        return {"status":"ok",
                "execution_count":self.execution_count,
                "payload":[],
                "user_expressions":[]
                }
    def do_is_complete(self, code):
        return {
            "status":"complete"
        }

def main():
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=StatKernel)

if __name__ == "__main__":
    main()