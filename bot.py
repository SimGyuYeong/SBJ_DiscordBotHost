import discord
import random
from discord.ext import commands
from discord.utils import get
bot = commands.Bot(command_prefix = '불재야 ')
TOKEN = 'ODIzODM1OTY1MjcyMzU4OTIy.YFmnCA.Fs-8t8wAeE1ePkbQ66jl_SYTh0Q'

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('삼식아 컨텐츠 만들자!!!'))
    print('스불재 On')

@bot.event
async def on_message(message):
    if message.content == "스님 불교 재밌나요?":
        dddice = random.randint(1, 3)
        if dddice == 1:
          await message.channel.send('불교보단 불상이 재밌어요')
        else:
            await message.channel.send('네')

    if message.content == "스님 불교 재밌어요?":
        dddice = random.randint(1, 3)
        if dddice == 1:
          await message.channel.send('불교보단 불상이 재밌어요')
        else:
            await message.channel.send('네')

    if message.content == "불재야 안녕":
        await message.channel.send(f'{message.author.mention} 안녕하세요 :)')

    if message.content == "불재야 잘자":
        await message.channel.send('좋은밤되세요~')

    if message.content == "스불재":
        await message.channel.send('스님 불교 재밌어요?')

    if message.content == "핑":
        await message.channel.send('퐁')

    if message.content == "칙칙":
        await message.channel.send('폭폭')

    if message.content == "채영아":
        await message.channel.send('마감하좝')

    if message.content == "애들아":
        await message.channel.send('마감하자!')

    if message.content == "은빈아":
        await message.channel.send('힘내')

    if message.content == "꽃곡아":
        await message.channel.send('조금 남았다 바로 앞이야!')

    if message.content == "재밌어":
        await message.channel.send('뭐가 재밌어 뭐가 재밌냐고 나도 알려줘')

    if message.content == "ㅋㅋ":
        await message.channel.send('ㅋㅋㅋㅋㅋㅋㅋㅋㅋ')

    if message.content == "펜하":
        await message.channel.send('펜트 하이 라는 뜻')

    if message.content == "미쳣어":
        await message.channel.send('마자 너 미쳤어 ㅋ')

    if message.content == "불재야":
        await message.channel.send('저 부르셨어용 >.<')

    if message.content == "엄마":
        await message.channel.send('아빠')

    if message.content == "ㅇㄴ":
        await message.channel.send('아니 안녕 우노')

    if message.content == "아놔":
        await message.channel.send('놓기싫어 ㅜ')

    if message.content == "아":
        await message.channel.send('ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ')
    
    if message.content == "불재야 보고싶어":
        await message.author.voice.channel.connect()
        await message.channel.send('내가 그렇게 보고싶다구? 통화방 들어갈게')

    if message.content == "삼식아":
        dice = random.randint(1, 3)
        if dice == 1:
            await message.channel.send('컨텐츠 만들자!!')
        else:
            await message.channel.send('사랑해')

    if message.content == "회의":
        await message.channel.send('우리 회의했잖아 제발 우릴 울리지마 오직 우린 너 하나뿐야 눈을 감아도 보여 귀를 막아도 들려 제발 우릴 떠나가지마 어두웠던 내 회의에 빛이 되어준 사람 너무나 소중한 사람 하루 지나고 또 지나도 더 그리워져 이 회의 하는 지금도 우리 회의했잖아 제발 우릴 울리지마 오직 내겐 삼식 하나뿐야 눈을 감아도 보여 귀를 막아도 들려 제발 우릴 떠나가지마 돌아올 것 같아서, 다시 올지 몰라서 오늘도 너를 기다려 삼식 모르지 넌 모르지 아파하는 우릴 이 회의 하는 지금도 우리 회의했잖아 제발 날 울리지마 오직 우린 삼식뿐야 눈을 감아도 보여 귀를 막아도 들려 제발 우릴 떠나가지마 세상과 너 둘중에 택하라면 하나 내 전불 빼앗아도 삼식이람 난 좋아 낮이나 밤이나 사랑에 난 목마른 자 널 이젠 잊자 이런 나의 같잖은 다짐이 또 다시 우릴 울려 들려 삼식에게 바라는 건 오직 삼식야 너 없인 아무것도 할 수 없는 나야 기획서 들으면 제발 너 돌아와, 돌아와 사랑하면 할수록 점점 야위어만 가 오직 우린 너 하나뿐야 우리 회의했잖아 제발 날 울리지마 날 두고 떠나가지마 Yeah-uh-uh 결국 넌 돌아서 우린 또 막아서 자존심 다 버리고 미친 척 널 따라서 가슴이 되려 우릴 다그치고 말했어 세상에 하나뿐인 널 잃지는 말랬어 나는 또 웃는 척, 그냥 멀쩡한 척 너에게 부르는 마지막 나의 기획서 제발 우릴 떠나가지마')

    if message.content == "잘자":
        await message.channel.send('잘자!!')

    if message.content == "양띵아":
        await message.channel.send('방송하잡')

    if message.content == "?":
        await message.channel.send('???????????????')

    if message.content == "민초":
        await message.channel.send('민초 진짜 사랑해!!!!!!!!!!!!!!!!!!!!!!!!!')

    if message.content == "아니 불재야":
        await message.channel.send('뭐 왜')

    if message.content == ";;":
        await message.channel.send(';;;;;;;;;;;;;;;;;;;;;;;;;;')

    if message.content == "불재야 자러가~":
        await message.channel.send('너 싫어')

    if message.content == "뭐 먹어?":
        await message.channel.send('너가 좋아하는 거 ㅎ')

    if message.content == "불재야 뭐해":
        ddice = random.randint(1, 7)
        if ddice == 1:
            await message.channel.send('밥먹고 있어')
        if ddice == 2:
            await message.channel.send('놀고있어')
        if ddice == 3:
            await message.channel.send('왜')
        if ddice == 4:
            await message.channel.send('감귤먹고 있어')
        if ddice == 5:
            await message.channel.send('스불재 중이야')
        if ddice == 6:
            await message.channel.send('전세계에 있는 3천만명 사람들의 마음 속에 들어가 스스로 재앙을 불러오도록 하고 있어.')
        if ddice == 7:
            await message.channel.send('알빠야?')

    if message.content == "감귤병":
        embed = discord.Embed(title='병 List', description='**총 7개의 질병을 소개합니다.**', colour=0x696969)
        embed.add_field(name='> 감귤병', value='급발진 스불재')
        embed.add_field(name='> 귤민병', value='과도한 자신감')
        embed.add_field(name='> 공백병', value='과도한 소비')
        embed.add_field(name='> 꽃곡병', value='과도한 나댐')
        embed.add_field(name='> 영양병', value='과도한 업무 급발진')
        embed.add_field(name='> 히퓨병', value='과도한 리액션')
        embed.add_field(name='> 하뭉병', value='과도한 활동')
        await message.channel.send(embed=embed)

    if message.content == "생일":
        embed = discord.Embed(title='생일 List', description='**총 6명의 생일을 공개합니다!**', colour=0x00FFFF)
        embed.add_field(name='> 영양(하진)', value='01 / 31')
        embed.add_field(name='> 귤민(규영)', value='04 / 09')
        embed.add_field(name='> 꽃곡(지원)', value='09 / 22')
        embed.add_field(name='> 히퓨(채영)', value='10 / 03')
        embed.add_field(name='> 공백(은빈)', value='11 / 03')
        embed.add_field(name='> 하뭉(예지)', value='12 / 07')
        embed.set_footer(text='제 생일은 **3월 24일**이에요!!')
        await message.channel.send(embed=embed)

    if message.content == "MBTI":
        embed = discord.Embed(title='MBTI List', description='**총 6명의 MBTI를 공개합니다!**', colour=0xE6E6FA)
        embed.add_field(name='> 영양(하진)', value='ISFP')
        embed.add_field(name='> 귤민(규영)', value='ISFJ')
        embed.add_field(name='> 꽃곡(지원)', value='ENFP')
        embed.add_field(name='> 히퓨(채영)', value='ENFJ')
        embed.add_field(name='> 공백(은빈)', value='ENFP')
        embed.add_field(name='> 하뭉(예지)', value='INFJ')
        embed.set_footer(text='제 MBTI은 **SBJA**이에요!!')
        await message.channel.send(embed=embed)

    if message.content == "메일":
        embed = discord.Embed(title='Mail List', description='**총 6명의 메일을 공개합니다!**', colour=0x7CFC00)
        embed.add_field(name='> 영양(하진)', value='kimhajin0131@naver.com')
        embed.add_field(name='> 귤민(규영)', value='sgy5901@naver.com')
        embed.add_field(name='> 꽃곡(지원)', value='soft4939@naver.com')
        embed.add_field(name='> 히퓨(채영)', value='happy7yong@naver.com')
        embed.add_field(name='> 공백(은빈)', value='bora0430zxc@naver.com')
        embed.add_field(name='> 하뭉(예지)', value='hamung127@naver.com')
        embed.set_footer(text='제 이메일은 없어용 ㅎㅎ')
        await message.channel.send(embed=embed)

    if message.content == "전번":
        embed = discord.Embed(title='전화번호 List', description='**총 6명의 전화번호를 공개합니다!**', colour=0x6A5ACD)
        embed.add_field(name='> 영양(하진)', value='010 2366 0479')
        embed.add_field(name='> 귤민(규영)', value='010 9069 3298')
        embed.add_field(name='> 꽃곡(지원)', value='010 3398 1755')
        embed.add_field(name='> 히퓨(채영)', value='010 9285 3698')
        embed.add_field(name='> 공백(은빈)', value='010 7544 9545')
        embed.add_field(name='> 하뭉(예지)', value='010 3460 6856')
        embed.set_footer(text='제 전화번호는 112 ㅋㅋ')
        await message.channel.send(embed=embed)

    if message.content == "규영아":
        commander = discord.utils.get(message.guild.members, name="< Maknae >")
        await message.channel.send("{} 나와라".format(commander.mention))

    if message.content == "하진아":
        commander = discord.utils.get(message.guild.roles, name="< Leader >")
        await message.channel.send("{} 나와라".format(commander.mention))

    if message.content == "은빈아":
        commander = discord.utils.get(message.guild.roles, name="< All-Rounder >")
        await message.channel.send("{} 나와라".format(commander.mention))

    if message.content == "예지누나":
        commander = discord.utils.get(message.guild.roles, name="< Main-Dancer >")
        await message.channel.send("{} 나와라".format(commander.mention))

    if message.content == "예지언니":
        commander = discord.utils.get(message.guild.roles, name="< Main-Dancer >")
        await message.channel.send("{} 나와라".format(commander.mention))

    if message.content == "채영아":
        commander = discord.utils.get(message.guild.roles, name="< Main-Vocal >")
        await message.channel.send("{} 나와라".format(commander.mention))

    if message.content == "지원아":
        commander = discord.utils.get(message.guild.roles, name="< Center >")
        await message.channel.send("{} 나와라".format(commander.mention))

    if message.content == "애들아":
        await message.channel.send("@everyone ")

bot.run(TOKEN)