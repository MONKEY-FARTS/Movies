html = '<ol id="lista-peliculas">\n'

for i in range(1, 26):
    html += f'''
                <li>
                    <div class="general">
                        <div class="contenido">
                            <div class="imagen" id="imagen{i}"></div>
                            <div class="descripcion" id="descripcion{i}">
                            <i class="fa-solid fa-star-sharp star"></i>
                            </div>
                        </div>
                    </div>
                </li>
    '''

html += '</ol>'

print(html)
