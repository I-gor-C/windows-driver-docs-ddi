# Point of Service (POS)

Overview of the Point of Service (POS) technology.

To develop Point of Service (POS), you need these headers:

 * [pointofservicecommontypes.h](..\pointofservicecommontypes\index.md)
 * [poscx.h](..\poscx\index.md)

For the programming guide, see [Point of Service (POS)](https://docs.microsoft.com/en-us/windows-hardware/drivers/pos).

## Functions

| Title   | Description   |
| ---- |:---- |
| [POS_CX_ATTRIBUTES_INIT function](..\poscx\nf-poscx-pos-cx-attributes-init.md) | POS_CX_ATTRIBUTES_INIT initializes a POS_CX_ATTRIBUTE structure. |
| [PosCxClaimDevice function](..\poscx\nf-poscx-poscxclaimdevice.md) | PosCxClaimDevice is called to claim a device for exclusive use. The caller should call PosCxReleaseDevice when the device is no longer needed. |
| [PosCxCleanPendingRequests function](..\poscx\nf-poscx-poscxcleanpendingrequests.md) | PosCxCleanPendingRequests is called to cancel all pending requests for a given caller, identified by the open instance. |
| [PosCxCleanupEvents function](..\poscx\nf-poscx-poscxcleanupevents.md) | PosCxCleanupEvents is called to clean up all pending events for a given caller, identified by the open instance. |
| [PosCxClose function](..\poscx\nf-poscx-poscxclose.md) | PosCxClose is called to delete an opened PosCx library instance. This function releases the device if the caller is the owner, and cancels pending requests. It should be called from the driver's EVT_WDF_FILE_CLOSE callback. |
| [PosCxGetDeviceInterfaceTag function](..\poscx\nf-poscx-poscxgetdeviceinterfacetag.md) | PosCxGetDeviceInterfaceTag returns the device interface tag that is set in PosCxOpen. |
| [PosCxGetPendingEvent function](..\poscx\nf-poscx-poscxgetpendingevent.md) | PosCxGetPendingEvent is called either from the device read callback, or when a new event arrives. |
| [PosCxInit function](..\poscx\nf-poscx-poscxinit.md) | PosCxInit is called to initialize the PosCx library's internal resources. The resources are tied to the device, and are released when the device goes away. |
| [PosCxIsDeviceOwner function](..\poscx\nf-poscx-poscxisdeviceowner.md) | PosCxIsDeviceOwner checks if the caller currently owns the claim on the device. |
| [PosCxIsPosApp function](..\poscx\nf-poscx-poscxisposapp.md) | PosCxIsPosApp checks if the open instance is associated with a point-of-service application. |
| [PosCxMarkPosApp function](..\poscx\nf-poscx-poscxmarkposapp.md) | PosCxMarkPosApp marks the open instance as associated or not associated with a point-of-service application. |
| [PosCxOpen function](..\poscx\nf-poscx-poscxopen.md) | PosCxOpen is called to create an open PosCx library instance. This function initializes all resources it needs to manage a single open instance. It should be called from the driver's EVT_WDF_DEVICE_FILE_CREATE callback. |
| [PosCxPutPendingEvent function](..\poscx\nf-poscx-poscxputpendingevent.md) | PosCxPutPendingEvent creates a new event object, copies the event data to the new event object, and tries to delegate it to the waiting caller. |
| [PosCxPutPendingEventMemory function](..\poscx\nf-poscx-poscxputpendingeventmemory.md) | PosCxPutPendingEventMemory tries to delegate a memory object containing the event data to a waiting caller. If the target caller does not have a read request waiting, the new event is added to the designated event queue (control or data). |
| [PosCxReleaseDevice function](..\poscx\nf-poscx-poscxreleasedevice.md) | PosCxReleaseDevice is called to release a device that was previously claimed with PosCxClaimDevice. Once the device is released, the next pending claim requester is promoted. |
| [PosCxRemoteRequestRelease function](..\poscx\nf-poscx-poscxremoterequestrelease.md) | PosCxRemoteRequestRelease is called whenever a remote device asks for the device to release. This initiates claim negotiation. |
| [PosCxRetainDevice function](..\poscx\nf-poscx-poscxretaindevice.md) | PosCxRetainDevice is called to extend the ownership of the device. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_POS_CX_DEVICE_OWNERSHIP_CHANGE callback](..\poscx\nc-poscx-evt-pos-cx-device-ownership-change.md) | The EVT_POS_CX_DEVICE_OWNERSHIP_CHANGE callback is called during the API claim ownership transition. The driver is expected to set the device back to a default state in this routine. |
| [EVT_POS_CX_DEVICE_REMOTE_CLAIM callback](..\poscx\nc-poscx-evt-pos-cx-device-remote-claim.md) | The EVT_POS_CX_DEVICE_REMOTE_CLAIM callback is called when the device is transitioning from unclaimed to claimed and allows the driver to do additional work. |
| [EVT_POS_CX_DEVICE_REMOTE_RELEASE callback](..\poscx\nc-poscx-evt-pos-cx-device-remote-release.md) | The EVT_POS_CX_DEVICE_REMOTE_RELEASE callback is called whenever the device is released and left with no owner and allows the driver to do additional work. |
| [EVT_POS_CX_DEVICE_REMOTE_RETAIN callback](..\poscx\nc-poscx-evt-pos-cx-device-remote-retain.md) | The EVT_POS_CX_DEVICE_REMOTE_RETAIN callback is called whenever PosCx attempts to hold onto a claim on a network device and allows the driver to do additional work. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [BarcodeSymbologyAttributesData structure](..\pointofservicecommontypes\ns-pointofservicecommontypes--barcodesymbologyattributesdata.md) | The BarcodeSymbologyAttributesData structure contains the attribute information for a barcode symbology. |
| [POS_CX_ATTRIBUTES structure](..\poscx\ns-poscx--pos-cx-attributes.md) | The POS_CX_ATTRIBUTES structure contains pointers to event callback functions implemented by the client driver. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [BarcodeSymbologyDecodeLengthType enumeration](..\pointofservicecommontypes\ne-pointofservicecommontypes--barcodesymbologydecodelengthtype.md) | The BarcodeSymbologyDecodeLengthType enum describes values for the decode length which can be set to support a range, two discrete values, or be set to any length. |
| [POS_CX_EVENT_ATTRIBUTES enumeration](..\poscx\ne-poscx--pos-cx-event-attributes.md) | The POS_CX_EVENT_ATTRIBUTES describes the priority and access rights for the POS events coming from the device. The values are a combination of the values defined in POS_CX_EVENT_DEST and POS_CX_EVENT_PRIORITY. |
| [POS_CX_EVENT_DEST enumeration](..\poscx\ne-poscx--pos-cx-event-dest.md) | The POS_CX_EVENT_DEST defines which applications receive this event. |
| [POS_CX_EVENT_PRIORITY enumeration](..\poscx\ne-poscx--pos-cx-event-priority.md) | The POS_CX_EVENT_PRIORITY defines the importance of the event and the order it will be delivered to the client application. |
