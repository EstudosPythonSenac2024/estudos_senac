'''
## 2 - Crie uma função para descobrir os clientes inadimplentes de uma empresa

- O objetivo é identificar quem são os clientes inadimplentes e enviar essa lista de clientes para o setor de cobrança poder fazer a cobrança dos clientes.
- Sua função deve então receber uma lista de clientes, analisar quais clientes estão inadimplentes, e retornar uma lista com os clientes inadimplentes (apenas o CPF deles já é suficiente)
- A inadimplência nessa empresa é calculada da seguinte forma:
    1. Se o cliente tiver devendo mais de 1.000 reais por mais de 20 dias, ele é considerado inadimplente.
    2. Isso significa que caso ou cliente esteja devendo 2.000 reais a 10 dias, ele não é inadimplente, pois não se passaram 20 dias ainda. Da mesma forma, se ele estiver devendo 500 reais por 40 dias, ele também não é inadimplente, dado que ele deve menos de 1.000 reais.
    3. As informações vêm no formato (cpf, valor_devido, qtde de dias)

clientes_devedores = [('462.286.561-65',14405,24),('251.569.170-81',16027,1),('297.681.579-21',8177,28),('790.223.154-40',9585,10),('810.442.219-10',18826,29),('419.210.299-79',11421,15),('908.507.760-43',12445,24),('911.238.364-17',1345,4),('131.115.339-28',11625,8),('204.169.467-27',5364,22),('470.806.376-11',932,29),('938.608.980-69',13809,19),('554.684.165-26',11227,2),('119.225.846-34',4475,9),('358.890.858-95',13932,20),('786.547.940-70',17048,25),('468.487.741-94',2902,8),('540.685.100-32',5806,21),('379.729.796-80',7622,24),('980.173.363-94',13167,24),('833.285.374-56',19581,24),('103.669.436-50',17126,4),('386.836.124-46',18825,11),('588.404.964-15',1545,30),('600.556.177-18',1921,7),('670.346.230-99',18079,28),('771.352.915-13',16581,23),('430.314.324-46',13942,24),('629.507.759-51',17951,11),('348.683.225-73',12424,10),('406.133.151-17',5888,30),('310.985.894-64',17316,30),('964.317.132-30',18818,30),('845.331.524-14',14284,13),('781.995.738-18',19369,29),('921.558.128-63',3206,27),('941.386.982-65',10228,26),('551.135.290-10',18822,18),('537.124.578-35',12670,6),('119.383.169-76',790,20),('938.473.410-98',8851,5),('279.775.182-54',5212,20),('210.872.954-53',13569,8),('684.995.531-65',8649,21),('653.886.282-57',504,28),('973.580.738-53',2533,9),('285.864.892-85',8200,21),('777.154.423-98',10336,8),('769.786.401-34',3233,12),('521.566.565-97',11882,14),('491.799.681-92',653,8),('344.357.819-36',8856,18),('265.362.581-99',8962,8),('331.410.527-56',18516,18),('143.188.958-61',7234,29),('751.630.472-61',13552,6),('714.707.807-80',2898,7),('585.584.932-83',239,25),('165.554.107-13',9572,23),('718.225.984-87',10534,25),('611.715.653-32',3210,11),('397.994.286-79',13651,24),('967.160.575-69',8997,25),('369.750.998-94',13952,2),('767.400.554-79',18320,11),('171.104.286-74',5821,21),('152.817.649-24',3358,30),('645.308.846-62',15176,25),('273.884.570-92',4436,13),('888.818.341-45',15730,3),('577.836.712-40',14670,16),('513.529.919-95',4002,1),('201.476.809-95',17442,21),('657.816.571-87',1582,2),('810.494.975-87',2157,9),('531.749.410-17',12355,18),('486.290.887-24',18576,26),('432.376.642-62',8027,23),('207.274.437-91',5125,29),('634.244.673-72',11387,15),('346.871.172-72',8105,23),('166.330.605-50',7865,11),('829.181.731-94',2425,8),('197.305.464-63',9681,8),('887.877.706-59',15681,10),('847.598.885-51',323,23),('817.170.984-26',5169,27),('591.397.550-29',13362,25),('872.733.198-95',5756,18),('615.629.238-82',11678,23),('194.782.846-77',11044,17),('146.392.158-88',6848,4),('240.427.458-70',3906,25),('583.662.427-52',3306,5),('841.627.523-64',4778,4),('985.337.216-77',15308,4),('912.410.722-57',11683,6),('700.720.266-23',12638,21),('605.405.529-53',3831,3),('383.256.402-25',2599,10),('248.103.486-68',9121,1),('261.974.594-90',2139,26),('297.126.704-91',18529,16),('680.569.318-52',10176,23),('296.334.647-38',225,13),('200.761.898-70',16244,20),('258.232.687-17',19462,18),('597.295.672-38',18840,11),('894.479.102-52',11375,12),('556.156.341-36',16269,23),('987.874.553-86',11253,17),('248.927.998-94',6510,1),('852.796.660-25',2662,23),('741.370.204-36',9303,16),('536.714.951-95',2877,23),('320.395.830-44',14554,5),('520.645.562-80',17547,24),('553.700.674-28',3147,14),('913.525.896-32',17651,28),('750.456.495-86',11524,9),('246.171.748-38',15184,4),('760.248.897-67',4953,25),('920.890.990-46',17172,20),('805.469.913-50',17500,21),('878.594.225-48',6255,3),('356.715.924-36',3454,13),('847.150.802-96',8602,22),('625.846.640-53',10888,19),('539.300.108-41',11225,21),('549.151.467-76',1286,21),('738.451.908-29',18905,22),('987.288.834-69',17533,25),('898.532.296-94',9719,11),('620.531.607-13',13584,10),('169.415.202-43',1871,29),('757.885.355-97',18150,28),('252.581.376-21',2497,3),('177.937.460-78',7178,8),('523.895.611-54',9878,26),('883.680.201-23',16761,3),('936.678.268-71',11017,9),('871.912.703-73',1754,9),('957.749.478-56',6914,9),('725.636.354-80',8605,13),('898.316.244-33',14363,12),('894.748.325-28',2764,3),('647.106.954-60',1482,6),('628.716.937-98',14107,8),('332.677.483-83',19146,15),('186.870.928-82',17050,12),('216.248.879-71',4384,16),('287.929.269-44',4894,19),('278.335.932-42',17220,13),('824.107.287-13',11797,7),('535.354.954-30',9195,22),('311.762.241-12',13871,2),('209.759.133-88',13580,21),('505.728.766-53',16950,13),('879.471.988-23',17427,14),('772.329.947-39',3462,8),('321.123.241-10',2592,22),('407.342.963-78',11435,21),('786.935.637-47',14240,9),('461.791.351-55',142,2),('770.920.161-42',1247,24),('639.870.185-59',6430,10),('815.943.237-83',19550,22),('141.774.255-61',17866,13),('379.995.400-37',9503,29),('261.103.178-64',19167,13),('495.461.913-57',12265,29),('498.848.750-79',14549,16),('578.770.731-84',1462,5),('408.987.269-72',5647,28),('191.970.336-40',6313,15),('761.137.848-34',10654,23),('810.512.154-21',14928,1),('256.371.788-38',7085,2),('216.401.188-57',1531,23),('956.318.620-43',6327,22),('986.516.478-33',3866,25),('105.665.555-60',7118,4),('259.228.430-72',1601,8),('133.627.971-58',10142,14),('327.988.845-70',14985,23),('363.167.322-63',17236,7),('189.986.406-38',16888,18),('661.194.373-45',7824,1),('805.728.877-53',514,10),('887.826.412-21',15977,24),('122.975.174-32',9409,25),('456.550.370-55',19922,18),('388.243.133-66',19785,17),('208.788.890-61',11893,22),('881.332.662-49',6344,16),('912.349.944-52',6858,15),('534.904.583-32',9559,11),('825.175.334-25',19805,15),('339.191.298-46',13325,8),('569.993.915-78',4339,15)]

'''
def identificar_inadimplentes(clientes):
    inadimplentes = []
   
    # Percorre todos os clientes
    for cliente in clientes:
        cpf, valor_devido, dias_devido = cliente
       
        # Verifica se o cliente atende à condição de inadimplência
        if valor_devido > 1000 and dias_devido > 20:
            inadimplentes.append(cpf)
   
    return inadimplentes

# Lista de clientes
clientes_devedores = [
    ('462.286.561-65', 14405, 24), ('251.569.170-81', 16027, 1), ('297.681.579-21', 8177, 28),
    ('790.223.154-40', 9585, 10), ('810.442.219-10', 18826, 29), ('419.210.299-79', 11421, 15),
    ('908.507.760-43', 12445, 24), ('911.238.364-17', 1345, 4), ('131.115.339-28', 11625, 8),
    ('204.169.467-27', 5364, 22), ('470.806.376-11', 932, 29), ('938.608.980-69', 13809, 19),
    ('554.684.165-26', 11227, 2), ('119.225.846-34', 4475, 9), ('358.890.858-95', 13932, 20),
    ('786.547.940-70', 17048, 25), ('468.487.741-94', 2902, 8), ('540.685.100-32', 5806, 21),
    ('379.729.796-80', 7622, 24), ('980.173.363-94', 13167, 24), ('833.285.374-56', 19581, 24),
    ('103.669.436-50', 17126, 4), ('386.836.124-46', 18825, 11), ('588.404.964-15', 1545, 30),
    ('600.556.177-18', 1921, 7), ('670.346.230-99', 18079, 28), ('771.352.915-13', 16581, 23),
    ('430.314.324-46', 13942, 24), ('629.507.759-51', 17951, 11), ('348.683.225-73', 12424, 10),
    ('406.133.151-17', 5888, 30), ('310.985.894-64', 17316, 30), ('964.317.132-30', 18818, 30),
    ('845.331.524-14', 14284, 13), ('781.995.738-18', 19369, 29), ('921.558.128-63', 3206, 27),
    ('941.386.982-65', 10228, 26), ('551.135.290-10', 18822, 18), ('537.124.578-35', 12670, 6),
    ('119.383.169-76', 790, 20), ('938.473.410-98', 8851, 5), ('279.775.182-54', 5212, 20),
    ('210.872.954-53', 13569, 8), ('684.995.531-65', 8649, 21), ('653.886.282-57', 504, 28),
    ('973.580.738-53', 2533, 9), ('285.864.892-85', 8200, 21), ('777.154.423-98', 10336, 8),
    ('769.786.401-34', 3233, 12), ('521.566.565-97', 11882, 14), ('491.799.681-92', 653, 8),
    ('344.357.819-36', 8856, 18), ('265.362.581-99', 8962, 8), ('331.410.527-56', 18516, 18),
    ('143.188.958-61', 7234, 29), ('751.630.472-61', 13552, 6), ('714.707.807-80', 2898, 7),
    ('585.584.932-83', 239, 25), ('165.554.107-13', 9572, 23), ('718.225.984-87', 10534, 25),
    ('611.715.653-32', 3210, 11), ('397.994.286-79', 13651, 24), ('967.160.575-69', 8997, 25),
    ('369.750.998-94', 13952, 2), ('767.400.554-79', 18320, 11), ('171.104.286-74', 5821, 21),
    ('152.817.649-24', 3358, 30), ('645.308.846-62', 15176, 25), ('273.884.570-92', 4436, 13),
    ('888.818.341-45', 15730, 3), ('577.836.712-40', 14670, 16), ('513.529.919-95', 4002, 1),
    ('201.476.809-95', 17442, 21), ('657.816.571-87', 1582, 2), ('810.494.975-87', 2157, 9),
    ('531.749.410-17', 12355, 18), ('486.290.887-24', 18576, 26), ('432.376.642-62', 8027, 23),
    ('207.274.437-91', 5125, 29), ('634.244.673-72', 11387, 15), ('346.871.172-72', 8105, 23),
    ('166.330.605-50', 7865, 11), ('829.181.731-94', 2425, 8), ('197.305.464-63', 9681, 8),
    ('887.877.706-59', 15681, 10), ('847.598.885-51', 323, 23), ('817.170.984-26', 5169, 27),
    ('591.397.550-29', 13362, 25), ('872.733.198-95', 5756, 18), ('615.629.238-82', 11678, 23),
    ('194.782.846-77', 11044, 17), ('146.392.158-88', 6848, 4), ('240.427.458-70', 3906, 25),
    ('583.662.427-52', 3306, 5), ('841.627.523-64', 4778, 4), ('985.337.216-77', 15308, 4),
    ('912.410.722-57', 11683, 6), ('700.720.266-23', 12638, 21), ('605.405.529-53', 3831, 3),
    ('383.256.402-25', 2599, 10), ('248.103.486-68', 9121, 1), ('261.974.594-90', 2139, 26),
    ('297.126.704-91', 18529, 16), ('680.569.318-52', 10176, 23), ('296.334.647-38', 225, 13),
    ('200.761.898-70', 16244, 20), ('258.232.687-17', 19462, 18), ('597.295.672-38', 18840, 11),
    ('894.479.102-52', 11375, 12), ('556.156.341-36', 16269, 23), ('987.874.553-86', 11253, 17),
    ('248.927.998-94', 6510, 1), ('852.796.660-25', 2662, 23), ('741.370.204-36', 9303, 16),
    ('536.714.951-95', 2877, 23), ('320.395.830-44', 14554, 5), ('520.645.562-80', 17547, 24),
    ('553.700.674-28', 3147, 14), ('913.525.896-32', 17651, 28), ('750.456.495-86', 11524, 9),
    ('246.171.748-38', 15184, 4), ('760.248.897-67', 4953, 25), ('920.890.990-46', 17172, 20),
    ('805.469.913-50', 17500, 21), ('878.594.225-48', 6255, 3), ('356.715.924-36', 3454, 13),
    ('847.150.802-96', 8602, 22), ('625.846.640-53', 10888, 19), ('539.300.108-41', 11225, 21),
    ('549.151.467-76', 1286, 21), ('738.451.908-29', 18905, 22), ('987.288.834-69', 17533, 25),
    ('898.532.296-94', 9719, 11), ('620.531.607-13', 13584, 10), ('169.415.202-43', 1871, 29),
    ('757.885.355-97', 18150, 28), ('252.581.376-21', 2497, 3), ('177.937.460-78', 7178, 8),
    ('523.895.611-54', 9878, 26), ('883.680.201-23', 16761, 3), ('936.678.268-71', 11017, 9),
    ('871.912.703-73', 1754, 9), ('957.749.478-56', 6914, 9), ('725.636.354-80', 8605, 13),
    ('898.316.244-33', 14363, 12), ('894.748.325-28', 2764, 3), ('647.106.954-60', 1482, 6),
    ('628.716.937-98', 14107, 8), ('332.677.483-83', 19146, 15), ('186.870.928-82', 17050, 12),
    ('216.248.879-71', 4384, 16), ('287.929.269-44', 4894, 19), ('278.335.932-42', 17220, 13),
    ('824.107.287-13', 11797, 7), ('535.354.954-30', 9195, 22), ('311.762.241-12', 13871, 2),
    ('209.759.133-88', 13580, 21), ('505.728.766-53', 16950, 13), ('879.471.988-23', 17427, 14),
    ('772.329.947-39', 3462, 8), ('321.123.241-10', 2592, 22), ('407.342.963-78', 11435, 21),
    ('786.935.637-47', 14240, 9), ('461.791.351-55', 142, 2), ('770.920.161-42', 1247, 24),
    ('639.870.185-59', 6430, 10), ('815.943.237-83', 19550, 22), ('141.774.255-61', 17866, 13),
    ('379.995.400-37', 9503, 29), ('261.103.178-64', 19167, 13), ('495.461.913-57', 12265, 29),
    ('498.848.750-79', 14549, 16), ('578.770.731-84', 1462, 5), ('408.987.269-72', 5647, 28),
    ('191.970.336-40', 6313, 15), ('761.137.848-34', 10654, 23), ('810.512.154-21', 14928, 1),
    ('256.371.788-38', 7085, 2), ('216.401.188-57', 1531, 23), ('956.318.620-43', 6327, 22),
    ('986.516.478-33', 3866, 25), ('105.665.555-60', 7118, 4), ('259.228.430-72', 1601, 8),
    ('133.627.971-58', 10142, 14), ('327.988.845-70', 14985, 23), ('363.167.322-63', 17236, 7),
    ('189.986.406-38', 16888, 18), ('661.194.373-45', 7824, 1), ('805.728.877-53', 514, 10),
    ('887.826.412-21', 15977, 24), ('122.975.174-32', 9409, 25), ('456.550.370-55', 19922, 18),
    ('388.243.133-66', 19785, 17), ('208.788.890-61', 11893, 22), ('881.332.662-49', 6344, 16),
    ('912.349.944-52', 6858, 15), ('534.904.583-32', 9559, 11), ('825.175.334-25', 19805, 15),
    ('339.191.298-46', 13325, 8), ('569.993.915-78', 4339, 15)
]

# Chama a função para identificar os inadimplentes
devedores = identificar_inadimplentes(clientes_devedores)

# Exibe a lista de inadimplentes (apenas CPFs)
print(clientes_devedores)