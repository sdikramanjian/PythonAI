<!doctype html> 
<html>

<head> 
   <link rel="stylesheet" href="/bootstrap/css/bootstrap.min.css">
   <script src="/bootstrap/js/bootstrap.min.js"></script>
</head> 

<body>

<form action = "/" method = "POST">
   <div class="container mt-5"></div>
      <div class="row justify-content-center">
         <div class="col-md-6">
                  <h1 class="card-title text-center mb-4">What type of an investor are you, {{name}}?</h1>
                 
                     <div class="form-group">
                        <select id="investor-type" name="investor_type" class="form-select form-select-lg mb-3">
                           <option selected>Please select one</option> 
                           % for type in investor_types:
                              <option>{{type}}</option>
                           % end
                        </select> 
                     </div>

                     <button type="submit" class="btn btn-primary btn-block">Submit</button>
                     <div class="result">      
                        <strong>{{result}}</strong><br><br>  
                     </div>
                     <div class="result">
                        % for stock in recommendation:
                           {{stock}}<br>  <!-- Insert a new line after each entry -->
                        % end
                     </div>         
         </div>
      </div>
   </div>
</form>


<div> <!-- Include the Agent Template where we test the Langchain code -->
  %include("agent_component.tpl") 
</div>

</body>
</html>
