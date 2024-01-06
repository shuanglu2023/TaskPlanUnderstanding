## Description
This is the repository for our paper *Extracting robotic task plan from natural language instruction using BERT and syntactic dependency parser*. 
We plan to add recent working updates after paper submission, which are under preparation. 
Please do not hesitate to reach out if you need more information.

The model is trained using (https://github.com/lavis-nlp/spert).
To reproduce the results, please download the annotated data and train it with SpERT.
The model trained with combined data with [hurm](https://github.com/personalrobotics/collaborative_manipulation_corpus), [huric](https://github.com/crux82/huric) and [semeval](https://github.com/heatherleaf/semeval-2014-task6) are reported in final_model.

You must also cite papers of these 3 datasets in any publications if you use the dataset and the final model (trained on 100K+ego).

## Usage
To annotate more data in SemEval Task 6 2014 dataset, the script annotate.py can be used. 
One should download the data from https://github.com/heatherleaf/semeval-2014-task6.git. 
The results of each sentence will be saved in to a folder with path "dataset/semeval/".

## Citation 
If this work is helpful in your research, please cite:
```
@INPROCEEDINGS{10309598,
  author={Lu, Shuang and Berger, Julia and Schilp, Johannes},
  booktitle={2023 32nd IEEE International Conference on Robot and Human Interactive Communication (RO-MAN)}, 
  title={Extracting robotic task plan from natural language instruction using BERT and syntactic dependency parser}, 
  year={2023},
  volume={},
  number={},
  pages={1794-1799},
  doi={10.1109/RO-MAN57019.2023.10309598}}
```

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

