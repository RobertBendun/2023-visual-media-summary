#!/usr/bin/env bash

if [ -z "$1" -o -z "$2" ]; then
	echo "usage: $(basename "$0") <imdb id> <stub>" 1>&2
	exit 1
fi

readonly ID="$1"
readonly STUB="$2"

if [ -z "$OMDB_KEY" ]; then
	echo "$(basename "$0"): OMDB_KEY variable is empty" 1>&2
	exit 1
fi

BASE_URL="http://www.omdbapi.com/?apikey=$OMDB_KEY&i="

curl -s "$(curl -s "$BASE_URL$ID" | jq -r '.Poster')" -o "$STUB.jpg"
