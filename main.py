if __name__ == "__main__":
	try:
		__import__("azula").main()
	except Exception as e:
		exit(str(e))
