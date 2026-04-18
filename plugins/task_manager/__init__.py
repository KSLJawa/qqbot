from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageEvent, Message
from nonebot.params import CommandArg
from .data_source import get_user, add_task, get_tasks, complete_task, delete_task

# 注册命令
start_cmd = on_command("start", aliases={"开始", "注册"}, priority=5)
add_cmd = on_command("add", aliases={"添加任务"}, priority=5)
list_cmd = on_command("list", aliases={"任务列表", "查看任务"}, priority=5)
done_cmd = on_command("done", aliases={"完成任务"}, priority=5)
delete_cmd = on_command("delete", aliases={"删除任务"}, priority=5)


# /start命令
@start_cmd.handle()
async def handle_start(event: MessageEvent):
    user_id = event.user_id
    user = await get_user(user_id)
    if user:
        await start_cmd.finish(f"欢迎回来！\n发送 /add 任务标题 添加任务\n发送 /list 查看任务列表")
    else:
        await start_cmd.finish(f"注册成功！欢迎使用任务助手\n发送 /add 任务标题 添加任务\n发送 /list 查看任务列表")


# /add命令
@add_cmd.handle()
async def handle_add(event: MessageEvent, arg: Message = CommandArg()):
    user_id = event.user_id
    title = arg.extract_plain_text().strip()
    if not title:
        await add_cmd.finish("请输入任务标题，如：/add 完成软件工程作业")

    task = await add_task(user_id, title)
    await add_cmd.finish(f"✅ 任务已添加：{task.title}")


# /list命令
@list_cmd.handle()
async def handle_list(event: MessageEvent):
    user_id = event.user_id
    tasks = await get_tasks(user_id)
    if not tasks:
        await list_cmd.finish("📭 你还没有任何任务")

    msg = "📋 你的任务列表：\n"
    for i, task in enumerate(tasks, 1):
        status = "✅" if task.is_completed else "❌"
        msg += f"{i}. {status} {task.title}\n"
    msg += "\n发送 /done 任务编号 标记完成\n发送 /delete 任务编号 删除任务"
    await list_cmd.finish(msg)


# /done命令
@done_cmd.handle()
async def handle_done(event: MessageEvent, arg: Message = CommandArg()):
    user_id = event.user_id
    try:
        task_num = int(arg.extract_plain_text().strip())
        task = await complete_task(user_id, task_num)
        if task:
            await done_cmd.finish(f"✅ 任务已完成：{task.title}")
        else:
            await done_cmd.finish("❌ 任务编号不存在")
    except ValueError:
        await done_cmd.finish("❌ 请输入有效的数字编号")


# /delete命令
@delete_cmd.handle()
async def handle_delete(event: MessageEvent, arg: Message = CommandArg()):
    user_id = event.user_id
    try:
        task_num = int(arg.extract_plain_text().strip())
        task = await delete_task(user_id, task_num)
        if task:
            await delete_cmd.finish(f"🗑️ 任务已删除：{task.title}")
        else:
            await delete_cmd.finish("❌ 任务编号不存在")
    except ValueError:
        await delete_cmd.finish("❌ 请输入有效的数字编号")
