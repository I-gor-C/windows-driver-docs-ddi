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
