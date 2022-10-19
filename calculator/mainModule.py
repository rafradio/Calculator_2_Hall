import logModule
import inputModule
import controllerModule as controller

if __name__ == '__main__':

    log = logModule.Logger()
    controller.controller(log)
    log.stop()