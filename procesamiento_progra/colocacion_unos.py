def colocacion_horarios(horario, horarios_list, m):
    index_inicial = 0
    index_final = 0

    if horario == horarios_list[0]: # 8 a 14 
        index_inicial =25
        index_final = 29
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[1]: # 8 30 a 14 30
        index_inicial =26
        index_final = 30
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[2]: # 9 a 15
        index_inicial =27
        index_final = 31
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[3]: # 9 30 a 15 30
        index_inicial =28
        index_final = 32
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[4]: # 10:00 a 16:00
        index_inicial =29
        index_final = 33
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[5]: # 10 30 a 16 30
        index_inicial =30
        index_final = 34
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[6]: # 11 a 17
        index_inicial =31
        index_final = 35
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[7]: # 11 30 a 17 30
        index_inicial =32
        index_final = 36
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[8]: # 12 a 18
        index_inicial =33
        index_final = 37
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[9]:# 12 30 a 18 30
        index_inicial =34
        index_final = 38
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[10]: # 13 a 19
        index_inicial =35
        index_final = 39
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[11]: # 13 30 a 19 30
        index_inicial =36
        index_final = 40
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[12]: # 14 a 20
        index_inicial =37
        index_final = 41
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[13]: # 14 30 a 20 30
        index_inicial =38
        index_final = 42
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[14]: # 15 a 21
        index_inicial =39
        index_final = 43
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[15]: # 15 30 a 21 30
        index_inicial =40
        index_final = 44
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[16]: # 16 a 22
        index_inicial =41
        index_final = 45
        m[index_inicial : index_final] = 1
        m[index_final] = "CO"
        m[index_final + 1: index_final + 4] = 1
        m[index_final + 4] = "R"
        m[index_final + 5: index_final + 8] = 1
    elif horario == horarios_list[17]: # Licencia
        index_inicial =25
        index_final = 36
        m[index_inicial : index_final] = "A"

    elif horario == horarios_list[18]: # 8 a 13
        index_inicial =25
        index_final = 47
        m[index_inicial : index_final] = 1
   
    elif horario == horarios_list[19]: # 8 a 15 30
        index_inicial =25
        index_final = 40
        m[index_inicial : index_final] = 1

    elif horario == horarios_list[20]: # 9  16 30
        index_inicial =27
        index_final = 42
        m[index_inicial : index_final] = 1
     
    elif horario == horarios_list[21]: # 9 a 19
        index_inicial =27
        index_final = 47
        m[index_inicial : index_final] = 1
  
    elif horario == horarios_list[22]:  # 9 30 a 17
        index_inicial =28
        index_final = 43
        m[index_inicial : index_final] = 1
        
    elif horario == horarios_list[23]: # 10 a 17 30
        index_inicial =29
        index_final = 44
        m[index_inicial : index_final] = 1
    
    elif horario == horarios_list[24]: # 11 a 18 30 
        index_inicial =31
        index_final = 48
        m[index_inicial : index_final] = 1
        
    elif horario == horarios_list[25]: # 11 30 a 19
        index_inicial =32
        index_final = 47
        m[index_inicial : index_final] = 1
    elif horario == horarios_list[26]: # 12 30 a 20
        index_inicial =34
        index_final = 49
        m[index_inicial : index_final] = 1
    elif horario == horarios_list[27]: # 13 30 a 21
        index_inicial =32
        index_final = 47
        m[index_inicial : index_final] = 1
    elif horario == horarios_list[28]: # 11 30 a 19
        index_inicial =32
        index_final = 47
        m[index_inicial : index_final] = 1

    elif horario == horarios_list[29]: # 08:30 a 15:30
        index_inicial =26
        index_final = 40
        m[index_inicial : index_final] = 1
    elif horario == horarios_list[30]: # 14:00 a 21:30
        index_inicial =37
        index_final = 51
        m[index_inicial : index_final] = 1



# faltan horas 08:00 a 13:00
# Falta 14:00 a 21:30

