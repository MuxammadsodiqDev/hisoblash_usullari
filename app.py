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
        result = eval(expression, {'__builtins__': None}, {'x': x_value, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'e': math.exp, 'log': math.log})
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
        if calculate_function(func, x):
            x_values = np.arange(a, b, ϵ)
            y_values = [calculate_function(func, x) for x in x_values]
            y=0/x_values
    
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines',line=dict(color="green"), name='funksiya'))
            fig.add_trace(go.Scatter(x=x_values, y=y, mode='lines',line=dict(color='red'),name='X oqi'))
            fig.update_layout(title=f'funksiya: {func}',
                            xaxis_title='x',
                            yaxis_title='y')
            st.plotly_chart(fig)
    except:
        st.write('Malumotlar hato kiritilgan!')

#Kesmani teng ikkiga bo'lish usuli
if st.button('1.Kesmani teng ikkiga bo\'lish usuli'):
    try:
        if calculate_function(func,a)*calculate_function(func,b)<0:
            # Iterativ yechim topish
            while abs(a - b) > ϵ :
                c = (a + b) / 2
                if calculate_function(func,c) == 0:
                    break
                elif calculate_function(func,c) * calculate_function(func,a) < 0:
                    b = c
                else:
                    a = c
            
            st.write('x=',c)
    except:
        st.write('x=yechim mavjud emas!')
                    

#Vatarlar yordamida hisoblash usuli
if st.button('2.Vatarlar usuli'):
    try:
        if calculate_function(func,a)*calculate_function(func,b)<0:
            if calculate_function(func,a)*calculate_function(func2,a)>0:
                consta=a
                xi=b
            else:
                consta=b
                xi=a
            xn=xi-(calculate_function(func,xi)*(consta-xi))/(calculate_function(func,consta)-calculate_function(func,xi))
            while abs(xn-xi)>ϵ:
                xi=xn
                xn=xi-(calculate_function(func,xi)*(consta-xi))/(calculate_function(func,consta)-calculate_function(func,xi))
            st.write('x=',xn)        
    except:
        st.write('x=yechim mavjud emas!')
        
#Urunmalar yordamida hisoblash usuli
if st.button('3.Urunma usuli'):
    try:
        if calculate_function(func,a)*calculate_function(func,b)<0:
            if calculate_function(func,a)*calculate_function(func2,a)>0:
                xi=a
            else:
                xi=b
            xn=xi-calculate_function(func,xi)/calculate_function(func1,xi)
            while abs(xn-xi)>ϵ:
                xi=xn
                xn=xi-calculate_function(func,xi)/calculate_function(func1,xi)
            st.write('x=',xn)       
    except:
        st.write('x=yechim mavjud emas!')
        
#Urunma (modifiqatsiyasi) yordamida hisoblash usuli
if st.button('4.Urunma (modifiqatsiya) usuli'):
    try:
        if calculate_function(func,a)*calculate_function(func,b)<0:
            if calculate_function(func,a)*calculate_function(func2,a)>0:
                xi=a
            else:
                xi=b
            x0=xi
            xn=xi-calculate_function(func,xi)/calculate_function(func1,x0)
            while abs(xn-xi)>ϵ:
                xi=xn
                xn=xi-calculate_function(func,xi)/calculate_function(func1,x0)
            st.write('x=',xn)
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
