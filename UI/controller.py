import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizzaAreoporti(self, e):
        distanza = self._view.txt_distanza.value

        # 1) CONTROLLO SE è VUOTO
        if distanza is None or distanza == "":
            self._view.create_alert("Inserire distanza minima")
            return

        # 2) CONTROLLO CHE VENGA INSERITO UN INTERO
        try:
            idOggetto = float(distanza)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text(f"Attenzione, inserire un valore numerico nel campo distanza.", color="red"))
            self._view.update_page()
            return



        # 3)
        self._model.buildGraph(distanza)
        nodi= self._model.getNumNodes()
        archi= self._model.getNumEdges()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Il numero di vertici del grafo è {nodi}\n"
                                                      f"Il numero di archi è {archi}\n"
                                                      f"{self._model._graph.nodes()}" ))


        self._view.update_page()

