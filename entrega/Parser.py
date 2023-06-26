#importar librerias
from ply import lex 
import time
import re
import ply.yacc as yacc



import os
import codecs
import ply.yacc as yacc
correcto = 0
##################### LEXER#####################################
reservadas = ['APERTURA_XML','OPEN_ARTICLE','CLOSE_ARTICLE','OPEN_SECTION','CLOSE_SECTION','OPEN_SIMPLE_SECTION','CLOSE_SIMPLE_SECTION','OPEN_INFO','CLOSE_INFO','OPEN_ABSTRAC',
'CLOSE_ABSTRACT','OPEN_ADDRESS','CLOSE_ADDRESS','OPEN_AUTHOR','CLOSE_AUTHOR','OPEN_COPYRIGHT','CLOSE_COPYRIGHT','OPEN_TITLE','CLOSE_TITLE','OPEN_EMPHASIS',
'CLOSE_EMPHASIS','OPEN_LINK','CLOSE_LINK','OPEN_EMAIL','CLOSE_EMAIL','OPEN_SIMPARA','CLOSE_SIMPARA','OPEN_PARA','CLOSE_PARA','OPEN_MEDIA','CLOSE_MEDIA','OPEN_TABLE','CLOSE_TABLE',
'OPEN_IMPORTANT','CLOSE_IMPORTANT','OPEN_COMMENT','CLOSE_COMMENT','OPEN_FIRST_NAME','CLOSE_FIRST_NAME','OPEN_SURNAME','CLOSE_SURNAME','OPEN_STREET','CLOSE_STREET','OPEN_PHONE','CLOSE_PHONE'
,'OPEN_DATE','CLOSE_DATE','OPEN_YEAR','CLOSE_YEAR','OPEN_HOLDER','CLOSE_HOLDER','OPEN_STATE','CLOSE_STATE','OPEN_CITY','CLOSE_CITY' , 'OPEN_PERSON_NAME' , 'CLOSE_PERSON_NAME', 
'OPEN_POSTCODE', 'CLOSE_POSTCODE','TAG_ERRONEO' , 'CARACTER_INVALIDO', 'OPEN_IMAGE_OBJECT', 'CLOSE_IMAGE_OBJECT','OPEN_VIDEO_OBJECT','CLOSE_VIDEO_OBJECT' ,'DOCTYPE', 'op_imagedata'
,'intro_url2', 'intro_url3', 'IMAGE_DATA', 'VIDEO_DATA', 'ClOSE_URL_LINK', 'OPEN_BODY_TABLE','CLOSE_BODY_TABLE','OPEN_ROW','CLOSE_ROW','OPEN_ENTRY','CLOSE_ENTRY', 'OPEN_ABSTRACT', 'ignore','OPEN_ITEMIZED_LIST',
'CLOSE_ITEMIZED_LIST', 'OPEN_BODY','CLOSE_BODY','OPEN_T_GROUP','CLOSE_T_GROUP','OPEN_HEAD','CLOSE_HEAD','OPEN_FOOT','CLOSE_FOOT' ]




tokens = reservadas+['TEXTO', 'URL'] 
t_APERTURA_XML = r'<?xml[^<>]*?>'
t_DOCTYPE= r"<!DOCTYPE[ ]article>"


def t_OPEN_LINK (t):
     r'<link'
     return t



def t_intro_url (t) :
     r'xlink:href="'
     return (print (f"Atributo de referencia a link: {t.value}"))

def t_op_imagedata (t):
     r'<imagedata'
     return (print (f"Apertura de imagedata: {t.value}"))

def t_op_videodata (t):
     r'<videodata'
     return (print (f"Apertura de videodata: {t.value}"))

def t_intro_url2 (t):
     r'fileref='
     return ((print (f"Atributo de referencia fileref: {t.value}")))
     

# Definición de la expresión regular para la URL de video
def t_VIDEO_DATA(t):
      r'"https?://[^\s<>"]+|www\.[^\s<>"]+\.(mp4|mov|wmv|avi|avch|flv|f4v|swf|mkv|mpeg-2)"'
      return t

# Definición de la expresión regular para la URL de imagen
def t_IMAGE_DATA(t):
      r'"https?://[^\s<>"]+|www\.[^\s<>"]+\.(png|jpg|jpeg|gif|bmp|tiff|pdf|eps|svg)+[^\s<>"]'
      return t

def t_intro_url3 (t) :
     r'.(png|jpg|jpeg|gif)'
     return (print (f"Atributo de referencia a imagen: {t.value}"))    
#definición de tokens de cadena de URL 
def t_URL(t):
    r'\"(http|https|ftp|ftps)://[^/\s:]+(:\d+)?(/[^#\s])?(\#\S)?\"'
    return (print (f"URL: {t.value}"))

def t_ClOSE_URL_LINK(t):
    r' >'
    return t

# Función para reconocer URLs


#definición de tokens de cadena de texto


t_TEXTO= r'[^<>]+'

#definicion de tokens de docbook

t_OPEN_ARTICLE  =r'<article>'

def t_CLOSE_ARTICLE (t):
    r'</article>'
    return t

def t_OPEN_SECTION (t):
      r'<section>'
      return t
def t_CLOSE_SECTION (t):
     r'</section>'
     return t

def t_OPEN_SIMPLE_SECTION (t) :
     r'<simplesection>'
     return (t)

def t_CLOSE_SIMPLE_SECTION (t) :
     r'</simplesection>'
     return (t)

def t_OPEN_INFO (t):
      r'<info>'
      return t
def t_CLOSE_INFO (t):
      r'</info>'
      return t

def t_OPEN_ABSTRACT (t):
      r'<abstract>'
      return t
def t_CLOSE_ABSTRACT (t):
      r'</abstract>'
      return t

def t_OPEN_ADDRESS (t):
      r'<address>'
      return t
def t_CLOSE_ADDRESS (t):
      r'</address>'
      return t
def t_OPEN_AUTHOR (t):
      r'<author>'
      return t
def t_CLOSE_AUTHOR (t):
      r'</author>'
      return t

def t_OPEN_COPYRIGHT(t):
      r'<copyright>'
      return t
def t_CLOSE_COPYRIGHT (t):
      r'</copyright>'
      return t

def t_OPEN_TITLE (t):
      r'<title>'
      return t
def t_CLOSE_TITLE (t):
      r'</title>'
      return t

def t_OPEN_EMPHASIS (t):
      r'<emphasis>'
      return t
def t_CLOSE_EMPHASIS (t):
      r'</emphasis>'
      return t

def t_OPEN_LINK (t):
     r'<link'
     return t

def t_CLOSE_LINK (t):
      r'</link>'
      return t

def t_OPEN_EMAIL (t):
      r'<email>'
      return t
def t_CLOSE_EMAIL (t):
      r'</email>'
      return t

def t_OPEN_SIMPARA (t):
      r'<simpara>'
      return t
def t_CLOSE_SIMPARA (t):
      r'</simpara>'
      return t

def t_OPEN_PARA (t):
      r'<para>'
      return t
def t_CLOSE_PARA (t):
      r'</para>'
      return t

def t_OPEN_MEDIA (t):
    r'<mediaobject>'  
    return t
def t_CLOSE_MEDIA (t):
     r'</mediaobject>'
     return t

def t_OPEN_TABLE (t):
      r'<informatable frame = "[<>]"'
      return t
def t_CLOSE_TABLE (t):
      r'</informaltable>'
      return t

## elementos de tabla
def t_OPEN_BODY_TABLE (t):  
      r'<bodytable>'
      return t
def t_CLOSE_BODY_TABLE (t):
      r'</bodytable>'
      return t

def t_CLOSE_ROW (t):
      r'</row>'
      return t
def t_OPEN_ROW (t):
      r'<row>'
      return t

def t_OPEN_ENRTY (t):
      r'<entry>'
      return t

def t_CLOSE_ENRTY (t):
      r'</entry>'
      return t


def t_OPEN_IMPORT (t):
      r'<important>'
      return t
def t_CLOSE_IMPORT (t):
      r'</important>'
      return t

def t_OPEN_COMMENT (t):
      r'<comment>'
      return t
def t_CLOSE_COMMENT (t):
      r'</comment>'
      return t

def t_OPEN_FIRST_NAME (t):
      r'<firstname>'
      return t
def t_CLOSE_FIRST_NAME (t):
      r'</firstname>'
      return t

def t_OPEN_SURNAME (t):
      r'<surname>'
      return t
def t_CLOSE_SURNAME (t):
      r'</surname>'
      return t

def t_OPEN_STREET (t):
      r'<street>'
      return t
def t_CLOSE_STREET (t):
      r'</street>'
      return t

def t_OPEN_PHONE (t):
      r'<phone>'
      return t
def t_CLOSE_PHONE (t):
      r'</phone>'
      return t

def t_OPEN_DATE (t):
      r'<date>'
      return t
def t_CLOSE_DATE (t):
      r'</date>'
      return t

def t_OPEN_YEAR (t):
      r'<year>'
      return t
def t_CLOSE_YEAR (t):
      r'</year>'
      return t

def t_OPEN_HOLDER (t):
      r'<holder>'
      return t
def t_CLOSE_HOLDER (t):
      r'</holder>'
      return t

def t_OPEN_STATE (t):
      r'<state>'
      return t
def t_CLOSE_STATE (t):
      r'</state>'
      return t

def t_OPEN_CITY (t):
      r'<city>'
      return t
def t_CLOSE_CITY (t):
      r'</city>'
      return t

def t_OPEN_PERSON_NAME (t):
      r'<personname>'
      return t
def t_CLOSE_PERSON_NAME (t):
      r'</personname>'
      return t

def t_OPEN_POSTCODE (t):
      r'<postcode>'
      return t
def t_CLOSE_POSTCODE (t):
      r'/postcode>'
      return t

def t_ESPACIO(t):
    r'\ '
    pass

def t_TAB(t):
  r'\t'
  pass
      
def t_OPEN_BODY (t):
     r'<tbody>'
     return t


def t_OPEN_GROUP (t):
     r'<tgroup>'
     return t

def t_CLOSE_GROUP (t):
     r'</tgroup>'
     return t

def t_OPEN_HEAD (t):
     r'<thead>'
     return t

def t_CLOSE_HEAD (t):
     r'</thead>'
     return t

def t_OPEN_FOOT (t):
     r'<tfoot>'
     return t

def t_CLOSE_FOOT (t):
     r'</tfoot>'
     return t


def t_OPEN_IMAGE_OBJECT (t):
      r'<imageobject>'
      return t
def t_CLOSE_IMAGE_OBJECT (t):
      r'</imageobject>'
      return t

def t_OPEN_VIDEO_OBJECT (t):
      r'<videoobject>'
      return t
def t_CLOSE_VIDEO_OBJECT (t):
      r'</videoobject>'
      return t

def t_TAG_ERRONEO(t):
    r'<[^>]+>'
    t.type = 'TAG_ERRONEO'
    return t

def t_OPEN_ITEMIZED_LIST (t):
     r'<itemizedlist mark= "[<>]"'
     return t

def t_CLOSE_ITEMIZED_LIST (t):
     r'</itemizedlist>'
     return t
def t_CARACTER_INVALIDO(t):  # funciona como el t_error
    r'[<>]'
    return print (f'Caracter no valido: {t.value}')

# Manejo de errores, solo lo usamos debido a que sin esto, no se ejecuta
def t_error(t):  
    print("Carácter no válido: %s" % t.value[0])
    t.lexer.skip(1)

#definición de salto de pagina
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \n'



def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.extend([file for file in files if file.endswith('.xml')])

    if not ficheros:
        print("Error: No se encontraron archivos .xml en el directorio especificado.")
        return None

    for file in ficheros:
        print(f"{cont}. {file}")
        cont += 1

    while not respuesta:
        numArchivo = input('\nPonga el número del archivo que desea procesar: ')
        try:
            numArchivo = int(numArchivo)
            if 1 <= numArchivo <= len(ficheros):
                respuesta = True
            else:
                print("Número de archivo fuera de rango. Por favor, ingrese un número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

  

    return ficheros[numArchivo - 1]


#--------------------------------------------------- Arranca el programa-----------------------------------

   

###################PARSER##########################

#gramaticas

correcto = 0

def p_error(p):
    if p is not None:
        global correcto
        correcto += 1
        print (f"Error de sintaxis en el token {p.value} ,error en la linea "+str(p.lineno))
      


        

def p_GEN_article(p):
    '''GEN_article : OPEN_ARTICLE GENALL_ART CLOSE_ARTICLE'''
    p [0] = p [2]
   

def p_GENALL_ART (p) :
    ''' GENALL_ART : GEN_INFO CONT
        | GEN_INFO GEN_TITL CONT
        | GEN_TITL CONT
        | CONT
    '''
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]

def p_CONT (p):
    '''CONT : GEN_LIST CONT 
    | GEN_IMPORTANT CONT 
    | GEN_PARA CONT 
    | GEN_SIMP CONT 
    | AD CONT 
    | MO CONT 
    | GEN_TABLE CONT 
    | GEN_COM CONT 
    | GEN_ABS CONT 
    | GEN_LIST 
    | GEN_IMPORTANT 
    | GEN_PARA 
    | GEN_SIMP 
    | AD 
    | MO 
    | GEN_TABLE 
    | GEN_COM 
    | GEN_ABS 
    | GEN_SECTION
    '''
    if len (p) == 2 :
         p [0] = p (p[1],p[2])
    else:
         p [0] = p[1]


def p_GEN_SECTION (p):
    ''' GEN_SECTION : OPEN_SECTION GENALL_ART CLOSE_SECTION        
    '''

    p[0] = p [2]

def p_GEN_SIMPSEC (p):
    '''GEN_SIMPEC : OPEN_SIMPLE_SECTION SIMPSEC CLOSE_SIMPLE_SECTION'''
    p[0] = p [2]

def p_SIMPSEC (p) :
    '''SIMPSEC : GEN_LIST CONT 
    | GEN_IMPORTANT CONT 
    | GEN_PARA CONT 
    | GEN_SIMP CONT 
    | AD CONT 
    | MO CONT 
    | GEN_TABLE CONT 
    | GEN_COM CONT 
    | GEN_ABS CONT 
    | GEN_LIST 
    | GEN_IMPORTANT 
    | GEN_PARA 
    | GEN_SIMP 
    | AD 
    | MO 
    | GEN_TABLE 
    | GEN_COM 
    | GEN_ABS  '''
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]


def p_GEN_INFO  (p):
    '''GEN_INFO : OPEN_INFO INFO CLOSE_INFO'''
    p[0] = p [2]

def p_INFO (p): 
    '''INFO : MO 
            | GEN_ABS 
            | AD 
            | GEN_AUT 
            | GEN_DATE 
            | GEN_COP 
            | GEN_TITL 
            | GEN_EMAIL 
            | MO INFO 
            | GEN_ABS INFO 
            | AD INFO 
            | GEN_AUT INFO 
            | GEN_DATE INFO 
            | GEN_COP INFO 
            | GEN_TITL INFO 
            | GEN_EMAIL INFO
    '''
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]

def p_GEN_ABS (p):
    ''' GEN_ABS : OPEN_ABSTRACT GEN_TITL INFOAB CLOSE_ABSTRACT
        | OPEN_ABSTRACT INFOAB CLOSE_ABSTRACT '''
    
    p [0] = p [2]

def p_INFOAB (p):
    ''' INFOAB : GEN_PARA
        | GEN_SIMP
        | GEN_PARA INFOAB
        | GEN_SIMP INFOAB '''
    
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]

def p_GENx (p):### CORREGIR EN EL WORD
    ''' GENx : GEN_STREET_AD 
        | GEN_STATE_AD
        | GEN_CITY_AD
        | GEN_PHONE_AD
        | GEN_MAIL_AD
        | TEXTO
        | GEN_STREET_AD GENx
        | GEN_STATE_AD GENx
        | GEN_CITY_AD GENx
        | GEN_PHONE_AD GENx
        | GEN_MAIL_AD GENx 
        | TEXTO GENx '''
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]

def p_GENALL_AD (p):
    ''' GENALL_AD : TEXTO
        | GEN_LINK
        | GEN_EMP
        | GEN_COM
        | TEXTO CONEX2
        | GEN_LINK CONEX2
        | GEN_EMP CONEX2
        | GEN_COM CONEX2 '''
    
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]

def p_AD (p):
    ''' AD : OPEN_ADDRESS GENx CLOSE_ADDRESS
        | OPEN_ADDRESS TEXTO CLOSE_ADDRESS '''
    p [0] = p [2]

def p_GEN_STREET_AD (p):
    ''' GEN_STREET_AD : OPEN_STREET GENALL_AD CLOSE_STREET '''
    p [0] = p [2]

def p_GEN_STATE_AD (p):
    ''' GEN_STATE_AD : OPEN_STATE GENALL_AD CLOSE_STATE '''
    p [0] = p [2]

def p_GEN_CITY_AD (p):
    ''' GEN_CITY_AD : OPEN_CITY GENALL_AD CLOSE_CITY '''
    p [0] = p [2]

def p_GEN_PHONE_AD (p):
    ''' GEN_PHONE_AD : OPEN_PHONE GENALL_AD CLOSE_PHONE '''
    p [0] = p [2]

def p_GEN_MAIL_AD (p):
    ''' GEN_MAIL_AD : OPEN_EMAIL GENALL_AD CLOSE_EMAIL'''
    p [0] = p [2]

def p_GEN_AUT (p):
    ''' GEN_AUT : OPEN_AUTHOR AUT CLOSE_AUTHOR '''
    p [0] = p [2]

def p_AUT (p):
    ''' AUT : GEN_FIRSTN
        | GEN_SURN
        | GEN_FIRSTN AUT
        | GEN_SURN AUT '''
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]

def p_GEN_COP (p):
    ''' GEN_COP : OPEN_COPYRIGHT COP CLOSE_COPYRIGHT '''
    p [0] = p [2]

def p_COP (p):
    ''' COP : GEN_YEAR
        | GEN_HOLDER
        | GEN_YEAR COP
        | GEN_HOLDER COP '''
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]

def p_GEN_TITL (p): ### CORREGIR WORD 
    ''' GEN_TITL : OPEN_TITLE CONT_TIT CLOSE_TITLE '''  
    p [0] = p [2]

def p_CONT_TIT (p):
    ''' CONT_TIT : TEXTO
        | GEN_EMP
        | GEN_LINK
        | GEN_EMAIL
        | TEXTO CONT_TIT
        | GEN_EMP CONT_TIT
        | GEN_EMAIL CONT_TIT
        | GEN_LINK CONT_TIT '''
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]

def p_GEN_SIMP (p):### CORREGIR WORD 
    ''' GEN_SIMP : OPEN_SIMPARA CONEX CLOSE_SIMPARA ''' 
    p [0] = p [2]

def p_GEN_EMP (p):### CORREGIR WORD 
    ''' GEN_EMP : OPEN_EMPHASIS CONEX CLOSE_EMPHASIS '''    
    p [0] = p [2]

def p_CONEX2 (p):
    '''CONEX2 : TEXTO CONEX2
        | GEN_LINK
        | GEN_EMP
        | GEN_COM
        | GEN_LINK CONEX2
        | GEN_EMP CONEX2 
        | GEN_COM CONEX2
        | TEXTO
     ''' 
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]
    
def p_CONEX (p):
    ''' CONEX : TEXTO 
        | GEN_EMP
        | GEN_LINK
        | GEN_EMAIL
        | GEN_AUT
        | GEN_COM
        | GEN_EMP CONEX
        | TEXTO CONEX
        | GEN_LINK CONEX
        | GEN_EMAIL CONEX
        | GEN_AUT CONEX
        | GEN_COM CONEX '''
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]

def p_GEN_LINK (p):
    ''' GEN_LINK : OPEN_LINK CONEX CLOSE_LINK '''
    p [0] = p [2]

def p_GEN_COM (p):
    ''' GEN_COM : OPEN_COMMENT CONEX CLOSE_COMMENT '''
    p [0] = p [2]

def p_GEN_PARA (p):
    ''' GEN_PARA : OPEN_PARA OP_PARA CLOSE_PARA '''
    p [0] = p [2]

def p_OP_PARA (p):
    ''' OP_PARA : TEXTO
        | GEN_LINK
        | GEN_EMP
        | GEN_EMAIL
        | GEN_AUT
        | GEN_COM
        | GEN_LIST
        | GEN_IMPORTANT
        | AD
        | MO
        | GEN_TABLE
        | TEXTO OP_PARA
        | GEN_LINK OP_PARA 
        | GEN_EMP OP_PARA
        | GEN_EMAIL OP_PARA
        | GEN_AUT OP_PARA
        | GEN_COM OP_PARA
        | GEN_LIST OP_PARA
        | GEN_IMPORTANT OP_PARA
        | AD OP_PARA
        | MO OP_PARA
        | GEN_TABLE OP_PARA '''
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]

def p_GEN_IMPORTANT (p):### CORREGIR WORD 
    ''' GEN_IMPORTANT : OPEN_IMPORTANT GEN_TITL CLOSE_IMPORTANT   
        | OPEN_IMPORTANT GEN_TITL IMPORTANT CLOSE_IMPORTANT
        | OPEN_IMPORTANT IMPORTANT CLOSE_IMPORTANT '''

def p_IMPORTANT (p):
    ''' IMPORTANT : GEN_LIST
        | GEN_IMPORTANT
        | GEN_PARA
        | GEN_SIMP
        | AD
        | MO
        | GEN_TABLE
        | GEN_COM
        | GEN_ABS
        | GEN_LIST IMPORTANT
        | GEN_IMPORTANT IMPORTANT
        | GEN_PARA IMPORTANT
        | GEN_SIMP IMPORTANT
        | AD IMPORTANT
        | MO IMPORTANT
        | GEN_TABLE IMPORTANT
        | GEN_COM IMPORTANT
        | GEN_ABS IMPORTANT '''
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]
    
def p_GEN_FIRSTN (p):
    ''' GEN_FIRSTN : OPEN_FIRST_NAME GENALL CLOSE_FIRST_NAME '''
    p [0] = p [2]

def p_GENALL (p):   ### CORREGIR WORD 
    ''' GENALL : TEXTO
        | GEN_LINK
        | GEN_EMP
        | GEN_COM
        | TEXTO GENALL
        | GEN_LINK GENALL
        | GEN_EMP GENALL
        | GEN_COM GENALL '''
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]

def p_GEN_SURN (p):
    ''' GEN_SURN : OPEN_SURNAME GENALL CLOSE_SURNAME '''
    p [0] = p [2]

def p_GEN_STREET (p):
    ''' GEN_STREET : OPEN_STREET GENALL CLOSE_STREET '''
    p [0] = p [2]

def p_GEN_CITY(p):
    ''' GEN_CITY : OPEN_CITY GENALL CLOSE_CITY '''
    p [0] = p [2]

def p_GEN_STATE(p):
    ''' GEN_STATE : OPEN_STATE GENALL CLOSE_STATE '''
    p [0] = p [2]

def p_GEN_PHONE (p):
    ''' GEN_PHONE : OPEN_PHONE GENALL CLOSE_PHONE '''
    p [0] = p [2]

def p_GEN_EMAIL (p):
    ''' GEN_EMAIL : OPEN_EMAIL GENALL CLOSE_EMAIL '''
    p [0] = p [2]

def p_GEN_DATE (p):
    ''' GEN_DATE : OPEN_DATE GENALL CLOSE_DATE '''
    p [0] = p [2]

def p_GEN_YEAR (p):
    ''' GEN_YEAR : OPEN_YEAR GENALL CLOSE_YEAR '''
    p [0] = p [2]


def p_GEN_HOLDER (p):
    ''' GEN_HOLDER : OPEN_HOLDER GENALL CLOSE_HOLDER '''
    p [0] = p [2]


def p_MO (p):
    ''' MO : OPEN_MEDIA J CLOSE_MEDIA '''
    p [0] = p [2]


def p_J (p):
    ''' J : OPEN_INFO INFO CLOSE_INFO VIDEO 
        | OPEN_INFO INFO CLOSE_INFO IMAGE
        | R '''
    
    if len (p) == 1:
         p [0]= p[1]
    else:
         p[0]= p (p[2], p[4])

def p_R (p):
    ''' R : IMAGE
        | VIDEO
        | IMAGE R
        | VIDEO R '''
    if len (p) == 2 :
         p [0] =p(p[1],p[2])
    else:
         p [0] = p[1]

def p_VIDEO (p):
    ''' VIDEO : OPEN_VIDEO_OBJECT VO CLOSE_VIDEO_OBJECT '''
    p [0] = p [2]


def p_VO (p): 
    ''' VO : OPEN_INFO INFO CLOSE_INFO VDATA
        | VDATA '''
    if len (p) == 2 :
         p [0] = p(p[2],p[4])
    else:
         p [0] = p[1]

def p_VDATA (p):
    ''' VDATA : VIDEO_DATA '''
    p [0] = p[1]

def p_IMAGE (p):
    ''' IMAGE : OPEN_IMAGE_OBJECT IO CLOSE_IMAGE_OBJECT '''
    p [0] = p[2]

def p_IO (p):
    ''' IO : OPEN_INFO INFO CLOSE_INFO IDATA
        | IDATA '''
    if len (p) == 2 :
         p [0] = p(p[2],p[4])
    else:
         p [0] = p[1]

def p_IDATA (p):
    ''' IDATA : IMAGE_DATA '''
    p [0] = p[1]

def p_GEN_LIST (p):
    ''' GEN_LIST : OPEN_ITEMIZED_LIST LIST_IT CLOSE_ITEMIZED_LIST '''
    p [0] = p [2]


def p_LIST_IT (p):
    ''' LIST_IT : OPEN_ITEMIZED_LIST GEN_LISTITEM CLOSE_ITEMIZED_LIST LIST_IT
        | OPEN_ITEMIZED_LIST GEN_LISTITEM CLOSE_ITEMIZED_LIST '''
    if len (p) == 4 :
        p [0] = p (p[2],p[4])
    else:
         p [0] = p[2]


def p_GEN_LISTITEM (p):
    ''' GEN_LISTITEM : GEN_LIST
        | IMPORTANT
        | GEN_PARA
        | GEN_SIMP
        | AD
        | MO
        | GEN_TABLE
        | GEN_COM
        | GEN_ABS
        | GEN_LIST GEN_LISTITEM
        | IMPORTANT GEN_LISTITEM
        | GEN_PARA GEN_LISTITEM
        | GEN_SIMP GEN_LISTITEM
        | AD GEN_LISTITEM
        | MO GEN_LISTITEM
        | GEN_TABLE GEN_LISTITEM
        | GEN_COM GEN_LISTITEM
        | GEN_ABS GEN_LISTITEM '''
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]

def p_GEN_TABLE (p):
    ''' GEN_TABLE : OPEN_TABLE INF_TB CLOSE_TABLE '''
    p [0] = p [2]


def p_INF_TB (p):
    ''' INF_TB : MO
        | T_GROUP
        | MO INF_TB
        | T_GROUP INF_TB '''
    if len (p) == 2 :
         p [0] = p(p[1],p[2])
    else:
         p [0] = p[1]

def p_T_GROUP (p):
    ''' T_GROUP : OPEN_T_GROUP GEN_TGROUP CLOSE_T_GROUP '''
    p [0] = p [2]


def p_GEN_TGROUP (p):
    ''' GEN_TGROUP : T_HEAD T_BODY 
        | T_FOOT T_BODY
        | T_BODY
        | T_HEAD T_FOOT T_BODY '''

def p_T_HEAD (p):
    ''' T_HEAD : OPEN_HEAD ROW CLOSE_HEAD '''
    p [0] = p [2]


def p_T_BODY (p):
    ''' T_BODY : OPEN_BODY ROW CLOSE_BODY '''
    p [0] = p [2]


def p_T_FOOT (p):
    ''' T_FOOT : OPEN_FOOT ROW CLOSE_FOOT '''
    p [0] = p [2]


def p_ROW (p):
    ''' ROW : OPEN_ROW ENTRY CLOSE_ROW ROW
        | OPEN_ROW ENTRY CLOSE_ROW
        | OPEN_ROW ENTRY_TB CLOSE_ROW
        | OPEN_ROW ENTRY_TB CLOSE_ROW ROW '''
    p [0] = p [2]

def p_ENTRY_TB (p):
    ''' ENTRY_TB : T_HEAD
        | T_BODY
        | T_HEAD T_BODY '''
    
    if len (p) ==2:
         p [0] =p(p[1],p[2])
    else:
        p[0] = p[1]

def p_ENTRY (p):
    ''' ENTRY : OPEN_ENTRY TEXTO CLOSE_ENTRY 
        | OPEN_ENTRY GEN_LIST CLOSE_ENTRY 
        | OPEN_ENTRY IMPORTANT CLOSE_ENTRY 
        | OPEN_ENTRY GEN_PARA CLOSE_ENTRY 
        | OPEN_ENTRY GEN_SIMP CLOSE_ENTRY
        | OPEN_ENTRY MO CLOSE_ENTRY
        | OPEN_ENTRY GEN_COM CLOSE_ENTRY
        | OPEN_ENTRY TEXTO CLOSE_ENTRY ENTRY
        | OPEN_ENTRY GEN_LIST CLOSE_ENTRY ENTRY
        | OPEN_ENTRY IMPORTANT CLOSE_ENTRY ENTRY
        | OPEN_ENTRY GEN_PARA CLOSE_ENTRY ENTRY
        | OPEN_ENTRY GEN_SIMP CLOSE_ENTRY ENTRY
        | OPEN_ENTRY MO CLOSE_ENTRY ENTRY
        | OPEN_ENTRY GEN_COM CLOSE_ENTRY ENTRY '''
    p [0] = p [2]




LEXER = lex.lex()  #armamos el lexer

#iterativo o archivo

time.sleep (1)
print ('Tipo de carga:')
print ('A) Interactiva')
print ('B) Carga por archivo')
print ('Si desea que se analice una archivo creado por el grupo elija cualquier opcion distinta de A o B')
time.sleep (1)
rta = (input ('Ingrese la opcion\n>'))
time.sleep (1)

if rta.upper() == "A":
      print ('Escriba su texto, recuerde que si pulsa el ENTER se da como finalizado el texto.')
      time.sleep (1)
      print ('Escriba su texto todo de seguido: ')
      info = input ()

elif rta.upper ()=="B":
      print ("Por favor, ingrese por teclado la dirección de la carpeta en donde se encuentran los archivos.xml")
      directorio = input() +'/'
      archivo = buscarFicheros(directorio)
      test = directorio+archivo
      fp = codecs.open(test,"r","utf-8")
      info = fp.read()
      fp.close()  
#else:# abrir archivos en .bin



parser = yacc.yacc()

result = parser.parse(info, lexer = LEXER)


if correcto ==0 :
    print ('Felicidades, su código es sintacticamente correcto')


input ("Presione enter para salir")

