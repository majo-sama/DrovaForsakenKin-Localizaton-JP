from typing import List
from llm_utils import get_llm_response


def sniff_persona(name: str, sentences: List[str]) -> str:
    """セリフをもとに、そのセリフの人物像を推測し、その人物像に合わせた翻訳のヒントを提供します。"""
    dialog = "\n".join([s for s in sentences if s.strip()])[:5000]
    messages = [
        {
            "role": "user",
            "content": f"""```Example
I need to take a break...
Have you gathered enough bog iron?
That should be enough. (Give bog iron)
I took it to Rura.
I'm still on it. (end conversation)
Chunnaic will be pleased about that. I'll give it to Muc once he's back, and I'll let Georg know, should he ask about you.
Got any more work for me?
Who's Chunnaic?
See you later. (end conversation)
No. But you can ask Dylara. She almost certainly needs help with the bridge.
Where can I find Dylara?
Follow the path west, then head north. She's supervising the bridge repairs.
Why's the bridge out?
A few nights ago, a quake struck. Now the bridge is gone, so we can no longer reach the Woodcutter Camp. Too bad for us, and for the Nemeton...
The finest blacksmith far and wide. There's no blade she can't forge.
If you find yourself in Nemeton, be sure to pay her a visit.
Ah, good. That's exactly where the bog iron needed to go anyway. Then Muc won't have to kill himself lugging it.
I'm always stuck doing this crap for Georg. I've had it up to here!
Now, now, don't exaggerate. Sometimes we've got to do unpleasant things, but it's the goal that counts.
Easy for you to say, you're part of the Nemeton. "Unpleasant things"? We're busting our asses here for nothing!
I could put in a good word for you with the Nemeton...
They can all kiss my grits! I'd rather go to the Remnants' camp...
What are you arguing about?
(end conversation)
Arguing? We're just talking. I'm Jerzy. That blockhead there is Jurek.
At least that blockhead sees things the way they are. Ever since the split, it's been downhill for Nemeton. They might as well shut it all down.
They always promise the Land of Legends, a land in harmony with the Divinities. But set one foot into the moor, and the bloodflies will eat you alive.
How is anyone supposed to trust the Nemeton? Keep kidding yourself now that they've accepted you, but I don't see a peaceful life on the horizon!
What's the problem with Nemeton?
Why didn't you join the Nemeton too?
I brought you both some food.
The Nemeton are the largest faction in Drova, and Georgefarm is part of it. The creatures in the moor are getting more and more aggressive, but the Nemeton are sending fewer and fewer fighters.
We're just talking about what a peaceful life we're going to have one day, but I hardly dare even taking a dump outside anymore. Nemeton is going downhill...
Jurek, what do you expect the Nemeton to do? More and more people are running off to the Remnants' camp.
Yeah, and whose fault is that? Nemeton's! People know they're better off elsewhere. I'm starting to believe it myself...
They don't accept just anyone. And I don't want to be accepted anymore, anyway. I'm sick of being shunned by them. They'd let you rot in the moor...
Things will get better again, Jurek.
Maybe for you — you can hide behind their big fat palisades...
Food! There's nothing better!
Come on, Jurek. Let's eat in peace.
*grumbles* We'll continue this conversation some other time...
Phew, dammit, I'm hungry...
Eating is the highlight of the day. They definitely don't have anything this tasty in Nemeton.
Thanks for bringing us the food.
Wait, this isn't enough... We need two portions...
Not now. Jurek and I must sort something out.
Got any work for me? Georg sent me.
Don't think so. We're managing just fine on our own.
Managing? Us? What nonsense. If the old fart sent you, then go ahead and work. Just collect some bog iron from the fields up ahead.
Ha, good idea. Muc always collects bog iron from us for Chunnaic the blacksmith. Gather some and bring it to me.
What does the bog iron look like?
What is bog iron?
I'll bring you the bog iron. (end conversation)
Small, brownish lumps. They always get plowed up to the surface.
Chunnaic refines it into iron. It's not as good as the stuff from the mines, but it's usable.
Bring me $GVAR:QuestVars_IronForFarmers.NumItemsNeeded$ pieces. I'll give to Muc at the next opportunity.
Why don't you just go to Nemeton?
You don't know what I mean!
Don't be like that!
Come on, just leave me alone!

=>
### Gender
Answer: Male
Reason: Jerzy's gender is not explicitly stated in the dialogue, and the name "Jerzy" can be used for both males and females in different cultures. However, the context and interactions suggest a male character, especially given the camaraderie and banter with Jurek, which often implies a male-male friendship dynamic in many narratives.

### Personality
Answer: Pragmatic, disillusioned, hardworking, frustrated, practical, responsible, grounded, cooperative, realistic, sarcastic, cynical, humorous
Reason: Jerzy comes across as pragmatic and somewhat disillusioned. He seems to be a hardworking individual who is frustrated with the current state of affairs, particularly with the Nemeton faction. Jerzy is practical, focusing on tasks like gathering bog iron and dealing with immediate needs like food. He also shows a sense of responsibility, as he is involved in tasks and seems to be a point of contact for others seeking work or information. Despite his frustrations, he maintains a level of realism and doesn't indulge in excessive complaints, suggesting a grounded personality.

### Speaking Style
Answer: Straightforward, informal, direct, slightly sarcastic, cynical, cooperative, no-nonsense, humorous
Reason: Jerzy's speaking style is straightforward and somewhat informal. He uses direct language and doesn't shy away from expressing his dissatisfaction, especially regarding the Nemeton. His tone can be slightly sarcastic or cynical, particularly when discussing the promises of the Nemeton or the challenges they face. However, he also shows a cooperative side, as he is willing to help others find work or provide directions. His dialogue reflects a no-nonsense attitude, with occasional humor or sarcasm, especially in his interactions with Jurek.
```


上記のExampleの通り、提供されたRPGの人物名とそのセリフから、その人物の性別、性格、話し方の雰囲気（口調）を描写してください。
### **Name**
{name}

### **Dialogue**:
{dialog}

""",
        },
    ]
    response = get_llm_response(
        model_name="gpt-4o",
        messages=messages,
        params_={"temperature": 0.0, "top_p": 0.3},
    )
    return response
