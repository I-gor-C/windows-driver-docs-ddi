# Declarations in the poscx header
This header Poscx contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_POS_CX_DEVICE_REMOTE_CLAIM callback](nc-poscx-evt-pos-cx-device-remote-claim.md) | The EVT_POS_CX_DEVICE_REMOTE_CLAIM callback is called when the device is transitioning from unclaimed to claimed and allows the driver to do additional work. |
| [*PFN_POSCXISDEVICEOWNER callback function](nc-poscx-pfn-poscxisdeviceowner.md) | TBD |
| [EVT_POS_CX_DEVICE_OWNERSHIP_CHANGE callback](nc-poscx-evt-pos-cx-device-ownership-change.md) | The EVT_POS_CX_DEVICE_OWNERSHIP_CHANGE callback is called during the API claim ownership transition. The driver is expected to set the device back to a default state in this routine. |
| [*PFN_POSCXISPOSAPP callback function](nc-poscx-pfn-poscxisposapp.md) | TBD |
| [*PFN_POSCXRELEASEDEVICE callback function](nc-poscx-pfn-poscxreleasedevice.md) | TBD |
| [*PFN_POSCXGETDEVICEINTERFACETAG callback function](nc-poscx-pfn-poscxgetdeviceinterfacetag.md) | TBD |
| [*PFN_POSCXGETPENDINGEVENT callback function](nc-poscx-pfn-poscxgetpendingevent.md) | TBD |
| [*PFN_POSCXCLEANPENDINGREQUESTS callback function](nc-poscx-pfn-poscxcleanpendingrequests.md) | TBD |
| [*PFN_POSCXOPEN callback function](nc-poscx-pfn-poscxopen.md) | TBD |
| [*PFN_POSCXPUTPENDINGEVENT callback function](nc-poscx-pfn-poscxputpendingevent.md) | TBD |
| [*PFN_POSCXPUTPENDINGEVENTMEMORY callback function](nc-poscx-pfn-poscxputpendingeventmemory.md) | TBD |
| [PPOSCX_EXPORTED_INTERFACES callback function](nc-poscx-pposcx-exported-interfaces.md) | TBD |
| [EVT_POS_CX_DEVICE_REMOTE_RETAIN callback](nc-poscx-evt-pos-cx-device-remote-retain.md) | The EVT_POS_CX_DEVICE_REMOTE_RETAIN callback is called whenever PosCx attempts to hold onto a claim on a network device and allows the driver to do additional work. |
| [*PFN_POSCXCLAIMDEVICE callback function](nc-poscx-pfn-poscxclaimdevice.md) | TBD |
| [*PFN_POSCXREMOTEREQUESTRELEASE callback function](nc-poscx-pfn-poscxremoterequestrelease.md) | TBD |
| [*PFN_POSCXCLOSE callback function](nc-poscx-pfn-poscxclose.md) | TBD |
| [EVT_POS_CX_DEVICE_REMOTE_RELEASE callback](nc-poscx-evt-pos-cx-device-remote-release.md) | The EVT_POS_CX_DEVICE_REMOTE_RELEASE callback is called whenever the device is released and left with no owner and allows the driver to do additional work. |
| [*PFN_POSCXINIT callback function](nc-poscx-pfn-poscxinit.md) | TBD |
| [*PFN_POSCXCLEANUPEVENTS callback function](nc-poscx-pfn-poscxcleanupevents.md) | TBD |
| [*PFN_POSCXRETAINDEVICE callback function](nc-poscx-pfn-poscxretaindevice.md) | TBD |
| [*PFN_POSCXMARKPOSAPP callback function](nc-poscx-pfn-poscxmarkposapp.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [POS_CX_EVENT_PRIORITY enumeration](ne-poscx--pos-cx-event-priority.md) | The POS_CX_EVENT_PRIORITY defines the importance of the event and the order it will be delivered to the client application. |
| [POS_CX_EVENT_DEST enumeration](ne-poscx--pos-cx-event-dest.md) | The POS_CX_EVENT_DEST defines which applications receive this event. |
| [POS_CX_EVENT_ATTRIBUTES enumeration](ne-poscx--pos-cx-event-attributes.md) | The POS_CX_EVENT_ATTRIBUTES describes the priority and access rights for the POS events coming from the device. The values are a combination of the values defined in POS_CX_EVENT_DEST and POS_CX_EVENT_PRIORITY. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [PosCxClaimDevice function](nf-poscx-poscxclaimdevice.md) | PosCxClaimDevice is called to claim a device for exclusive use. The caller should call PosCxReleaseDevice when the device is no longer needed. |
| [PosCxIsPosApp function](nf-poscx-poscxisposapp.md) | PosCxIsPosApp checks if the open instance is associated with a point-of-service application. |
| [PosCxReleaseDevice function](nf-poscx-poscxreleasedevice.md) | PosCxReleaseDevice is called to release a device that was previously claimed with PosCxClaimDevice. Once the device is released, the next pending claim requester is promoted. |
| [PosCxCleanPendingRequests function](nf-poscx-poscxcleanpendingrequests.md) | PosCxCleanPendingRequests is called to cancel all pending requests for a given caller, identified by the open instance. |
| [PosCxRetainDevice function](nf-poscx-poscxretaindevice.md) | PosCxRetainDevice is called to extend the ownership of the device. |
| [PosCxGetPendingEvent function](nf-poscx-poscxgetpendingevent.md) | PosCxGetPendingEvent is called either from the device read callback, or when a new event arrives. |
| [PosCxInit function](nf-poscx-poscxinit.md) | PosCxInit is called to initialize the PosCx library's internal resources. The resources are tied to the device, and are released when the device goes away. |
| [PosCxIsDeviceOwner function](nf-poscx-poscxisdeviceowner.md) | PosCxIsDeviceOwner checks if the caller currently owns the claim on the device. |
| [PosCxCleanupEvents function](nf-poscx-poscxcleanupevents.md) | PosCxCleanupEvents is called to clean up all pending events for a given caller, identified by the open instance. |
| [PosCxPutPendingEvent function](nf-poscx-poscxputpendingevent.md) | PosCxPutPendingEvent creates a new event object, copies the event data to the new event object, and tries to delegate it to the waiting caller. |
| [POS_CX_ATTRIBUTES_INIT function](nf-poscx-pos-cx-attributes-init.md) | POS_CX_ATTRIBUTES_INIT initializes a POS_CX_ATTRIBUTE structure. |
| [PosCxMarkPosApp function](nf-poscx-poscxmarkposapp.md) | PosCxMarkPosApp marks the open instance as associated or not associated with a point-of-service application. |
| [PosCxPutPendingEventMemory function](nf-poscx-poscxputpendingeventmemory.md) | PosCxPutPendingEventMemory tries to delegate a memory object containing the event data to a waiting caller. If the target caller does not have a read request waiting, the new event is added to the designated event queue (control or data). |
| [PosCxRemoteRequestRelease function](nf-poscx-poscxremoterequestrelease.md) | PosCxRemoteRequestRelease is called whenever a remote device asks for the device to release. This initiates claim negotiation. |
| [PosCxGetDeviceInterfaceTag function](nf-poscx-poscxgetdeviceinterfacetag.md) | PosCxGetDeviceInterfaceTag returns the device interface tag that is set in PosCxOpen. |
| [PosCxOpen function](nf-poscx-poscxopen.md) | PosCxOpen is called to create an open PosCx library instance. This function initializes all resources it needs to manage a single open instance. It should be called from the driver's EVT_WDF_DEVICE_FILE_CREATE callback. |
| [PosCxClose function](nf-poscx-poscxclose.md) | PosCxClose is called to delete an opened PosCx library instance. This function releases the device if the caller is the owner, and cancels pending requests. It should be called from the driver's EVT_WDF_FILE_CLOSE callback. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [POS_CX_ATTRIBUTES structure](ns-poscx--pos-cx-attributes.md) | The POS_CX_ATTRIBUTES structure contains pointers to event callback functions implemented by the client driver. |
| [WDF_DRIVER_GLOBALS structure](ns-poscx--wdf-driver-globals.md) | TBD |

This header is used in these topics:

- [pos](..content/_pos)
