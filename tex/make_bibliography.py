import os.path
import sys


def get_cit_keys(aux_file):
    if not os.path.isfile(aux_file):
        return []
        
    keys = []
    with open(aux_file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('\\citation'):
                key = (line.split('\citation')[1])[1:-1]
                if key not in keys:
                    keys.append(key)

    return keys


def get_doi(line):
    parts = line.split('http://')
    if len(parts) == 1:
        parts = line.split('https://')

    if len(parts) == 1:
        return None

    line = parts[1]
    if len(line) == 0:
        return None

    parts = line.split('}')
    if len(parts) == 1:
        return None

    return parts[0]


def get_cits(bib_file):
    if not os.path.isfile(bib_file):
        return []
        
    cits = dict()
    last_key = None
    dois = set()
    with open(bib_file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line and line[0] != '%':
                if line.startswith('\\bibitem'):
                    last_key = (line.split('\\bibitem')[1])[1:-1]
                elif last_key:
                    doi = get_doi(line)
                    if doi and doi in dois:
                        print('WARNING! Duplicated DOI', doi, f'(key:{last_key})')
                        sys.exit(1)
                    else:
                        dois.add(doi)

                    cits[last_key] = line
                    last_key = None

    return cits


def dump(keys, cits):
    print(r'{\hypersetup{colorlinks,breaklinks,urlcolor=[rgb]{0,0,0},linkcolor=[rgb]{0,0,0},citecolor=[rgb]{0,0,0}}')
    print('\\begin{thebibliography}{xxx}\n')
    for key in keys:
        print('\t\\bibitem{' + key + '}')
        print('\t' + cits[key])
        print('')
    print('\\end{thebibliography}}')


if __name__ == '__main__':
    keys = get_cit_keys('build/thesis.aux')
    cits = get_cits('bibliography_unsorted.tex')
    dump(keys, cits)
