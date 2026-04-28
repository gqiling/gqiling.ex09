---
layout: page
title: COMP110 Continuous Improvement Analysis
---

# COMP110 Continuous Improvement Analysis

## Project idea

My proposed course improvement is to add more real-world, cross-disciplinary programming project options to COMP110. Instead of every student completing only one fixed application context, students could choose from examples connected to fields such as biology, public policy, journalism, business, psychology, or data science.

This change would create value for enrolled students because it could make the course feel more relevant to their own academic interests. It would also create value for the broader workforce because students from many majors would leave COMP110 with a clearer sense of how programming can support their future field.

## Research question

The survey data can help answer this question:

**Do students who are more interested in the connections between computer science and other fields also find COMP110 more intellectually interesting, more valuable, and more worth recommending?**

If the answer is yes, then cross-disciplinary project options are a promising course design improvement.

## Data used

I analyzed anonymized COMP110 survey responses from both course survey files. My analysis focused on these columns:

- `interested_connections`: whether students are interested in connections between computer science and other fields
- `interesting`: whether students find the course topics intellectually interesting
- `valuable`: whether students believe the skills learned in the course will be valuable in the future
- `would_recommend`: whether students would recommend the course to other students
- `comp_major`: whether students intend to major or minor in computer science

Before analyzing the data, I removed rows with empty responses in the numeric Likert-scale columns so that the visualizations only used complete responses for the selected variables.

## Visualization 1: Distribution of cross-disciplinary interest

![Distribution of interest in CS connections](exercises\ex09\chart1_connections_distribution.png)

This chart shows how students answered the `interested_connections` question, separated by CS major/minor status. The main purpose of this graph is to see whether there is already demand for course material that connects computer science to other fields.

The distribution suggests that many students, including many non-CS students, are interested in cross-disciplinary connections. This matters because COMP110 serves students from many majors, not only students planning to major in computer science.

## Visualization 2: Cross-disciplinary interest and intellectual interest

![Interest in CS connections vs course intellectual interest](exercises\ex09\chart2_connections_vs_interesting.png)

This scatter plot compares each student's `interested_connections` score with their `interesting` score. If the points generally move upward as `interested_connections` increases, that suggests students who care more about cross-disciplinary connections also tend to find the course more intellectually interesting.

The pattern supports the idea that connecting COMP110 to other fields could improve student engagement. The relationship is not perfect, but students with high interest in CS connections generally appear to report high intellectual interest in the course.

## Visualization 3: Course interest grouped by cross-disciplinary interest

![Boxplot of course interest by CS connections interest](exercises\ex09\chart3_boxplot_interesting_by_connections.png)

This box plot groups students by their `interested_connections` score and shows the distribution of their `interesting` scores. This is useful because it summarizes the median and spread for each group rather than only showing individual points.

If the median `interesting` score rises across the groups, that gives additional support to the idea that cross-disciplinary framing is connected to stronger course interest.

## Visualization 4: Mean course sentiment scores

![Mean course sentiment scores by cross-disciplinary interest](exercises\ex09\chart4_mean_scores_by_connections.png)

This line plot compares the average values of three course sentiment measures at each level of `interested_connections`: `interesting`, `valuable`, and `would_recommend`.

This chart is important because the course improvement idea should not only make the course more interesting. Ideally, it should also make students see the course as valuable and worth recommending. If these three lines rise together, then students who care about cross-disciplinary connections also tend to evaluate the course more positively overall.

## Conclusion

Overall, the analysis provides moderate-to-strong support for adding more cross-disciplinary project options to COMP110. Students who are more interested in connections between computer science and other fields also tend to report stronger intellectual interest in the course, stronger belief that the course skills are valuable, and greater willingness to recommend the course.

Based on this evidence, I recommend that COMP110 pilot a small number of optional project contexts connected to different majors or career interests. For example, students might choose between a biology-themed data analysis, a public policy dataset, a journalism/text-processing activity, or a business analytics scenario. The underlying programming concepts could remain the same, but the context would feel more personally relevant to different students.

## Trade-offs and limitations

There are some costs and limitations to this idea. Creating multiple project contexts would require more work from instructional staff, and grading could become more complex if students choose different contexts. There is also a risk that the application context could distract from the core programming concept if the assignment is not designed carefully.

The data is also correlational, so it does not prove that cross-disciplinary projects would directly cause students to enjoy the course more. Students who already like making connections across fields may simply be more likely to enjoy COMP110 in general. A stronger future test would be to compare sections or assignments with and without cross-disciplinary framing.

## Future work

A useful next step would be to run a small pilot. One group of students could complete a standard assignment, while another group could complete the same programming concept through a cross-disciplinary context. A follow-up survey could then compare changes in `interesting`, `valuable`, and `would_recommend` scores. This would help determine whether the proposed course change actually creates value for students.