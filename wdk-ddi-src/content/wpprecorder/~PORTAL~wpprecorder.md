# Wpprecorder.h header


This header is used by unknown technology.

Wpprecorder.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [RECORDER_CONFIGURE_PARAMS_INIT function](nf-wpprecorder-recorder-configure-params-init.md) | The RECORDER_CONFIGURE_PARAMS_INIT function is used to initialize the RECORDER_CONFIGURE_PARAMS structure. |
| [RECORDER_LOG_CREATE_PARAMS_INIT function](nf-wpprecorder-recorder-log-create-params-init.md) | The RECORDER_LOG_CREATE_PARAMS_INIT function is used to initialize the RECORDER_LOG_CREATE_PARAMS structure. |
| [RECORDER_LOG_CREATE_PARAMS_INIT_APPEND_POINTER function](nf-wpprecorder-recorder-log-create-params-init-append-pointer.md) | The RECORDER_LOG_CREATE_PARAMS_INIT_APPEND_POINTER method initializes the RECORDER_LOG_CREATE_PARAMS with the pointer to link logs. |
| [WppRecorderConfigure function](nf-wpprecorder-wpprecorderconfigure.md) | The WppRecorderConfigure method enables or disables the default log to which WPP prints. |
| [WppRecorderDumpLiveDriverData function](nf-wpprecorder-wpprecorderdumplivedriverdata.md) | The WppRecorderDumpLiveDriverData method gets the buffer associated with the specified Inflight Trace Recorder log. |
| [WppRecorderGetTriageInfo function](nf-wpprecorder-wpprecordergettriageinfo.md) | The WppRecorderGetTriageInfo. |
| [WppRecorderLinkCounters function](nf-wpprecorder-wpprecorderlinkcounters.md) | The WppRecorderLinkCounters. |
| [WppRecorderLogCreate function](nf-wpprecorder-wpprecorderlogcreate.md) | The WppRecorderLogCreate method creates a buffer to contain the recorder log. |
| [WppRecorderLogDelete function](nf-wpprecorder-wpprecorderlogdelete.md) | The WppRecorderLogDelete method deletes the specified recorder log. |
| [WppRecorderLogSetIdentifier function](nf-wpprecorder-wpprecorderlogsetidentifier.md) | The WppRecorderLogSetIdentifier method sets a string identifier for the recorder log. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [RECORDER_CONFIGURE_PARAMS structure](ns-wpprecorder--recorder-configure-params.md) | The RECORDER_CONFIGURE_PARAMS structure is an input parameter to the WppRecorderConfigure method to enable or disable the default log to which WPP prints. |
| [RECORDER_LOG_CREATE_PARAMS structure](ns-wpprecorder--recorder-log-create-params.md) | The RECORDER_LOG_CREATE_PARAMS structure is an input parameter to the WppRecorderLogCreate method. |
| [WPP_TRIAGE_INFO structure](ns-wpprecorder--wpp-triage-info.md) | Used to locate the WPP log for WER reporting. |
