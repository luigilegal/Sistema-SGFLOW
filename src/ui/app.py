import os
import sys
from pathlib import Path

from flask import Flask, Response, flash, redirect, render_template, request, url_for

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
UPLOAD_DIR = os.path.join(ROOT_DIR, "uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from service.sgflow_service import SGFlowService

app = Flask(__name__)
app.secret_key = "sgflow-final-scroll-totais"

service = SGFlowService()


def montar_contexto(selected_id=None):
    fila = service.listar_fila()
    selecionado = None

    if selected_id:
        selecionado = service.selecionar(selected_id)

    if not selecionado:
        selecionado = service.em_atendimento or (fila[0] if fila else None)

    return {
        "fila": fila,
        "selecionado": selecionado,
        "em_atendimento": service.em_atendimento,
        "rotas": service.listar_rotas(),
        "ordem_rotas": service.ordem_rotas,
    }


@app.route("/")
def index():
    selected_id = request.args.get("selected_id")
    return render_template("index.html", **montar_contexto(selected_id))


@app.route("/performance")
def performance():
    return render_template(
        "performance.html",
        metricas=service.listar_metricas(),
        resumo=service.resumo_performance(),
    )


@app.route("/performance/limpar", methods=["POST"])
def limpar_performance():
    sucesso, mensagem = service.limpar_metricas()
    flash(mensagem, "success" if sucesso else "danger")
    return redirect(url_for("performance"))


@app.route("/performance/baixar")
def baixar_performance():
    conteudo = service.exportar_metricas_txt()

    return Response(
        conteudo,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment; filename=sgflow_performance.txt"},
    )


@app.route("/caminhao/adicionar", methods=["POST"])
def adicionar_caminhao():
    cargas_texto = request.form.get("cargas", "")
    cargas = [carga.strip() for carga in cargas_texto.split("|") if carga.strip()]

    sucesso, mensagem = service.cadastrar_caminhao(
        request.form.get("placa", ""),
        request.form.get("motorista", ""),
        request.form.get("operacao", ""),
        request.form.get("destino", ""),
        request.form.get("distancia", ""),
        cargas,
    )

    flash(mensagem, "success" if sucesso else "danger")
    return redirect(url_for("index"))


@app.route("/fila/atender", methods=["POST"])
def atender_proximo():
    sucesso, mensagem = service.atender_proximo()
    flash(mensagem, "success" if sucesso else "danger")
    return redirect(url_for("index"))


@app.route("/carga/adicionar", methods=["POST"])
def adicionar_carga():
    sucesso, mensagem = service.adicionar_carga_carga(request.form.get("item", ""))
    flash(mensagem, "success" if sucesso else "danger")
    return redirect(url_for("index"))


@app.route("/descarga/adicionar", methods=["POST"])
def adicionar_carga_descarga():
    sucesso, mensagem = service.adicionar_carga_descarga(request.form.get("item", ""))
    flash(mensagem, "success" if sucesso else "danger")
    return redirect(url_for("index"))


@app.route("/descarga/remover", methods=["POST"])
def descarregar():
    sucesso, mensagem = service.descarregar()
    flash(mensagem, "success" if sucesso else "danger")
    return redirect(url_for("index"))


@app.route("/carga/finalizar", methods=["POST"])
def finalizar_carga():
    sucesso, mensagem = service.finalizar_carga()
    flash(mensagem, "success" if sucesso else "danger")
    return redirect(url_for("index"))


@app.route("/rotas/inverter", methods=["POST"])
def inverter_rota():
    sucesso, mensagem = service.inverter_ordem_rotas()
    flash(mensagem, "success" if sucesso else "danger")
    return redirect(url_for("index"))


@app.route("/rotas/liberar", methods=["POST"])
def liberar_rota():
    sucesso, mensagem = service.liberar_partida()
    flash(mensagem, "success" if sucesso else "danger")
    return redirect(url_for("index"))


@app.route("/importar", methods=["POST"])
def importar():
    arquivo = request.files.get("arquivo")

    if not arquivo or arquivo.filename == "":
        flash("Selecione um arquivo CSV ou XLSX.", "danger")
        return redirect(url_for("index"))

    extensao = Path(arquivo.filename).suffix.lower()

    if extensao not in [".csv", ".xlsx"]:
        flash("Formato inválido. Somente .csv e .xlsx são aceitos.", "danger")
        return redirect(url_for("index"))

    destino = os.path.join(UPLOAD_DIR, arquivo.filename)
    arquivo.save(destino)

    sucesso, mensagem = service.importar_arquivo(destino)
    flash(mensagem, "success" if sucesso else "warning")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
