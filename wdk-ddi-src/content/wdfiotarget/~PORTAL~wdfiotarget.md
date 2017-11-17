# Declarations in the wdfiotarget header
This header Wdfiotarget contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFIOTARGETWDMGETTARGETPHYSICALDEVICE callback function](nc-wdfiotarget-pfn-wdfiotargetwdmgettargetphysicaldevice.md) | TBD |
| [EVT_WDF_IO_TARGET_QUERY_REMOVE callback](nc-wdfiotarget-evt-wdf-io-target-query-remove.md) | A driver's EvtIoTargetQueryRemove event callback function indicates whether the framework can safely remove a specified remote I/O target's device. |
| [PFN_WDFIOTARGETSENDINTERNALIOCTLOTHERSSYNCHRONOUSLY callback function](nc-wdfiotarget-pfn-wdfiotargetsendinternalioctlotherssynchronously.md) | TBD |
| [EVT_WDF_IO_TARGET_REMOVE_CANCELED callback](nc-wdfiotarget-evt-wdf-io-target-remove-canceled.md) | A driver's EvtIoTargetRemoveCanceled event callback function performs operations when the removal of a specified remote I/O target is canceled. |
| [PFN_WDFIOTARGETGETSTATE callback function](nc-wdfiotarget-pfn-wdfiotargetgetstate.md) | TBD |
| [PFN_WDFIOTARGETQUERYTARGETPROPERTY callback function](nc-wdfiotarget-pfn-wdfiotargetquerytargetproperty.md) | TBD |
| [PFN_WDFIOTARGETFORMATREQUESTFORINTERNALIOCTL callback function](nc-wdfiotarget-pfn-wdfiotargetformatrequestforinternalioctl.md) | TBD |
| [PFN_WDFIOTARGETALLOCANDQUERYTARGETPROPERTY callback function](nc-wdfiotarget-pfn-wdfiotargetallocandquerytargetproperty.md) | TBD |
| [EVT_WDF_IO_TARGET_REMOVE_COMPLETE callback](nc-wdfiotarget-evt-wdf-io-target-remove-complete.md) | A driver's EvtIoTargetRemoveComplete event callback function performs operations when the removal of a specified remote I/O target is complete. |
| [PFN_WDFIOTARGETWDMGETTARGETFILEHANDLE callback function](nc-wdfiotarget-pfn-wdfiotargetwdmgettargetfilehandle.md) | TBD |
| [PFN_WDFIOTARGETFORMATREQUESTFORREAD callback function](nc-wdfiotarget-pfn-wdfiotargetformatrequestforread.md) | TBD |
| [PFN_WDFIOTARGETSENDREADSYNCHRONOUSLY callback function](nc-wdfiotarget-pfn-wdfiotargetsendreadsynchronously.md) | TBD |
| [PFN_WDFIOTARGETFORMATREQUESTFORWRITE callback function](nc-wdfiotarget-pfn-wdfiotargetformatrequestforwrite.md) | TBD |
| [PFN_WDFIOTARGETFORMATREQUESTFORINTERNALIOCTLOTHERS callback function](nc-wdfiotarget-pfn-wdfiotargetformatrequestforinternalioctlothers.md) | TBD |
| [PFN_WDFIOTARGETCREATE callback function](nc-wdfiotarget-pfn-wdfiotargetcreate.md) | TBD |
| [*PFN_WDFIOTARGETSTOP callback function](nc-wdfiotarget-pfn-wdfiotargetstop.md) | TBD |
| [PFN_WDFIOTARGETOPEN callback function](nc-wdfiotarget-pfn-wdfiotargetopen.md) | TBD |
| [PFN_WDFIOTARGETCLOSE callback function](nc-wdfiotarget-pfn-wdfiotargetclose.md) | TBD |
| [PFN_WDFIOTARGETQUERYFORINTERFACE callback function](nc-wdfiotarget-pfn-wdfiotargetqueryforinterface.md) | TBD |
| [PFN_WDFIOTARGETGETDEVICE callback function](nc-wdfiotarget-pfn-wdfiotargetgetdevice.md) | TBD |
| [PFN_WDFIOTARGETWDMGETTARGETFILEOBJECT callback function](nc-wdfiotarget-pfn-wdfiotargetwdmgettargetfileobject.md) | TBD |
| [PFN_WDFIOTARGETFORMATREQUESTFORIOCTL callback function](nc-wdfiotarget-pfn-wdfiotargetformatrequestforioctl.md) | TBD |
| [PFN_WDFIOTARGETSENDINTERNALIOCTLSYNCHRONOUSLY callback function](nc-wdfiotarget-pfn-wdfiotargetsendinternalioctlsynchronously.md) | TBD |
| [PFN_WDFIOTARGETWDMGETTARGETDEVICEOBJECT callback function](nc-wdfiotarget-pfn-wdfiotargetwdmgettargetdeviceobject.md) | TBD |
| [PFN_WDFIOTARGETSTART callback function](nc-wdfiotarget-pfn-wdfiotargetstart.md) | TBD |
| [PFN_WDFIOTARGETSENDIOCTLSYNCHRONOUSLY callback function](nc-wdfiotarget-pfn-wdfiotargetsendioctlsynchronously.md) | TBD |
| [PFN_WDFIOTARGETCLOSEFORQUERYREMOVE callback function](nc-wdfiotarget-pfn-wdfiotargetcloseforqueryremove.md) | TBD |
| [*PFN_WDFIOTARGETPURGE callback function](nc-wdfiotarget-pfn-wdfiotargetpurge.md) | TBD |
| [PFN_WDFIOTARGETSENDWRITESYNCHRONOUSLY callback function](nc-wdfiotarget-pfn-wdfiotargetsendwritesynchronously.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_IO_TARGET_OPEN_TYPE enumeration](ne-wdfiotarget--wdf-io-target-open-type.md) | The WDF_IO_TARGET_OPEN_TYPE enumeration specifies how a driver identifies a remote I/O target when the driver calls WdfIoTargetOpen. |
| [WDF_IO_TARGET_SENT_IO_ACTION enumeration](ne-wdfiotarget--wdf-io-target-sent-io-action.md) | The WDF_IO_TARGET_SENT_IO_ACTION enumeration identifies the actions that the framework can take when a driver calls WdfIoTargetStop to stop an I/O target. |
| [WDF_IO_TARGET_STATE enumeration](ne-wdfiotarget--wdf-io-target-state.md) | The WDF_IO_TARGET_STATE enumeration specifies the states that an I/O target can be in. |
| [WDF_IO_TARGET_PURGE_IO_ACTION enumeration](ne-wdfiotarget--wdf-io-target-purge-io-action.md) | The WDF_IO_TARGET_PURGE_IO_ACTION enumeration identifies the actions that the framework can take when a driver calls WdfIoTargetPurge to purge an I/O target. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfIoTargetGetState function](nf-wdfiotarget-wdfiotargetgetstate.md) | The WdfIoTargetGetState method returns state information for a local or remote I/O target. |
| [WdfIoTargetOpen function](nf-wdfiotarget-wdfiotargetopen.md) | The WdfIoTargetOpen method opens a remote I/O target so the driver can send I/O requests to it. |
| [WdfIoTargetWdmGetTargetFileHandle function](nf-wdfiotarget-wdfiotargetwdmgettargetfilehandle.md) | The WdfIoTargetWdmGetTargetFileHandle method returns a handle to the file that is associated with a specified remote I/O target. |
| [WdfIoTargetGetDevice function](nf-wdfiotarget-wdfiotargetgetdevice.md) | The WdfIoTargetGetDevice method returns a handle to the framework device object that is the parent of the specified local or remote I/O target. |
| [WdfIoTargetFormatRequestForIoctl function](nf-wdfiotarget-wdfiotargetformatrequestforioctl.md) | The WdfIoTargetFormatRequestForIoctl method builds a device control request for an I/O target but does not send the request. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE function](nf-wdfiotarget-wdf-io-target-open-params-init-existing-device.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so that the driver can open a remote I/O target by specifying a Windows Driver Model (WDM) device object. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_CREATE_BY_NAME function](nf-wdfiotarget-wdf-io-target-open-params-init-create-by-name.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_CREATE_BY_NAME function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so the driver can open an I/O target by specifying the name of the device, file, or device interface. |
| [WdfIoTargetWdmGetTargetPhysicalDevice function](nf-wdfiotarget-wdfiotargetwdmgettargetphysicaldevice.md) | The WdfIoTargetWdmGetTargetPhysicalDevice method returns a pointer to the Windows Driver Model (WDM) physical device object (PDO) that represents a remote I/O target's device. |
| [WdfIoTargetFormatRequestForInternalIoctlOthers function](nf-wdfiotarget-wdfiotargetformatrequestforinternalioctlothers.md) | The WdfIoTargetFormatRequestForInternalIoctlOthers method builds a non-standard internal device control request for an I/O target but does not send the request. |
| [WdfIoTargetCreate function](nf-wdfiotarget-wdfiotargetcreate.md) | The WdfIoTargetCreate method creates a remote I/O target for a specified device. |
| [WdfIoTargetSendInternalIoctlSynchronously function](nf-wdfiotarget-wdfiotargetsendinternalioctlsynchronously.md) | The WdfIoTargetSendInternalIoctlSynchronously method builds an internal device control request and sends it synchronously to an I/O target. |
| [WdfIoTargetWdmGetTargetFileObject function](nf-wdfiotarget-wdfiotargetwdmgettargetfileobject.md) | The WdfIoTargetWdmGetTargetFileObject method returns a pointer to the Windows Driver Model (WDM) file object that is associated with a specified remote I/O target. |
| [WdfIoTargetStop function](nf-wdfiotarget-wdfiotargetstop.md) | The WdfIoTargetStop method stops sending queued requests to a local or remote I/O target. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_NAME function](nf-wdfiotarget-wdf-io-target-open-params-init-open-by-name.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_NAME function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so the driver can open an I/O target by specifying the name of the device, file, or device interface. |
| [WdfIoTargetSendReadSynchronously function](nf-wdfiotarget-wdfiotargetsendreadsynchronously.md) | The WdfIoTargetSendReadSynchronously method builds a read request and sends it synchronously to an I/O target. |
| [WdfIoTargetCloseForQueryRemove function](nf-wdfiotarget-wdfiotargetcloseforqueryremove.md) | The WdfIoTargetCloseForQueryRemove method temporarily closes a specified remote I/O target because the target device might soon be removed. |
| [WdfIoTargetQueryTargetProperty function](nf-wdfiotarget-wdfiotargetquerytargetproperty.md) | The WdfIoTargetQueryTargetProperty method retrieves a specified device property for a specified I/O target. |
| [WdfIoTargetQueryForInterface function](nf-wdfiotarget-wdfiotargetqueryforinterface.md) | The WdfIoTargetQueryForInterface method obtains access to the GUID-identified, driver-defined interface of a remote I/O target. |
| [WdfIoTargetFormatRequestForWrite function](nf-wdfiotarget-wdfiotargetformatrequestforwrite.md) | The WdfIoTargetFormatRequestForWrite method builds a write request for an I/O target but does not send the request. |
| [WdfIoTargetSendIoctlSynchronously function](nf-wdfiotarget-wdfiotargetsendioctlsynchronously.md) | The WdfIoTargetSendIoctlSynchronously method builds a device control request and sends it synchronously to an I/O target. |
| [WdfIoTargetFormatRequestForRead function](nf-wdfiotarget-wdfiotargetformatrequestforread.md) | The WdfIoTargetFormatRequestForRead method builds a read request for an I/O target but does not send the request. |
| [WdfIoTargetClose function](nf-wdfiotarget-wdfiotargetclose.md) | The WdfIoTargetClose method closes a specified remote I/O target. |
| [WdfIoTargetWdmGetTargetDeviceObject function](nf-wdfiotarget-wdfiotargetwdmgettargetdeviceobject.md) | The WdfIoTargetWdmGetTargetDeviceObject method returns a pointer to the Windows Driver Model (WDM) device object that is associated with a specified local or remote I/O target. |
| [WdfIoTargetFormatRequestForInternalIoctl function](nf-wdfiotarget-wdfiotargetformatrequestforinternalioctl.md) | The WdfIoTargetFormatRequestForInternalIoctl method builds an internal device control request for an I/O target but does not send the request. |
| [WdfIoTargetAllocAndQueryTargetProperty function](nf-wdfiotarget-wdfiotargetallocandquerytargetproperty.md) | The WdfIoTargetAllocAndQueryTargetProperty method allocates a buffer and retrieves a specified device property for a specified I/O target. |
| [WdfIoTargetPurge function](nf-wdfiotarget-wdfiotargetpurge.md) | The WdfIoTargetPurge method cancels all I/O requests queued to a local, remote, or specialized I/O target and prevents any new I/O requests from being queued. |
| [WdfIoTargetSendInternalIoctlOthersSynchronously function](nf-wdfiotarget-wdfiotargetsendinternalioctlotherssynchronously.md) | The WdfIoTargetSendInternalIoctlOthersSynchronously method builds a non-standard internal device control request and sends it synchronously to an I/O target. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN function](nf-wdfiotarget-wdf-io-target-open-params-init-reopen.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so the driver can reopen a remote I/O target. |
| [WdfIoTargetStart function](nf-wdfiotarget-wdfiotargetstart.md) | The WdfIoTargetStart method starts sending queued requests to a local or remote I/O target. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_FILE function](nf-wdfiotarget-wdf-io-target-open-params-init-open-by-file.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_FILE function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so the driver can open an I/O target by specifying a filename. |
| [WdfIoTargetSendWriteSynchronously function](nf-wdfiotarget-wdfiotargetsendwritesynchronously.md) | The WdfIoTargetSendWriteSynchronously method builds a write request and sends it synchronously to an I/O target. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_IO_TARGET_OPEN_PARAMS structure](ns-wdfiotarget--wdf-io-target-open-params.md) | The WDF_IO_TARGET_OPEN_PARAMS structure contains parameters that the WdfIoTargetOpen method uses. |

This header is used in these topics:

- [wdf](..content/_wdf)
