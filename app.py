import streamlit as st
import plotly.graph_objs as go
import numpy as np
import math 

#Asosiy matn
st.markdown("<h1 style='color: green;'>TAQRIBIY YECHISH</h1>", unsafe_allow_html=True)

#Funksiya kiritish qo'llanma
if st.button("Funksiya kiritish qo'llanmasi"):
    st.write("1. (ayirish -> -), (qo'shish -> +), (ko'paytrish -> *), bo'lish -> /")
    st.write("2. daraja ko'tarish -> **(n)  ,ildiz hisoblash -> **(1/n), (bu yerda 1/n soni -n inchi darajasi)")
    st.write("3. logarifmik funksiyalar: ln(x),log(x,n)... -> (bu yerda n logarifm asosi) ")
    st.write('4. triginametrik funksiyalar: sin(x),cos(x),tan(x),arcsin(x)..., sh(x)... -> (kamchilik cotangens ni 1/tangens orqali kiritiladi)')
    st.write('5. e^x - e**(x); π - pi ')


#Berilgan funksiyani hisobberuvchi function
def calculate_function(expression, x_value):
    try:
        result = eval(expression, {'__builtins__': None}, 
                                                          {'x': x_value, 
                                                           'e**': math.exp,'pi':math.pi,
                                                           'sin': math.sin, 'arcsin': math.asin,'sh': math.sinh, 'arcsh': math.asinh,
                                                           'cos': math.cos,  'arccos': math.acos,'ch': math.cosh,'arcch': math.acosh,
                                                           'tan': math.tan,  'arctan': math.atan, 'th': math.tanh, 'arcth': math.atanh,
                                                           'ln': math.log,"log":math.log
                                                           
                      })
        return result
        
    except Exception as e:
        return str(e)

#Foydalanuvchi tamonidan kiritilishi kerak
func = st.text_input("Funksiya: ","x**2-9")
c = st.number_input("min: ")
d = st.number_input("max: ")


#Funksiyani grafigi chizish
if st.button('Funksiya grafigi'):
    try:
            
            if func:
                x_values = np.arange(c, d, 0.001)
                y_values = [calculate_function(func, x) for x in x_values]
                y=0/x_values
        
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines',line=dict(color="green"), name='funksiya'))
                fig.add_trace(go.Scatter(x=x_values, y=y, mode='lines',line=dict(color='red'),name='X oqi'))
                fig.update_layout(title=f'funksiya: {func}',
                          xaxis_title='x',
                          yaxis_title='y',
                          xaxis_showgrid=True,
                          yaxis_showgrid=True)
                
                st.plotly_chart(fig)
            else:
                error
    except:
        st.write('Malumotlar hato kiritilgan!')

#Foydalanuvchi tamonidan kiritilishi kerak
func1 = st.text_input("f': ","2*x")
func2 = st.text_input('f": ',"2")
a = st.number_input("a: ")
b = st.number_input("b: ")
ϵ = st.number_input('ϵ: ')

#Yechish usulini tanlash
option = st.selectbox(
    "Yechish usulini tanla:",
    ("1.Kesmani teng ikkiga bo'lish usul:", "2.Vatarlar usuli:", "3.Urunmalar usuli:","4.Urunma (madifiqatsiya) usuli:","Barcha usullarda hisobla"))
kalit = option[0]


#Yechish
if st.button("Yechish: "):
    #Kesmani teng ikkiga bo'lish usuli
    if a==0.00 and b==0.00 and c==0.00:
        st.write("Malumotlar to'liq kiritilmagan")
    
    x_list=[]
    itaratsiya_list=[]
    if kalit=="1":
        try:
            if calculate_function(func,a)*calculate_function(func,b)<0:
                # Iterativ yechim topish
                max_itaratsiya=100
                itaratsiya=0
                
                while abs(a - b) > ϵ:
                    c = (a + b) / 2
                    x_list.append(c)
                    itaratsiya_list.append(itaratsiya+1)
                    
                    if calculate_function(func,c) == 0:
                        break
                    elif calculate_function(func,c) * calculate_function(func,a) < 0:
                        b = c
                    else:
                        a = c
                    itaratsiya+=1  

                    if itaratsiya>100:
                        st.write("itaratsiya 100 dan oshdi")
                    
                st.write('x=',c)
                st.write('itaratsiya= ',itaratsiya)
                
                if len(itaratsiya_list)==len(x_list):
                    fig = go.Figure(data=[go.Bar(x=itaratsiya_list, y=x_list,marker_color="green")])
                    fig.update_layout(xaxis_title="itaratsiyalar", yaxis_title="x")
                    st.plotly_chart(fig)
                else:
                    st.write('hato')
            else:
                st.write('x=yechim mavjud emas!')
        except:
            st.write('x=yechim mavjud emas!')
                    

    #Vatarlar yordamida hisoblash usuli
    x_list=[]
    itaratsiya_list=[]
    if kalit == '2':
            try:
                if calculate_function(func,a)*calculate_function(func,b)<0:
                    #itarativ yechim topish
                    max_itaratsiya=100
                    itaratsiya=0
                
                    if calculate_function(func,a)*calculate_function(func2,a)>0:
                        consta=a
                        xi=b
                    else:
                        consta=b
                        xi=a
                        
                    x_list.append(xi)
                    itaratsiya_list.append(1)
                    xn=xi-(calculate_function(func,xi)*(consta-xi))/(calculate_function(func,consta)-calculate_function(func,xi))
                    
                    while abs(xn-xi)>ϵ and itaratsiya<max_itaratsiya:
                        xi=xn
                        x_list.append(xi)
                        xn=xi-(calculate_function(func,xi)*(consta-xi))/(calculate_function(func,consta)-calculate_function(func,xi))
                        itaratsiya+=1
                        itaratsiya_list.append(itaratsiya)
                    st.write('x=',xn)
                    st.write('itaratsiya= ',itaratsiya)
        
                    if len(itaratsiya_list)==len(x_list):
                        fig = go.Figure(data=[go.Bar(x=itaratsiya_list, y=x_list,marker_color="green")])
                        fig.update_layout(xaxis_title="itaratsiyalar", yaxis_title="x")
                        st.plotly_chart(fig)
                    else:
                        st.write("hato")
                else:
                    st.write('x=yechim mavjud emas!')
            except:
                st.write('x=yechim mavjud emas!')
        
    #Urunmalar yordamida hisoblash usuli
    x_list=[]
    itaratsiya_list=[]
    if kalit=="3":
        try:
            if calculate_function(func,a)*calculate_function(func,b)<0:
                #itaratsiyaviy yechim topish
                max_itaratsiya=100
                itaratsiya=0
                
                if calculate_function(func,a)*calculate_function(func2,a)>0:
                    xi=a
                else:
                    xi=b
                x_list.append(xi)   
                itaratsiya_list.append(1)
                xn=xi-calculate_function(func,xi)/calculate_function(func1,xi)
                
                while abs(xn-xi)>ϵ and itaratsiya<max_itaratsiya:
                    xi=xn
                    xn=xi-calculate_function(func,xi)/calculate_function(func1,xi)
                    itaratsiya+=1
                    x_list.append(xn)
                    itaratsiya_list.append(itaratsiya)
                    
                st.write('x=',xn)       
                st.write('itaratsiya',itaratsiya)
    
                if len(itaratsiya_list)==len(x_list):
                    fig = go.Figure(data=[go.Bar(x=itaratsiya_list, y=x_list,marker_color="green")])
                    fig.update_layout(xaxis_title="itaratsiyalar", yaxis_title="x")
                    st.plotly_chart(fig)
                else:
                    st.write("hato")
            else:
                st.write('x=yechim mavjud emas!')
                
        except:
            st.write('x=yechim mavjud emas!')
        
    #Urunma (modifiqatsiyasi) yordamida hisoblash usuli
    x_list=[]
    itaratsiya_list=[]
    if kalit=='4':
        try:
            if calculate_function(func,a)*calculate_function(func,b)<0:
                #itaratsaviy yechim topish
                max_itaratsiya=100
                itaratsiya=0
                
                if calculate_function(func,a)*calculate_function(func2,a)>0:
                    xi=a
                else:
                    xi=b
                    
                x_list.append(xi)   
                itaratsiya_list.append(1)
                x0=xi
                xn=xi-calculate_function(func,xi)/calculate_function(func1,x0)
                
                while abs(xn-xi)>ϵ and itaratsiya<max_itaratsiya:
                    xi=xn
                    xn=xi-calculate_function(func,xi)/calculate_function(func1,x0)
                    itaratsiya+=1
                    x_list.append(xn)
                    itaratsiya_list.append(itaratsiya)
                    
                st.write('x=',xn)
                st.write('itaratsiya',itaratsiya)
                
                if len(itaratsiya_list)==len(x_list):
                    fig = go.Figure(data=[go.Bar(x=itaratsiya_list, y=x_list,marker_color="green")])
                    fig.update_layout(xaxis_title="itaratsiyalar", yaxis_title="x")
                    st.plotly_chart(fig)
                else:
                    st.write("hato")
            else:
                    st.write('x=yechim mavjud emas!')
                
        except:
            st.write('x=yechim mavjud emas!')
        
#Yukoridagi barchasi hisoblash
    if kalit=='B':
        try:
            if calculate_function(func,a)*calculate_function(func,b)<0:
                try:
                    #Kesmani teng ikkiga bo'lish usuli
                    max_itaratsiya=100
                    itaratsiya=0
                    a1=a
                    b1=b
                    while abs(a1 - b1) > ϵ and itaratsiya<max_itaratsiya:
                        c = (a1 + b1) / 2
                        if calculate_function(func,c) == 0:
                            break
                        elif calculate_function(func,c) * calculate_function(func,a1) < 0:
                            b1 = c
                        else:
                            a1 = c
                        itaratsiya+=1
                    if itaratsiya>100:
                        st.write("itaratsiyalar soni 100 dan oshdi")
                        
                    st.write("1. x= ",c)
                    st.write("itaratsiya=",itaratsiya)
                except:
                    st.write('1. x=yechim mavjud emas!')
    
                try:
                    #Vatarlar yordamida hisoblash usuli
                    max_itaratsiya=100
                    itaratsiya=0
                    a2=a
                    b2=b
                    if calculate_function(func,a2)*calculate_function(func2,a2)>0:
                        consta=a2
                        xi=b2
                    else:
                        consta=b2
                        xi=a2
                    xn=xi-(calculate_function(func,xi)*(consta-xi))/(calculate_function(func,consta)-calculate_function(func,xi))
                    while abs(xn-xi)>ϵ:
                        xi=xn
                        xn=xi-(calculate_function(func,xi)*(consta-xi))/(calculate_function(func,consta)-calculate_function(func,xi))
                        itaratsiya+=1
                        if itaratsiya>100:
                            st.write("itaratsiya 100 dan oshdi")
                            break
                    
                    st.write('2. x=',xn)
                    st.write('itaratsiya= ',itaratsiya)
                except:
                    st.write('2. x=yechim mavjud emas!')
                try:    
                    #Urunmalar yordamida hisoblash usuli
                    max_itaratsiya=100
                    itaratsiya=0
                    a3=a
                    b3=b
                    if calculate_function(func,a3)*calculate_function(func2,a3)>0:
                        xi=a3
                    else:
                        xi=b3
                    xn=xi-calculate_function(func,xi)/calculate_function(func1,xi)
                    while abs(xn-xi)>ϵ:
                        xi=xn
                        xn=xi-calculate_function(func,xi)/calculate_function(func1,xi)
                        itaratsiya+=1
                        
                        if itaratsiya>100:
                            st.write("itaratsiya 100 dan oshdi")
                            break
                    st.write('3. x=',xn)
                    st.write('itaratsiya= ',itaratsiya)
                    
                except:
                    st.write('3. x=yechim mavjud emas!')
    
                try:
                    #Urunma (modifiqatsiyasi) yordamida hisoblash usuli
                    max_itaratsiya=100
                    itaratsiya=0
                    a4=a
                    b4=b
                    if calculate_function(func,a4)*calculate_function(func2,a4)>0:
                        xi=a4
                    else:
                        xi=b4
                    x0=xi
                    xn=xi-calculate_function(func,xi)/calculate_function(func1,x0)
                    while abs(xn-xi)>ϵ:
                        xi=xn
                        xn=xi-calculate_function(func,xi)/calculate_function(func1,x0)
                        itaratsiya+=1
                        if itaratsiya>100:
                            st.write("itaratsiya 100 dan oshdi")
                            break
                    st.write('4. x=',xn)
                    st.write('itaratsiya= ',itaratsiya)
                    
                except:
                    st.write('4. x=yechim mavjud emas!')
            else:
                st.write("Biror usulda yechim mavjud emas!")
        except:
            st.write('Funksiya mavjud emas!')

if st.button("Dastur haqida"):
    st.write("Maqsad: Hisoblash usullari fani uchun transsendent tenglamalarni")
    st.write("1.Kesmani teng ikki bo'lish usuli")
    st.write("2.Vatarlar usuli")
    st.write("3.Urunma usuli")
    st.write("4.Urunma madifiqatsiya usullari orqali kiritilgan oraliqda taqribiy yechimni aniqlaydi")
    st.write("")
    st.write("")
    st.write("")
    st.write("Ishlab chiqdi: Urganchda Davlat Universiteti Fizika-Matematika fakulteti, 211 amaliy matematika talabasi, Xaytyazov Muxammadsodiq Matnazar o'g'li")
    st.write("Dastur qodi: Yuqorida o'ng tarafdagi github belgisi ustiga bosing ↗️")
    st.page_link("https://t.me/my_projects_chanel",label='mening proyektlarim',icon="➡️")
    st.write("Ishlab chiqilgan vaqt: 2024-yil , 3 - kurs bahorgi semestr")
    
