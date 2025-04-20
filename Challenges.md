## Challenge 1: Uploading a 50MB Dataset to GitHub

**Problem:**

While working on the Kaggle Pandas course, I encountered a challenge when attempting to upload a large dataset file, `winemag-data-130k-v2.csv` (approximately 50MB), to my GitHub repository. GitHub’s web interface limits direct file uploads to 25MB, and it typically rejects files larger than 100MB. Since my dataset was neither small enough to upload through the web interface nor large enough to require Git Large File Storage (LFS), I had to find an alternative solution to upload it.

**Solution:**

To solve this problem, I used Git through the terminal for manual uploading. Git allows for better handling of larger files, and this method ensures that files up to 100MB are uploaded without issue.

Here are the steps I followed:

1. **Cloning the Repository:**
   - First, I cloned the `Pandas` repository from GitHub to my local machine.
   ```bash
   git clone https://github.com/AhmadTigress/Pandas.git
   cd Pandas

2. **Moving the Dataset:**

   - I moved the `winemag-data-130k-v2.csv` file from my local `Downloads` folder into the repository’s local directory, specifically into the `datasets/` folder to keep the project organized.

3. **Staging the File:**

   - Using Git, I staged the large CSV file for commit.
   ```bash
   git add datasets/winemag-data-130k-v2.csv

   4. **Committing the Changes:**

      - I created a commit with a relevant message to track the dataset upload.
      ```bash
   git commit -m "Added 50MB wine reviews dataset (winemag-data-130k-v2.csv)"
