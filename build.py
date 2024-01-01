import subprocess
import yaml
import textwrap
import dataclasses
import typing

def render_posters(data):
    poster_template = data["templates"]["poster"]
    return "\n".join(poster_template.format(**m) for m in data["media"])

def render_details(data):
    result = ""
    media_template = data["templates"]["details"]
    external_template = data["templates"]["external"]
    postprocessed = {}

    for media in data["media"]:
        assert isinstance(media_template, dict)

        external = ''.join(external_template.format(**external) for external in media.get("external", []))
        if external:
            external = f"<h4>See more</h4><ul>{external}</ul>"
            postprocessed["external"] = external

        result += media_template["template"].format(**{
            **data["common"],
            **media_template["defaults"],
            **media,
            **postprocessed,
        })

    return result


def main():
    with open('./data.yml') as f:
        data = yaml.safe_load(f)

    posters = render_posters(data)
    details = render_details(data)
    print(data["templates"]["page"].format(
        **data["common"],
        posters = posters,
        details = details,
        style = data["style"],
    ))


if __name__ == "__main__":
    main()
