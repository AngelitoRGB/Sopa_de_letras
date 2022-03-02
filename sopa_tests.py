import sopav6

Archivo_prueba = ['DIMENSION\n', '8\n', 'PALABRAS\n', 'perro\n', 'gato\n', 'lagarto\n', 'mouse\n', 'teclado\n', 'COMPLEJIDAD\n', '0']
Archivo_prueba2 = ['Dimension\n', "10\n", "PALABRAS\n", "ventilador\n", "guitarra\n", "microfono\n", "mesa\n", "ropero\n", "COMPLEJIDAD\n", "2"]
def test_leerArchivo():
    sopav6.leerArchivo(Archivo_prueba) == (8, ["perro", "gato", "lagarto", "mouse", "teclado"], 0)
    sopav6.leerArchivo(Archivo_prueba2) == (10, ["ventilador", "guitarra", "microfono", "mesa", "ropero"], 2)

def test_generarSopa_vacia():
    assert sopav6.generarSopa_vacia(4) == ["    ", "    ", "    ", "    "]
    assert sopav6.generarSopa_vacia(8) == ["        ", "        ", "        ", "        ", "        ", "        ", "        ", "        "]

def test_verificarFilaVacia():
    assert sopav6.verificarFilaVacia("      ") == (True, [])
    assert sopav6.verificarFilaVacia("a g hg  ") == (False, [0, 2, 4, 5])

def test_hay_espacio():
    assert sopav6.hay_espacio([0, 2, 4, 5], 5, 6) == (False, [-1, 0, 2, 4, 5, 6])
    assert sopav6.hay_espacio([2, 3], 4, 10) == (True, 4)

sopa_prueba = ["dsaa", "anjg", "dorr", "odjb"]
sopa_prueba2 = ["gdchgt", "mlujnd", "njaeui", "njdñlk", "bjroej", "zxonmj"]
sopa_prueba3 = ["abcd", "efgh", "ijkl", "mnop"]
def test_obtenerColumna():
    assert sopav6.obtenerColumna(sopa_prueba, 0, 4) == "dado"
    assert sopav6.obtenerColumna(sopa_prueba2, 2, 6) == "cuadro"

def test_rotarSopa():
    assert sopav6.rotarSopa(sopa_prueba) == ["dado", "snod", "ajrj", "agrb"]
    assert sopav6.rotarSopa(sopa_prueba2) == ["gmnnbz", "dljjjx", "cuadro", "hjeñon", "gnulem", "tdikjj"]

def test_rotarSopa2():
    assert sopav6.rotarSopa2(sopa_prueba3) == ["dhlp", "cgko", "bfjn", "aeim"]
    assert sopav6.rotarSopa2(sopa_prueba) == ["agrb", "ajrj", "snod", "dado"]

def test_rotarSopa3():
    assert sopav6.rotarSopa3(sopa_prueba3) == ["miea", "njfb", "okgc", "plhd"]
    assert sopav6.rotarSopa3(sopa_prueba) == ["odad", "dons", "jrja", "brga"]

def test_filaHorizontal():
    assert sopav6.filaHorizontal("    ", "gato") == ("gato", False)
    assert sopav6.filaHorizontal("a     yk ", "mouse") == ("amouseyk ", False)
    assert sopav6.filaHorizontal(" j jh p", "mesa") == (" j jh p", True)

def test_ponerPalabra():
    assert sopav6.ponerPalabra(" e   k n", [1,5,7], "perro", 8) == "perrok n"
    assert sopav6.ponerPalabra(" l n y", [1, 3, 5], "sol", 6) == " l n y"

def test_obtenerVertical():
    assert sopav6.obtenerVertical(sopa_prueba2, 0, 1) == "duelj"
    assert sopav6.obtenerVertical(sopa_prueba2, 2, 0)  == "njrn"
    assert sopav6.obtenerVertical(sopa_prueba3, 0, 2) == "ch"

sopa_prueba4 = ["    ", "    ", "    ", "    "]
sopa_prueba5 = ["abdjhm", " gatos", "m solt", "at izy", "lhq sw", "oprx t"]

def test_ponerVertical():
    assert sopav6.ponerVertical(sopa_prueba4, "gato", 0, 0) == ["g   ", " a  ", "  t ", "   o"]
    assert sopav6.ponerVertical(sopa_prueba5, "balde", 1, 0) == ["abdjhm", "bgatos", "masolt", "atlizy", "lhqdsw", "oprxet"]

sopa_prueba6 = ["camariat", "orqweufe", "hqwercil", "edsfdsba", "telazzra", "erqweroh", "mvznmznl", "monitorp"]
sopa_prueba7 = ["camariah", "orqweufj", "hqwercik", "edsfdsbn", "telazzra", "erqweroh", "mvznmznl", "monitorp"]
def test_buscar_palabras_repetidasD0():
    assert sopav6.buscar_palabras_repetidasD0(sopa_prueba6, ["maria", "cohete", "tela", "fibron", "monitor"]) == True
    assert sopav6.buscar_palabras_repetidasD0(sopa_prueba7, ["maria", "cohete", "tela", "fibron", "monitor"]) == False

sopa_prueba8 = ["abcd", "sefs", "goho", "ijll"]
def test_buscar_palabras_repetidasD1():
    assert sopav6.buscar_palabras_repetidasD1(sopa_prueba8, ["sol"]) == True
    assert sopav6.buscar_palabras_repetidasD1(sopa_prueba7, ["maria", "cohete", "tela", "fibron", "monitor"]) == False

sopa_prueba9 = ["fghzxm", "demesa", "emsnqt", "wtxoae", "mdafiz", "lkimaf"]

def test_buscar_palabras_repetidasD2():
    assert sopav6.buscar_palabras_repetidasD2(sopa_prueba9, ["sol", "mesa", "mate"]) == True
    assert sopav6.buscar_palabras_repetidasD2(sopa_prueba7, ["maria", "cohete", "tela", "fibron", "monitor"]) == False