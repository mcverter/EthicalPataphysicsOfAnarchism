files=( "abstract.html" "constellation.html" "doubling.html" "flat.html" "objective.html" "parallelism.html" "combination.html" "definition.html" "etymology.html" "intersection.html" "opposition.html" "two_dimensional.html")

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

PAGES_DIR=${SCRIPT_DIR}/../../word_analysis/templates/pages

for str in ${files[@]}; do
  echo ${str::-5}_pages.html
  touch ${PAGES_DIR}/${str::-5}_pages.html
done

echo $PAGES_DIR
pwd
ls