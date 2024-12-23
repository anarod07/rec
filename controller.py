from flask import render_template, Blueprint, request, redirect, session, flash, make_response
from model import Viagem

home = Blueprint('home', __name__)

@home.route('/diario')
def inicio():
    return render_template('home.html')

#pegando as informações do cadastro
@home.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        destino = request.form.get("destino")
        data = request.form.get("data")
        descricao = request.form.get("descricao")
        star = request.form.get("star")

        if not destino or not data or not descricao or not star:
            flash("Erro: Todos os campos devem ser preenchidos corretamente!", "error")
            return redirect("/cadastro")

        nova_viagem = Viagem(destino, data, descricao, int(star))
        if "viagens" not in session:
            session["viagens"] = []
        session["viagens"].append(vars(nova_viagem))
        flash("Viagem cadastrada com sucesso!", "success")

        # atualizar cookies
        total_viagens = len(session["viagens"])
        response = make_response(redirect("/diario"))
        response.set_cookie("total_viagens", str(total_viagens))
        return response

    return render_template("cadastro.html")

@home.route('/diario')
def diario():
    if "viagens" not in session or not session["viagens"]:
        flash("Você precisa cadastrar ao menos uma viagem!", "error")
        return redirect("/cadastro")

    viagens = session["viagens"]
    total_viagens = request.cookies.get("total_viagens", "0")
    return render_template("home.html", viagens=viagens, total_viagens=total_viagens)

