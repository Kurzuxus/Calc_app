import flet as ft



Data={
    'RM':3,
    'Literary Discourse':3,
    'Civilization':2,
    'MENA':2,
    'PD':2,
    'MAT':2,
    'Open Source':2,
    'Ethics':1
}

Results=[]
Notes=[]
class Main_view(ft.View):
    def __init__(self,route,width,height,**kwargs):
        super().__init__(**kwargs)
        self.bgcolor='#faf5fe'
        self.width=width
        self.height=height
        self.vertical_alignment=ft.MainAxisAlignment.CENTER
        self.horizontal_alignment=ft.CrossAxisAlignment.CENTER
        self.scroll=ft.ScrollMode.AUTO


    def Title_heading(self):
        Title=ft.Text('Average Calculator',
                    color='black',
                    font_family='Century Gothic',
                    size=22,
                    weight=ft.FontWeight.W_500)
        
        Subtitle=ft.Text('(Results may not be entirely accurate)',
                    color='black',
                    font_family='Century Gothic',
                    size=14,
                    weight=ft.FontWeight.W_200)
        
        return ft.Column(controls=[Title,Subtitle],
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.START,
                        width=self.width)


    def Main_body(self):

        def List_creation(name,cof):

            if cof==1:
                Tilelist=ft.ListTile(
                    leading=ft.Text(
                        value=name,
                        font_family='Century Gothic',
                        color='black',
                        size=12,
                        width=100),
                    title=ft.TextField(
                        border_color='transparent',
                        border_radius=20,
                        bgcolor='#F36940',
                        height=60,
                        helper_text=cof,
                        suffix_text='/20',
                        label='Exam',
                        width=100,
                        helper_style=ft.TextStyle(
                            color='black',
                            font_family='Century Gothic'),

                        suffix_style=ft.TextStyle(
                            color='black',
                            font_family='Century Gothic',
                            size=20),
                        
                        label_style=ft.TextStyle(
                            color='black',
                            font_family='Century Gothic',
                            size=15),

                        text_style=ft.TextStyle(
                            color='black',
                            font_family='Century Gothic',
                            size=20)
                    ),
                    bgcolor='#F5EBFD',
                    width=350,
                    title_alignment=ft.ListTileTitleAlignment.CENTER
                )
            else:
                Tilelist=ft.ListTile(
                    leading=ft.Text(
                        value=name,
                        font_family='Century Gothic',
                        color='black',
                        size=12,
                        width=100),
                    title=ft.TextField(
                        border_color='transparent',
                        border_radius=20,
                        bgcolor='#F36940',
                        height=60,
                        helper_text=cof,
                        suffix_text='/20',
                        label='Exam',
                        width=100,
                        helper_style=ft.TextStyle(
                            color='black',
                            font_family='Century Gothic'),

                        suffix_style=ft.TextStyle(
                            color='black',
                            font_family='Century Gothic',
                            size=12),
                        
                        label_style=ft.TextStyle(
                            color='black',
                            font_family='Century Gothic',
                            size=15),

                        text_style=ft.TextStyle(
                            color='black',
                            font_family='Century Gothic',
                            size=20)
                    ),

                    trailing=ft.TextField(
                        border_color='transparent',
                        border_radius=20,
                        bgcolor='#F36940',
                        height=80,
                        suffix_text='/20',
                        label='Test',
                        width=100,
                        helper_style=ft.TextStyle(
                            color='black',
                            font_family='Century Gothic'),

                        suffix_style=ft.TextStyle(
                            color='black',
                            font_family='Century Gothic',
                            size=20),
                        
                        label_style=ft.TextStyle(
                            color='black',
                            font_family='Century Gothic',
                            size=15),

                        text_style=ft.TextStyle(
                            color='black',
                            font_family='Century Gothic',
                            size=20)
                    ),
                    bgcolor='#F5EBFD',
                    width=350,
                    title_alignment=ft.ListTileTitleAlignment.CENTER
                )                
            return Tilelist
        
        def Anim(e):
            if e.data=='true':
                e.control.scale=1.10
            else:
                e.control.scale=1
            
            e.control.update()

        def notification():
            Dialog=ft.AlertDialog(title=ft.Text('Please Enter the information correctly',
                                        font_family='Century Gothic',
                                        weight='bold',
                                        color='black'),
                                bgcolor='white')
            return self.page.open(Dialog)
        
        def getall():
            Results.clear()
            for item in Main_cont.content.controls:
                try:
                    exam=float(item.title.value)
                    td=float(item.trailing.value) if item.trailing else 0
                    cof=int(item.title.helper_text)
                    if exam > 20 or td >20:
                        print('maximum')
                        return 0
                    Results.append((cof,exam,td))
                except ValueError:
                    return 0
            return Results
        
        def calculations():
            Notes.clear()
            feedback:list=getall()
            if feedback==0:
                notification()
            else:
                for module in Results:
                    cof,exam,test=module
                    if cof==3:
                        equation = ((exam * 0.6 + test * 0.4) * cof)
                        Notes.append(equation)
                    else:
                        equation=(exam*cof)
                        Notes.append(equation) 
                Average=round(((sum(Notes)/17)),2)
                
                self.Score_field.value=None
                self.Score_field.value=Average

                self.update()

        def Delete():
            Results.clear()
            for widget in Main_cont.content.controls:
                widget.title.value=None
                if widget.trailing:
                    widget.trailing.value= None
                else:
                    pass
                
                widget.update()


        Main_cont=ft.Container(
            bgcolor='#F5EBFD',
            width=self.width,
            height=self.height,
            border_radius=20,
            alignment=ft.alignment.center,
            content=ft.Column(expand=True,
                        spacing=0,
                        wrap=True,
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        scroll=ft.ScrollMode.AUTO))

        for data in Data.items():
            name=data[0]
            cof=data[1]
            Main_cont.content.controls.append(List_creation(name,cof))
        

        self.Score_field=ft.TextField(
            width=200,
            border_color=200,
            bgcolor='#F36940',
            border_radius=20,
            border_width=0,
            label='Your Score',
            label_style=ft.TextStyle(
                font_family='Century Gothic',
                color='black',
                size=20),
            disabled=True,
            text_style=ft.TextStyle(
                font_family='Century Gothic',
                size=20,
                color='black',
                weight='bold'),
        )

        self.Submit_bu=ft.ElevatedButton(text='Submit',
                    bgcolor='#9823F1',
                    style=ft.ButtonStyle(
                        color='white',
                        text_style=ft.TextStyle(
                            font_family='Century Gothic',
                            size=20,
                            weight='bold'
                        )),
                    width=100,
                    height=45,
                    scale=1,
                    animate_scale=ft.animation.Animation(300,ft.AnimationCurve.FAST_OUT_SLOWIN),
                    on_hover=lambda e: Anim(e),
                    on_click=lambda e: calculations())

        self.Delete_bu=ft.ElevatedButton(text='Clear',
                    bgcolor='#F67293',
                    style=ft.ButtonStyle(
                        color='white',
                        text_style=ft.TextStyle(
                            font_family='Century Gothic',
                            size=16,
                            weight='bold'
                        )),
                    width=70,
                    height=45,
                    scale=1,
                    animate_scale=ft.animation.Animation(300,ft.AnimationCurve.FAST_OUT_SLOWIN),
                    on_hover=lambda e: Anim(e),
                    on_click=lambda e: Delete())

        self.Info=ft.IconButton(ft.Icons.INFO_OUTLINE_ROUNDED,
                        tooltip='Made By Baroudi Sidahmed',
                        icon_color='black')
        return Main_cont
    
    def build(self):
        return [self.Title_heading(),self.Main_body(),ft.Row(height=50,
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            vertical_alignment=ft.CrossAxisAlignment.START,
                                                            controls=[self.Score_field,self.Submit_bu,self.Delete_bu,self.Info])]




def main(page: ft.Page):
    page.fonts={
        'Century Gothic':r'fonts\GOTHIC.TTF'
    }
    page.scroll=ft.ScrollMode.AUTO
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    page.theme_mode=ft.ThemeMode.LIGHT

    View=Main_view(route='/Main',width=page.width,height=page.height)
    page.views.append(View)
    page.update()
    page.add(ft.Text('If you see this, ya fucked up'))
    page.go('/Main')
    page.update()





ft.app(main,assets_dir='assets')




