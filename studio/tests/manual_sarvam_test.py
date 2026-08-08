from pathlib import Path

from studio.voice_engine.sarvam_provider import (
    SarvamProvider,
)


def main():

    output_dir = Path("output")
    output_dir.mkdir(
        exist_ok=True
    )

    provider = SarvamProvider()

    voices = [
        {
            "name": "leo",
            "voice_id": "shubh",
            "text": "हमें उसकी मदद करनी होगी!",
        },
        {
            "name": "meera",
            "voice_id": "priya",
            "text": "रुको लियो, पहले हमें सोचना होगा!",
        },
        {
            "name": "robbie",
            "voice_id": "manan",
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

        print(
            f"Generating {voice['name']}..."
        )

        provider.synthesize(
            text=voice["text"],
            voice_profile=voice_profile,
            output_path=str(output_path),
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