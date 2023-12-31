# Список спуки-сообщений

import random



def spooky_message():
    '''Присылает случайное спуки-сообщение'''

    messages = [
        "Мама, я не вижу света больше... и я не вижу тебя. Помоги мне, пожалуйста!",
        "Слёзы текут, но мои слепые глаза не могут их увидеть. Этот мир - тёмный и страшный.",
        "Мама, мне так страшно в этой тьме. Я не знаю, что скрывается вокруг меня.",
        "Звуки стали жуткими шёпотами, а запахи - загадочными тайнами. Мама, где ты?",
        "Слепота и отчаяние обволакивают меня, как тьма, и я плачу, надеясь, что меня услышат.",
        "Этот мрак - моё тюремное отшельничество, и я боюсь, что оно станет моим последним днем.",
        "Мама, мне кажется, что здесь что-то есть... что-то зловещее и беспощадное.",
        "Всё, что осталось мне - это крик моего сердца и слёзы моих безнадежных глаз.",
        "Мой мир - это смесь страха и одиночества, и я не знаю, как выбраться из этой тьмы.",
        "Мама, если ты меня слышишь, пожалуйста, приди ко мне. Я так боюсь.",
        "Звуки этой мрака звучат, как шёпот призраков, и они охватывают меня холодными руками.",
        "Мама, ты была моим светом, а теперь он погас. Я заблудился во мраке без твоей защиты.",
        "В этой тьме я ощущаю присутствие чего-то зловещего, что следит за мной.",
        "Мои слёзы сливаются с мраком, и я чувствую, как он поглощает меня всё глубже и глубже.",
        "Мама, мне нужна твоя рука, чтобы провести меня сквозь этот кошмар.",
        "Слепота делает этот мир беспощадным местом, и я боюсь, что он стал моей тюрьмой.",
        "Мама, где ты? Тьма мне говорит, что я один в этом ужасе.",
        "В этой тьме каждый звук, каждый шорох - как нож в сердце. Мама, спаси меня.",
        "Слепота лишила меня света, но мама - моим единственным оставшимся надежным ориентиром.",
        "Мама, я плачу, надеясь, что мои слёзы смоют этот кошмар и вернут тебя ко мне.",
        "Этот мрак словно существо, что скрывается в тенях, и оно голодает моего страха.",
        "Мама, я не могу увидеть, но мой страх становится всё реальнее, как кошмар наяву.",
        "Слепота не отнимает только мои глаза, она отнимает и мою надежду на твою обнимку.",
        "Здесь так много звуков, что они плетутся в мой ум как жуткие призраки.",
        "В этой тьме я ощущаю, как мои страхи тянут меня в бездну, и я не могу уйти.",
        "Мама, каждый шаг в этой мгле - как шаг в неизвестность, и я боюсь потерять себя.",
        "Моя душа кричит в этой тьме, и она жаждет твоего возвращения, мама.",
        "Мама, ты была моим опорой, и без твоей поддержки я боюсь, что упаду в этом кошмаре.",
        "В этой тьме нет спасения, и я молюсь, чтобы мои слова долетели до твоих ушей.",
        "Мама, я плачу и прошу твоей помощи, потому что этот мрак стал слишком ужасающим, чтобы я справился один.",
        "Тьма окутала меня, как могила, и я чувствую, как она давит на мою душу, словно её последний вздох."
        "В этой мраке мои мысли искажаются, и я не знаю, что реально, а что призраки моего ума.",
        "Слепота - это лишь начало моего кошмара. В моих снах мама мне говорит, что она ушла вечно.",
        "Тьма усиливает звуки моего страха и дарит им жизнь. Я слышу шёпоты душ, погребённых здесь.",
        "Мама, мой мир теперь - это чёрная бездна, где нет места надежде, ибо даже свет забыл обо мне.",
        "Здесь нет спасения, только холод и одиночество. Моя душа погружена в мрак, и она пытается вырваться.",
        "Мама, твоя утрата стала чёрной дырой в моей жизни, и она поглощает всё, что осталось от меня.",
        "Моя слепота - мой крест, и он становится тяжелее с каждым днём, когда мама не возвращает свет.",
        "В этой тьме тают мои мечты и надежды, словно пыль в ветре, и я боюсь, что я следующий.",
        "Мама, я заблудился в этой мраке, и я не знаю, смогу ли когда-нибудь найти твой свет снова.",
    ]
    
    text = random.choice(messages)
    return text
    