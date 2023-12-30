# Question Answering on Document Images

## Setting up the Project

1. Clone this repo:

   ```bash
   git clone https://github.com/jaimin001/question-answering-document-images
   ```

2. Make virtual environment:

   ```bash
   python3 -m venv venv
   ```

   Then install dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

3. Activate the virtual environment:

   For Linux/MacOS

   ```bash
   source venv/bin/activate
   ```

   For Windows:

   ```bash
   .\venv\Scripts\activate
   ```

4. Download the data through this:
   Go to https://rrc.cvc.uab.es/?ch=17
   and download all zip files of :

   Task 1 - Single Page Document Visual Question Answering

   - Annotations (questions, answers, question types...)
   - Images
   - OCR (Microsoft OCR)
   - IMDBs (processed dataset for MP-DocVQA framework)

   upzip them like in the next step mentioned.

   Download the layoutlm-base-uncased/ folder from https://huggingface.co/microsoft/layoutlm-base-uncased:

   - Either Clone the huggingface repository
   - Or download the files individually if facing any problem (select files -> click download individually for each file)

5. Put it in like this:

   ```
   data/
       layoutlm-base-uncased/
       spdocvqa_images/
       spdocvqa_imdb/
       spdocvqa_ocr/
       spdocvqa_qas/
       config.json
   env/
   models/
   README.md
   ans.json
   bounding_box.py
   create_dataset.py
   ...
   ```

6. Create dataset :

   please check python/python3 and change the file accordingly

   ```bash
   bash create_dataset_script.sh
   ```

7. Train the model:

   ```bash
   bash run.sh
   ```

## Test for custom image:

    - To use this codebase for custom images, we have used `tesseract` OCR tool.
    - Ensure the tesseract is installed in your system.
    - for more info, refer https://tesseract-ocr.github.io/tessdoc/
