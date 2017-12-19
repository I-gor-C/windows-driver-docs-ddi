---
UID: NF.wdfdevice.WdfDeviceCreate
title: WdfDeviceCreate function
author: windows-driver-content
description: The WdfDeviceCreate method creates a framework device object.
old-location: wdf\wdfdevicecreate.htm
old-project: wdf
ms.assetid: 2a72d08a-a95b-4d50-a47b-e0e31ad43676
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfDeviceCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfDeviceCreate
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: AccessHardwareKey, AddPdoToStaticChildList, ChangeQueueState, ChildDeviceInitAPI, ChildListConfiguration, ControlDeviceDeleted, ControlDeviceInitAllocate, ControlDeviceInitAPI, CtlDeviceFinishInitDeviceAdd, CtlDeviceFinishInitDrEntry, DeviceCreateFail, DeviceInitAllocate, DeviceInitAPI, DriverCreate, InitFreeDeviceCreate, InitFreeDeviceCreateType2, InitFreeDeviceCreateType4, InitFreeNull, KmdfIrql, KmdfIrql2, PdoDeviceInitAPI, PdoInitFreeDeviceCreate, PdoInitFreeDeviceCreateType2, PdoInitFreeDeviceCreateType4
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceCreate function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfDeviceCreate</b> method creates a framework device object.



## -syntax

````
NTSTATUS WdfDeviceCreate(
  _Inout_  PWDFDEVICE_INIT        *DeviceInit,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES DeviceAttributes,
  _Out_    WDFDEVICE              *Device
);
````


## -parameters

### -param DeviceInit [in, out]

The address of a pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure. If <b>WdfDeviceCreate</b> encounters no errors, it sets the pointer to <b>NULL</b>.


### -param DeviceAttributes [in, optional]

A pointer to a caller-allocated <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that contains attributes for the new object. (The structure's <b>ParentObject</b> member must be <b>NULL</b>.) This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.


### -param Device [out]

A pointer to a location that receives a handle to the new framework device object.


## -returns
If the <b>WdfDeviceCreate</b> method encounters no errors, it returns STATUS_SUCCESS. Additional return values include:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An invalid <i>Device</i> or <i>DeviceInit</i> handle is supplied.
<dl>
<dt><b>STATUS_INVALID_DEVICE_STATE</b></dt>
</dl>The driver has already created a device object for the device.
<dl>
<dt><b>STATUS_INVALID_SECURITY_DESCR</b></dt>
</dl>the driver called <a href="wdf.wdfdeviceinitassignsddlstring">WdfDeviceInitAssignSDDLString</a> or <a href="wdf.wdfdeviceinitsetdeviceclass">WdfDeviceInitSetDeviceClass</a> but did not provide a name for the device object.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>A  device object could not be allocated.
<dl>
<dt><b>STATUS_OBJECT_NAME_COLLISION</b></dt>
</dl>The device name that was specified by a call to <a href="wdf.wdfdeviceinitassignname">WdfDeviceInitAssignName</a> already exists. The driver can call <b>WdfDeviceInitAssignName</b> again to assign a new name.

 

For a list of other return values that WdfDeviceCreate can return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.

The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.


## -remarks
Before calling <b>WdfDeviceCreate</b>, the driver must call framework-supplied functions that initialize the WDFDEVICE_INIT structure. For more information about initializing this structure, see <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a>. If the driver encounters errors while calling the initialization functions, it must not call <b>WdfDeviceCreate</b>. In this case, the driver might have to call <a href="wdf.wdfdeviceinitfree">WdfDeviceInitFree</a>. For information about when to call <b>WdfDeviceInitFree</b>, see <a href="wdf.wdfdeviceinitfree">WdfDeviceInitFree</a>.

A call to <b>WdfDeviceCreate</b> creates a framework device object that represents either a functional device object (FDO) or a physical device object (PDO). The type of device object that the function creates depends on how the driver obtained the WDFDEVICE_INIT structure: 

If the driver received the WDFDEVICE_INIT structure from an <a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a> callback, <b>WdfDeviceCreate</b> creates an FDO. 

If the driver received the WDFDEVICE_INIT structure from an <a href="..\wdfchildlist\nc-wdfchildlist-evt_wdf_child_list_create_device.md">EvtChildListCreateDevice</a> callback, or from a call to <a href="wdf.wdfpdoinitallocate">WdfPdoInitAllocate</a>, <b>WdfDeviceCreate</b> creates a PDO.

After the driver calls <b>WdfDeviceCreate</b>, it can no longer access the WDFDEVICE_INIT structure.

Miniport drivers that use the framework must call <a href="wdf.wdfdeviceminiportcreate">WdfDeviceMiniportCreate</a> instead of <b>WdfDeviceCreate</b>. 

The parent of each framework device object is the driver's framework driver object. The driver cannot change this parent, and the <b>ParentObject</b> member of the <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure must be <b>NULL</b>. The framework deletes each framework device object (except for some <a href="wdf.using_control_device_objects">control device objects</a>) when the Plug and Play (PnP) manager determines that the device has been removed.

If your driver provides <a href="..\wdfobject\nc-wdfobject-evt_wdf_object_context_cleanup.md">EvtCleanupCallback</a> or <a href="..\wdfobject\nc-wdfobject-evt_wdf_object_context_destroy.md">EvtDestroyCallback</a> callback functions for the framework device object, note that the framework calls these callback functions at IRQL = PASSIVE_LEVEL.

For more information about creating device objects, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.

The following code example shows how an <a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a> callback function might initialize and create a device object.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_accesshardwarekey">AccessHardwareKey</a>, <a href="devtest.kmdf_addpdotostaticchildlist">AddPdoToStaticChildList</a>, <a href="devtest.kmdf_changequeuestate">ChangeQueueState</a>, <a href="devtest.kmdf_childdeviceinitapi">ChildDeviceInitAPI</a>, <a href="devtest.kmdf_childlistconfiguration">ChildListConfiguration</a>, <a href="devtest.kmdf_controldevicedeleted">ControlDeviceDeleted</a>, <a href="devtest.kmdf_controldeviceinitallocate">ControlDeviceInitAllocate</a>, <a href="devtest.kmdf_controldeviceinitapi">ControlDeviceInitAPI</a>, <a href="devtest.kmdf_ctldevicefinishinitdeviceadd">CtlDeviceFinishInitDeviceAdd</a>, <a href="devtest.kmdf_ctldevicefinishinitdrentry">CtlDeviceFinishInitDrEntry</a>, <a href="devtest.kmdf_devicecreatefail">DeviceCreateFail</a>, <a href="devtest.kmdf_deviceinitallocate">DeviceInitAllocate</a>, <a href="devtest.kmdf_deviceinitapi">DeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_initfreedevicecreate">InitFreeDeviceCreate</a>, <a href="devtest.kmdf_initfreedevicecreatetype2">InitFreeDeviceCreateType2</a>, <a href="devtest.kmdf_initfreedevicecreatetype4">InitFreeDeviceCreateType4</a>, <a href="devtest.kmdf_initfreenull">InitFreeNull</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_pdodeviceinitapi">PdoDeviceInitAPI</a>, <a href="devtest.kmdf_pdoinitfreedevicecreate">PdoInitFreeDeviceCreate</a>, <a href="devtest.kmdf_pdoinitfreedevicecreatetype2">PdoInitFreeDeviceCreateType2</a>, <a href="devtest.kmdf_pdoinitfreedevicecreatetype4">PdoInitFreeDeviceCreateType4</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552404">WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE</a>
</dt>
<dt>
<a href="wdf.wdf_pnppower_event_callbacks_init">WDF_PNPPOWER_EVENT_CALLBACKS_INIT</a>
</dt>
<dt>
<a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a>
</dt>
<dt>
<a href="wdf.wdfdeviceinitfree">WdfDeviceInitFree</a>
</dt>
<dt>
<a href="wdf.wdfdeviceinitsetpnppowereventcallbacks">WdfDeviceInitSetPnpPowerEventCallbacks</a>
</dt>
<dt>
<a href="wdf.wdfdeviceminiportcreate">WdfDeviceMiniportCreate</a>
</dt>
<dt>
<a href="wdf.wdfdeviceinitsetiotype">WdfDeviceInitSetIoType</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceCreate method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

