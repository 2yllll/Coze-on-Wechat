from typing import Dict
from config import conf
import json
from bridge.reply import Reply, ReplyType
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED
from concurrent.futures import ProcessPoolExecutor
import worker.scheduler
import datetime


class Workflow:
    def __init__(self, coze):
        self.coze_client = coze
        self.workflows: Dict[str, str] = conf().get("workflows")
        self._base_url = conf().get("coze_api_base")
        self.current_flow_id = None
        self.scheduler = BackgroundScheduler(executor=ProcessPoolExecutor(max_workers=5))
        self.scheduler.add_listener(self._timer_executed, mask=EVENT_JOB_EXECUTED)
        self.context = None

    def _get_workflows(self, match: str):
        flow_id: str or None = self.workflows[match]
        if flow_id == '' or flow_id is None:
            self.current_flow_id = None
        else:
            self.current_flow_id = flow_id
        return flow_id

    def _call_workflow(self):
        if self.context is None:
            return Reply(ReplyType.TEXT, "执行失败")

        workflow = self.coze_client.workflows.runs.create(
            workflow_id=self.current_flow_id
        )

        if isinstance(workflow.data, str):
            try:
                obj = json.loads(workflow.data)
                news = obj.get('news')
                output = obj.get('output')
                if news and len(news) > 0:
                    for new in news:
                        self.context.kwargs.get("channel").send(Reply(ReplyType.LINK, new), self.context)
                    return Reply(ReplyType.TEXT, '执行完毕')
                elif output:
                    return Reply(ReplyType.TEXT, output)
            except Exception as e:
                return Reply(ReplyType.TEXT, '工作流执行失败')

        return Reply(ReplyType.TEXT, "工作流执行结果转换失败")

    def apply(self, match: str, context):
        flow_id = self._get_workflows(match)
        self.context = None
        if flow_id != "":
            context.kwargs.get("channel").send(Reply(ReplyType.TEXT, "正在执行工作流，请稍等..."), context)
            self.context = context
            return self._call_workflow()
        else:
            return Reply(ReplyType.TEXT, '未找到相关工作流，请查看配置文件。')

    def timer_trigger(self, match: str, context, **kwargs):
        flow_id = self._get_workflows(match)
        self.context = None
        if flow_id != "":
            if self.scheduler.get_job(match):
                # context.kwargs.get("channel").send(Reply(ReplyType.TEXT, f"{fn_name}已经开启了，无需再开启。"), context)
                self.scheduler.pause_job(match)
                self.scheduler.remove_job(match)
                return Reply(ReplyType.TEXT, f"关闭{match}。")

            fn = getattr(worker.scheduler, f"{match}")
            if not fn:
                return Reply(ReplyType.TEXT, f"{match}未实现，无法开启。")

            self.context = context
            self.scheduler.add_job(fn, "cron", **kwargs, id=f"{match}", args=[self])
            # self.scheduler.add_job(fn, "interval", seconds=10, id=f"{match}", args=[self])

            self.scheduler.start()
            return Reply(ReplyType.TEXT, f"{match}已启用 {json.dumps(kwargs)}")

    def _timer_executed(self, event):
        if event.code == EVENT_JOB_EXECUTED:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{now} 执行 {event.job_id}  结果：{event.retval}")
