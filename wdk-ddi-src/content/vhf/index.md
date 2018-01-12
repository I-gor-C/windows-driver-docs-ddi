---
UID: NA:vhf
---

# Vhf.h header

## -description

This header is used by Human Interface Devices (HID). For more information, see
- [Human Interface Devices (HID)](../_hid/index.md)

Vhf.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [VHF_CONFIG_INIT function](nf-vhf-vhf_config_init.md) | Use the VHF_CONFIG_INIT function to initialize the required members of the VHF_CONFIG structure allocated by the HID source driver. |
| [VhfAsyncOperationComplete function](nf-vhf-vhfasyncoperationcomplete.md) | The HID source driver calls this method to set the results of an asynchronous operation. |
| [VhfCreate function](nf-vhf-vhfcreate.md) | The HID source driver calls this method to create a virtual HID device. |
| [VhfDelete function](nf-vhf-vhfdelete.md) | The HID Source device driver calls this method to delete a VHF device. |
| [VhfReadReportSubmit function](nf-vhf-vhfreadreportsubmit.md) | The HID source driver calls this method to submit a HID Read (Input) Report to Virtual HID Framework (VHF). |
| [VhfStart function](nf-vhf-vhfstart.md) | The HID source driver calls this method to start the virtual HID device. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_VHF_CONFIG structure](ns-vhf-_vhf_config.md) | Contains initial configuration information that is provided by the HID source driver when it calls VhfCreate to create a virtual HID device. |
