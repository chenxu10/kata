Given an QA dataset with column Line_Item_Descriptions and QA_adj_code as groundtruth. 
Build a minimalistic end-to-end pipeline using GPT4.1 model playing role as litigation auditor
working in a fortune 100 insurance company. Your job is to classify line item blling invoices into
1A adminstrative and 1T time reducntion. The model should be wrapper in MLflow wrapper as customized PythonModel. You are using MLflow 2.0. The input side of pipeline is QA dataset the output side is a model with evaluation metrics on precesion and logging total cost, time used and prompt.


- Now build a test of LLMClassiferWrapper that will be logged into mlflow