mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"wehr.markus@web.de\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml