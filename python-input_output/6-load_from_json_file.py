#!/usr/bin/python3
import json
import os

def load_from_json_file(filename):
    """
    Verilən JSON faylını oxuyur və Python obyektinə çevirir.

    Parametrlər:
    filename (str): Oxunacaq JSON faylının adı.

    Qayıdan dəyər:
    dict: JSON obyektini təmsil edən Python lüğəti.

    Xətalar:
    FileNotFoundError: Fayl tapılmadıqda.
    JSONDecodeError: Faylın tərkibi düzgün JSON formatında olmadıqda.
    """
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"'{filename}' faylı tapılmadı.")
    
    with open(filename, 'r', encoding='utf-8-sig') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"'{filename}' faylında JSON sintaksis səhvi: {e}")
