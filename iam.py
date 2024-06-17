from pywebio import start_server
from pywebio.input import*
from pywebio.output import *
def say():
    put_image(open('C:\\Qurran.jpg','rb',).read()).style('width:1000px;height:400px;')
    
    put_html('''
    <h2>تطبيق القران الكريم</h2>
    <p>اهلا وسهلا بكم في تطبيقنا الجديد</p>
     <ul>
           <li>-حفظ القران الكريم</li>
             <li>-احاديث نبويه</li>  
             <li>-تفسير القران الكريم</li>
             </ul>
<hr>
<h3> 1)-الشيخ ماهر المعيقلي</h3>




''')
    put_table([
        ['ترتيب السوره','اسم السوره','اسم القارئ','الملف الصوتي','الملف النصي'],
        ['1','الفاتحه','ماهر المعيقلي',put_html('<audio controls><source src = "https://i.top4top.io/m_2662c9q881.mp3"type="audio/mp3"></audio>'),put_html('<file.txt>بسم الله الرحمن الرحيم الحمد لله رب العالمين الرحمن الرحيم مالك يوم الدين اياك نعبد و اياك  نستعين اهدنا الصراط المستقيم صراط الذين انعمت عليهم غير المغضوب عليهم ولا الضالين امين صدق الله العظيم</file.txt>')],
        ['2','البقره','ماهر المعيقلي',put_html('<audio controls><source src = "" type="audio/mp3"></audio>'),""],
        ['3','ال عمران','ماهر المعيقلي',put_html('<audio controls><source src = "" type="audio/mp3"></audio>'),''],
        ['4','النساء','ماهر المعيقلي',put_html('<audio controls><source src = "" type="audio/mp3"></audio>'),''],
        ['5','المائده','ماهر المعيقلي',put_html('<audio controls><source src = "" type="audio/mp3"></audio>'),'']

    ]).style('width:1000px;height:400px;')
start_server(say , port=1234 ,debug= True)
