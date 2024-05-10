ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list.pop();
ft_list.append("World!");

ft_tuple = (ft_tuple[0], "Brazil!");
ft_set.pop();
ft_set.pop();
ft_set.add("Hello");
ft_set.add("SÃO PAULO!");

ft_dict = {"Hello" : "42SP!"};

print("ft_tuple: ", ft_tuple);
print("ft_list: ", ft_list);
print("ft_set: ", ft_set);
print("ft_dict: ", ft_dict);