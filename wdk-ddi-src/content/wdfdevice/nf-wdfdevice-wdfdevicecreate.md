---
UID: NF.wdfdevice.WdfDeviceCreate
title: WdfDeviceCreate
author: windows-driver-content
description: The WdfDeviceCreate method creates a framework device object.
old-location: wdf\wdfdevicecreate.htm
ms.assetid: 2a72d08a-a95b-4d50-a47b-e0e31ad43676
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
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
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: WdfDeviceCreate
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceCreate function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfDeviceCreate</b> method creates a framework device object.</p>


## -syntax

````
NTSTATUS WdfDeviceCreate(
  _Inout_  PWDFDEVICE_INIT        *DeviceInit,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES DeviceAttributes,
  _Out_    WDFDEVICE              *Device
);
````


## -parameters
<dl>

### -param <i>DeviceInit</i> [in, out]

<dd>
<p>The address of a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a> structure. If <b>WdfDeviceCreate</b> encounters no errors, it sets the pointer to <b>NULL</b>.</p>
</dd>

### -param <i>DeviceAttributes</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure that contains attributes for the new object. (The structure's <b>ParentObject</b> member must be <b>NULL</b>.) This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>Device</i> [out]

<dd>
<p>A pointer to a location that receives a handle to the new framework device object.</p>
</dd>
</dl>

## -returns
<p>If the <b>WdfDeviceCreate</b> method encounters no errors, it returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid <i>Device</i> or <i>DeviceInit</i> handle is supplied.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_STATE</b></dt>
</dl><p>The driver has already created a device object for the device.</p><dl>
<dt><b>STATUS_INVALID_SECURITY_DESCR</b></dt>
</dl><p>the driver called <a href="https://msdn.microsoft.com/library/windows/hardware/ff546035">WdfDeviceInitAssignSDDLString</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff546084">WdfDeviceInitSetDeviceClass</a> but did not provide a name for the device object.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A  device object could not be allocated.</p><dl>
<dt><b>STATUS_OBJECT_NAME_COLLISION</b></dt>
</dl><p>The device name that was specified by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff546029">WdfDeviceInitAssignName</a> already exists. The driver can call <b>WdfDeviceInitAssignName</b> again to assign a new name.</p>

<p> </p>

<p>For a list of other return values that WdfDeviceCreate can return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.</p>

<p>The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>Before calling <b>WdfDeviceCreate</b>, the driver must call framework-supplied functions that initialize the WDFDEVICE_INIT structure. For more information about initializing this structure, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a>. If the driver encounters errors while calling the initialization functions, it must not call <b>WdfDeviceCreate</b>. In this case, the driver might have to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546050">WdfDeviceInitFree</a>. For information about when to call <b>WdfDeviceInitFree</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546050">WdfDeviceInitFree</a>.</p>

<p>A call to <b>WdfDeviceCreate</b> creates a framework device object that represents either a functional device object (FDO) or a physical device object (PDO). The type of device object that the function creates depends on how the driver obtained the WDFDEVICE_INIT structure: </p>

<p>If the driver received the WDFDEVICE_INIT structure from an <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> callback, <b>WdfDeviceCreate</b> creates an FDO. </p>

<p>If the driver received the WDFDEVICE_INIT structure from an <a href="https://msdn.microsoft.com/296fbe06-1680-43a8-b5c3-1a1faa19c6c3">EvtChildListCreateDevice</a> callback, or from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548786">WdfPdoInitAllocate</a>, <b>WdfDeviceCreate</b> creates a PDO.</p>

<p>After the driver calls <b>WdfDeviceCreate</b>, it can no longer access the WDFDEVICE_INIT structure.</p>

<p>Miniport drivers that use the framework must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546802">WdfDeviceMiniportCreate</a> instead of <b>WdfDeviceCreate</b>. </p>

<p>The parent of each framework device object is the driver's framework driver object. The driver cannot change this parent, and the <b>ParentObject</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure must be <b>NULL</b>. The framework deletes each framework device object (except for some <a href="wdf.using_control_device_objects">control device objects</a>) when the Plug and Play (PnP) manager determines that the device has been removed.</p>

<p>If your driver provides <a href="https://msdn.microsoft.com/aba2efca-7d1f-4594-af65-13356f0e3f8b">EvtCleanupCallback</a> or <a href="https://msdn.microsoft.com/4c3b08d2-bb25-40bd-b2fc-1b9ea2d452b3">EvtDestroyCallback</a> callback functions for the framework device object, note that the framework calls these callback functions at IRQL = PASSIVE_LEVEL.</p>

<p>For more information about creating device objects, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>The following code example shows how an <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> callback function might initialize and create a device object.</p>

<p>Before calling <b>WdfDeviceCreate</b>, the driver must call framework-supplied functions that initialize the WDFDEVICE_INIT structure. For more information about initializing this structure, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a>. If the driver encounters errors while calling the initialization functions, it must not call <b>WdfDeviceCreate</b>. In this case, the driver might have to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546050">WdfDeviceInitFree</a>. For information about when to call <b>WdfDeviceInitFree</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546050">WdfDeviceInitFree</a>.</p>

<p>A call to <b>WdfDeviceCreate</b> creates a framework device object that represents either a functional device object (FDO) or a physical device object (PDO). The type of device object that the function creates depends on how the driver obtained the WDFDEVICE_INIT structure: </p>

<p>If the driver received the WDFDEVICE_INIT structure from an <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> callback, <b>WdfDeviceCreate</b> creates an FDO. </p>

<p>If the driver received the WDFDEVICE_INIT structure from an <a href="https://msdn.microsoft.com/296fbe06-1680-43a8-b5c3-1a1faa19c6c3">EvtChildListCreateDevice</a> callback, or from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548786">WdfPdoInitAllocate</a>, <b>WdfDeviceCreate</b> creates a PDO.</p>

<p>After the driver calls <b>WdfDeviceCreate</b>, it can no longer access the WDFDEVICE_INIT structure.</p>

<p>Miniport drivers that use the framework must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546802">WdfDeviceMiniportCreate</a> instead of <b>WdfDeviceCreate</b>. </p>

<p>The parent of each framework device object is the driver's framework driver object. The driver cannot change this parent, and the <b>ParentObject</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure must be <b>NULL</b>. The framework deletes each framework device object (except for some <a href="wdf.using_control_device_objects">control device objects</a>) when the Plug and Play (PnP) manager determines that the device has been removed.</p>

<p>If your driver provides <a href="https://msdn.microsoft.com/aba2efca-7d1f-4594-af65-13356f0e3f8b">EvtCleanupCallback</a> or <a href="https://msdn.microsoft.com/4c3b08d2-bb25-40bd-b2fc-1b9ea2d452b3">EvtDestroyCallback</a> callback functions for the framework device object, note that the framework calls these callback functions at IRQL = PASSIVE_LEVEL.</p>

<p>For more information about creating device objects, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>The following code example shows how an <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> callback function might initialize and create a device object.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975063">AccessHardwareKey</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975064">AddPdoToStaticChildList</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975067">ChangeQueueState</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975068">ChildDeviceInitAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975069">ChildListConfiguration</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543528">ControlDeviceDeleted</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975071">ControlDeviceInitAllocate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543531">ControlDeviceInitAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543607">CtlDeviceFinishInitDeviceAdd</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543610">CtlDeviceFinishInitDrEntry</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544839">DeviceCreateFail</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544841">DeviceInitAllocate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544843">DeviceInitAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547104">InitFreeDeviceCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547109">InitFreeDeviceCreateType2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547119">InitFreeDeviceCreateType4</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547122">InitFreeNull</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550354">PdoDeviceInitAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550362">PdoInitFreeDeviceCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550366">PdoInitFreeDeviceCreateType2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550368">PdoInitFreeDeviceCreateType4</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552404">WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552418">WDF_PNPPOWER_EVENT_CALLBACKS_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546050">WdfDeviceInitFree</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546135">WdfDeviceInitSetPnpPowerEventCallbacks</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546802">WdfDeviceMiniportCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546128">WdfDeviceInitSetIoType</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceCreate method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
