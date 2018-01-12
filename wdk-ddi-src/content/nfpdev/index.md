---
UID: NA:nfpdev
---

# Nfpdev.h header

## -description

This header is used by Near field communications (NFC). For more information, see
- [Near field communications (NFC)](../_nfpdrivers/index.md)

Nfpdev.h contain these programming interfaces:


## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_NFP_DISABLE IOCTL](ni-nfpdev-ioctl_nfp_disable.md) | A client sends the IOCTL_NFP_DISABLE request to temporarily disable subscriptions, publications, and presence events. |
| [IOCTL_NFP_ENABLE IOCTL](ni-nfpdev-ioctl_nfp_enable.md) | The client sends the IOCTL_NFP_ENABLE request to re-enable previously disabled subscriptions, publications, and presence events. |
| [IOCTL_NFP_GET_KILO_BYTES_PER_SECOND IOCTL](ni-nfpdev-ioctl_nfp_get_kilo_bytes_per_second.md) | A client sends the IOCTL_NFP_GET_KILO_BYTES_PER_SECOND request to any generic handle, one that is non-published and non-subscribed, to the provider device. |
| [IOCTL_NFP_GET_MAX_MESSAGE_BYTES IOCTL](ni-nfpdev-ioctl_nfp_get_max_message_bytes.md) | A client sends the IOCTL_NFP_GET_MAX_MESSAGE_BYTES request to any generic handle, one that is non-published and non-subscribed, to the provider device to determine the maximum message size supported. |
| [IOCTL_NFP_GET_NEXT_SUBSCRIBED_MESSAGE IOCTL](ni-nfpdev-ioctl_nfp_get_next_subscribed_message.md) | The client sends the IOCTL_NFP_GET_NEXT_SUBSCRIBED_MESSAGE request to the subscription handle repeatedly in order to receive subscribed messages as they arrive. |
| [IOCTL_NFP_GET_NEXT_TRANSMITTED_MESSAGE IOCTL](ni-nfpdev-ioctl_nfp_get_next_transmitted_message.md) | A client interested in receiving notifications that a message has been transmitted will send the IOCTL_NFP_GET_NEXT_TRANSMITTED_MESSAGE request to the proximity driver. |
| [IOCTL_NFP_SET_PAYLOAD IOCTL](ni-nfpdev-ioctl_nfp_set_payload.md) | A client application sends message data and confirms publication with the IOCTL_NFP_SET_PAYLOAD request. |
