import sys
import csv
import os

def parse_markdown(filename):
    with open(filename, 'r', encoding='utf8') as f:
        lines = f.readlines()
    
    normal_cards = []
    cloze_cards = []
    image_cards = []
    
    current_question = None
    current_answers = []
    has_cloze = False
    has_image = False

    for line in lines:
        stripped_line = line.rstrip("\n")
        
        if not stripped_line.strip():
            continue  # Skip blank lines
        
        # New flashcard starts on a non-indented line
        if not stripped_line.startswith(" ") and not stripped_line.startswith("\t"):
            if current_question is not None:
                if has_cloze:
                    cloze_cards.append((current_question, current_answers))
                elif has_image:
                    image_cards.append((current_question, current_answers))
                else:
                    normal_cards.append((current_question, current_answers))
            
            current_question = stripped_line
            current_answers = []
            has_cloze = ("{{c" in current_question)
            has_image = ("![[" in current_question)
        else:
            current_answers.append(stripped_line)
            if "{{c" in stripped_line:
                has_cloze = True
            if "![[" in stripped_line:
                has_image = True

    if current_question is not None:
        if has_cloze:
            cloze_cards.append((current_question, current_answers))
        elif has_image:
            image_cards.append((current_question, current_answers))
        else:
            normal_cards.append((current_question, current_answers))
    
    return normal_cards, cloze_cards, image_cards

def write_csv(cards, output_filename):
    with open(output_filename, 'w', newline='', encoding='utf8') as csvfile:
        writer = csv.writer(csvfile)
        for question, answers in cards:
            answer_text = "\n".join(answers)
            writer.writerow([question, answer_text])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py input.md")
        sys.exit(1)
    
    input_md = sys.argv[1]
    base_name = os.path.splitext(input_md)[0]  # Removes ".md" extension

    normal_csv = f"{base_name}.csv"
    cloze_csv = f"{base_name}_cloze.csv"
    
    normal_cards, cloze_cards, image_cards = parse_markdown(input_md)
    
    write_csv(normal_cards, normal_csv)
    write_csv(cloze_cards, cloze_csv)
    
    print(f"Successfully processed flashcards from {input_md}:")
    print(f" - {len(normal_cards)} normal flashcards written to {normal_csv}")
    print(f" - {len(cloze_cards)} cloze deletion flashcards written to {cloze_csv}")

    if image_cards:
        print("\nThe following flashcards contain images and were omitted from the CSVs (please handle manually):")
        for question, answers in image_cards:
            print("Question:", question)
            if answers:
                print("Answers:")
                for ans in answers:
                    print(ans)
            print("---")
