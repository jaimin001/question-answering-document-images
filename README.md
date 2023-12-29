# Question Answering on Document Images

## Setting up the Project

1. Clone this repo:
    ```bash
    git clone <>
    ```

2. Make virtual environment:
    
    ** check if you alias as python3/python **

    ```bash
    python/python3 -m venv venv
    ```

    Then install dependencies:

    ```bash
    pip/pip3 install -r requirements.txt
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

