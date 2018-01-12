---
UID: NA:wdfiotarget
---

# Wdfiotarget.h header

## -description

This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdfiotarget.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [PFN_WDFIOTARGETALLOCANDQUERYTARGETPROPERTY function](nc-wdfiotarget-pfn_wdfiotargetallocandquerytargetproperty.md) | The WdfIoTargetAllocAndQueryTargetProperty method allocates a buffer and retrieves a specified device property for a specified I/O target. |
| [PFN_WDFIOTARGETCLOSE function](nc-wdfiotarget-pfn_wdfiotargetclose.md) | The WdfIoTargetClose method closes a specified remote I/O target. |
| [PFN_WDFIOTARGETCLOSEFORQUERYREMOVE function](nc-wdfiotarget-pfn_wdfiotargetcloseforqueryremove.md) | The WdfIoTargetCloseForQueryRemove method temporarily closes a specified remote I/O target because the target device might soon be removed. |
| [PFN_WDFIOTARGETCREATE function](nc-wdfiotarget-pfn_wdfiotargetcreate.md) | The WdfIoTargetCreate method creates a remote I/O target for a specified device. |
| [PFN_WDFIOTARGETFORMATREQUESTFORINTERNALIOCTL function](nc-wdfiotarget-pfn_wdfiotargetformatrequestforinternalioctl.md) | The WdfIoTargetFormatRequestForInternalIoctl method builds an internal device control request for an I/O target but does not send the request. |
| [PFN_WDFIOTARGETFORMATREQUESTFORINTERNALIOCTLOTHERS function](nc-wdfiotarget-pfn_wdfiotargetformatrequestforinternalioctlothers.md) | The WdfIoTargetFormatRequestForInternalIoctlOthers method builds a non-standard internal device control request for an I/O target but does not send the request. |
| [PFN_WDFIOTARGETFORMATREQUESTFORIOCTL function](nc-wdfiotarget-pfn_wdfiotargetformatrequestforioctl.md) | The WdfIoTargetFormatRequestForIoctl method builds a device control request for an I/O target but does not send the request. |
| [PFN_WDFIOTARGETFORMATREQUESTFORREAD function](nc-wdfiotarget-pfn_wdfiotargetformatrequestforread.md) | The WdfIoTargetFormatRequestForRead method builds a read request for an I/O target but does not send the request. |
| [PFN_WDFIOTARGETFORMATREQUESTFORWRITE function](nc-wdfiotarget-pfn_wdfiotargetformatrequestforwrite.md) | The WdfIoTargetFormatRequestForWrite method builds a write request for an I/O target but does not send the request. |
| [PFN_WDFIOTARGETGETDEVICE function](nc-wdfiotarget-pfn_wdfiotargetgetdevice.md) | The WdfIoTargetGetDevice method returns a handle to the framework device object that is the parent of the specified local or remote I/O target. |
| [PFN_WDFIOTARGETGETSTATE function](nc-wdfiotarget-pfn_wdfiotargetgetstate.md) | The WdfIoTargetGetState method returns state information for a local or remote I/O target. |
| [PFN_WDFIOTARGETOPEN function](nc-wdfiotarget-pfn_wdfiotargetopen.md) | The WdfIoTargetOpen method opens a remote I/O target so the driver can send I/O requests to it. |
| [PFN_WDFIOTARGETQUERYFORINTERFACE function](nc-wdfiotarget-pfn_wdfiotargetqueryforinterface.md) | The WdfIoTargetQueryForInterface method obtains access to the GUID-identified, driver-defined interface of a remote I/O target. |
| [PFN_WDFIOTARGETQUERYTARGETPROPERTY function](nc-wdfiotarget-pfn_wdfiotargetquerytargetproperty.md) | The WdfIoTargetQueryTargetProperty method retrieves a specified device property for a specified I/O target. |
| [PFN_WDFIOTARGETSENDINTERNALIOCTLOTHERSSYNCHRONOUSLY function](nc-wdfiotarget-pfn_wdfiotargetsendinternalioctlotherssynchronously.md) | The WdfIoTargetSendInternalIoctlOthersSynchronously method builds a non-standard internal device control request and sends it synchronously to an I/O target. |
| [PFN_WDFIOTARGETSENDINTERNALIOCTLSYNCHRONOUSLY function](nc-wdfiotarget-pfn_wdfiotargetsendinternalioctlsynchronously.md) | The WdfIoTargetSendInternalIoctlSynchronously method builds an internal device control request and sends it synchronously to an I/O target. |
| [PFN_WDFIOTARGETSENDIOCTLSYNCHRONOUSLY function](nc-wdfiotarget-pfn_wdfiotargetsendioctlsynchronously.md) | The WdfIoTargetSendIoctlSynchronously method builds a device control request and sends it synchronously to an I/O target. |
| [PFN_WDFIOTARGETSENDREADSYNCHRONOUSLY function](nc-wdfiotarget-pfn_wdfiotargetsendreadsynchronously.md) | The WdfIoTargetSendReadSynchronously method builds a read request and sends it synchronously to an I/O target. |
| [PFN_WDFIOTARGETSENDWRITESYNCHRONOUSLY function](nc-wdfiotarget-pfn_wdfiotargetsendwritesynchronously.md) | The WdfIoTargetSendWriteSynchronously method builds a write request and sends it synchronously to an I/O target. |
| [PFN_WDFIOTARGETSTART function](nc-wdfiotarget-pfn_wdfiotargetstart.md) | The WdfIoTargetStart method starts sending queued requests to a local or remote I/O target. |
| [PFN_WDFIOTARGETWDMGETTARGETFILEHANDLE function](nc-wdfiotarget-pfn_wdfiotargetwdmgettargetfilehandle.md) | The WdfIoTargetWdmGetTargetFileHandle method returns a handle to the file that is associated with a specified remote I/O target. |
| [PFN_WDFIOTARGETWDMGETTARGETPHYSICALDEVICE function](nc-wdfiotarget-pfn_wdfiotargetwdmgettargetphysicaldevice.md) | The WdfIoTargetWdmGetTargetPhysicalDevice method returns a pointer to the Windows Driver Model (WDM) physical device object (PDO) that represents a remote I/O target's device. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_CREATE_BY_NAME function](nf-wdfiotarget-wdf_io_target_open_params_init_create_by_name.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_CREATE_BY_NAME function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so the driver can open an I/O target by specifying the name of the device, file, or device interface. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE function](nf-wdfiotarget-wdf_io_target_open_params_init_existing_device.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so that the driver can open a remote I/O target by specifying a Windows Driver Model (WDM) device object. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_FILE function](nf-wdfiotarget-wdf_io_target_open_params_init_open_by_file.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_FILE function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so the driver can open an I/O target by specifying a filename. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_NAME function](nf-wdfiotarget-wdf_io_target_open_params_init_open_by_name.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_NAME function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so the driver can open an I/O target by specifying the name of the device, file, or device interface. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN function](nf-wdfiotarget-wdf_io_target_open_params_init_reopen.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so the driver can reopen a remote I/O target. |
| [WdfIoTargetAllocAndQueryTargetProperty function](nf-wdfiotarget-wdfiotargetallocandquerytargetproperty.md) | The WdfIoTargetAllocAndQueryTargetProperty method allocates a buffer and retrieves a specified device property for a specified I/O target. |
| [WdfIoTargetClose function](nf-wdfiotarget-wdfiotargetclose.md) | The WdfIoTargetClose method closes a specified remote I/O target. |
| [WdfIoTargetCloseForQueryRemove function](nf-wdfiotarget-wdfiotargetcloseforqueryremove.md) | The WdfIoTargetCloseForQueryRemove method temporarily closes a specified remote I/O target because the target device might soon be removed. |
| [WdfIoTargetCreate function](nf-wdfiotarget-wdfiotargetcreate.md) | The WdfIoTargetCreate method creates a remote I/O target for a specified device. |
| [WdfIoTargetFormatRequestForInternalIoctl function](nf-wdfiotarget-wdfiotargetformatrequestforinternalioctl.md) | The WdfIoTargetFormatRequestForInternalIoctl method builds an internal device control request for an I/O target but does not send the request. |
| [WdfIoTargetFormatRequestForInternalIoctlOthers function](nf-wdfiotarget-wdfiotargetformatrequestforinternalioctlothers.md) | The WdfIoTargetFormatRequestForInternalIoctlOthers method builds a non-standard internal device control request for an I/O target but does not send the request. |
| [WdfIoTargetFormatRequestForIoctl function](nf-wdfiotarget-wdfiotargetformatrequestforioctl.md) | The WdfIoTargetFormatRequestForIoctl method builds a device control request for an I/O target but does not send the request. |
| [WdfIoTargetFormatRequestForRead function](nf-wdfiotarget-wdfiotargetformatrequestforread.md) | The WdfIoTargetFormatRequestForRead method builds a read request for an I/O target but does not send the request. |
| [WdfIoTargetFormatRequestForWrite function](nf-wdfiotarget-wdfiotargetformatrequestforwrite.md) | The WdfIoTargetFormatRequestForWrite method builds a write request for an I/O target but does not send the request. |
| [WdfIoTargetGetDevice function](nf-wdfiotarget-wdfiotargetgetdevice.md) | The WdfIoTargetGetDevice method returns a handle to the framework device object that is the parent of the specified local or remote I/O target. |
| [WdfIoTargetGetState function](nf-wdfiotarget-wdfiotargetgetstate.md) | The WdfIoTargetGetState method returns state information for a local or remote I/O target. |
| [WdfIoTargetOpen function](nf-wdfiotarget-wdfiotargetopen.md) | The WdfIoTargetOpen method opens a remote I/O target so the driver can send I/O requests to it. |
| [WdfIoTargetPurge function](nf-wdfiotarget-wdfiotargetpurge.md) | The WdfIoTargetPurge method cancels all I/O requests queued to a local, remote, or specialized I/O target and prevents any new I/O requests from being queued. |
| [WdfIoTargetQueryForInterface function](nf-wdfiotarget-wdfiotargetqueryforinterface.md) | The WdfIoTargetQueryForInterface method obtains access to the GUID-identified, driver-defined interface of a remote I/O target. |
| [WdfIoTargetQueryTargetProperty function](nf-wdfiotarget-wdfiotargetquerytargetproperty.md) | The WdfIoTargetQueryTargetProperty method retrieves a specified device property for a specified I/O target. |
| [WdfIoTargetSendInternalIoctlOthersSynchronously function](nf-wdfiotarget-wdfiotargetsendinternalioctlotherssynchronously.md) | The WdfIoTargetSendInternalIoctlOthersSynchronously method builds a non-standard internal device control request and sends it synchronously to an I/O target. |
| [WdfIoTargetSendInternalIoctlSynchronously function](nf-wdfiotarget-wdfiotargetsendinternalioctlsynchronously.md) | The WdfIoTargetSendInternalIoctlSynchronously method builds an internal device control request and sends it synchronously to an I/O target. |
| [WdfIoTargetSendIoctlSynchronously function](nf-wdfiotarget-wdfiotargetsendioctlsynchronously.md) | The WdfIoTargetSendIoctlSynchronously method builds a device control request and sends it synchronously to an I/O target. |
| [WdfIoTargetSendReadSynchronously function](nf-wdfiotarget-wdfiotargetsendreadsynchronously.md) | The WdfIoTargetSendReadSynchronously method builds a read request and sends it synchronously to an I/O target. |
| [WdfIoTargetSendWriteSynchronously function](nf-wdfiotarget-wdfiotargetsendwritesynchronously.md) | The WdfIoTargetSendWriteSynchronously method builds a write request and sends it synchronously to an I/O target. |
| [WdfIoTargetStart function](nf-wdfiotarget-wdfiotargetstart.md) | The WdfIoTargetStart method starts sending queued requests to a local or remote I/O target. |
| [WdfIoTargetStop function](nf-wdfiotarget-wdfiotargetstop.md) | The WdfIoTargetStop method stops sending queued requests to a local or remote I/O target. |
| [WdfIoTargetWdmGetTargetDeviceObject function](nf-wdfiotarget-wdfiotargetwdmgettargetdeviceobject.md) | The WdfIoTargetWdmGetTargetDeviceObject method returns a pointer to the Windows Driver Model (WDM) device object that is associated with a specified local or remote I/O target. |
| [WdfIoTargetWdmGetTargetFileHandle function](nf-wdfiotarget-wdfiotargetwdmgettargetfilehandle.md) | The WdfIoTargetWdmGetTargetFileHandle method returns a handle to the file that is associated with a specified remote I/O target. |
| [WdfIoTargetWdmGetTargetFileObject function](nf-wdfiotarget-wdfiotargetwdmgettargetfileobject.md) | The WdfIoTargetWdmGetTargetFileObject method returns a pointer to the Windows Driver Model (WDM) file object that is associated with a specified remote I/O target. |
| [WdfIoTargetWdmGetTargetPhysicalDevice function](nf-wdfiotarget-wdfiotargetwdmgettargetphysicaldevice.md) | The WdfIoTargetWdmGetTargetPhysicalDevice method returns a pointer to the Windows Driver Model (WDM) physical device object (PDO) that represents a remote I/O target's device. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_WDF_IO_TARGET_OPEN_PARAMS structure](ns-wdfiotarget-_wdf_io_target_open_params.md) | The WDF_IO_TARGET_OPEN_PARAMS structure contains parameters that the WdfIoTargetOpen method uses. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_WDF_IO_TARGET_OPEN_TYPE enumeration](ne-wdfiotarget-_wdf_io_target_open_type.md) | The WDF_IO_TARGET_OPEN_TYPE enumeration specifies how a driver identifies a remote I/O target when the driver calls WdfIoTargetOpen. |
| [_WDF_IO_TARGET_PURGE_IO_ACTION enumeration](ne-wdfiotarget-_wdf_io_target_purge_io_action.md) | The WDF_IO_TARGET_PURGE_IO_ACTION enumeration identifies the actions that the framework can take when a driver calls WdfIoTargetPurge to purge an I/O target. |
| [_WDF_IO_TARGET_SENT_IO_ACTION enumeration](ne-wdfiotarget-_wdf_io_target_sent_io_action.md) | The WDF_IO_TARGET_SENT_IO_ACTION enumeration identifies the actions that the framework can take when a driver calls WdfIoTargetStop to stop an I/O target. |
| [_WDF_IO_TARGET_STATE enumeration](ne-wdfiotarget-_wdf_io_target_state.md) | The WDF_IO_TARGET_STATE enumeration specifies the states that an I/O target can be in. |
