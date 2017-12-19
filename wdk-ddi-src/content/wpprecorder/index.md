---
UID: NA:
---

# Wpprecorder.h header

## -description

This header is used by Driver test tools. For more information, see
- [Driver test tools](../_devtest/index.md)

Wpprecorder.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [RECORDER_CONFIGURE_PARAMS_INIT function](nf-wpprecorder-recorder_configure_params_init.md) | The RECORDER_CONFIGURE_PARAMS_INIT function is used to initialize the RECORDER_CONFIGURE_PARAMS structure. |
| [RECORDER_LOG_CREATE_PARAMS_INIT function](nf-wpprecorder-recorder_log_create_params_init.md) | The RECORDER_LOG_CREATE_PARAMS_INIT function is used to initialize the RECORDER_LOG_CREATE_PARAMS structure. |
| [RECORDER_LOG_CREATE_PARAMS_INIT_APPEND_POINTER function](nf-wpprecorder-recorder_log_create_params_init_append_pointer.md) | The RECORDER_LOG_CREATE_PARAMS_INIT_APPEND_POINTER method initializes the RECORDER_LOG_CREATE_PARAMS with the pointer to link logs. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_RECORDER_CONFIGURE_PARAMS structure](ns-wpprecorder-_recorder_configure_params.md) | The RECORDER_CONFIGURE_PARAMS structure is an input parameter to the WppRecorderConfigure method to enable or disable the default log to which WPP prints. |
| [_RECORDER_LOG_CREATE_PARAMS structure](ns-wpprecorder-_recorder_log_create_params.md) | The RECORDER_LOG_CREATE_PARAMS structure is an input parameter to the WppRecorderLogCreate method. |
| [_WPP_TRIAGE_INFO structure](ns-wpprecorder-_wpp_triage_info.md) | Used to locate the WPP log for WER reporting. |

## Macros

| Title   | Description   |
| ---- |:---- |
| [WppRecorderConfigure macro](nf-wpprecorder-wpprecorderconfigure.md) | The WppRecorderConfigure method enables or disables the default log to which WPP prints. |
| [WppRecorderDumpLiveDriverData macro](nf-wpprecorder-wpprecorderdumplivedriverdata.md) | The WppRecorderDumpLiveDriverData method gets the buffer associated with the specified Inflight Trace Recorder log. |
| [WppRecorderGetTriageInfo macro](nf-wpprecorder-wpprecordergettriageinfo.md) | The WppRecorderGetTriageInfo. |
| [WppRecorderLinkCounters macro](nf-wpprecorder-wpprecorderlinkcounters.md) | The WppRecorderLinkCounters. |
| [WppRecorderLogCreate macro](nf-wpprecorder-wpprecorderlogcreate.md) | The WppRecorderLogCreate method creates a buffer to contain the recorder log. |
| [WppRecorderLogDelete macro](nf-wpprecorder-wpprecorderlogdelete.md) | The WppRecorderLogDelete method deletes the specified recorder log. |
| [WppRecorderLogSetIdentifier macro](nf-wpprecorder-wpprecorderlogsetidentifier.md) | The WppRecorderLogSetIdentifier method sets a string identifier for the recorder log. |
