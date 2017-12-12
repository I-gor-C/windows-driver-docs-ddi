---
UID: NA:
---

# Nfcradiodev.h header

## -description

This header is used by Near field communications (NFC). For more information, see
- [Near field communications (NFC)](../_nfpdrivers/index.md)

Nfcradiodev.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_NFCRM_RADIO_STATE structure](ns-nfcradiodev-_nfcrm_radio_state.md) | This structure is used to indicate the radio state. |
| [_NFCRM_SET_RADIO_STATE structure](ns-nfcradiodev-_nfcrm_set_radio_state.md) | This structure is used to set the radio state. The driver, in the case of airplane mode, has to persist the radio state and restore it when airplane mode is disabled. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_NFCRM_QUERY_RADIO_STATE IOCTL](ni-nfcradiodev-ioctl_nfcrm_query_radio_state.md) | This IOCTL is used by the radio management application or service to query the current radio power state of the proximity device. |
| [IOCTL_NFCRM_SET_RADIO_STATE IOCTL](ni-nfcradiodev-ioctl_nfcrm_set_radio_state.md) | This IOCTL is used by the radio management application or service to set the radio power state of the proximity device. |
| [IOCTL_NFCSERM_QUERY_RADIO_STATE IOCTL](ni-nfcradiodev-ioctl_nfcserm_query_radio_state.md) | This IOCTL is used by the SE radio management application or service to query the current radio power state of the proximity device. |
| [IOCTL_NFCSERM_SET_RADIO_STATE IOCTL](ni-nfcradiodev-ioctl_nfcserm_set_radio_state.md) | This IOCTL is used by the SE radio management application or service to query the current radio power state of the proximity device. |
