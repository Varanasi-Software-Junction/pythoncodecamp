import time
import win32print


# ----------------------------------------------------------------------
def print_job_checker():
    """
    Prints out all jobs in the print queue every 5 seconds
    """
    jobs = [1]
    while jobs:
        jobs = []
        for p in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL,
                                         None, 1):
            flags, desc, name, comment = p

            phandle = win32print.OpenPrinter(name)
            print_jobs = win32print.EnumJobs(phandle, 0, -1, 1)
            if print_jobs:
                jobs.extend(list(print_jobs))
            for job in print_jobs:
                print
                "printer name => " + name
                document = job["pDocument"]
                print
                "Document name => " + document
            win32print.ClosePrinter(phandle)

        time.sleep(5)
    print
    "No more jobs!"


# ----------------------------------------------------------------------
if __name__ == "__main__":
    print_job_checker()