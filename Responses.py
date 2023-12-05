import json

class Response(object):
    def __init__(self,response):
        response.raise_for_status()
        self._response = response
        self._request = response.url
        self._json = json.loads(response.content)

class PageSpeedResponse(Response):

    @property
    def url(self):
        return self._json['id']
    @property
    def loadingExperience(self):
        return self._json['loadingExperience']['overall_category']

    @property
    def originaLoadingExperience(self):
        return self._json['originLoadingExperience']['overall_category']

    @property
    def originLoadingExperienceDetailed(self):
        meterics = self._json['originLoadingExperience']['metrics']
        keys_ = list(metrics.keys())
        originLoadingExperienceDetailed_ = {}
        for each in keys_:
            originLoadingExperienceDetailed_[each] = metrics[each]['category']
        return originLoadinfExperienceDetailed_
    @property
    def loadingExperienceDetailed(self):
        metrics = self._json['loadingExperience']['metrics']
        keys_ = list(metrics.keys())
        loadingExperienceDetailed_ = {}
        for each in keys_:
            loadingExperienceDetailed_[each] = metrics[each]['category']
        return loadingExperienceDetailed_

    @property
    def requestedUrl(self):
        return self._json['lighthouseResult']['requestedUrl']
    @property
    def finalUrl(self):
        return self._json['lighthouseResult']['finalUrl']
    @property
    def version(self):
        return self._json['lighthouseResult']['lighthouseVersion']
    @property
    def userAgent(self):
        return self._json['lighthouseResult']['userAgent']
    @property
    def lighthouseResults(self):
        return self._json['lighthouseResult']
