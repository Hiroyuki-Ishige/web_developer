"""
CSS application priority

By Position
li {
color: red;
color: blue; <-This will apply
}

By Specificity
li{color: blue;}
.first-class{color: red;}
li[draggable]{color:purple;}
#first-id{color: orange;} <-This will apply

By Type
<link rel="styleshet" href="./style.css"> (External CSS)
<style> </style> (Internal CSS)
<h1 style="">Hello</h1> (Inline CSS) <-This will apply

By importance
color:red;
color:green !important; <-This will apply


"""