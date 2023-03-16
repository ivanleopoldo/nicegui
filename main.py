from nicegui import ui

with ui.column().classes('grid items-center place-content-center h-screen w-full border-2'):
    ui.html('<p class="text-6xl">Hello <strong>World</strong></p>')



ui.run()
