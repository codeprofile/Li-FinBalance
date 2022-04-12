import numpy as np
from flask import Flask, render_template, jsonify, request, flash
import os
import joblib
import pandas as pd
from constants import *

TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('styles')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = 'Li-FinB@l@nce'

predictions = dict()
"""Loading Multi-label Classifier """
clf = joblib.load('finalized_model.sav')


@app.route('/', methods=["GET"])
def create_profile():
    return render_template('create_profile.html')


@app.route('/set_goal')
def set_goal():
    return render_template('set_goal.html')


@app.route('/goal')
def goal_index():
    return render_template('goal_index.html')


@app.route('/non_eligible_plan')
def non_eligible_plan():
    data = {}
    tax_code = pd.DataFrame.from_dict(predictions, orient="index", columns=["output"])
    tax_code["tax_section"] = tax_code.index
    tax_code.index = range(len(tax_code))
    non_eligible_tax_code = tax_code[tax_code["output"] == 0]
    for dat in non_eligible_tax_code["tax_section"].values:
        data.update({dat: tax_section[dat]})
    return render_template("non_eligibility_card.html", content=data)


@app.route('/eligible_plan')
def eligible_plan():
    data = {}
    tax_code = pd.DataFrame.from_dict(predictions, orient="index", columns=["output"])
    tax_code["tax_section"] = tax_code.index
    tax_code.index = range(len(tax_code))
    eligible_tax_code = tax_code[tax_code["output"] == 1]
    for dat in eligible_tax_code["tax_section"].values:
        data.update({dat: tax_section[dat]})
    return render_template("eligibility_card.html", content=data)


def get_taxable_amount(amount: float) -> float:
    """
    :param amount:
    :return:
    """
    taxable_amt = 0
    if amount <= 250000:
        taxable_amt = 0
    elif amount <= 500000:
        taxable_amt = (amount - 250000) * 0.05
    elif amount <= 1000000:
        taxable_amt = (amount - 500000) * 0.20 + 12500
    else:
        taxable_amt = (amount - 1000000) * 0.30 + 200000
    return taxable_amt


@app.route('/predict', methods=["POST"])
def classify():
    try:
        amount = float(request.form.get('income'))
        investment_opt = request.form.get('80C')
        FIRST_PROPERTY = request.form.get('FIRST_PROPERTY')
        SPECIFIC_ILLNESS = request.form.get('SPECIFIC_ILLNESS')
    except Exception as e:
        return jsonify({"message": "Please Check the Input format Provided"}), 400
    taxable_amt = get_taxable_amount(amount)
    data = np.array([[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]])
    pred = clf.predict(data).toarray()
    pred = pd.DataFrame(pred,
                        columns=['80D', '80DD', '80DDB', '80E', '80EE', '80EEA', '80TTB', '80TTA', '80CCD', '80C'])
    global predictions
    predictions = pred.to_dict('list')
    flash("User Created Successfully")
    return render_template('profile_2_set_goal.html')
