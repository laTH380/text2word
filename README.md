# text2word_by_LLM
LLMを用いてテキストを特定の指示に従い単語レベルに分解し取得するプログラム

## ollama
ollamaでLLMを動かしていることを前提としている
インストール参考：https://zenn.dev/fp16/articles/e8c61e2f62e6b6
ollama serve
curl -X POST http://localhost:11434/api/generate -d '{ "model": "llama3.1", "prompt":"あなたの考えを教えてください", "stream":false }'