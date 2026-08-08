from pathlib import Path

from studio.voice_engine.sarvam_provider import (
    SarvamProvider,
)
from studio.voice_engine.voice_performance import (
    VoicePerformance,
)


def main():

    output_dir = Path("output")
    output_dir.mkdir(
        exist_ok=True
    )

    provider = SarvamProvider()
    performance_builder = VoicePerformance()

    voices = [
        {
            "name": "leo",
            "voice_id": "shubh",
            "emotion": "happy",
            "voice_style": "cheerful",
            "speaking_speed": "normal",
            "text": "हमें उसकी मदद करनी होगी!",
        },
        {
            "name": "meera",
            "voice_id": "priya",
            "emotion": "worried",
            "voice_style": "soft",
            "speaking_speed": "slow",
            "text": "रुको लियो, पहले हमें सोचना होगा!",
        },
        {
            "name": "robbie",
            "voice_id": "manan",
            "emotion": "excited",
            "voice_style": "energetic",
            "speaking_speed": "fast",
            "text": "खतरा पता चला! हमें जल्दी करनी होगी!",
        },
    ]

    for voice in voices:

        output_path = (
            output_dir
            / f"{voice['name']}_test.wav"
        )

        voice_profile = {
            "provider": "sarvam",
            "provider_voice_id": voice[
                "voice_id"
            ],
            "language_code": "hi-IN",
        }

        performance = (
            performance_builder.build(
                emotion=voice["emotion"],
                voice_style=voice["voice_style"],
                speaking_speed=voice["speaking_speed"],
            )
        )

        print(
            f"Generating {voice['name']}..."
        )

        print(
            f"  Emotion : {voice['emotion']}"
        )

        print(
            f"  Style   : {voice['voice_style']}"
        )

        print(
            f"  Speed   : {voice['speaking_speed']}"
        )

        print(
            f"  Voice   : {voice['voice_id']}"
        )

        print(
            f"  Performance: {performance}"
        )

        provider.synthesize(
            text=voice["text"],
            voice_profile=voice_profile,
            output_path=str(output_path),
            performance=performance,
        )

        print(
            f"Created: {output_path}"
        )

        print(
            f"Size: {output_path.stat().st_size} bytes"
        )

        print()

    print(
        "All three voice samples generated."
    )


if __name__ == "__main__":
    main()