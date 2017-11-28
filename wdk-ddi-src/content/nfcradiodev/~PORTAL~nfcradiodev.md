# Nfcradiodev.h header


This header is used by unknown technology.

Nfcradiodev.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [NFCRM_RADIO_STATE structure](ns-nfcradiodev--nfcrm-radio-state.md) | This structure is used to indicate the radio state. |
| [NFCRM_SET_RADIO_STATE structure](ns-nfcradiodev--nfcrm-set-radio-state.md) | This structure is used to set the radio state. The driver, in the case of airplane mode, has to persist the radio state and restore it when airplane mode is disabled. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_NFCRM_QUERY_RADIO_STATE IOCTL](ni-nfcradiodev-ioctl-nfcrm-query-radio-state.md) | This IOCTL is used by the radio management application or service to query the current radio power state of the proximity device. |
| [IOCTL_NFCRM_SET_RADIO_STATE IOCTL](ni-nfcradiodev-ioctl-nfcrm-set-radio-state.md) | This IOCTL is used by the radio management application or service to set the radio power state of the proximity device. |
| [IOCTL_NFCSERM_QUERY_RADIO_STATE IOCTL](ni-nfcradiodev-ioctl-nfcserm-query-radio-state.md) | This IOCTL is used by the SE radio management application or service to query the current radio power state of the proximity device. |
| [IOCTL_NFCSERM_SET_RADIO_STATE IOCTL](ni-nfcradiodev-ioctl-nfcserm-set-radio-state.md) | This IOCTL is used by the SE radio management application or service to query the current radio power state of the proximity device. |
