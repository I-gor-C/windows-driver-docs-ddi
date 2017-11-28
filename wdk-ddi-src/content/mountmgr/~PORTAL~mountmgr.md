# Mountmgr.h header


This header is used by unknown technology.

Mountmgr.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [MOUNTDEV_NAME structure](ns-mountmgr--mountdev-name.md) | The MOUNTDEV_NAME structure holds the name of a device. |
| [MOUNTMGR_CHANGE_NOTIFY_INFO structure](ns-mountmgr--mountmgr-change-notify-info.md) | The MOUNTMGR_CHANGE_NOTIFY_INFO structure is used by the mount manager to send epic numbers to its clients and vice versa. |
| [MOUNTMGR_CREATE_POINT_INPUT structure](ns-mountmgr--mountmgr-create-point-input.md) | The MOUNTMGR_CREATE_POINT_INPUT structure is used by the mount manager to send a symbolic link name to a client that has requested symbolic link name by means of an IOCTL_MOUNTMGR_CREATE_POINT request. |
| [MOUNTMGR_DRIVE_LETTER_INFORMATION structure](ns-mountmgr--mountmgr-drive-letter-information.md) | The MOUNTMGR_DRIVE_LETTER_INFORMATION structure is used by the mount manager to furnish a drive letter to a client that has requested a driver letter by means of an IOCTL_MOUNTMGR_NEXT_DRIVE_LETTER request. |
| [MOUNTMGR_DRIVE_LETTER_TARGET structure](ns-mountmgr--mountmgr-drive-letter-target.md) | The MOUNTMGR_DRIVE_LETTER_TARGET structure is used by a mount manager client with an IOCTL_MOUNTMGR_NEXT_DRIVE_LETTER request to furnish a nonpersistent target device name to the mount manager. |
| [MOUNTMGR_MOUNT_POINT structure](ns-mountmgr--mountmgr-mount-point.md) | The MOUNTMGR_MOUNT_POINT structure is used by mount manager clients in conjunction with an IOCTL_MOUNTMGR_QUERY_POINTS request to query the mount manager for all of the mount points (symbolic links) associated with a device. |
| [MOUNTMGR_MOUNT_POINTS structure](ns-mountmgr--mountmgr-mount-points.md) | The MOUNTMGR_MOUNT_POINTS structure is used by mount manager to send a client the list of mount points associated with a device. |
| [MOUNTMGR_TARGET_NAME structure](ns-mountmgr--mountmgr-target-name.md) | The MOUNTMGR_TARGET_NAME structure contains the nonpersistent target device name for a device and is used by mount manager clients with the IOCTL_MOUNTMGR_KEEP_LINKS_WHEN_OFFLINE request to tell the mount manager to keep the symbolic link for a device active even after the device has gone offline. |
| [MOUNTMGR_VOLUME_MOUNT_POINT structure](ns-mountmgr--mountmgr-volume-mount-point.md) | The MOUNTMGR_VOLUME_MOUNT_POINT structure is used in conjunction with the IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_CREATED request to inform the mount manager that a volume mount point has been created. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_MOUNTDEV_QUERY_DEVICE_NAME IOCTL](ni-mountmgr-ioctl-mountdev-query-device-name.md) | Support for this IOCTL by the mount manager clients is mandatory. |
| [IOCTL_MOUNTMGR_AUTO_DL_ASSIGNMENTS IOCTL](ni-mountmgr-ioctl-mountmgr-auto-dl-assignments.md) | This IOCTL informs the mount manager that it should assign drive letters to volumes automatically as they are introduced in the system. |
| [IOCTL_MOUNTMGR_CHANGE_NOTIFY IOCTL](ni-mountmgr-ioctl-mountmgr-change-notify.md) | Clients send this IOCTL to the mount manager to be informed whenever there is a change in the mount manager's persistent symbolic link name database. |
| [IOCTL_MOUNTMGR_CHECK_UNPROCESSED_VOLUMES IOCTL](ni-mountmgr-ioctl-mountmgr-check-unprocessed-volumes.md) | When a volume arrives in the system, it registers for the MOUNTDEV_MOUNTED_DEVICE_GUID interface class and the mount manager receives a Plug and Play notification (see Mount Manager I/O Control Codes for a discussion of this process). |
| [IOCTL_MOUNTMGR_CREATE_POINT IOCTL](ni-mountmgr-ioctl-mountmgr-create-point.md) | The mount manager clients can use this IOCTL to request that the mount manager create a persistent symbolic link name for the indicated volume. |
| [IOCTL_MOUNTMGR_DELETE_POINTS IOCTL](ni-mountmgr-ioctl-mountmgr-delete-points.md) | This IOCTL is identical in input and output to IOCTL_MOUNTMGR_QUERY_POINTS. The difference is that IOCTL_MOUNTMGR_DELETE_POINTS has the side effect of deleting the symbolic links and the mount manager database entries for the triples returned. |
| [IOCTL_MOUNTMGR_DELETE_POINTS_DBONLY IOCTL](ni-mountmgr-ioctl-mountmgr-delete-points-dbonly.md) | This IOCTL is identical in input and output to IOCTL_MOUNTMGR_QUERY_POINTS. |
| [IOCTL_MOUNTMGR_KEEP_LINKS_WHEN_OFFLINE IOCTL](ni-mountmgr-ioctl-mountmgr-keep-links-when-offline.md) | This IOCTL directs the mount manager to keep a symbolic link active after the Plug and Play manager has given notification that its corresponding volume has gone offline. |
| [IOCTL_MOUNTMGR_NEXT_DRIVE_LETTER IOCTL](ni-mountmgr-ioctl-mountmgr-next-drive-letter.md) | This IOCTL checks to see if the given volume has a drive letter. |
| [IOCTL_MOUNTMGR_QUERY_POINTS IOCTL](ni-mountmgr-ioctl-mountmgr-query-points.md) | This IOCTL returns triples that consist of a persistent symbolic link name for the volume (that is, a mount point), a unique ID for the volume, and a nonpersistent device name (such as &#0034;\Device\HarddiskVolume1&#0034;) for the volume. |
| [IOCTL_MOUNTMGR_VOLUME_ARRIVAL_NOTIFICATION IOCTL](ni-mountmgr-ioctl-mountmgr-volume-arrival-notification.md) | This IOCTL allows a client to simulate a Plug and Play device interface arrival notification with the given volume name. |
| [IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_CREATED IOCTL](ni-mountmgr-ioctl-mountmgr-volume-mount-point-created.md) | This IOCTL alerts the mount manager that a volume mount point has been created, so that the mount manager can replicate the database entry for the given mount point. |
| [IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_DELETED IOCTL](ni-mountmgr-ioctl-mountmgr-volume-mount-point-deleted.md) | The mount manager clients use this IOCTL to alert the mount manager that a volume mount point has been deleted so that the mount manager can replicate the database entry for the given mount point. |
