python3 run_docvqa.py \
	--data_dir /data/spdocvqa_images \
	--model_type layoutlm \
	--model_name_or_path ./data/layoutlm-base-uncased \
	--max_seq_length 512 \
	--do_train \
	--num_train_epochs 15 \
	--logging_steps 500 \
	--evaluate_during_training \
	--save_steps 500 \
	--do_eval \
	--output_dir ./data/output/ \
	--per_gpu_train_batch_size 8 \
	--overwrite_output_dir \
	--cache_dir ./models \
	--skip_match_answers \
	--val_json ./val_out.json \
	--train_json ./train_out.json

