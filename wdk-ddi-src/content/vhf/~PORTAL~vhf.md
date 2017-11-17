# Declarations in the vhf header
This header Vhf contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [HID_XFER_PACKET structure](ns-vhf--hid-xfer-packet.md) | TBD |
| [VHF_CONFIG structure](ns-vhf--vhf-config.md) | Contains initial configuration information that is provided by the HID source driver when it calls VhfCreate to create a virtual HID device. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_VHF_READY_FOR_NEXT_READ_REPORT callback](nc-vhf-evt-vhf-ready-for-next-read-report.md) | The HID source driver implements this event call back function to use its buffering scheme for HID Input Reports, and wants to get notified when the next report can be submitted to VHF. |
| [EVT_VHF_ASYNC_OPERATION callback](nc-vhf-evt-vhf-async-operation.md) | The HID source driver implements this event callback if it wants to support one of the four asynchronous operation to get and set HID reports. |
| [EVT_VHF_CLEANUP callback](nc-vhf-evt-vhf-cleanup.md) | The HID source driver implements this event callback to free resources that might the driver allocated to the virtual HID device. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [VHF_CONFIG_INIT function](nf-vhf-vhf-config-init.md) | Use the VHF_CONFIG_INIT function to initialize the required members of the VHF_CONFIG structure allocated by the HID source driver. |
| [VhfAsyncOperationComplete function](nf-vhf-vhfasyncoperationcomplete.md) | TBD |
| [VhfStart function](nf-vhf-vhfstart.md) | TBD |
| [VhfDelete function](nf-vhf-vhfdelete.md) | TBD |
| [VhfReadReportSubmit function](nf-vhf-vhfreadreportsubmit.md) | TBD |
| [VhfCreate function](nf-vhf-vhfcreate.md) | TBD |

This header is used in these topics:

- [hid](..content/_hid)
