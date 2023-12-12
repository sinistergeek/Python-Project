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

def tasks(ctx):
    if ctx.obj['TASKS']:
        click.echo('YOUR TASKS\n************')
        for i,task in ctx.obj['TASKS'].items():
            click.echo('.'+task+'(ID:'+i+')')
        click.echo('')
    else:
        click.echo('No tasks yet! Use ADD to add one.\n')

@todo.command()
@click.pass_context
@click.option('-add','--add_task',prompt='Enter task to add')

def add(ctx,add_task):
    if add_task:
        ctx.obj['TASKS'][ctx.obj['LATEST']] = add_task
        click.echo('Added task"'+ add_task +'"with ID' + str(ctx.obj['LATEST']))
        curr_ind = [str(ctx.obj['LATEST'] + 1)]
        tasks = [str(i) + '```' + t for (i,t) in ctx.obj['TASKS'].items()]
        with open('./todo.txt','w') as f:
            f.writelines(['%s\n'%en for en in curr_ind + tasks])

@todo.command()
@click.pass_context
@click.option('-fin','--fin_taskid',prompt='Enter ID of task to finish',type=int)

def done(ctx,fin_taskid):
    if str(fin_taskid) in ctx.obj['TASKS'].keys():
        task=ctx.obj['TASKS'][str(fin_taskid)]
        del ctx.obj['TASKS'][str(fin_taskid)]
        click.echo('Finished and removed task"'+ task +'" with id'+str(fin_taskid))
        if ctx.obj['TASKS']:
            curr_ind = [str(ctx.obj['LATEsT'] + 1)]
            tasks =[str(i) + '```' + t for (i,t) om ctx.obj['TASKS'].items()]
            with open('./todo.txt','w') as f:
                f.writelines(['%s\n' % en for en in curr_ind + tasks])

        else:
            with open('./todo.txt','w') as f:
                f.writelines([str(0) + '\n'])
    else:
        click.echo('Error: no task with id' + str(fin_taskid))


if __name__ == '__main__':
    todo()
