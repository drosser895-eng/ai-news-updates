#!/bin/bash

echo -e "\033[1;33mStarting AI News Updates Deployment\033[0m"

# Create build directory
mkdir -p _build

echo -e "\033[0;32mGenerating initial AI news content...\033[0m"
python3 content_generator.py

# Set up daily cron job for fresh content
crontab -l 2>/dev/null | grep -v "ai-news-updates" | crontab -
(crontab -l 2>/dev/null; echo "0 7 * * * cd /Users/davidrosser/clawd/ai-news-updates && python3 content_generator.py && npx --yes gh-pages -d _build -b gh-pages -m \"daily AI news update\"") | crontab -

echo -e "\033[0;32mCron job set up for daily AI news updates at 7 AM\033[0m"

echo -e "\033[0;32mDeployment complete!\033[0m"
echo -e "\033[1;33mNext steps:\033[0m"
echo "1. Customize the site name and identity in the templates"
echo "2. Add your Google Analytics ID (replace G-AINEWS123)"
echo "3. Add your affiliate program IDs"
echo "4. Deploy the contents of /Users/davidrosser/clawd/ai-news-updates/_build to your web server"
echo "5. Verify your domain with Google Search Console"