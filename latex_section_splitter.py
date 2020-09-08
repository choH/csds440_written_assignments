import itertools
import re
import os
import subprocess
import shutil

assignment_number = '4'
input_filename = 'assignment_'+ assignment_number + '/article.tex'
starting_q_num = 10
output_dir = 'assignment_' + assignment_number + '/split_by_question/'

splitted_file_list = []
section_line_num = []

with open(input_filename) as input_file:
    line_counter = 0
    for i in input_file:
        if re.search(r"^\\section", i) or re.search(r"^% \\section", i):
            print(i, line_counter)
            section_line_num.extend([line_counter-1, line_counter])
        line_counter += 1


section_line_num.pop(0)
section_line_num.append(line_counter)


section_line_num = list(zip(*[iter(section_line_num)]*2))
section_line_num.insert(0, (0, section_line_num[0][0] - 1))
print(section_line_num)


content = []
with open(input_filename) as input_file:
    all_lines = input_file.readlines()

    for i, j in section_line_num:
        content.append(all_lines[i:j+1])

header = content.pop(0)
footer = content.pop()

file_nums = list(range(starting_q_num, starting_q_num+len(content)))
tex_file_names = ["".join(["article_", str(i), ".tex"]) for i in file_nums]
pdf_file_names = ["".join(["article_", str(i), ".pdf"]) for i in file_nums]
section_index_list = list(range(len(content)))




if not os.path.exists(output_dir):
    os.mkdir(output_dir)



for a_file, section_index in zip(tex_file_names, section_index_list):
    with open(output_dir+a_file, 'a') as f:
        lines_to_write = header + content[section_index] + footer
        for line in lines_to_write:
            f.write(f"{line}")

for tex_file, pdf_file in zip(tex_file_names, pdf_file_names):
    tex_file_w_path = output_dir + tex_file
    subprocess.call(["pdflatex", "-cd -e -f -pdf -interaction=nonstopmode -synctex=1", tex_file_w_path])
    subprocess.call(["pdflatex", "-cd -e -f -pdf -interaction=nonstopmode -synctex=1", tex_file_w_path])
    # shutil.move(pdf_file, output_dir)
    shutil.move(os.path.join('./', pdf_file), os.path.join(output_dir, pdf_file))

files_in_workspace = os.listdir('./')
for file in files_in_workspace:
    if file.endswith(".out") or file.endswith(".aux") or file.endswith(".log"):
        os.remove(os.path.join('./', file))

files_in_output_dir = os.listdir(output_dir)
for file in files_in_output_dir:
    if file.endswith(".tex"):
        os.remove(os.path.join(output_dir, file))