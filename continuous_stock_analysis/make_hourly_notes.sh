filename=$(date +"%Y_%m_%d_%I_%M_%p").txt
/home/saionee/opensource/stock-analysis/continuous_stock_analysis/venv/bin/python bse_scraper.py > "${filename}"
echo "`date` stock prices stores in ${filename}" >> bse_scraper.log
