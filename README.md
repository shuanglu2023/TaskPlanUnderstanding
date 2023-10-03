## Description
The model is trained using (https://github.com/lavis-nlp/spert).
To reproduce the results, please download the annotated data and train it with SpERT.
The final model trained with combined data with hurm, huric and semeval are reported in [final_model].

## Usage
To annotate more data in SemEval Task 6 2014 dataset, the script annotate.py can be used. 
One should download the data from https://github.com/heatherleaf/semeval-2014-task6.git. 
The results of each sentence will be saved in to a folder with path "dataset/semeval/".

## References
<a id="1">[1]</a> 
A. Vanzo, D. Croce, E. Bastianelli, R. Basili, and D. Nardi,
“Grounded language interpretation of robotic commands through
structured learning,” Artificial Intelligence, vol. 278, 2020.

<a id="2">[2]</a> 
K. Dukes, “SemEval-2014 task 6: Supervised semantic parsing of
robotic spatial commands,” in Proceedings of the 8th International
Workshop on Semantic Evaluation (SemEval 2014). Dublin, Ireland: Association for Computational Linguistics, Aug. 2014, pp. 45–53.

<a id="3">[3]</a> 
R. Scalise, S. Li, H. Admoni, S. Rosenthal, and S. S. Srinivasa, “Natural
language instructions for human–robot collaborative manipulation,”
The International Journal of Robotics Research, vol. 37, no. 6, pp.
558–565, 2018.

<a id="4">[4]</a> 
Markus Eberts, Adrian Ulges. Span-based Joint Entity and Relation Extraction with Transformer Pre-training. 24th European Conference on Artificial Intelligence, 2020.
## Authors and acknowledgment
This research was conducted within the project MeMoRob (AKZ: DIK0358/01) funded by the Bavarian Ministry
of Economic Affairs, Regional Development and Energy
(StMWi). The authors would like to thank the StMWi for
their financial support.

## License
Apache-2.0 license

