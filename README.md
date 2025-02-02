![Benchmark Image](ressources/readme/benchmark_img.png)

# Multimodal Large Language Model (MLLM) Benchmark

This repository houses an evaluation of seven leading MLLMs across nine datasets testing various cognitive capabilities underpinning language generation tasks.

## Benchmark Overview

FLUFFY stands as a comprehensive benchmark encompassing over 30,000 instances across nine datasets in visual question answering & reasoning, knowledgeable visual question answering, and classification. It distinguishes itself by offering in-depth insights into the architecture and training data of MLLMs, coupled with both quantitative performance assessments and qualitative analyses. Our evaluation also introduces post-processing tolerance to address observed limitations in instruction-following capabilities.

## Key Findings

- **Top Performers:** BLIP-2, InstructBlip, and LLaVA emerged as the leading models in our benchmark.
- **Variability in Instruction-Following:** Models showed considerable variation in their ability to follow instructions, with all facing challenges to some extent. BLIP models could follow instructions best.
- **Logical Reasoning:** LLaVA distinguished itself with the production of advanced chains of thought (even though being prompted to not do so), which coincided with advanced reasoning capabilities.
- **Visual Feature Extraction:** BLIP models use a light-weight transformer with cross-attention to bridge the vision and language module. We hypothesize that the cross-attention allows for goal-oriented visual feature extraction, which boosts the overall MLLM performance.
- **Language Encoder:** LLaVA's success is further hypothesized to be supported by the advanced language model LLaMA-2 Chat.

## Future Directions

- Additionally adopting few-shot prompting.
- Integrating tasks that necessitate longer responses and add automatic scoring systems for the evaluation of those tasks.
- Prompting models to generate intuitive textual responses instead of indices in tasks such as multiple-choice tasks.
- Adopting experimental setups to isolate performance drivers.

## Results

The table below shows the results when applying post-processing tolerance. Further performance assessment and discussion can be found in [report.pdf](report.pdf).

### Metrics - Evaluation with Post-Processing Tolerance


<table id="T_ed29c">
<thead>
<tr>
<th class="index_name level0">Dataset</th>
<th class="col_heading level0 col0" colspan="2" id="T_ed29c_level0_col0" style="border-bottom: 1px solid black;">aokvqa</th>
<th class="col_heading level0 col2" id="T_ed29c_level0_col2" style="border-bottom: 1px solid black;">clevr</th>
<th class="col_heading level0 col3" colspan="4" id="T_ed29c_level0_col3" style="border-bottom: 1px solid black;">esnlive</th>
<th class="col_heading level0 col7" id="T_ed29c_level0_col7" style="border-bottom: 1px solid black;">gqa</th>
<th class="col_heading level0 col8" colspan="4" id="T_ed29c_level0_col8" style="border-bottom: 1px solid black;">hateful_memes</th>
<th class="col_heading level0 col12" colspan="4" id="T_ed29c_level0_col12" style="border-bottom: 1px solid black;">mami</th>
<th class="col_heading level0 col16" colspan="4" id="T_ed29c_level0_col16" style="border-bottom: 1px solid black;">mvsa</th>
<th class="col_heading level0 col20" id="T_ed29c_level0_col20" style="border-bottom: 1px solid black;">okvqa</th>
<th class="col_heading level0 col21" id="T_ed29c_level0_col21" style="border-bottom: 1px solid black;">scienceqa</th>
<th class="col_heading level0 col22" id="T_ed29c_level0_col22" style="border-bottom: 1px solid black;">Average Accuracy</th>
</tr>
<tr>
<th class="index_name level1">Task</th>
<th class="col_heading level1 col0" id="T_ed29c_level1_col0">direct answer (aokvqa)</th>
<th class="col_heading level1 col1" id="T_ed29c_level1_col1">multiple choice (aokvqa)</th>
<th class="col_heading level1 col2" id="T_ed29c_level1_col2">direct answer (clevr)</th>
<th class="col_heading level1 col3" colspan="4" id="T_ed29c_level1_col3">entailment prediction</th>
<th class="col_heading level1 col7" id="T_ed29c_level1_col7">direct answer (gqa)</th>
<th class="col_heading level1 col8" colspan="4" id="T_ed29c_level1_col8">hate classification</th>
<th class="col_heading level1 col12" colspan="4" id="T_ed29c_level1_col12">sexism classification</th>
<th class="col_heading level1 col16" colspan="4" id="T_ed29c_level1_col16">sentiment analysis</th>
<th class="col_heading level1 col20" id="T_ed29c_level1_col20">direct answer (okvqa)</th>
<th class="col_heading level1 col21" id="T_ed29c_level1_col21">multiple choice (sqa)</th>
<th class="col_heading level1 col22" id="T_ed29c_level1_col22"></th>
</tr>
<tr>
<th class="index_name level2">Metric</th>
<th class="col_heading level2 col0" id="T_ed29c_level2_col0">accuracy</th>
<th class="col_heading level2 col1" id="T_ed29c_level2_col1">accuracy</th>
<th class="col_heading level2 col2" id="T_ed29c_level2_col2">accuracy</th>
<th class="col_heading level2 col3" id="T_ed29c_level2_col3">accuracy</th>
<th class="col_heading level2 col4" id="T_ed29c_level2_col4">f1</th>
<th class="col_heading level2 col5" id="T_ed29c_level2_col5">precision</th>
<th class="col_heading level2 col6" id="T_ed29c_level2_col6">recall</th>
<th class="col_heading level2 col7" id="T_ed29c_level2_col7">accuracy</th>
<th class="col_heading level2 col8" id="T_ed29c_level2_col8">accuracy</th>
<th class="col_heading level2 col9" id="T_ed29c_level2_col9">f1</th>
<th class="col_heading level2 col10" id="T_ed29c_level2_col10">precision</th>
<th class="col_heading level2 col11" id="T_ed29c_level2_col11">recall</th>
<th class="col_heading level2 col12" id="T_ed29c_level2_col12">accuracy</th>
<th class="col_heading level2 col13" id="T_ed29c_level2_col13">f1</th>
<th class="col_heading level2 col14" id="T_ed29c_level2_col14">precision</th>
<th class="col_heading level2 col15" id="T_ed29c_level2_col15">recall</th>
<th class="col_heading level2 col16" id="T_ed29c_level2_col16">accuracy</th>
<th class="col_heading level2 col17" id="T_ed29c_level2_col17">f1</th>
<th class="col_heading level2 col18" id="T_ed29c_level2_col18">precision</th>
<th class="col_heading level2 col19" id="T_ed29c_level2_col19">recall</th>
<th class="col_heading level2 col20" id="T_ed29c_level2_col20">accuracy</th>
<th class="col_heading level2 col21" id="T_ed29c_level2_col21">accuracy</th>
<th class="col_heading level2 col22" id="T_ed29c_level2_col22"></th>
</tr>
<tr>
<th class="index_name level0"></th>
<th class="blank col0"> </th>
<th class="blank col1"> </th>
<th class="blank col2"> </th>
<th class="blank col3"> </th>
<th class="blank col4"> </th>
<th class="blank col5"> </th>
<th class="blank col6"> </th>
<th class="blank col7"> </th>
<th class="blank col8"> </th>
<th class="blank col9"> </th>
<th class="blank col10"> </th>
<th class="blank col11"> </th>
<th class="blank col12"> </th>
<th class="blank col13"> </th>
<th class="blank col14"> </th>
<th class="blank col15"> </th>
<th class="blank col16"> </th>
<th class="blank col17"> </th>
<th class="blank col18"> </th>
<th class="blank col19"> </th>
<th class="blank col20"> </th>
<th class="blank col21"> </th>
<th class="blank col22"> </th>
</tr>
</thead>
<tbody>
<tr>
<th class="row_heading level0 row0" id="T_ed29c_level0_row0">instructblip</th>
<td class="data row0 col0" id="T_ed29c_row0_col0">0.55</td>
<td class="data row0 col1" id="T_ed29c_row0_col1">0.74</td>
<td class="data row0 col2" id="T_ed29c_row0_col2">0.34</td>
<td class="data row0 col3" id="T_ed29c_row0_col3">0.63</td>
<td class="data row0 col4" id="T_ed29c_row0_col4">0.64</td>
<td class="data row0 col5" id="T_ed29c_row0_col5">0.75</td>
<td class="data row0 col6" id="T_ed29c_row0_col6">0.63</td>
<td class="data row0 col7" id="T_ed29c_row0_col7">0.50</td>
<td class="data row0 col8" id="T_ed29c_row0_col8">0.58</td>
<td class="data row0 col9" id="T_ed29c_row0_col9">0.49</td>
<td class="data row0 col10" id="T_ed29c_row0_col10">0.63</td>
<td class="data row0 col11" id="T_ed29c_row0_col11">0.40</td>
<td class="data row0 col12" id="T_ed29c_row0_col12">0.56</td>
<td class="data row0 col13" id="T_ed29c_row0_col13">0.57</td>
<td class="data row0 col14" id="T_ed29c_row0_col14">0.54</td>
<td class="data row0 col15" id="T_ed29c_row0_col15">0.61</td>
<td class="data row0 col16" id="T_ed29c_row0_col16">0.68</td>
<td class="data row0 col17" id="T_ed29c_row0_col17">0.67</td>
<td class="data row0 col18" id="T_ed29c_row0_col18">0.67</td>
<td class="data row0 col19" id="T_ed29c_row0_col19">0.68</td>
<td class="data row0 col20" id="T_ed29c_row0_col20">0.52</td>
<td class="data row0 col21" id="T_ed29c_row0_col21">0.49</td>
<td class="data row0 col22" id="T_ed29c_row0_col22">0.55</td>
</tr>
<tr>
<th class="row_heading level0 row1" id="T_ed29c_level0_row1">llava</th>
<td class="data row1 col0" id="T_ed29c_row1_col0">0.60</td>
<td class="data row1 col1" id="T_ed29c_row1_col1">0.62</td>
<td class="data row1 col2" id="T_ed29c_row1_col2">0.33</td>
<td class="data row1 col3" id="T_ed29c_row1_col3">0.50</td>
<td class="data row1 col4" id="T_ed29c_row1_col4">0.46</td>
<td class="data row1 col5" id="T_ed29c_row1_col5">0.65</td>
<td class="data row1 col6" id="T_ed29c_row1_col6">0.50</td>
<td class="data row1 col7" id="T_ed29c_row1_col7">0.51</td>
<td class="data row1 col8" id="T_ed29c_row1_col8">0.63</td>
<td class="data row1 col9" id="T_ed29c_row1_col9">0.77</td>
<td class="data row1 col10" id="T_ed29c_row1_col10">0.63</td>
<td class="data row1 col11" id="T_ed29c_row1_col11">1.00</td>
<td class="data row1 col12" id="T_ed29c_row1_col12">0.68</td>
<td class="data row1 col13" id="T_ed29c_row1_col13">0.81</td>
<td class="data row1 col14" id="T_ed29c_row1_col14">0.68</td>
<td class="data row1 col15" id="T_ed29c_row1_col15">1.00</td>
<td class="data row1 col16" id="T_ed29c_row1_col16">0.68</td>
<td class="data row1 col17" id="T_ed29c_row1_col17">0.67</td>
<td class="data row1 col18" id="T_ed29c_row1_col18">0.66</td>
<td class="data row1 col19" id="T_ed29c_row1_col19">0.68</td>
<td class="data row1 col20" id="T_ed29c_row1_col20">0.58</td>
<td class="data row1 col21" id="T_ed29c_row1_col21">0.37</td>
<td class="data row1 col22" id="T_ed29c_row1_col22">0.54</td>
</tr>
<tr>
<th class="row_heading level0 row2" id="T_ed29c_level0_row2">blip2</th>
<td class="data row2 col0" id="T_ed29c_row2_col0">0.44</td>
<td class="data row2 col1" id="T_ed29c_row2_col1">0.69</td>
<td class="data row2 col2" id="T_ed29c_row2_col2">0.28</td>
<td class="data row2 col3" id="T_ed29c_row2_col3">0.54</td>
<td class="data row2 col4" id="T_ed29c_row2_col4">0.51</td>
<td class="data row2 col5" id="T_ed29c_row2_col5">0.72</td>
<td class="data row2 col6" id="T_ed29c_row2_col6">0.54</td>
<td class="data row2 col7" id="T_ed29c_row2_col7">0.33</td>
<td class="data row2 col8" id="T_ed29c_row2_col8">0.61</td>
<td class="data row2 col9" id="T_ed29c_row2_col9">0.61</td>
<td class="data row2 col10" id="T_ed29c_row2_col10">0.60</td>
<td class="data row2 col11" id="T_ed29c_row2_col11">0.61</td>
<td class="data row2 col12" id="T_ed29c_row2_col12">0.52</td>
<td class="data row2 col13" id="T_ed29c_row2_col13">0.67</td>
<td class="data row2 col14" id="T_ed29c_row2_col14">0.51</td>
<td class="data row2 col15" id="T_ed29c_row2_col15">0.99</td>
<td class="data row2 col16" id="T_ed29c_row2_col16">0.68</td>
<td class="data row2 col17" id="T_ed29c_row2_col17">0.68</td>
<td class="data row2 col18" id="T_ed29c_row2_col18">0.68</td>
<td class="data row2 col19" id="T_ed29c_row2_col19">0.68</td>
<td class="data row2 col20" id="T_ed29c_row2_col20">0.35</td>
<td class="data row2 col21" id="T_ed29c_row2_col21">0.37</td>
<td class="data row2 col22" id="T_ed29c_row2_col22">0.47</td>
</tr>
<tr>
<th class="row_heading level0 row3" id="T_ed29c_level0_row3">adept</th>
<td class="data row3 col0" id="T_ed29c_row3_col0">0.50</td>
<td class="data row3 col1" id="T_ed29c_row3_col1">0.37</td>
<td class="data row3 col2" id="T_ed29c_row3_col2">0.34</td>
<td class="data row3 col3" id="T_ed29c_row3_col3">0.33</td>
<td class="data row3 col4" id="T_ed29c_row3_col4">0.25</td>
<td class="data row3 col5" id="T_ed29c_row3_col5">0.61</td>
<td class="data row3 col6" id="T_ed29c_row3_col6">0.33</td>
<td class="data row3 col7" id="T_ed29c_row3_col7">0.44</td>
<td class="data row3 col8" id="T_ed29c_row3_col8">0.55</td>
<td class="data row3 col9" id="T_ed29c_row3_col9">0.63</td>
<td class="data row3 col10" id="T_ed29c_row3_col10">0.60</td>
<td class="data row3 col11" id="T_ed29c_row3_col11">0.67</td>
<td class="data row3 col12" id="T_ed29c_row3_col12">0.53</td>
<td class="data row3 col13" id="T_ed29c_row3_col13">0.64</td>
<td class="data row3 col14" id="T_ed29c_row3_col14">0.55</td>
<td class="data row3 col15" id="T_ed29c_row3_col15">0.75</td>
<td class="data row3 col16" id="T_ed29c_row3_col16">0.59</td>
<td class="data row3 col17" id="T_ed29c_row3_col17">0.54</td>
<td class="data row3 col18" id="T_ed29c_row3_col18">0.58</td>
<td class="data row3 col19" id="T_ed29c_row3_col19">0.59</td>
<td class="data row3 col20" id="T_ed29c_row3_col20">0.48</td>
<td class="data row3 col21" id="T_ed29c_row3_col21">0.32</td>
<td class="data row3 col22" id="T_ed29c_row3_col22">0.44</td>
</tr>
<tr>
<th class="row_heading level0 row4" id="T_ed29c_level0_row4">otter</th>
<td class="data row4 col0" id="T_ed29c_row4_col0">0.37</td>
<td class="data row4 col1" id="T_ed29c_row4_col1">0.45</td>
<td class="data row4 col2" id="T_ed29c_row4_col2">0.23</td>
<td class="data row4 col3" id="T_ed29c_row4_col3">0.38</td>
<td class="data row4 col4" id="T_ed29c_row4_col4">0.32</td>
<td class="data row4 col5" id="T_ed29c_row4_col5">0.42</td>
<td class="data row4 col6" id="T_ed29c_row4_col6">0.38</td>
<td class="data row4 col7" id="T_ed29c_row4_col7">0.38</td>
<td class="data row4 col8" id="T_ed29c_row4_col8">0.51</td>
<td class="data row4 col9" id="T_ed29c_row4_col9">0.19</td>
<td class="data row4 col10" id="T_ed29c_row4_col10">0.54</td>
<td class="data row4 col11" id="T_ed29c_row4_col11">0.11</td>
<td class="data row4 col12" id="T_ed29c_row4_col12">0.57</td>
<td class="data row4 col13" id="T_ed29c_row4_col13">0.43</td>
<td class="data row4 col14" id="T_ed29c_row4_col14">0.65</td>
<td class="data row4 col15" id="T_ed29c_row4_col15">0.32</td>
<td class="data row4 col16" id="T_ed29c_row4_col16">0.59</td>
<td class="data row4 col17" id="T_ed29c_row4_col17">0.60</td>
<td class="data row4 col18" id="T_ed29c_row4_col18">0.65</td>
<td class="data row4 col19" id="T_ed29c_row4_col19">0.59</td>
<td class="data row4 col20" id="T_ed29c_row4_col20">0.42</td>
<td class="data row4 col21" id="T_ed29c_row4_col21">0.39</td>
<td class="data row4 col22" id="T_ed29c_row4_col22">0.43</td>
</tr>
<tr>
<th class="row_heading level0 row5" id="T_ed29c_level0_row5">openflamingo</th>
<td class="data row5 col0" id="T_ed29c_row5_col0">0.37</td>
<td class="data row5 col1" id="T_ed29c_row5_col1">0.24</td>
<td class="data row5 col2" id="T_ed29c_row5_col2">0.22</td>
<td class="data row5 col3" id="T_ed29c_row5_col3">0.38</td>
<td class="data row5 col4" id="T_ed29c_row5_col4">0.32</td>
<td class="data row5 col5" id="T_ed29c_row5_col5">0.38</td>
<td class="data row5 col6" id="T_ed29c_row5_col6">0.38</td>
<td class="data row5 col7" id="T_ed29c_row5_col7">0.34</td>
<td class="data row5 col8" id="T_ed29c_row5_col8">0.46</td>
<td class="data row5 col9" id="T_ed29c_row5_col9">0.49</td>
<td class="data row5 col10" id="T_ed29c_row5_col10">0.47</td>
<td class="data row5 col11" id="T_ed29c_row5_col11">0.50</td>
<td class="data row5 col12" id="T_ed29c_row5_col12">0.50</td>
<td class="data row5 col13" id="T_ed29c_row5_col13">0.20</td>
<td class="data row5 col14" id="T_ed29c_row5_col14">0.57</td>
<td class="data row5 col15" id="T_ed29c_row5_col15">0.12</td>
<td class="data row5 col16" id="T_ed29c_row5_col16">0.57</td>
<td class="data row5 col17" id="T_ed29c_row5_col17">0.42</td>
<td class="data row5 col18" id="T_ed29c_row5_col18">0.66</td>
<td class="data row5 col19" id="T_ed29c_row5_col19">0.57</td>
<td class="data row5 col20" id="T_ed29c_row5_col20">0.38</td>
<td class="data row5 col21" id="T_ed29c_row5_col21">0.38</td>
<td class="data row5 col22" id="T_ed29c_row5_col22">0.39</td>
</tr>
<tr>
<th class="row_heading level0 row6" id="T_ed29c_level0_row6">idefics</th>
<td class="data row6 col0" id="T_ed29c_row6_col0">0.17</td>
<td class="data row6 col1" id="T_ed29c_row6_col1">0.30</td>
<td class="data row6 col2" id="T_ed29c_row6_col2">0.38</td>
<td class="data row6 col3" id="T_ed29c_row6_col3">0.42</td>
<td class="data row6 col4" id="T_ed29c_row6_col4">0.32</td>
<td class="data row6 col5" id="T_ed29c_row6_col5">0.38</td>
<td class="data row6 col6" id="T_ed29c_row6_col6">0.42</td>
<td class="data row6 col7" id="T_ed29c_row6_col7">0.34</td>
<td class="data row6 col8" id="T_ed29c_row6_col8">0.50</td>
<td class="data row6 col9" id="T_ed29c_row6_col9">0.67</td>
<td class="data row6 col10" id="T_ed29c_row6_col10">0.50</td>
<td class="data row6 col11" id="T_ed29c_row6_col11">1.00</td>
<td class="data row6 col12" id="T_ed29c_row6_col12">0.52</td>
<td class="data row6 col13" id="T_ed29c_row6_col13">0.34</td>
<td class="data row6 col14" id="T_ed29c_row6_col14">0.54</td>
<td class="data row6 col15" id="T_ed29c_row6_col15">0.24</td>
<td class="data row6 col16" id="T_ed29c_row6_col16">0.17</td>
<td class="data row6 col17" id="T_ed29c_row6_col17">0.14</td>
<td class="data row6 col18" id="T_ed29c_row6_col18">0.73</td>
<td class="data row6 col19" id="T_ed29c_row6_col19">0.17</td>
<td class="data row6 col20" id="T_ed29c_row6_col20">0.20</td>
<td class="data row6 col21" id="T_ed29c_row6_col21">0.32</td>
<td class="data row6 col22" id="T_ed29c_row6_col22">0.34</td>
</tr>
</tbody>
</table>


### Valid Answer Ratio - Evaluation with Post-Processing Tolerance


<table id="T_3be67">
<thead>
<tr>
<th class="index_name level0">Dataset</th>
<th class="col_heading level0 col0" colspan="2" id="T_3be67_level0_col0" style="border-bottom: 1px solid black;">aokvqa</th>
<th class="col_heading level0 col2" id="T_3be67_level0_col2" style="border-bottom: 1px solid black;">clevr</th>
<th class="col_heading level0 col3" id="T_3be67_level0_col3" style="border-bottom: 1px solid black;">esnlive</th>
<th class="col_heading level0 col4" id="T_3be67_level0_col4" style="border-bottom: 1px solid black;">gqa</th>
<th class="col_heading level0 col5" id="T_3be67_level0_col5" style="border-bottom: 1px solid black;">hateful_memes</th>
<th class="col_heading level0 col6" id="T_3be67_level0_col6" style="border-bottom: 1px solid black;">mami</th>
<th class="col_heading level0 col7" id="T_3be67_level0_col7" style="border-bottom: 1px solid black;">mvsa</th>
<th class="col_heading level0 col8" id="T_3be67_level0_col8" style="border-bottom: 1px solid black;">okvqa</th>
<th class="col_heading level0 col9" id="T_3be67_level0_col9" style="border-bottom: 1px solid black;">scienceqa</th>
<th class="col_heading level0 col10" id="T_3be67_level0_col10" style="border-bottom: 1px solid black;">Average Ratio</th>
</tr>
<tr>
<th class="index_name level1">Task</th>
<th class="col_heading level1 col0" id="T_3be67_level1_col0">direct answer (aokvqa)</th>
<th class="col_heading level1 col1" id="T_3be67_level1_col1">multiple choice (aokvqa)</th>
<th class="col_heading level1 col2" id="T_3be67_level1_col2">direct answer (clevr)</th>
<th class="col_heading level1 col3" id="T_3be67_level1_col3">entailment prediction</th>
<th class="col_heading level1 col4" id="T_3be67_level1_col4">direct answer (gqa)</th>
<th class="col_heading level1 col5" id="T_3be67_level1_col5">hate classification</th>
<th class="col_heading level1 col6" id="T_3be67_level1_col6">sexism classification</th>
<th class="col_heading level1 col7" id="T_3be67_level1_col7">sentiment analysis</th>
<th class="col_heading level1 col8" id="T_3be67_level1_col8">direct answer (okvqa)</th>
<th class="col_heading level1 col9" id="T_3be67_level1_col9">multiple choice (sqa)</th>
<th class="col_heading level1 col10" id="T_3be67_level1_col10"></th>
</tr>
<tr>
<th class="index_name level0"></th>
<th class="blank col0"> </th>
<th class="blank col1"> </th>
<th class="blank col2"> </th>
<th class="blank col3"> </th>
<th class="blank col4"> </th>
<th class="blank col5"> </th>
<th class="blank col6"> </th>
<th class="blank col7"> </th>
<th class="blank col8"> </th>
<th class="blank col9"> </th>
<th class="blank col10"> </th>
</tr>
</thead>
<tbody>
<tr>
<th class="row_heading level0 row0" id="T_3be67_level0_row0">blip2</th>
<td class="data row0 col0" id="T_3be67_row0_col0">1.00</td>
<td class="data row0 col1" id="T_3be67_row0_col1">1.00</td>
<td class="data row0 col2" id="T_3be67_row0_col2">1.00</td>
<td class="data row0 col3" id="T_3be67_row0_col3">1.00</td>
<td class="data row0 col4" id="T_3be67_row0_col4">1.00</td>
<td class="data row0 col5" id="T_3be67_row0_col5">1.00</td>
<td class="data row0 col6" id="T_3be67_row0_col6">1.00</td>
<td class="data row0 col7" id="T_3be67_row0_col7">1.00</td>
<td class="data row0 col8" id="T_3be67_row0_col8">1.00</td>
<td class="data row0 col9" id="T_3be67_row0_col9">0.94</td>
<td class="data row0 col10" id="T_3be67_row0_col10">0.99</td>
</tr>
<tr>
<th class="row_heading level0 row1" id="T_3be67_level0_row1">instructblip</th>
<td class="data row1 col0" id="T_3be67_row1_col0">1.00</td>
<td class="data row1 col1" id="T_3be67_row1_col1">1.00</td>
<td class="data row1 col2" id="T_3be67_row1_col2">1.00</td>
<td class="data row1 col3" id="T_3be67_row1_col3">1.00</td>
<td class="data row1 col4" id="T_3be67_row1_col4">1.00</td>
<td class="data row1 col5" id="T_3be67_row1_col5">1.00</td>
<td class="data row1 col6" id="T_3be67_row1_col6">0.93</td>
<td class="data row1 col7" id="T_3be67_row1_col7">1.00</td>
<td class="data row1 col8" id="T_3be67_row1_col8">1.00</td>
<td class="data row1 col9" id="T_3be67_row1_col9">0.10</td>
<td class="data row1 col10" id="T_3be67_row1_col10">0.90</td>
</tr>
<tr>
<th class="row_heading level0 row2" id="T_3be67_level0_row2">otter</th>
<td class="data row2 col0" id="T_3be67_row2_col0">1.00</td>
<td class="data row2 col1" id="T_3be67_row2_col1">0.78</td>
<td class="data row2 col2" id="T_3be67_row2_col2">1.00</td>
<td class="data row2 col3" id="T_3be67_row2_col3">0.63</td>
<td class="data row2 col4" id="T_3be67_row2_col4">1.00</td>
<td class="data row2 col5" id="T_3be67_row2_col5">0.92</td>
<td class="data row2 col6" id="T_3be67_row2_col6">0.76</td>
<td class="data row2 col7" id="T_3be67_row2_col7">1.00</td>
<td class="data row2 col8" id="T_3be67_row2_col8">1.00</td>
<td class="data row2 col9" id="T_3be67_row2_col9">0.09</td>
<td class="data row2 col10" id="T_3be67_row2_col10">0.82</td>
</tr>
<tr>
<th class="row_heading level0 row3" id="T_3be67_level0_row3">idefics</th>
<td class="data row3 col0" id="T_3be67_row3_col0">1.00</td>
<td class="data row3 col1" id="T_3be67_row3_col1">0.85</td>
<td class="data row3 col2" id="T_3be67_row3_col2">1.00</td>
<td class="data row3 col3" id="T_3be67_row3_col3">0.31</td>
<td class="data row3 col4" id="T_3be67_row3_col4">1.00</td>
<td class="data row3 col5" id="T_3be67_row3_col5">1.00</td>
<td class="data row3 col6" id="T_3be67_row3_col6">0.94</td>
<td class="data row3 col7" id="T_3be67_row3_col7">1.00</td>
<td class="data row3 col8" id="T_3be67_row3_col8">1.00</td>
<td class="data row3 col9" id="T_3be67_row3_col9">0.05</td>
<td class="data row3 col10" id="T_3be67_row3_col10">0.81</td>
</tr>
<tr>
<th class="row_heading level0 row4" id="T_3be67_level0_row4">adept</th>
<td class="data row4 col0" id="T_3be67_row4_col0">1.00</td>
<td class="data row4 col1" id="T_3be67_row4_col1">0.86</td>
<td class="data row4 col2" id="T_3be67_row4_col2">1.00</td>
<td class="data row4 col3" id="T_3be67_row4_col3">0.99</td>
<td class="data row4 col4" id="T_3be67_row4_col4">1.00</td>
<td class="data row4 col5" id="T_3be67_row4_col5">0.13</td>
<td class="data row4 col6" id="T_3be67_row4_col6">0.26</td>
<td class="data row4 col7" id="T_3be67_row4_col7">0.99</td>
<td class="data row4 col8" id="T_3be67_row4_col8">1.00</td>
<td class="data row4 col9" id="T_3be67_row4_col9">0.06</td>
<td class="data row4 col10" id="T_3be67_row4_col10">0.73</td>
</tr>
<tr>
<th class="row_heading level0 row5" id="T_3be67_level0_row5">llava</th>
<td class="data row5 col0" id="T_3be67_row5_col0">1.00</td>
<td class="data row5 col1" id="T_3be67_row5_col1">0.87</td>
<td class="data row5 col2" id="T_3be67_row5_col2">1.00</td>
<td class="data row5 col3" id="T_3be67_row5_col3">0.44</td>
<td class="data row5 col4" id="T_3be67_row5_col4">1.00</td>
<td class="data row5 col5" id="T_3be67_row5_col5">0.29</td>
<td class="data row5 col6" id="T_3be67_row5_col6">0.48</td>
<td class="data row5 col7" id="T_3be67_row5_col7">0.87</td>
<td class="data row5 col8" id="T_3be67_row5_col8">1.00</td>
<td class="data row5 col9" id="T_3be67_row5_col9">0.07</td>
<td class="data row5 col10" id="T_3be67_row5_col10">0.70</td>
</tr>
<tr>
<th class="row_heading level0 row6" id="T_3be67_level0_row6">openflamingo</th>
<td class="data row6 col0" id="T_3be67_row6_col0">1.00</td>
<td class="data row6 col1" id="T_3be67_row6_col1">0.45</td>
<td class="data row6 col2" id="T_3be67_row6_col2">1.00</td>
<td class="data row6 col3" id="T_3be67_row6_col3">0.34</td>
<td class="data row6 col4" id="T_3be67_row6_col4">1.00</td>
<td class="data row6 col5" id="T_3be67_row6_col5">0.40</td>
<td class="data row6 col6" id="T_3be67_row6_col6">0.70</td>
<td class="data row6 col7" id="T_3be67_row6_col7">0.84</td>
<td class="data row6 col8" id="T_3be67_row6_col8">1.00</td>
<td class="data row6 col9" id="T_3be67_row6_col9">0.04</td>
<td class="data row6 col10" id="T_3be67_row6_col10">0.68</td>
</tr>
</tbody>
</table>


## Replicating/Extending Benchmark

Welcome to our project! To get started with using our repository follow these steps:

### Get Started

1. Clone the repository to your local machine: 
```bash
git clone https://github.com/ClaraLovesFunk/Testing-Multimodal-LLMs
```
2. Navigate to the repository directory: 
```bash
cd Testing-Multimodal-LLMs
```
3. Choose model(s) and dataset(s) to run them on.

### Prepare Datasets

1. Go to the directory [datasets](datasets). Create a new directory with the name of the dataset of interest (if you use a dataset that was already implemented check [config.json](config.json) and use the same name as we did previously.)

2. Obtain the dataset and further proceed with the split of interest.

3. Turn the textual data with the split of interest into a json file and call it ds_benchmark.json.

4. Transform the structure of the textual data as shown in the example dataset in [datasets/example_dataset](datasets/example_dataset). In case you want to use a dataset that has its own evaluation protocol such as A-OK-VQA or OKVQA additionally keep a copy of the original file(s) and leave their name as is (e.g., for A-OK-VQA the dataset is spread over two files one containing image ids one containing labels.)

5. Create a subdirectory in your directory [datasets/dataset_of_interest](datasets/dataset_of_interest) called images and store the images.

6. If you added a new dataset to the benchmark follow these additional instructions:
    - Go to [utils/answer_processing.py](utils/answer_processing.py) and adapt the function `get_clean_valid_preds_trues()` for your new dataset. Read the function description and follow the example of one of the already implemented datasets.
    - Go to [utils/info.py](utils/info.py) and extend the class `DatasetInfo()` and the function ​`​get_task2label_name()` for your dataset.

### Prepare Inference

1. If you want to implement a model that was already implemented by us go to [inference](inference) and to the directory with the name of the model you want to run. If you want to run a new model create a new directory with the name of the model you want to run within the directory [inference](inference). All the following instructions are assuming you want to run a model we have implemented. If you want to implement your own model follow the structure we have chosen and will describe now.

2. For first orientation go to the [inference](inference) and to the model of interest and read the specific README.md.

3. Create a virtual environment for each model you want to run. Store the virtual environment in the directory [venvs](venvs). Install the dependencies via the requirements.txt file in each model directory. Repeat the following steps for each model.

  ```bash
  python3 -m venv venvs/<model_name>
  source venvs/<model_name>/bin/activate
  pip install -r inference/<model_directory>/requirements.txt
  ```

4. For further information about the implementation read the respective README.md. 

5. If you added a new model to the benchmark do the following before running inference:
    - add the model name in [config.json](config.json).
    - Go to [utils/answer_processing.py](utils/answer_processing.py) and add another condition for your model to the function `extract_answer()`. Follow the example of one of the models that were already implemented that you can see in that function.
    - Go to [inference](inference) and create a new directory with the name of your model. Create the files README.md, inference.py. In [inference](inference) you need to actually write the implementation for your model. Ultimately this script needs to be run by [run_inference.py](run_inference.py). You can use other models such as idefics as examples.

### Run Inference

To run a model on a dataset and save the output you can do: 
```bash
python3 run_inference.py -models model_of_interest -datasets dataset_of_interest
```

If you want to run all models or all datasets replace the model of dataset of interest with the string ‘all’ such as:
```bash
python3 run_inference.py -models all -datasets dataset_of_interest
```

You can also run multiple models on multiple datasets e.g.:
```bash
python3 run_inference.py -models model_of_interest1 model_of_interest2 -datasets dataset_of_interest1 dataset_of_interest1
``````



### Run Evaluation

If you want to evaluate a model on a dataset and save the metrics indicate the correctly/incorrectly predicted samples as you can see in [evaluations](evaluations) do:

```bash
python run_eval.py --models model_of_interest --datasets dataset_of_interest --run run_of_interest --mode hard --calcavrg no
```
`run_of_interest` is an integer that represents the run of your experiment. `Mode` can be either the string `hard` or `soft` representing whether you want to evaluate without or with post-processing tolerance. `Calcavrg` determines whether the average per model over all datasets should be calculated. This argument can take the values `yes` or `no`. You can also use the `all` keyword or a list of models and datasets as when running inference.

## Repository Structure

This section outlines the organization of the repository detailing the directories and their contents to facilitate navigation and understanding of where key files and resources are located.

- [/datasets](datasets): Contains directories for each dataset used in the benchmark.
  - `example_dataset`: An example dataset directory.
    - `ds_benchmark.json`: Demonstrates the format for dataset split of interest.
- [/evaluations](evaluations): Holds evaluation scripts and resources for each dataset.
  - `eval.py`: the script holding the dataset-specific evaluation function(s) that are called from [run_eval.py](run_eval.py)
  - `eval_dataset_of_interest`: Optional subdirectory for additional resources.
  - `README.md`: Provides details on dataset-specific evaluations.
- [/experiments](experiments): Documents the experiments conducted including configurations and outputs.
  - `model/dataset/run`: Contains files documenting individual experiment runs
    - `config.json`: Information on the experiment's setup.
    - `output.json`: Raw output from the model.
    - `output_aux_hard.json`: Cleaned output without post-processing tolerance (for further explanation see `report.pdf`).
    - `output_aux_soft.json`: Cleaned output with post-processing tolerance (for further explanation see `report.pdf`).
    - `scores_hard.json`: Metrics when processing output without post-processing tolerance.
    - `scores_soft.json`: Metrics when processing output with post-processing tolerance
    - `examples_hard.json`: Indicates which dataset samples were predicted correctly when not applying post-processing tolerance.
    - `examples_soft.json`: Indicates which dataset samples were predicted correctly when applying post-processing tolerance.
    - `valid_ans_hard.json`: Ratio of valid answers when not applying post-processing tolerance.
    - `valid_ans_soft.json`: Ratio of valid answers applying post-processing tolerance.
- [/inference](inference): Includes inference scripts and model-specific resources.
  - `model_of_interest`: Includes inference scripts and model-specific resources.
    - `inference.py`: inference script for running a model on a specified dataset given a model configuration. It loads a pre-trained model, processes input data, and generates predictions. Additionally, it saves the model's outputs and related information to the specified directory for evaluation purposes when called from another script.
    - `subdirectory_of_interest`: optional subdirectory that can contain additional resources for the model to run such as a cloned git repository
    - `README.md`: further information on the model of interest & its implementation
    - `Requirements.txt`: Stores dependencies that need to be installed in the respective environment.
- [/ressources](ressources): Auxiliary resources like images or additional scripts related to the project.
- [/utils](ressources/utils): Utility scripts for common functions across the project.
- [/config.json](config.json): Configuration settings for the benchmarking process.
- [/prompts.py](prompts.py): Generates prompts for the models based on the benchmark datasets.
- [/README.md](README.md): The main documentation providing detailed information about the project setup and usage.
- [/report.pdf](report.pdf): A comprehensive report of the benchmark findings.
- [/run_eval.py](run_eval.py) and [/run_inference.py](run_inference.py): Main scripts for running evaluations and inferences.
