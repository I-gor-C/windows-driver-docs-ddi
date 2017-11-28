# Nfpdev.h header


This header is used by unknown technology.

Nfpdev.h contain these programming interfaces:


## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_NFP_DISABLE IOCTL](ni-nfpdev-ioctl-nfp-disable.md) | A client sends the IOCTL_NFP_DISABLE request to temporarily disable subscriptions, publications, and presence events. |
| [IOCTL_NFP_ENABLE IOCTL](ni-nfpdev-ioctl-nfp-enable.md) | The client sends the IOCTL_NFP_ENABLE request to re-enable previously disabled subscriptions, publications, and presence events. |
| [IOCTL_NFP_GET_KILO_BYTES_PER_SECOND IOCTL](ni-nfpdev-ioctl-nfp-get-kilo-bytes-per-second.md) | A client sends the IOCTL_NFP_GET_KILO_BYTES_PER_SECOND request to any generic handle, one that is non-published and non-subscribed, to the provider device. |
| [IOCTL_NFP_GET_MAX_MESSAGE_BYTES IOCTL](ni-nfpdev-ioctl-nfp-get-max-message-bytes.md) | A client sends the IOCTL_NFP_GET_MAX_MESSAGE_BYTES request to any generic handle, one that is non-published and non-subscribed, to the provider device to determine the maximum message size supported. |
| [IOCTL_NFP_GET_NEXT_SUBSCRIBED_MESSAGE IOCTL](ni-nfpdev-ioctl-nfp-get-next-subscribed-message.md) | The client sends the IOCTL_NFP_GET_NEXT_SUBSCRIBED_MESSAGE request to the subscription handle repeatedly in order to receive subscribed messages as they arrive. |
| [IOCTL_NFP_GET_NEXT_TRANSMITTED_MESSAGE IOCTL](ni-nfpdev-ioctl-nfp-get-next-transmitted-message.md) | A client interested in receiving notifications that a message has been transmitted will send the IOCTL_NFP_GET_NEXT_TRANSMITTED_MESSAGE request to the proximity driver. |
| [IOCTL_NFP_SET_PAYLOAD IOCTL](ni-nfpdev-ioctl-nfp-set-payload.md) | A client application sends message data and confirms publication with the IOCTL_NFP_SET_PAYLOAD request. |
