# exp_no-7-practical

✅ 1. train.py (fixed indentation + profiling)
✅ 2. requirements.txt
Make sure the file is named exactly requirements.txt (not requirement.txt).
✅ 3. .github/workflows/train.yaml

This workflow:

Runs on every push to main

Sets up Python

Installs dependencies

Runs your training script with profiling

Uploads both model and profile as GitHub artifacts
✅ 4. Project Structure Example

Your repository should look like this:

📦 your-repo/
 ┣ 📜 train.py
 ┣ 📜 requirements.txt
 ┗ 📂 .github/
     ┗ 📂 workflows/
         ┗ 📜 train.yaml

✅ 5. What Happens When You Push

You commit and push to main.

GitHub Actions automatically:

Sets up Python

Installs scikit-learn

Runs train.py

Saves the model and profiling output

Uploads them to Actions → Artifacts.

After the run completes:

Go to GitHub → Actions → Latest Run → Artifacts

Download trained-model.zip
