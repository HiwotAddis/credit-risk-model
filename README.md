# Credit Scoring Business Understanding

## 1. Basel II and the Need for Interpretable Models

The Basel II Capital Accord emphasizes the importance of accurate, transparent, and risk-sensitive capital requirements. It introduces three pillars: minimum capital requirements, supervisory review, and market discipline. Under Pillar 1, banks must quantify credit risk using either standardized or internal ratings-based (IRB) approaches.
Because of this regulatory framework:

- Interpretability is essential: Supervisors and internal stakeholders must understand how risk scores are derived to ensure fairness, consistency, and compliance.
- Documentation is critical: Models must be auditable and explainable, especially when used to determine capital adequacy or loan approvals.
- Model governance: Basel II encourages robust validation, monitoring, and stress testing, which are easier to implement with interpretable models like logistic regression.

## 2. Why We Need a Proxy Variable for Default

In the absence of a direct "default" label (e.g., no explicit record of missed payments or charge-offs), we must engineer a proxy variable to approximate credit risk. For example, we might define a customer as "high risk" if they:

- Have not made a purchase in the last 90 days (recency)
- Have low purchase frequency or monetary value
- Exhibit sudden drops in engagement or spending

However, this approach introduces business risks:

- Misclassification: If the proxy doesn’t align well with actual defaults, we may reject creditworthy customers or approve risky ones.
- Bias and fairness: Poorly chosen proxies can reflect systemic biases, leading to reputational or regulatory consequences.
- Model drift: Behavioral proxies may change over time, requiring frequent recalibration.
  Thus, the proxy must be carefully validated against known outcomes or expert judgment to ensure it reflects real-world credit behavior.

### 3. Trade-offs: Simple vs. Complex Models

| Aspect                | Logistic Regression with WoE                          | Gradient Boosting                                     |
| --------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| Interpretability      | High – easy to explain to regulators and stakeholders | Low – often considered a "black box"                  |
| Performance           | Moderate – good baseline accuracy                     | High – captures nonlinearities and interactions       |
| Regulatory Compliance | Preferred in regulated environments                   | Requires additional explainability tools (e.g., SHAP) |
| Speed & Maintenance   | Fast to train, easy to update                         | Slower training, more complex tuning                  |
| Use Case Fit          | Ideal for scorecards and compliance-driven lending    | Suitable for high-volume, low-regulation environments |
