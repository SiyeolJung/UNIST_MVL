def sort_text_file(filename):
    # 파일을 읽어서 lines 리스트에 저장합니다.
    with open(filename, 'r') as file:
        lines = file.readlines()

    # 각 줄을 (앞 숫자, 뒷 숫자, 원래 문장) 형태로 저장하는 리스트를 생성합니다.
    entries = []
    for line in lines:
        parts = line.strip().split('_')
        front_number = int(parts[0])
        rest = '_'.join(parts[1:])
        entries.append((front_number, int(parts[1]), line))

    # 앞 숫자를 기준으로 오름차순으로 정렬하고, 같은 앞 숫자 경우에는 뒷 숫자를 기준으로 오름차순으로 정렬합니다.
    sorted_entries = sorted(entries, key=lambda x: (x[0], x[1]))

    # 정렬된 결과를 파일에 씁니다.
    with open(filename, 'w') as file:
        for entry in sorted_entries:
            file.write(entry[2])

sort_text_file('data_test5.txt')
