#!/usr/bin/env python
# coding: utf-8

# In[6]:


import kfp
client = kfp.Client()
my_experiment = client.create_experiment(name='demofinal')
my_run = client.run_pipeline(my_experiment.id, 'my-pipeline-final', 
  '$HOME/aidevops_12/roles/pipeline-sdk/files/model_generation_new1.pipeline.zip')


# In[ ]:





# In[ ]:




