# Mountdev.h header


This header is used by unknown technology.

Mountdev.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [MOUNTDEV_SUGGESTED_LINK_NAME structure](ns-mountdev--mountdev-suggested-link-name.md) | Mount manager clients that are able to keep track of their drive letters use this structure to request that the mount manager assign them a particular link name. |
| [MOUNTDEV_UNIQUE_ID structure](ns-mountdev--mountdev-unique-id.md) | The MOUNTDEV_UNIQUE_ID structure contains a unique volume ID that a mount manager client provides to the mount manager in response to an IOCTL_MOUNTDEV_QUERY_UNIQUE_ID request. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_MOUNTDEV_LINK_CREATED IOCTL](ni-mountdev-ioctl-mountdev-link-created.md) | Support for this IOCTL by the mount manager clients is optional. The mount manager uses this IOCTL to alert the client driver that a persistent name has been assigned to its volume. The input for this IOCTL is the persistent name assigned. |
| [IOCTL_MOUNTDEV_LINK_DELETED IOCTL](ni-mountdev-ioctl-mountdev-link-deleted.md) | Support for this IOCTL by the mount manager clients is optional. It alerts the mount manager client that a persistent name associated with it has been deleted. The input for this IOCTL is the persistent name that was deleted. |
| [IOCTL_MOUNTDEV_QUERY_SUGGESTED_LINK_NAME IOCTL](ni-mountdev-ioctl-mountdev-query-suggested-link-name.md) | Support for this IOCTL by the mount manager clients is optional. |
| [IOCTL_MOUNTDEV_QUERY_UNIQUE_ID IOCTL](ni-mountdev-ioctl-mountdev-query-unique-id.md) | Support for this IOCTL by mount manager clients is mandatory. |
