import click

@click.group()
@click.pass_context

def todo(ctx):
    ctx.ensure_object(dict)
    with open('./todo.txt') as f:
        content = f.readlines()
    ctx.obj['LATEST'] = int(content[:1][0])
    ctx.obj['TASKS'] = {en.split('```')[0]:en.split('```')[1][:-1] for en in content[1:]}
@todo.command()
@click.pass_context

