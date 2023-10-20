import bcrypt

motdepasse = b's$cret12'

sel = 'ABCDEFG'
haché = bcrypt.hashpw (motdepasse, sel)
imprimer(haché)