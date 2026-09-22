"""CURSOS 2026ISIL - Recordatorio de fechas de entrega de tareas universitarias."""

import json
import os
import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import ttk

# Archivo donde se guardan las tareas marcadas como realizadas
ARCHIVO_COMPLETADAS = Path(os.environ.get("APPDATA", Path.home())) / "CURSOS 2026ISIL" / "completadas.json"

tareas_data = [
    # 4536 - CCNA I
    {"fecha": "2026-09-22", "curso": "4536 - CCNA I", "tarea": "PROCESO DE APRENDIZAJE 1"},
    {"fecha": "2026-10-13", "curso": "4536 - CCNA I", "tarea": "PROCESO DE APRENDIZAJE 2"},
    {"fecha": "2026-11-03", "curso": "4536 - CCNA I", "tarea": "PROCESO DE APRENDIZAJE 3"},
    {"fecha": "2026-11-24", "curso": "4536 - CCNA I", "tarea": "PROCESO DE APRENDIZAJE 4"},
    {"fecha": "2026-12-15", "curso": "4536 - CCNA I", "tarea": "EVALUACIÓN INTEGRAL"},

    # 4149 - CRIPTOGRAFIA
    {"fecha": "2026-09-26", "curso": "4149 - CRIPTOGRAFIA", "tarea": "PROCESO DE APRENDIZAJE 1"},
    {"fecha": "2026-10-17", "curso": "4149 - CRIPTOGRAFIA", "tarea": "PROCESO DE APRENDIZAJE 2"},
    {"fecha": "2026-11-07", "curso": "4149 - CRIPTOGRAFIA", "tarea": "PROCESO DE APRENDIZAJE 3"},
    {"fecha": "2026-11-28", "curso": "4149 - CRIPTOGRAFIA", "tarea": "PROCESO DE APRENDIZAJE 4"},
    {"fecha": "2026-12-19", "curso": "4149 - CRIPTOGRAFIA", "tarea": "EVALUACIÓN INTEGRAL"},

    # 2972 - ESTANDARES Y NORMATIVAS
    {"fecha": "2026-10-12", "curso": "2972 - ESTANDARES CIBERSEGURIDAD", "tarea": "PROCESO DE APRENDIZAJE 2"},
    {"fecha": "2026-11-02", "curso": "2972 - ESTANDARES CIBERSEGURIDAD", "tarea": "PROCESO DE APRENDIZAJE 3"},
    {"fecha": "2026-11-23", "curso": "2972 - ESTANDARES CIBERSEGURIDAD", "tarea": "PROCESO DE APRENDIZAJE 4"},
    {"fecha": "2026-12-14", "curso": "2972 - ESTANDARES CIBERSEGURIDAD", "tarea": "EVALUACIÓN INTEGRAL"},

    # 2950 - ANÁLISIS DE AMENAZAS
    {"fecha": "2026-09-25", "curso": "2950 - ANÁLISIS DE AMENAZAS", "tarea": "PROCESO DE APRENDIZAJE 1"},
    {"fecha": "2026-10-16", "curso": "2950 - ANÁLISIS DE AMENAZAS", "tarea": "PROCESO DE APRENDIZAJE 2"},
    {"fecha": "2026-11-06", "curso": "2950 - ANÁLISIS DE AMENAZAS", "tarea": "PROCESO DE APRENDIZAJE 3"},
    {"fecha": "2026-11-27", "curso": "2950 - ANÁLISIS DE AMENAZAS", "tarea": "PROCESO DE APRENDIZAJE 4"},
    {"fecha": "2026-12-18", "curso": "2950 - ANÁLISIS DE AMENAZAS", "tarea": "EVALUACIÓN INTEGRAL"},

    # 2090 - CALCULO
    {"fecha": "2026-09-25", "curso": "2090 - CALCULO", "tarea": "PROCESO DE APRENDIZAJE 1"},
    {"fecha": "2026-10-16", "curso": "2090 - CALCULO", "tarea": "PROCESO DE APRENDIZAJE 2"},
    {"fecha": "2026-11-06", "curso": "2090 - CALCULO", "tarea": "PROCESO DE APRENDIZAJE 3"},
    {"fecha": "2026-11-27", "curso": "2090 - CALCULO", "tarea": "PROCESO DE APRENDIZAJE 4"},
    {"fecha": "2026-12-18", "curso": "2090 - CALCULO", "tarea": "EVALUACIÓN INTEGRAL"},

    # 1552 - DIRECCION DE PERSONAS
    {"fecha": "2026-09-28", "curso": "1552 - DIRECCION DE PERSONAS", "tarea": "PROCESO DE APRENDIZAJE 1"},
    {"fecha": "2026-10-19", "curso": "1552 - DIRECCION DE PERSONAS", "tarea": "PROCESO DE APRENDIZAJE 2"},
    {"fecha": "2026-11-09", "curso": "1552 - DIRECCION DE PERSONAS", "tarea": "PROCESO DE APRENDIZAJE 3"},
    {"fecha": "2026-11-30", "curso": "1552 - DIRECCION DE PERSONAS", "tarea": "PROCESO DE APRENDIZAJE 4"},
    {"fecha": "2026-12-14", "curso": "1552 - DIRECCION DE PERSONAS", "tarea": "EVALUACIÓN INTEGRAL"},

    # 1477 - RESILIENCIA
    {"fecha": "2026-09-09", "curso": "1477 - RESILIENCIA", "tarea": "BITÁCORAS DE RESILIENCIA 1 (ATRASADO)"},
    {"fecha": "2026-09-30", "curso": "1477 - RESILIENCIA", "tarea": "PROCESO DE APRENDIZAJE 1"},
    {"fecha": "2026-10-21", "curso": "1477 - RESILIENCIA", "tarea": "PROCESO DE APRENDIZAJE 2"},
    {"fecha": "2026-11-11", "curso": "1477 - RESILIENCIA", "tarea": "PROCESO DE APRENDIZAJE 3"},
    {"fecha": "2026-12-02", "curso": "1477 - RESILIENCIA", "tarea": "PROCESO DE APRENDIZAJE 4"},

    # 1007 - ADMINISTRACION DE WINDOWS
    {"fecha": "2026-09-09", "curso": "1007 - ADMINISTRACION WINDOWS", "tarea": "INSTALACION WINDOWS SERVER (ATRASADO)"},
    {"fecha": "2026-09-30", "curso": "1007 - ADMINISTRACION WINDOWS", "tarea": "PROCESO DE APRENDIZAJE 1"},
    {"fecha": "2026-10-21", "curso": "1007 - ADMINISTRACION WINDOWS", "tarea": "PROCESO DE APRENDIZAJE 2"},
    {"fecha": "2026-11-11", "curso": "1007 - ADMINISTRACION WINDOWS", "tarea": "PROCESO DE APRENDIZAJE 3"},
    {"fecha": "2026-12-02", "curso": "1007 - ADMINISTRACION WINDOWS", "tarea": "PROCESO DE APRENDIZAJE 4"},
]

COLUMNAS = (
    # (id, encabezado, ancho, alineación)
    ("hecho", "✔", 50, "center"),
    ("fecha", "Fecha de Entrega", 120, "center"),
    ("curso", "Curso", 250, "center"),
    ("tarea", "Tarea / Evaluación", 300, "w"),
    ("dias", "Días Restantes", 120, "center"),
)

ESTILOS_TAGS = {
    "completado": ("#d4edda", "#155724"),
    "atrasado": ("#e6e6e6", "#666666"),
    "urgente": ("#ffcccc", "#990000"),
    "proximo": ("#fff2cc", "#b45f06"),
    "normal": ("#ffffff", "#000000"),
}


def clave(item):
    """Identificador único de una tarea."""
    return f"{item['fecha']}|{item['curso']}|{item['tarea']}"


def cargar_completadas():
    try:
        return set(json.loads(ARCHIVO_COMPLETADAS.read_text(encoding="utf-8")))
    except (OSError, ValueError):
        return set()


def guardar_completadas(completadas):
    ARCHIVO_COMPLETADAS.parent.mkdir(parents=True, exist_ok=True)
    ARCHIVO_COMPLETADAS.write_text(json.dumps(sorted(completadas), ensure_ascii=False, indent=2), encoding="utf-8")


def clasificar(dias):
    """Devuelve (tag, texto) según los días restantes."""
    if dias < 0:
        return "atrasado", f"Vencido ({abs(dias)} días)"
    if dias == 0:
        return "urgente", "¡HOY!"
    if dias <= 7:
        return "urgente", f"¡{dias} días!"
    if dias <= 15:
        return "proximo", f"{dias} días"
    return "normal", f"{dias} días"


class RecordatorioApp:
    def __init__(self, root):
        self.root = root
        self.completadas = cargar_completadas()
        root.title("CURSOS 2026ISIL - Recordatorio de Entregas")
        root.geometry("900x600")
        root.configure(bg="#f0f0f0")

        tk.Label(
            root,
            text="📅 Recordatorio de Entregas - ISIL 2026",
            font=("Arial", 16, "bold"),
            fg="#333",
            bg="#f0f0f0",
        ).pack(pady=(15, 10))

        marco = tk.Frame(root, bg="#f0f0f0")
        marco.pack(fill="both", expand=True, padx=15)

        self.tabla = ttk.Treeview(
            marco, columns=[c[0] for c in COLUMNAS], show="headings"
        )
        for col_id, encabezado, ancho, alineacion in COLUMNAS:
            self.tabla.heading(col_id, text=encabezado)
            self.tabla.column(col_id, width=ancho, anchor=alineacion)
        for tag, (fondo, texto) in ESTILOS_TAGS.items():
            self.tabla.tag_configure(tag, background=fondo, foreground=texto)

        scroll = ttk.Scrollbar(marco, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        self.tabla.bind("<Button-1>", self.al_hacer_clic)
        self.tabla.bind("<Double-1>", self.al_doble_clic)
        self.tabla.bind("<space>", lambda e: self.alternar_seleccionadas())

        tk.Label(
            root,
            text="Haz clic en la casilla ☐ (o doble clic en la fila) para marcar una tarea como realizada.",
            font=("Arial", 9),
            fg="#555",
            bg="#f0f0f0",
        ).pack(pady=(8, 0))

        botones = tk.Frame(root, bg="#f0f0f0")
        botones.pack(pady=15)
        estilo_boton = dict(
            fg="white",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=15,
            pady=6,
            cursor="hand2",
        )
        tk.Button(
            botones,
            text="✔ Marcar / Desmarcar Realizada",
            bg="#28a745",
            activebackground="#1e7e34",
            command=self.alternar_seleccionadas,
            **estilo_boton,
        ).pack(side="left", padx=5)

        tk.Button(
            botones,
            text="🔄 Actualizar Días Restantes",
            bg="#007bff",
            activebackground="#0056b3",
            command=self.cargar_datos,
            **estilo_boton,
        ).pack(side="left", padx=5)

        self.cargar_datos()

    def cargar_datos(self):
        seleccion = self.tabla.selection()
        self.tabla.delete(*self.tabla.get_children())
        hoy = datetime.now().date()
        for item in sorted(tareas_data, key=lambda t: t["fecha"]):
            fecha = datetime.strptime(item["fecha"], "%Y-%m-%d").date()
            iid = clave(item)
            if iid in self.completadas:
                casilla, tag, texto_dias = "☑", "completado", "✔ Realizada"
            else:
                casilla = "☐"
                tag, texto_dias = clasificar((fecha - hoy).days)
            self.tabla.insert(
                "",
                "end",
                iid=iid,
                values=(casilla, fecha.strftime("%d/%m/%Y"), item["curso"], item["tarea"], texto_dias),
                tags=(tag,),
            )
        self.tabla.selection_set([i for i in seleccion if self.tabla.exists(i)])

    def alternar(self, iids):
        for iid in iids:
            self.completadas ^= {iid}
        guardar_completadas(self.completadas)
        self.cargar_datos()

    def alternar_seleccionadas(self):
        self.alternar(self.tabla.selection())

    def al_hacer_clic(self, evento):
        fila = self.tabla.identify_row(evento.y)
        if fila and self.tabla.identify_column(evento.x) == "#1":
            self.alternar([fila])
            return "break"

    def al_doble_clic(self, evento):
        fila = self.tabla.identify_row(evento.y)
        if fila and self.tabla.identify_column(evento.x) != "#1":
            self.alternar([fila])


if __name__ == "__main__":
    ventana = tk.Tk()
    RecordatorioApp(ventana)
    ventana.mainloop()
