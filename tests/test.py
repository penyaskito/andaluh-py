#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: ts=4
###
# 
# Copyright (c) 2018-2019 Andalugeeks
# Authors:
# - Ksar Feui <a.moreno.losana@gmail.com>
# - J. Félix Ontañón <felixonta@gmail.com>

# Import package form parent dir https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

# Now it can be imported :)
import andaluh

# Basic tests
def test1():
    assert andaluh.epa('Todo Xenomorfo dice: [haber], que el Éxito y el éxtasis asfixian, si no eres un xilófono Chungo.') == u'Tó Çenomorfo diçe: [abêh], que el Éççito y el éttaçî âffîççian, çi no erê un çilófono Xungo.'
    assert andaluh.epa('Lleva un Guijarrito el ABuelo, ¡Qué Bueno! ¡para la VERGÜENZA!') == u'Yeba un Giharrito el AGuelo, ¡Qué Gueno! ¡pa la BERGUENÇA!'
    assert andaluh.epa('VALLA valla, si vas toda de ENVIDIA') == u'BAYA baya, çi bâ toa de EMBIDIA'
    assert andaluh.epa('Alrededor de la Alpaca había un ALfabeto ALTIVO de valkirias malnacidas') == u'Arrededôh de la Arpaca abía un ARfabeto ARTIBO de barkiriâ mânnaçidâ'
    assert andaluh.epa('En la Zaragoza y el Japón asexual se Sabía SÉriamente sILBAR con el COxis') == u'En la Çaragoça y er Hapón açêççuâh çe Çabía ÇÉriamente çIRBÂH con er CÔççî'
    assert andaluh.epa('Transportandonos a la connotación perspicaz del abstracto solsticio de Alaska, el aislante plástico adsorvente asfixió al aMnésico pseudoescritor granadino de constituciones, para ConMemorar broncas adscritas') == u'Trâpportandonô a la cônnotaçión perppicâh del âttrâtto çorttiçio de Alâkka, el aîl-lante pláttico âççorbente âffîççió al ânnéçico çeudoêccritôh granadino de côttituçionê, pa CôMMemorâh broncâ âccritâ'
    assert andaluh.epa('En la postmodernidad, el transcurso de los transportes y translados en postoperatorios transcienden a la postre unas postillas postpalatales apostilladas se transfieren') == u'En la pômmodênnidá, er trâccurço de lô trâpportê y trâl-láô en pôttoperatoriô trâççienden a la pôttre unâ pôttiyâ pôppalatalê apôttiyâh çe trâffieren'
    assert andaluh.epa('Venid todos a correr en anorak de visón a Cádiz con actitud y maldad, para escuchar el tríceps de Albéniz tocar ápud con virtud de laúd.') == u'Benîh tôh a corrêh en anorâh de biçón a Cádî con âttitûh y mardá, pa êccuxâh er tríçê de Arbénî tocâh ápû con birtûh de laûh.'
    assert andaluh.epa('Una comida fabada con fado, y sin descuido será casada y amarrada al acolchado roido.') == u'Una comida fabada con fado, y çin dêccuido çerá caçá y amarrá al acorxao roío.'
    assert andaluh.epa('Los SABuesos ChiHuaHUA comían cacaHuETes, FramBuESas y Heno, ¡y HABLAN ESPANGLISH!') == u'Lô ÇAGueçô XiGuaGUA comían cacaGuETê, FramBuEÇâ y Eno, ¡y ABLAN ÊPPANGLÎ!'

# Lemario test
def test2(report_all = False):

    import csv
    file = "./tests/lemario_cas_and.csv"

    transcriptions = []
    transcription_errors = []
    stats = {"total": 0, "ok": 0, "fail": 0}

    with open(file) as fh:
        rd = csv.DictReader(fh, delimiter=',')

        for row in rd:
            caste = unicode(row['cas'], 'utf-8')
            andal = unicode(row['and'], 'utf-8')
            trans = andaluh.epa(row['cas'])

            if andal != trans:
                transcription_errors.append((caste, andal, trans))
                stats["fail"] += 1
            else:
                stats["ok"] += 1

            transcriptions.append((caste, andal, trans))
            stats["total"] += 1
    

    if report_all:
        for error in transcription_errors:
            print error[0] + " => " + error[1] + ', ' + error[2]
    import pprint
    pprint.pprint(stats)

if __name__ == '__main__':
    test1()
    test2(True)