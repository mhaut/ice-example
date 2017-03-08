

module Arithmetic { 
  
    exception GenericError { 
        string reason; 
    }; 

    interface Natural { 
        int add(int a, int b) throws GenericError; 
        int substract(int a, int b) throws GenericError; 
    }; 
}; 