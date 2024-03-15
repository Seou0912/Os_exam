import psutil

for proc in psutil.process_iter():
    ps_name = proc.name()

    if "Chrome" in ps_name:
        child = proc.children()
        print(ps_name, proc.status(), proc.parent(), child)

        if child:
            print(f"{ps_name} child precess", child)
