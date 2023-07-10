import pickle 
import numpy as np
import config

class ConcreteStrength():
    def __init__(self,cement,slag,flyash,water,superplasticizer,coarseaggregate,fineaggregate,age):
        print("****************INIT FUNCTION***********************")
        self.cement=cement
        self.slag=slag
        self.flyash=flyash
        self.water=water
        self.superplasticizer=superplasticizer
        self.coarseaggregate=coarseaggregate
        self.fineaggregate=fineaggregate
        self.age=age

    def __load_saved_data(self):
        model_file_name=config.MODEL_DFILE_PATH
        with open(model_file_name,'rb') as f:
            self.model=pickle.load(f)


    def get_predicted_strength(self):
        self.__load_saved_data()
        test_array=np.zeros((1,self.model.n_features_in_))
        test_array[0,0]=self.cement
        test_array[0,1]=self.slag
        test_array[0,2]=self.flyash
        test_array[0,3]=self.water
        test_array[0,4]=self.superplasticizer
        test_array[0,5]=self.coarseaggregate
        test_array[0,6]=self.fineaggregate
        test_array[0,7]=self.age

        predicted_strenth=np.around(self.model.predict(test_array)[0],3)
        return predicted_strenth
