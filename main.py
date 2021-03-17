if __name__ == '__main__':
    import core, ui_backend
    Core = core.core()
    ui = ui_backend.ui_backend(Core)
    ui.setup()