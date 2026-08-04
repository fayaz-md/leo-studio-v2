import edge_tts
import asyncio


class EdgeProvider:

    async def _generate(
        self,
        text,
        voice,
        output_file,
        rate="+0%",
        pitch="+0%",
        volume="+0%",
    ):

        communicate = edge_tts.Communicate(
            text=text,
            voice=voice,
            rate=rate,
            pitch=pitch,
            volume=volume,
        )

        await communicate.save(output_file)

    def generate(
        self,
        text,
        voice,
        output_file,
        rate="+0%",
        pitch="+0Hz",
        volume="+0%",
    ):

        asyncio.run(
            self._generate(
                text,
                voice,
                output_file,
                rate,
                pitch,
                volume,
            )
        )