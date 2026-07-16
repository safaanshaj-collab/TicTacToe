from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.clock import Clock

Window.clearcolor = (0.08, 0.08, 0.08, 1)


class TicTacToe(App):
    title = "Tic Tac Toe"

    def build(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        root = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=15
        )

        title = Label(
            text="TIC TAC TOE",
            font_size=42,
            color=(0, 1, 1, 1),
            size_hint=(1, 0.18)
        )

        self.status = Label(
            text="Player X Turn",
            font_size=26,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.12)
        )

        grid = GridLayout(
            cols=3,
            spacing=10,
            size_hint=(1, 0.65)
        )

        for i in range(9):
            btn = Button(
                text="",
                font_size=52,
                background_normal="",
                background_color=(0.15, 0.15, 0.15, 1)
            )

            btn.bind(on_press=lambda instance, i=i: self.click(i))

            self.buttons.append(btn)
            grid.add_widget(btn)

        restart_btn = Button(
            text="Restart Game",
            font_size=24,
            size_hint=(1, 0.16),
            background_normal="",
            background_color=(0, 1, 1, 1),
            color=(0, 0, 0, 1)
        )

        restart_btn.bind(on_press=self.restart_game)

        root.add_widget(title)
        root.add_widget(self.status)
        root.add_widget(grid)
        root.add_widget(restart_btn)

        return root

    def click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].text = self.current_player
            self.buttons[index].disabled = True

            if self.current_player == "X":
                self.buttons[index].color = (0, 1, 1, 1)
            else:
                self.buttons[index].color = (1, 0.5, 0, 1)

            if not self.check_winner():
                if self.current_player == "X":
                    self.current_player = "O"
                else:
                    self.current_player = "X"

                self.status.text = f"Player {self.current_player} Turn"

    def check_winner(self):
        wins = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != "":
                self.buttons[a].background_color = (0, 1, 0, 1)
                self.buttons[b].background_color = (0, 1, 0, 1)
                self.buttons[c].background_color = (0, 1, 0, 1)

                self.status.text = f"Player {self.board[a]} Wins!"
                self.show_popup(f"Player {self.board[a]} Wins!")
                self.disable_buttons()

                return True

        if "" not in self.board:
            self.status.text = "It's a Draw!"
            self.show_popup("It's a Draw!")
            self.disable_buttons()
            return True

        return False

    def disable_buttons(self):
        for btn in self.buttons:
            btn.disabled = True

    def restart_game(self, instance):
        self.current_player = "X"
        self.board = [""] * 9
        self.status.text = "Player X Turn"

        for btn in self.buttons:
            btn.text = ""
            btn.disabled = False
            btn.background_color = (0.15, 0.15, 0.15, 1)
            btn.color = (1, 1, 1, 1)

    def show_popup(self, text):
        popup = Popup(
            title="Game Over",
            content=Label(
                text=text,
                font_size=24
            ),
            size_hint=(0.7, 0.4)
        )

        popup.open()

        Clock.schedule_once(
            lambda dt: popup.dismiss(),
            2
        )


if __name__ == "__main__":
    TicTacToe().run()