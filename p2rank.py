import pandas as pd
import subprocess
import os

prank_path = '/Users/baderal-hamdan/Desktop/SBI Assignment/p2rank_2.4.1/prank'
output_dir = 'data/output'

os.makedirs(output_dir, exist_ok=True)
results = []

for i in range(0, 3064):
    pdb_file = f'{i}_protein.pdb'
    output_file = f'{pdb_file}_predictions.csv'
    input_file = os.path.join('data/test', pdb_file)

    subprocess.run([ 
            prank_path,
            'predict',
            '-f',
            input_file,
            '-o',
            output_dir
        ], 
        capture_output=True
    )

    df = pd.read_csv(f'{output_dir}/{output_file}')

    residue_ids = df.loc[0, ' residue_ids'] if not df.empty and ' residue_ids' in df.columns else ""

    results.append({'id': i, 'prediction': residue_ids})
    print(f"Processed file {output_file}")

result_df = pd.DataFrame(results)
result_df.to_csv(f'submission.csv', index=False)
