import flet as ft
def main(page: ft.Page):
    page.title = "Простое приложение на Flet"

    header = ft.Text("Добро пожаловать в мое простое приложение!", style="headlineLarge")
    input_field = ft.TextField(label="Введите сообщение")
    result_text = ft.Text()


    def on_button_click(e):
        result_text.value = f"Вы ввели: {input_field.value}"
        print(f"New user with text {input_field.value}")
        page.update()


    submit_button = ft.ElevatedButton(text="Отправить", on_click=on_button_click)


    page.add(
        header,
        input_field,
        submit_button,
        result_text
    )

# ft.app(target=main, view=None, port=8888)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)

