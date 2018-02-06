---
UID: NA:vhf
ms.assetid: 6241ba6a-2367-3ead-8146-3f3598ed3ab0
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# vhf.h header



vhf.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [EVT_VHF_ASYNC_OPERATION](nc-vhf-evt_vhf_async_operation.md) | The HID source driver implements this event callback if it wants to support one of the four asynchronous operation to get and set HID reports. |
| [EVT_VHF_CLEANUP](nc-vhf-evt_vhf_cleanup.md) | The HID source driver implements this event callback to free resources that might the driver allocated to the virtual HID device. |
| [EVT_VHF_READY_FOR_NEXT_READ_REPORT](nc-vhf-evt_vhf_ready_for_next_read_report.md) | The HID source driver implements this event call back function to use its buffering scheme for HID Input Reports, and wants to get notified when the next report can be submitted to VHF. |
| [VHF_CONFIG_INIT](nf-vhf-vhf_config_init.md) | Use the VHF_CONFIG_INIT function to initialize the required members of the VHF_CONFIG structure allocated by the HID source driver. |
| [VhfAsyncOperationComplete](nf-vhf-vhfasyncoperationcomplete.md) | The HID source driver calls this method to set the results of an asynchronous operation. |
| [VhfCreate](nf-vhf-vhfcreate.md) | The HID source driver calls this method to create a virtual HID device. |
| [VhfDelete](nf-vhf-vhfdelete.md) | The HID Source device driver calls this method to delete a VHF device. |
| [VhfReadReportSubmit](nf-vhf-vhfreadreportsubmit.md) | The HID source driver calls this method to submit a HID Read (Input) Report to Virtual HID Framework (VHF). |
| [VhfStart](nf-vhf-vhfstart.md) | The HID source driver calls this method to start the virtual HID device. |



## Structures
| Title | Description |
| ---- |:---- |
| [_VHF_CONFIG](ns-vhf-_vhf_config.md) | Contains initial configuration information that is provided by the HID source driver when it calls VhfCreate to create a virtual HID device. |