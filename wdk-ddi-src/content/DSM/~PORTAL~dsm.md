# Declarations in the dsm header
This header Dsm contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [DSM_DEVICE_SERIAL_NUMBER callback function](nc-dsm-dsm-device-serial-number.md) | TBD |
| [DSM_CATEGORIZE_REQUEST callback function](nc-dsm-dsm-categorize-request.md) | TBD |
| [DSM_REMOVE_PATH callback function](nc-dsm-dsm-remove-path.md) | TBD |
| [DSM_COMPARE_DEVICES callback function](nc-dsm-dsm-compare-devices.md) | TBD |
| [DSM_UNLOAD callback function](nc-dsm-dsm-unload.md) | TBD |
| [DSM_EXECUTE_METHOD_EX callback function](nc-dsm-dsm-execute-method-ex.md) | TBD |
| [DSM_INQUIRE_DRIVER callback function](nc-dsm-dsm-inquire-driver.md) | TBD |
| [DSM_SRB_DEVICE_CONTROL callback function](nc-dsm-dsm-srb-device-control.md) | TBD |
| [DSM_LB_GET_PATH callback function](nc-dsm-dsm-lb-get-path.md) | TBD |
| [DSM_FUNCTION_CONTROL_EX callback function](nc-dsm-dsm-function-control-ex.md) | TBD |
| [DSM_REMOVE_PENDING callback function](nc-dsm-dsm-remove-pending.md) | TBD |
| [DSM_GET_CONTROLLER_INFO callback function](nc-dsm-dsm-get-controller-info.md) | TBD |
| [DSM_BROADCAST_SRB callback function](nc-dsm-dsm-broadcast-srb.md) | TBD |
| [DSM_QUERY_DATABLOCK callback function](nc-dsm-dsm-query-datablock.md) | TBD |
| [DSM_QUERY_DATABLOCK_EX callback function](nc-dsm-dsm-query-datablock-ex.md) | TBD |
| [DSM_PATH_VERIFY callback function](nc-dsm-dsm-path-verify.md) | TBD |
| [DSM_FUNCTION_CONTROL callback function](nc-dsm-dsm-function-control.md) | TBD |
| [DSM_SET_DATABLOCK_EX callback function](nc-dsm-dsm-set-datablock-ex.md) | TBD |
| [DSM_ADDRESS_TYPE_SUPPORTED callback function](nc-dsm-dsm-address-type-supported.md) | TBD |
| [DSM_SET_COMPLETION callback function](nc-dsm-dsm-set-completion.md) | TBD |
| [DSM_REMOVE_DEVICE callback function](nc-dsm-dsm-remove-device.md) | TBD |
| [DSM_MOVE_DEVICE callback function](nc-dsm-dsm-move-device.md) | TBD |
| [DSM_COMPLETION_ROUTINE callback function](nc-dsm-dsm-completion-routine.md) | TBD |
| [DSM_EXECUTE_METHOD callback function](nc-dsm-dsm-execute-method.md) | TBD |
| [DSM_SET_DEVICE_INFO callback function](nc-dsm-dsm-set-device-info.md) | TBD |
| [DSM_INTERPRET_ERROR_EX callback function](nc-dsm-dsm-interpret-error-ex.md) | TBD |
| [DSM_INTERPRET_ERROR callback function](nc-dsm-dsm-interpret-error.md) | TBD |
| [DSM_INVALIDATE_PATH callback function](nc-dsm-dsm-invalidate-path.md) | TBD |
| [DSM_IS_PATH_ACTIVE callback function](nc-dsm-dsm-is-path-active.md) | TBD |
| [DSM_SET_DATABLOCK callback function](nc-dsm-dsm-set-datablock.md) | TBD |
| [DSM_DEVICE_NOT_USED callback function](nc-dsm-dsm-device-not-used.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [DsmSendTUR function](nf-dsm-dsmsendtur.md) | TBD |
| [DsmSendRequestEx function](nf-dsm-dsmsendrequestex.md) | TBD |
| [DsmGetPDO function](nf-dsm-dsmgetpdo.md) | TBD |
| [DsmSendPassThroughDirect function](nf-dsm-dsmsendpassthroughdirect.md) | TBD |
| [DsmSendDeviceIoControlSynchronous function](nf-dsm-dsmsenddeviceiocontrolsynchronous.md) | TBD |
| [DsmCompleteRequest function](nf-dsm-dsmcompleterequest.md) | TBD |
| [DsmGetVersion function](nf-dsm-dsmgetversion.md) | TBD |
| [DsmReleaseQueue function](nf-dsm-dsmreleasequeue.md) | TBD |
| [DsmSendRequest function](nf-dsm-dsmsendrequest.md) | TBD |
| [DsmWriteEvent function](nf-dsm-dsmwriteevent.md) | TBD |
| [DsmGetAssociatedDevice function](nf-dsm-dsmgetassociateddevice.md) | TBD |
| [DsmGetContextFromSrb function](nf-dsm-dsmgetcontextfromsrb.md) | TBD |
| [DsmNotification function](nf-dsm-dsmnotification.md) | TBD |
| [DsmGetScsiAddress function](nf-dsm-dsmgetscsiaddress.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [CONTROLLER_INFO structure](ns-dsm--controller-info.md) | TBD |
| [DSM_COMPLETION_INFO structure](ns-dsm--dsm-completion-info.md) | TBD |
| [SCSI_PASS_THROUGH_DIRECT_WITH_BUFFER structure](ns-dsm--scsi-pass-through-direct-with-buffer.md) | TBD |
| [DSM_WMILIB_CONTEXT structure](ns-dsm--dsm-wmilib-context.md) | TBD |
| [MPIO_VERSION_INFO structure](ns-dsm--mpio-version-info.md) | TBD |
| [DSM_MPIO_CONTEXT structure](ns-dsm--dsm-mpio-context.md) | TBD |
| [DSM_IDS structure](ns-dsm--dsm-ids.md) | TBD |
| [DSM_INIT_DATA structure](ns-dsm--dsm-init-data.md) | TBD |
| [SCSI_PASS_THROUGH_WITH_BUFFERS structure](ns-dsm--scsi-pass-through-with-buffers.md) | TBD |
| [DSM_VERSION_INFO structure](ns-dsm--dsm-version-info.md) | TBD |
| [DSM_DEREGISTER_DATA structure](ns-dsm--dsm-deregister-data.md) | TBD |
| [CONTROLLER_IDS structure](ns-dsm--controller-ids.md) | TBD |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_MPDSM_DEREGISTER IOCTL](ni-dsm-ioctl-mpdsm-deregister.md) | TBD |
| [IOCTL_MPDSM_REGISTER IOCTL](ni-dsm-ioctl-mpdsm-register.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [DSM_TYPE enumeration](ne-dsm--dsm-type~r2.md) | TBD |
| [DSM_TYPE enumeration](ne-dsm--dsm-type~r1.md) | TBD |
| [DSM_TYPE enumeration](ne-dsm--dsm-type.md) | TBD |
| [DSM_NOTIFICATION_TYPE enumeration](ne-dsm--dsm-notification-type.md) | TBD |

This header is used in these topics:

