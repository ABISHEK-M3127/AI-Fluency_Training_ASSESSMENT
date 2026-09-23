# Day 2 - Reasoning and Acting

## 1. Scenario

For this experiment, I selected a college event budget planning scenario.

A college event has 40 students attending. Snacks cost Rs. 80 per person, lunch costs Rs. 150 per person, and juice costs Rs. 40 per person. Decoration costs Rs. 2,500 and a sound system costs Rs. 4,000. The club has a budget of Rs. 15,000.

The main question is:

"Will the budget be enough? If not, how much more is needed?"

The correct calculation is:

- Snacks = 40 × Rs. 80 = Rs. 3,200
- Lunch = 40 × Rs. 150 = Rs. 6,000
- Juice = 40 × Rs. 40 = Rs. 1,600
- Decoration = Rs. 2,500
- Sound system = Rs. 4,000

Therefore:

Total cost = Rs. 3,200 + Rs. 6,000 + Rs. 1,600 + Rs. 2,500 + Rs. 4,000

Total cost = Rs. 17,300

Available budget = Rs. 15,000

Shortfall = Rs. 17,300 - Rs. 15,000 = Rs. 2,300

Therefore, the correct answer is that the budget is not enough and an additional Rs. 2,300 is required.

---

## 2. Direct Prompting

Direct Prompting asks the language model to answer the question directly without requesting a step-by-step reasoning process.

In my experiment, the direct prompting approach was given three questions related to the college event scenario.

For Question 1, the model correctly calculated the total event cost as Rs. 17,300 and identified the shortfall as Rs. 2,300.

For Question 2, the model correctly calculated the total expenditure as Rs. 8,600 and stated that Rs. 1,400 would remain from the Rs. 10,000 budget.

For Question 3, which was a logic question about the order in which four volunteers arrived, the model correctly identified Divya as the first person and Charan as the last person.

The main advantage observed was that the direct responses were short and fast. The model did not display intermediate reasoning, so the output was easier to read but provided less explanation about how the answer was obtained.

Direct Prompting does not use external tools in this experiment. It depends on the information already present in the prompt and the model's existing knowledge.

---

## 3. Chain-of-Thought

The Chain-of-Thought approach was tested using the same questions.

Instead of requesting only the final answer, the prompt instructed the model to solve the problem step by step and show the calculations.

For Question 1, the model separately calculated the cost of snacks, lunch and juice, added the decoration and sound-system costs, calculated the total of Rs. 17,300, and compared it with the Rs. 15,000 budget. It correctly concluded that Rs. 2,300 more was required.

For Question 2, the model calculated:

60 × Rs. 75 = Rs. 4,500 for snacks.

60 × Rs. 35 = Rs. 2,100 for juice.

After adding Rs. 2,000 for decoration, the total was Rs. 8,600. The model correctly calculated that Rs. 1,400 would remain.

For Question 3, the model converted the relationships into an ordering:

Divya < Anu < Bala < Charan

It therefore correctly identified Divya as the first and Charan as the last.

The main advantage observed was that Chain-of-Thought made the intermediate calculations and logic visible in the response. This makes it easier to inspect how the final answer was obtained.

The disadvantage is that the responses were longer than the direct responses. More generated text can also require more tokens and therefore potentially more time and cost.

Chain-of-Thought did not use tools in this experiment.

---

## 4. ReAct Agent

The ReAct approach was tested using the event-budget question.

The purpose of ReAct is to allow an agent to reason about a problem and interact with tools when necessary. A typical ReAct process consists of reasoning, taking an action through a tool, receiving an observation, and then continuing until a final answer can be produced.

In my experiment, the ReAct program returned the correct final result. It calculated the total event cost as Rs. 17,300 and identified the shortfall as Rs. 2,300.

However, an important observation from my actual output is that the terminal output did not display any tool actions or observations.

The output was:

    --- REACT AGENT TRACE ---

    --- FINAL ANSWER ---

Therefore, I cannot claim that the tool was actually used in this particular run. The final answer was correct, but the expected Thought -> Action -> Observation trace was not visible.

This is an important limitation of this experiment. The Day 2 ReAct experiment is intended to demonstrate tool usage, so a future run should be checked to ensure that the agent actually calls the required tools and prints the resulting observations.

---

## 5. Comparison of the Three Approaches

| Basis for comparison | Direct Prompting | Chain-of-Thought | ReAct Agent |
|---|---|---|---|
| Reasoning depth | Low. The model directly provides an answer. | Higher. The model explicitly works through multiple steps. | Potentially high because it can reason and interact with tools. |
| Tool usage | No tools used. | No tools used. | Designed for tool usage, but no tool calls were visible in my actual run. |
| Reliability on multi-step questions | Correct on all three questions tested. | Correct on all three questions tested and showed the calculations. | Correct final answer for the event-budget question. |
| Transparency | Low because only the final response is emphasized. | High because calculations and logical steps are shown. | Potentially high through tool actions and observations, but the trace was not visible in this run. |
| Speed / cost | Generally lower because the response is direct and shorter. | Potentially higher because the response contains more generated text. | Potentially higher because an agent may make multiple model and tool calls. |
| Consistency | The tested answers were correct, but only one run was made for each question. | The tested answers were correct, but one run alone is not enough to measure consistency. | The tested answer was correct, but only one run was performed. |
| Event-budget result | Rs. 17,300 total and Rs. 2,300 shortfall. | Rs. 17,300 total and Rs. 2,300 shortfall. | Rs. 17,300 total and Rs. 2,300 shortfall. |

Overall, the experiment showed that all three approaches can produce the same correct answer when all the required numerical information is already available in the prompt. Their differences become more important when a problem requires information that is not already available and must be obtained through a tool.

---

## 6. Self-Consistency Experiment

Self-consistency was tested using the first event-budget question.

The same Chain-of-Thought question was run five times with a temperature of 0.8.

The results were:

| Run | Model output |
|---|---|
| Run 1 | Rs. 2,300 more |
| Run 2 | 2300 |
| Run 3 | The budget is not enough; an additional Rs. 2,300 is needed |
| Run 4 | 2300 |
| Run 5 | 2300 Rs more is needed |

All five responses represented the same underlying numerical answer: Rs. 2,300.

The program reported:

    Majority answer (2 of 5 runs): 2300

This happened because the program used exact text matching when counting the answers. Although all five responses meant the same thing, their wording was different. Only two responses contained exactly the same extracted string, "2300".

Therefore, this experiment shows that the model was semantically consistent but textually different across runs.

The temperature was set to 0.8 so that the model could produce different responses between runs. A temperature of 0 would generally make the responses more deterministic, depending on the model and API.

---

## 7. Suitability Analysis

For the particular event-budget questions tested here, Direct Prompting was sufficient because all the required information was already included in the questions and the model produced the correct answers.

Chain-of-Thought was useful when the purpose was to inspect the calculation and logical process. It made the intermediate steps visible and therefore made it easier to verify the calculations.

ReAct becomes particularly useful when the problem requires information from external or private sources. In that situation, the agent can use tools to obtain information and then reason over the observations. In my current ReAct run, however, the terminal output did not show tool calls, so the tool-use capability was not successfully demonstrated.

Therefore, the suitability of each approach depends on the type of problem. Direct Prompting is appropriate for straightforward questions. Chain-of-Thought is useful for problems involving several reasoning steps. ReAct is appropriate when reasoning needs to be combined with interaction with tools or external/private information.

---

## 8. Limitations and Observations

There are two important observations from this experiment.

First, the Direct Prompting and Chain-of-Thought approaches both produced correct answers for the selected questions. Therefore, this experiment alone does not prove that Chain-of-Thought is always more accurate than Direct Prompting. It only shows that both approaches successfully solved these particular questions.

Second, the ReAct output did not contain visible tool calls or observations. Therefore, the tool-use part of the ReAct experiment needs further verification. The final answer was correct, but the trace did not demonstrate the expected Thought -> Action -> Observation cycle.

The self-consistency experiment also showed that exact-string majority voting can underestimate agreement when different responses use different wording for the same answer.

---

## 9. Conclusion

This experiment compared Direct Prompting, Chain-of-Thought and ReAct using a college event budget planning scenario.

Direct Prompting produced concise answers and successfully solved the tested questions. Chain-of-Thought produced longer responses with explicit intermediate calculations and logical steps. ReAct produced the correct final event-budget answer, although the expected tool-use trace was not visible in the recorded run.

The self-consistency experiment showed that the five runs produced different wordings but the same underlying numerical result of Rs. 2,300.

In general, the choice of approach should depend on the problem. Direct Prompting is suitable when a straightforward answer is needed and the necessary information is already available. Chain-of-Thought is useful for problems involving multiple reasoning steps. ReAct is useful when reasoning needs to be combined with tool interaction and information retrieval.