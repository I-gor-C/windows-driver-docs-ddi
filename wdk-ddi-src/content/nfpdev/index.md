---
UID : NA:nfpdev
ms.assetid : c6cd0690-4a5c-374c-bd0a-6f9c7f555b2d
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# nfpdev.h header



nfpdev.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_NFP_DISABLE](ni-nfpdev-ioctl_nfp_disable.md) | A client sends the IOCTL_NFP_DISABLE request to temporarily disable subscriptions, publications, and presence events. |
| [IOCTL_NFP_ENABLE](ni-nfpdev-ioctl_nfp_enable.md) | The client sends the IOCTL_NFP_ENABLE request to re-enable previously disabled subscriptions, publications, and presence events. |
| [IOCTL_NFP_GET_KILO_BYTES_PER_SECOND](ni-nfpdev-ioctl_nfp_get_kilo_bytes_per_second.md) | A client sends the IOCTL_NFP_GET_KILO_BYTES_PER_SECOND request to any generic handle, one that is non-published and non-subscribed, to the provider device. |
| [IOCTL_NFP_GET_MAX_MESSAGE_BYTES](ni-nfpdev-ioctl_nfp_get_max_message_bytes.md) | A client sends the IOCTL_NFP_GET_MAX_MESSAGE_BYTES request to any generic handle, one that is non-published and non-subscribed, to the provider device to determine the maximum message size supported. |
| [IOCTL_NFP_GET_NEXT_SUBSCRIBED_MESSAGE](ni-nfpdev-ioctl_nfp_get_next_subscribed_message.md) | The client sends the IOCTL_NFP_GET_NEXT_SUBSCRIBED_MESSAGE request to the subscription handle repeatedly in order to receive subscribed messages as they arrive. |
| [IOCTL_NFP_GET_NEXT_TRANSMITTED_MESSAGE](ni-nfpdev-ioctl_nfp_get_next_transmitted_message.md) | A client interested in receiving notifications that a message has been transmitted will send the IOCTL_NFP_GET_NEXT_TRANSMITTED_MESSAGE request to the proximity driver. |
| [IOCTL_NFP_SET_PAYLOAD](ni-nfpdev-ioctl_nfp_set_payload.md) | A client application sends message data and confirms publication with the IOCTL_NFP_SET_PAYLOAD request. |