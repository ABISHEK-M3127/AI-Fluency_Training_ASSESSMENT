# Day 1 Practice Task
## Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

The chosen private-data scenario is a small shop inventory system.

The private data contains product codes, product names, categories,
prices, and stock quantities.

The products used are:

- P101 - Wireless Mouse - ₹800 - 25 units
- P102 - Mechanical Keyboard - ₹2,500 - 12 units
- P103 - USB-C Hub - ₹1,200 - 18 units
- P104 - Laptop Stand - ₹1,500 - 8 units
- P105 - Webcam - ₹2,000 - 15 units

## 2. Plain Chatbot

The plain chatbot uses an LLM to generate responses.

It does not directly access the private shop inventory data.

Therefore, it can answer general questions and generate promotional
content, but it cannot reliably retrieve exact private prices or stock
information.

## 3. Rule-Based Workflow

The rule-based workflow uses predefined conditions and the private
inventory data.

It does not use an LLM.

It can answer predefined questions reliably, but it becomes less flexible
when the user asks a question that was not covered by the programmed rules.

## 4. AI Agent

The AI agent combines an LLM, tools, and a loop.

The LLM interprets the user's request and decides which tool should be
used.

The tools provide access to private product prices and stock information.

The calculator tool performs arithmetic when required.

The loop allows the agent to continue after receiving tool results and
produce a final answer.

## 5. Comparison

| Basis | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | High for general language | Low | High |
| Decision-making | LLM response generation | Predefined conditions | LLM selects tools/actions |
| Tool usage | No | No | Yes |
| Private-data access | No direct access | Direct access | Through tools |
| Multi-step task handling | Limited | Limited to predefined steps | Supports multiple tool steps |
| Automation | Low | High for fixed tasks | High |
| Reliability | May generate unsupported information | High for predefined rules | Depends on tool use and LLM decisions |

## 6. Suitability Analysis

The rule-based workflow is suitable for fixed and predictable questions
where reliability and predefined processing are important.

The plain chatbot is suitable for general conversation and tasks that do
not require exact private data.

The AI agent is suitable for flexible questions that require private data,
tool usage, calculations, and multiple steps.

## 7. Conclusion

A plain chatbot mainly uses an LLM to generate responses.

A rule-based workflow follows predefined rules and conditions.

An AI agent combines an LLM, tools, and a loop to select tools, observe
their results, and continue working until the task is completed.

Therefore, the appropriate approach depends on the type of problem,
the need for private-data access, the amount of flexibility required,
and the importance of predictable behavior.