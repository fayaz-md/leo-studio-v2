class StorySchema:
    """
    Central Story JSON schema used by PromptBuilder.

    This class defines the contract between
    Gemini and Leo Studio.

    StoryParser relies on this structure.
    """

    @staticmethod
    def json_contract():

        return """
{
    "title":"",
    "summary":"",
    "youtube_title":"",
    "description":"",
    "tags":[""],
    "ending_message":"",

    "characters":[
        {
            "id":"",
            "display_name":"",
            "species":"",
            "gender":"",
            "age":"",
            "role":""
        }
    ],

    "locations":[
        {
            "id":"",
            "name":""
        }
    ],

    "props":[
        {
            "id":"",
            "name":""
        }
    ],

    "scenes":[
        {
            "number":1,
            "title":"",
            "narration":"",
            "image_prompt":"",
            "animation_prompt":"",
            "camera":"",
            "music":"",
            "sfx":"",
            "dialogues":[
                {
                    "speaker":"",
                    "emotion":"happy",
                    "text":""
                }
            ]
        }
    ]
}
"""