# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport
import time


class kb_QualiMap(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login',
            service_ver='release',
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def _check_job(self, job_id):
        return self._client._check_job('kb_QualiMap', job_id)

    def _run_bamqc_submit(self, params, context=None):
        return self._client._submit_job(
             'kb_QualiMap.run_bamqc', [params],
             self._service_ver, context)

    def run_bamqc(self, params, context=None):
        """
        :param params: instance of type "RunBamQCParams" (Runs on either a
           ReadsAlignment or ReadsAlignmentSet. On a ReadsAlignment this will
           run BAM QC. On a set the mult-sample BAM QC is run. If the
           create_report flag is set, the result will be packaged as an HTML
           report. Either way you'll be provided with a qc_result_folder_path
           with an index.html file suitable for a report.) -> structure:
           parameter "input_ref" of String, parameter "create_report" of type
           "bool", parameter "output_workspace" of String
        :returns: instance of type "RunBamQCResult" -> structure: parameter
           "report_ref" of String, parameter "report_name" of String,
           parameter "qc_result_folder_path" of String, parameter
           "qc_result_zip_info" of type "BamQZResultZipFileInfo" ->
           structure: parameter "name" of String, parameter "shock_id" of
           String, parameter "index_html_file_name" of String, parameter
           "description" of String
        """
        job_id = self._run_bamqc_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def status(self, context=None):
        job_id = self._client._submit_job('kb_QualiMap.status', 
            [], self._service_ver, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]
