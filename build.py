import subprocess
import yaml
import textwrap

def render_sections(templates, sections):
    result = ""
    section_template = templates["section"]
    media_template = templates["media"]

    for nth, section in enumerate(sections):
        media = ""
        for entry in section["entries"]:
            media += media_template.format(**entry)
        result += section_template.format(**section, media = media, nth = nth)

    return result

def render_details(templates, sections):
    result = ""
    section_template = templates["section_details"]
    media_template = templates["media_details"]

    for section in sections:
        media = ""
        for entry in section["entries"]:
            if isinstance(media_template, list):
                for template in media_template:
                    if all(requirement in entry.keys() for requirement in template["if contains"]):
                        media += template["template"].format(**entry)
                        break
                else:
                    raise NotImplementedError("what if we don't find template that matches requirements?")
            else:
                media += media_template.format(**entry)
        result += section_template.format(**section, media = media)

    return result


def main():
    with open('./data.yml') as f:
        data = yaml.safe_load(f)

    templates, media, style = data["templates"], data["media"], data["style"]

    sections = render_sections(templates, media)
    details = render_details(templates, media)
    print(templates["page"].format(**{
        "sections": sections,
        "details": details,
        "style": data["style"],
    }))


if __name__ == "__main__":
    main()
