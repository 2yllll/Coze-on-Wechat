import json
from bridge.reply import Reply, ReplyType


def get_info(workflow):
    work_res = workflow.coze_client.workflows.runs.create(
        workflow_id=workflow.current_flow_id
    )

    if isinstance(work_res.data, str):
        try:
            obj = json.loads(work_res.data)

            news = obj.get('news')
            output = obj.get('output')
            if news and len(news) > 0:
                for new in news:
                    workflow.context.kwargs.get("channel").send(Reply(ReplyType.LINK, new), workflow.context)
            elif output:
                workflow.context.kwargs.get("channel").send(Reply(ReplyType.TEXT, output), workflow.context)

            return True
        except Exception as e:
            workflow.context.kwargs.get("channel").send(Reply(ReplyType.TEXT, "工作流执行失败"), workflow.context)
            return False

    workflow.context.kwargs.get("channel").send(Reply(ReplyType.TEXT, "工作流执行结果转换失败"), workflow.context)
    return False
