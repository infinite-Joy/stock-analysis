while true; do
	filename=$(date +"%Y_%m_%d_%I_%M_%p").txt
	python bse_scraper.py > "${filename}"
	sleep 1h
done
