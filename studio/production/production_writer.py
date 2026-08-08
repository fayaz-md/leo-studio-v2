import json


class ProductionWriter:

    def save(
        self,
        report,
        path,
    ):

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                report,
                f,
                indent=4,
                ensure_ascii=False,
            )