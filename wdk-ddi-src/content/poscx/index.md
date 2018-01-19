---
UID : NA:poscx
ms.assetid : 0484e206-0de1-3054-8ac2-1ef67c0f4f2d
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# poscx.h header



poscx.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [EVT_POS_CX_DEVICE_OWNERSHIP_CHANGE](nc-poscx-evt_pos_cx_device_ownership_change.md) | The EVT_POS_CX_DEVICE_OWNERSHIP_CHANGE callback is called during the API claim ownership transition. The driver is expected to set the device back to a default state in this routine. |
| [EVT_POS_CX_DEVICE_REMOTE_CLAIM](nc-poscx-evt_pos_cx_device_remote_claim.md) | The EVT_POS_CX_DEVICE_REMOTE_CLAIM callback is called when the device is transitioning from unclaimed to claimed and allows the driver to do additional work. |
| [EVT_POS_CX_DEVICE_REMOTE_RELEASE](nc-poscx-evt_pos_cx_device_remote_release.md) | The EVT_POS_CX_DEVICE_REMOTE_RELEASE callback is called whenever the device is released and left with no owner and allows the driver to do additional work. |
| [EVT_POS_CX_DEVICE_REMOTE_RETAIN](nc-poscx-evt_pos_cx_device_remote_retain.md) | The EVT_POS_CX_DEVICE_REMOTE_RETAIN callback is called whenever PosCx attempts to hold onto a claim on a network device and allows the driver to do additional work. |
| [POS_CX_ATTRIBUTES_INIT](nf-poscx-pos_cx_attributes_init.md) | POS_CX_ATTRIBUTES_INIT initializes a POS_CX_ATTRIBUTE structure. |
| [PosCxClaimDevice](nf-poscx-poscxclaimdevice.md) | PosCxClaimDevice is called to claim a device for exclusive use. The caller should call PosCxReleaseDevice when the device is no longer needed. |
| [PosCxCleanPendingRequests](nf-poscx-poscxcleanpendingrequests.md) | PosCxCleanPendingRequests is called to cancel all pending requests for a given caller, identified by the open instance. |
| [PosCxCleanupEvents](nf-poscx-poscxcleanupevents.md) | PosCxCleanupEvents is called to clean up all pending events for a given caller, identified by the open instance. |
| [PosCxClose](nf-poscx-poscxclose.md) | PosCxClose is called to delete an opened PosCx library instance. This function releases the device if the caller is the owner, and cancels pending requests. It should be called from the driver's EVT_WDF_FILE_CLOSE callback. |
| [PosCxGetDeviceInterfaceTag](nf-poscx-poscxgetdeviceinterfacetag.md) | PosCxGetDeviceInterfaceTag returns the device interface tag that is set in PosCxOpen. |
| [PosCxGetPendingEvent](nf-poscx-poscxgetpendingevent.md) | PosCxGetPendingEvent is called either from the device read callback, or when a new event arrives. |
| [PosCxInit](nf-poscx-poscxinit.md) | PosCxInit is called to initialize the PosCx library's internal resources. The resources are tied to the device, and are released when the device goes away. |
| [PosCxIsDeviceOwner](nf-poscx-poscxisdeviceowner.md) | PosCxIsDeviceOwner checks if the caller currently owns the claim on the device. |
| [PosCxIsPosApp](nf-poscx-poscxisposapp.md) | PosCxIsPosApp checks if the open instance is associated with a point-of-service application. |
| [PosCxMarkPosApp](nf-poscx-poscxmarkposapp.md) | PosCxMarkPosApp marks the open instance as associated or not associated with a point-of-service application. |
| [PosCxOpen](nf-poscx-poscxopen.md) | PosCxOpen is called to create an open PosCx library instance. This function initializes all resources it needs to manage a single open instance. It should be called from the driver's EVT_WDF_DEVICE_FILE_CREATE callback. |
| [PosCxPutPendingEvent](nf-poscx-poscxputpendingevent.md) | PosCxPutPendingEvent creates a new event object, copies the event data to the new event object, and tries to delegate it to the waiting caller. |
| [PosCxPutPendingEventMemory](nf-poscx-poscxputpendingeventmemory.md) | PosCxPutPendingEventMemory tries to delegate a memory object containing the event data to a waiting caller. If the target caller does not have a read request waiting, the new event is added to the designated event queue (control or data). |
| [PosCxReleaseDevice](nf-poscx-poscxreleasedevice.md) | PosCxReleaseDevice is called to release a device that was previously claimed with PosCxClaimDevice. Once the device is released, the next pending claim requester is promoted. |
| [PosCxRemoteRequestRelease](nf-poscx-poscxremoterequestrelease.md) | PosCxRemoteRequestRelease is called whenever a remote device asks for the device to release. This initiates claim negotiation. |
| [PosCxRetainDevice](nf-poscx-poscxretaindevice.md) | PosCxRetainDevice is called to extend the ownership of the device. |



## Structures
| Title | Description |
| ---- |:---- |
| [_POS_CX_ATTRIBUTES](ns-poscx-_pos_cx_attributes.md) | The POS_CX_ATTRIBUTES structure contains pointers to event callback functions implemented by the client driver. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_POS_CX_EVENT_ATTRIBUTES](ne-poscx-_pos_cx_event_attributes.md) | The POS_CX_EVENT_ATTRIBUTES describes the priority and access rights for the POS events coming from the device. The values are a combination of the values defined in POS_CX_EVENT_DEST and POS_CX_EVENT_PRIORITY. |
| [_POS_CX_EVENT_DEST](ne-poscx-_pos_cx_event_dest.md) | The POS_CX_EVENT_DEST defines which applications receive this event. |
| [_POS_CX_EVENT_PRIORITY](ne-poscx-_pos_cx_event_priority.md) | The POS_CX_EVENT_PRIORITY defines the importance of the event and the order it will be delivered to the client application. |