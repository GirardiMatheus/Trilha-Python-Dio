.PHONY: run

run:
	@uvicorn workoutapi.main:app --reload