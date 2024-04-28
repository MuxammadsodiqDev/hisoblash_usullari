import streamlit as st
import plotly.graph_objs as go
import numpy as np
import math 

#Asosiy matn
st.markdown("<h1 style='color: green;'>HISOBLASH USULLARI</h1>", unsafe_allow_html=True)

#Funksiya kiritish qo'llanma
if st.button("Funksiya kiritish qo'llanmasi"):
    st.write("1. ayirish: -  ,qo'shish: +  ,ko'paytrish: *, bo'lish: /")
    st.write("2. daraja ko'tarish,  ** ,ildiz hisoblash: **(1/n)")
    st.write("3. logarifmik funksiyalar: log(x),log10(x)... ")
    st.write('4. triginametrik funksiyalar: sin(x),cos(x),tan(x) ...')
    st.write('5. e^x - e(x); π - pi ')

#Berilgan funksiyani hisobberuvchi function
def calculate_function(expression, x_value):
    try:
        
        result = eval(expression, {'__builtins__': None}, 
                                                          {'x': x_value, 
                                                           'e': math.exp,'pi':math.pi,
                                                           'sin': math.sin, 'arcsin': math.asin,'sh': math.sinh, 'arcsh': math.asinh,
                                                           'cos': math.cos,  'arccos': math.acos,'ch': math.cosh,'arcch': math.acosh,
                                                           'tan': math.tan,  'arctan': math.atan, 'th': math.tanh, 'arcth': math.atanh,
                                                           'log': math.log, 'log2':math.log:math.log(2),'log3': math.log:math.log(3),'log4': math.log:math.log(4),'log5': math.log:math.log(5),
                                                           'log6': math.log:math.log(6),'log7': math.log:math.log(7),'log8': math.log:math.log(8),'log9': math.log:math.log(9),'log10': math.log:math.log(10)
                                                           
                      })
        return result
        
    except Exception as e:
        return str(e)

#Foydalanuvchi tamonidan kiritilishi kerak
func = st.text_input("Funksiya: ","x**2-9")
func1 = st.text_input("Funksiyaning 1-tartibli hosilasi: ","2*x")
func2 = st.text_input("Funksiyaning 2-tartibli hosilasi: ","2")

a = st.number_input("oraliqni boshlang'ich qiymati: ")
b = st.number_input("oraliqni oxirgi qiymati: ")
ϵ = st.number_input('hatolik: ')

#Funksiyani grafigi chizish
if st.button('Funksiya grafigi'):
    try:
        if func:
            x_values = np.arange(a, b, ϵ)
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

#Kesmani teng ikkiga bo'lish usuli
if st.button('1.Kesmani teng ikkiga bo\'lish usuli'):
    try:
        if calculate_function(func,a)*calculate_function(func,b)<0:
            # Iterativ yechim topish
            max_itaratsiya=100
            itaratsiya=0
        
            while abs(a - b) > ϵ and itaratsiya<max_itaratsiya:
                c = (a + b) / 2
                if calculate_function(func,c) == 0:
                    break
                elif calculate_function(func,c) * calculate_function(func,a) < 0:
                    b = c
                else:
                    a = c
                itaratsiya+=1
            st.write('x=',c)
            st.write('itaratsiya= ',itaratsiya)
    except:
        st.write('x=yechim mavjud emas!')
                    

#Vatarlar yordamida hisoblash usuli
if st.button('2.Vatarlar usuli'):
    try:
        if calculate_function(func,a)*calculate_function(func,b)<0:
            #itarativ yechim topish
            max_itaratsiya1=100
            itaratsiya1=0
        
            if calculate_function(func,a)*calculate_function(func2,a)>0:
                consta=a
                xi=b
            else:
                consta=b
                xi=a
            xn=xi-(calculate_function(func,xi)*(consta-xi))/(calculate_function(func,consta)-calculate_function(func,xi))
            while abs(xn-xi)>ϵ and itaratsiya1<max_itaratsiya1:
                xi=xn
                xn=xi-(calculate_function(func,xi)*(consta-xi))/(calculate_function(func,consta)-calculate_function(func,xi))
                itaratsiya1+=1
            st.write('x=',xn)
            st.write('itaratsiya= ',itaratsiya1)
    except:
        st.write('x=yechim mavjud emas!')
        
#Urunmalar yordamida hisoblash usuli
if st.button('3.Urunma usuli'):
    try:
        if calculate_function(func,a)*calculate_function(func,b)<0:
            #itaratsiyaviy yechim topish
            max_itaratsiya2=100
            itaratsiya2=0
            
            if calculate_function(func,a)*calculate_function(func2,a)>0:
                xi=a
            else:
                xi=b
            xn=xi-calculate_function(func,xi)/calculate_function(func1,xi)
            while abs(xn-xi)>ϵ and itaratsiy2<max_itaratsiya2:
                xi=xn
                xn=xi-calculate_function(func,xi)/calculate_function(func1,xi)
                itaratsiya+=1
            st.write('x=',xn)       
            st.write('itaratsiya',itaratsiya)
    except:
        st.write('x=yechim mavjud emas!')
        
#Urunma (modifiqatsiyasi) yordamida hisoblash usuli
if st.button('4.Urunma (modifiqatsiya) usuli'):
    try:
        if calculate_function(func,a)*calculate_function(func,b)<0:
            #itaratsaviy yechim topish
            max_itaratsiya3=100
            itaratsiya3=0
            
            if calculate_function(func,a)*calculate_function(func2,a)>0:
                xi=a
            else:
                xi=b
            x0=xi
            xn=xi-calculate_function(func,xi)/calculate_function(func1,x0)
            while abs(xn-xi)>ϵ and itaratsiya3<max_itaratsiya3:
                xi=xn
                xn=xi-calculate_function(func,xi)/calculate_function(func1,x0)
                itaratsiya+=1
            st.write('x=',xn)
            st.write('itaratsiya',itaratsiya)
    except:
        st.write('x=yechim mavjud emas!')
        
#Yukoridagi barchasi hisoblash
if st.button('Barchasini hisoblash'):
    try:
        if calculate_function(func,a)*calculate_function(func,b)<0:
            try:
                #Kesmani teng ikkiga bo'lish usuli
                a1=a
                b1=b
                while abs(a1 - b1) > ϵ:
                    c = (a1 + b1) / 2
                    if calculate_function(func,c) == 0:
                        break
                    elif calculate_function(func,c) * calculate_function(func,a1) < 0:
                        b1 = c
                    else:
                        a1 = c
                st.write("1. x= ",c)
            except:
                st.write('1. x=yechim mavjud emas!')

            try:
                #Vatarlar yordamida hisoblash usuli
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
                st.write('2. x=',xn)
            except:
                st.write('2. x=yechim mavjud emas!')
            try:    
                #Urunmalar yordamida hisoblash usuli
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
                st.write('3. x=',xn)
            except:
                st.write('3. x=yechim mavjud emas!')

            try:
                #Urunma (modifiqatsiyasi) yordamida hisoblash usuli
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
                st.write('4. x=',xn)
            except:
                st.write('4. x=yechim mavjud emas!')
    except:
        st.write('Funksiya mavjud emas!')
