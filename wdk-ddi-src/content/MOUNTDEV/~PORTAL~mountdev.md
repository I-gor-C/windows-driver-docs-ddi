# Declarations in the mountdev header
This header Mountdev contains these programming interfaces:

Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_MOUNTDEV_QUERY_STABLE_GUID IOCTL](ni-mountdev-ioctl-mountdev-query-stable-guid.md) | TBD |
| [IOCTL_MOUNTDEV_LINK_DELETED IOCTL](ni-mountdev-ioctl-mountdev-link-deleted.md) | TBD |
| [IOCTL_MOUNTDEV_QUERY_SUGGESTED_LINK_NAME IOCTL](ni-mountdev-ioctl-mountdev-query-suggested-link-name.md) | Support for this IOCTL by the mount manager clients is optional. |
| [IOCTL_MOUNTDEV_LINK_CREATED IOCTL](ni-mountdev-ioctl-mountdev-link-created.md) | TBD |
| [IOCTL_MOUNTDEV_QUERY_INTERFACE_NAME IOCTL](ni-mountdev-ioctl-mountdev-query-interface-name.md) | TBD |
| [IOCTL_MOUNTDEV_QUERY_UNIQUE_ID IOCTL](ni-mountdev-ioctl-mountdev-query-unique-id.md) | Support for this IOCTL by mount manager clients is mandatory. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [MOUNTDEV_UNIQUE_ID structure](ns-mountdev--mountdev-unique-id.md) | The MOUNTDEV_UNIQUE_ID structure contains a unique volume ID that a mount manager client provides to the mount manager in response to an IOCTL_MOUNTDEV_QUERY_UNIQUE_ID request. |
| [MOUNTDEV_STABLE_GUID structure](ns-mountdev--mountdev-stable-guid.md) | TBD |
| [MOUNTDEV_SUGGESTED_LINK_NAME structure](ns-mountdev--mountdev-suggested-link-name.md) | Mount manager clients that are able to keep track of their drive letters use this structure to request that the mount manager assign them a particular link name. |

This header is used in these topics:

- [Storage](..content/_Storage)
