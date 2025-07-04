from nicegui import ui, app

def create():
    @ui.page('/')
    def index():
        ui.label('Simple Counter').classes('text-2xl font-bold mb-4')
        
        # Initialize counter value in user storage
        if 'counter_value' not in app.storage.user:
            app.storage.user['counter_value'] = 0
        
        counter_display = ui.label(f'Count: {app.storage.user["counter_value"]}').classes('text-xl mb-4')
        
        def increment():
            app.storage.user['counter_value'] += 1
            counter_display.set_text(f'Count: {app.storage.user["counter_value"]}')
        
        def decrement():
            app.storage.user['counter_value'] -= 1
            counter_display.set_text(f'Count: {app.storage.user["counter_value"]}')
        
        with ui.row().classes('gap-4'):
            ui.button('Increment', on_click=increment, color='green')
            ui.button('Decrement', on_click=decrement, color='red')