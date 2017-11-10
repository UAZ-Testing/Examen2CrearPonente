# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

import sys

reload(sys)
sys.setdefaultencoding('utf8')

INFO_PONENTE_CREADO = 'Ponente creado con éxito'


@step(u'Given se muestra la lista de ponentes')
def given_se_muestra_la_lista_de_ponentes(step):
    world.browser = webdriver.Firefox()
    world.server_url = 'http://localhost:8000'
    world.browser.get(world.server_url)

    tabla = world.browser.find_element_by_id('tablaPonentes')
    world.ponente_rows = tabla.find_element_by_css_selector('.row-ponente')


@step(u'And cada ponente tiene <Nombre>')
def and_cada_ponente_tiene_nombre(step):
    ponente_nombre = world.ponente_rows.find_element_by_css_selector(
        '.nom-ponente')
    assert len(ponente_nombre.get_attribute('innerText')) > 0, \
        'El nombre no puede estar vacío'


@step(u'And cada ponente tiene <Primer Apellido>')
def and_cada_ponente_tiene_primer_apellido(step):
    ponente_papellido = world.ponente_rows.find_element_by_css_selector(
        '.pap-ponente')
    assert len(ponente_papellido.get_attribute('innerText')) > 0, \
        'El primer apellido no puede estar vacío'


@step(u'And cada ponente tiene <Segundo Apellido>')
def and_cada_ponente_tiene_segundo_apellido(step):
    ponente_sapellido = world.ponente_rows.find_element_by_css_selector(
        '.sap-ponente')


@step(u'And cada ponente tiene un botón <Editar Ponente>')
def and_cada_ponente_tiene_un_boton_editar_ponente(step):
    btn_editar = world.ponente_rows.find_element_by_css_selector('.btn-editar')


@step(u'And cada ponente tiene un botón <Eliminar Ponente>')
def and_cada_ponente_tiene_un_boton_eliminar_ponente(step):
    btn_eliminar = world.ponente_rows.find_element_by_css_selector(
        '.btn-eliminar')


@step(u'When se hace click en el botón <Nuevo Ponente>')
def when_se_hace_click_en_el_boton_nuevo_ponente(step):
    btn_nuevo = world.browser.find_element_by_id('btnNuevoPonente')
    btn_nuevo.click()


@step(u'And se llena en <Nombre> "([^"]*)"')
def and_se_llena_en_nombre_group1(step, nombre):
    txt_nombre = world.browser.find_element_by_id('id_nombre')
    txt_nombre.send_keys(nombre)
    world.nombre = nombre


@step(u'And se llena en <Primer Apellido> "([^"]*)"')
def and_se_llena_en_primer_apellido_group1(step, ap_pat):
    txt_ap_pat = world.browser.find_element_by_id('id_primer_apellido')
    txt_ap_pat.send_keys(ap_pat)
    world.ap_pat = ap_pat


@step(u'And se llena en <Segundo Apellido> "([^"]*)"')
def and_se_llena_en_segundo_apellido_group1(step, ap_mat):
    txt_ap_mat = world.browser.find_element_by_id('id_segundo_apellido')
    txt_ap_mat.send_keys(ap_mat)
    world.ap_mat = ap_mat


@step(u'And se hace click en el botón <Guardar Ponente>')
def and_se_hace_click_en_el_boton_guardar_ponente(step):
    btn_guardar = world.browser.find_element_by_id('btnGuardar')
    btn_guardar.click()


@step(u'Then se redirige a la lista de ponentes')
def then_se_redirige_a_la_liste_de_ponentes(step):
    titulo_h1 = world.browser.find_elements_by_tag_name('h1')[0]
    titulo_text = titulo_h1.get_attribute('innerText')
    assert titulo_text == 'Ponentes', 'Se esperaba el título "Ponentes" y se' \
                                      ' obtuvo "%s"' % (titulo_text)


@step(u'And se muestra el mensaje <Ponente creado con éxito>')
def and_se_muestra_el_mensaje_ponente_creado_con_exito(step):
    info_box = world.browser.find_element_by_css_selector('.alert-success')
    info_text = info_box.get_attribute('innerText')

    assert INFO_PONENTE_CREADO in info_text, 'Se esperaba "%s" y se obtuvo %s' \
                                             % (INFO_PONENTE_CREADO, info_text)


@step(u'And se muestra el ponente creado en la lista de ponentes')
def and_se_muestra_el_ponente_creado_en_la_lista_de_ponentes(step):
    tabla = world.browser.find_element_by_id('tablaPonentes')
    ponente_rows = tabla.find_elements_by_css_selector('.row-ponente')

    ponente_encontrado = False

    for row in ponente_rows:
        celdas = row.find_elements_by_tag_name('td')
        txt_c1 = celdas[0].get_attribute('innerText')
        txt_c2 = celdas[1].get_attribute('innerText')
        txt_c3 = celdas[2].get_attribute('innerText')

        if world.nombre == txt_c1 and world.ap_pat == txt_c2 and \
                        world.ap_mat == txt_c3:
            ponente_encontrado = True
            assert True

    if not ponente_encontrado:
        assert False, 'No se encontró el ponente %s %s' % (
            world.nombre, world.ap_pat)
