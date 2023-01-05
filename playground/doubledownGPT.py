import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
import torch
import torch.nn as nn
from transformers import pipeline

class TransformerFactory(ABC):
    """
    Declare an interface for operations that create abstract product objects.
    """

    @abstractmethod
    def generate_model(self):
        pass

class LSSTransformer(TransformerFactory):
    def generate_model(self):
        model = pipeline("zero-shot-classification")
        return model

class ReinforcementFactory(ABC):
    """
    Declare an interface for operations that create abstract product objects.
    """
    @abstractmethod
    def generate_model(self):
        pass

class LSSReinforcement(ReinforcementFactory):
    @abstractmethod
    def generate_model(self):
        return

class GPTFactory(ABC):
    """
    Declare an interface for operations that create abstract product objects.
    """

    @abstractmethod
    def create_transformer_nlp_model(self):
        pass

    @abstractmethod
    def create_deep_reinforcement_learning_model(self):
        pass
    
    @abstractmethod
    def create_gpt_model(self):
        pass

class LSSGPTFactory(GPTFactory):
    """
    Implement the operations to create concrete product objects.
    """
    def create_transformer_nlp_model(self):
        lsstransformer = LSSTransformer()
        lsstransformer_model = lsstransformer.generate_model()
        return lsstransformer_model

    def create_deep_reinforcement_learning_model(self):
        return LSSReinforcement()

    def create_gpt_model(self):
        # combine LSSTransformer and LSSReinforcement
        return self.create_transformer_nlp_model()

def get_lss_gpt_adjustment_model(factory):
    lss_gpt_model = factory.create_gpt_model()
    return lss_gpt_model

if __name__ == '__main__':
    lss_gpt_factory = LSSGPTFactory()
    lss_gpt_model = get_lss_gpt_adjustment_model(lss_gpt_factory)
    wrk_descriptions = ["Consultation on legal matters related to employment law","Representation at arbitration hearing"]
    labels = ["1A","1T"]
    result = lss_gpt_model(wrk_descriptions, labels)
    print(result)
   

