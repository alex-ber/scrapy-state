# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)


from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.settings import SETTINGS_PRIORITIES

def get_extension(type_name,  spider):
    for extension in spider.crawler.extensions.middlewares:
        if type_name in str(type(extension)):
            return extension
    return None


SETTINGS_PRIORITIES_NAMES = {v: k for k, v in SETTINGS_PRIORITIES.items()}

def get_settings_priority_name(priority):
    if isinstance(priority, str) or priority is None:
        return priority
    else:
        return SETTINGS_PRIORITIES_NAMES[priority]




class SpiderSettingsState(object):
    VAR_NAME = 'STATE'


    def _get_state_(self, settings):
        state = settings.getdict(self.VAR_NAME, None)
        return state

    def _get_state_priority(self, settings):
        state_priority = settings.getpriority(self.VAR_NAME)
        return  state_priority


    def _set_state_(self, state, state_priority, settings):
        logger.info('FINAL STATE is')
        logger.info(state)

        if state_priority is None:
            settings[self.VAR_NAME] = state
        else:
            # we want to ensure that set will actually happen
            settings.set(self.VAR_NAME, state, state_priority)



    def _check_configured(self, crawler):
        state = self._get_state_(crawler.settings)
        state_priority = self._get_state_priority(crawler.settings)

        logger.info('STATE is')
        logger.info(state)

        logger.info('priority is')
        logger.info(get_settings_priority_name(state_priority))

        if not state:
            raise NotConfigured


    def _init(self, crawler):
        self._check_configured(crawler)
        state = self._get_state_(crawler.settings)
        state_priority = self._get_state_priority(crawler.settings)
        self.change_state(state, state_priority, crawler.settings)
        self._set_state_(state, state_priority, crawler.settings)


    def __init__(self, crawler):
        self._init(crawler)


    @classmethod
    def from_crawler(cls, crawler):
        obj = cls(crawler)
        crawler.signals.connect(obj.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(obj.spider_closed, signal=signals.spider_closed)
        return obj

    def _init_spider_state(self, spider):
        state = getattr(spider, 'state', None)
        if not state:
            spider.state = {}

    def change_state(self, state, state_priority, settings):
        pass

    def validate_state(self, state, state_priority, spider):
        pass

    def _update_spider_state(self, state, state_priority, spider):
        spider.state.update(state)

    def spider_opened(self, spider):
        self._init_spider_state(spider)
        state = self._get_state_(spider.settings)
        state_priority = self._get_state_priority(spider.settings)
        self.validate_state(state, state_priority, spider)
        self._update_spider_state(state, state_priority, spider)

    def spider_closed(self, spider):
        pass

