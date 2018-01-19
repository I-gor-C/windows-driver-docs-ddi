---
UID : NA:nfcradiodev
ms.assetid : a2e40268-54ff-3618-9467-4f9e48215b04
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# nfcradiodev.h header



nfcradiodev.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_NFCRM_QUERY_RADIO_STATE](ni-nfcradiodev-ioctl_nfcrm_query_radio_state.md) | This IOCTL is used by the radio management application or service to query the current radio power state of the proximity device. |
| [IOCTL_NFCRM_SET_RADIO_STATE](ni-nfcradiodev-ioctl_nfcrm_set_radio_state.md) | This IOCTL is used by the radio management application or service to set the radio power state of the proximity device. |
| [IOCTL_NFCSERM_QUERY_RADIO_STATE](ni-nfcradiodev-ioctl_nfcserm_query_radio_state.md) | This IOCTL is used by the SE radio management application or service to query the current radio power state of the proximity device. |
| [IOCTL_NFCSERM_SET_RADIO_STATE](ni-nfcradiodev-ioctl_nfcserm_set_radio_state.md) | This IOCTL is used by the SE radio management application or service to query the current radio power state of the proximity device. |




## Structures
| Title | Description |
| ---- |:---- |
| [_NFCRM_RADIO_STATE](ns-nfcradiodev-_nfcrm_radio_state.md) | This structure is used to indicate the radio state. |
| [_NFCRM_SET_RADIO_STATE](ns-nfcradiodev-_nfcrm_set_radio_state.md) | This structure is used to set the radio state. The driver, in the case of airplane mode, has to persist the radio state and restore it when airplane mode is disabled. |