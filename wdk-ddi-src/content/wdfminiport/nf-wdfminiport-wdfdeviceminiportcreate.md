---
UID: NF.wdfminiport.WdfDeviceMiniportCreate
title: WdfDeviceMiniportCreate
author: windows-driver-content
description: The WdfDeviceMiniportCreate method creates a framework device object that a miniport driver can use.
old-location: wdf\wdfdeviceminiportcreate.htm
old-project: wdf
ms.assetid: d74dedbd-f418-4ea3-ae76-c0da9c5f2fb9
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfDeviceMiniportCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfminiport.h
req.include-header: Wdfminiport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDeviceMiniportCreate
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceMiniportCreate function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDeviceMiniportCreate</b> method creates a framework device object that a miniport driver can use.</p>


## -syntax

````
NTSTATUS WdfDeviceMiniportCreate(
  _In_     WDFDRIVER              Driver,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES Attributes,
  _In_     PDEVICE_OBJECT         DeviceObject,
  _In_opt_ PDEVICE_OBJECT         AttachedDeviceObject,
  _In_opt_ PDEVICE_OBJECT         Pdo,
  _Out_    WDFDEVICE              *Device
);
````


## -parameters
<dl>

### -param <i>Driver</i> [in]

<dd>
<p>A handle to the driver's framework driver object, obtained by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547175">WdfDriverCreate</a>.</p>
</dd>

### -param <i>Attributes</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure that contains attributes for the new object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>DeviceObject</i> [in]

<dd>
<p>A pointer to a WDM <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure that represents the functional device object (FDO) for the miniport driver.</p>
</dd>

### -param <i>AttachedDeviceObject</i> [in, optional]

<dd>
<p>A pointer to a WDM DEVICE_OBJECT structure that represents the next-lower device object in the device stack.</p>
</dd>

### -param <i>Pdo</i> [in, optional]

<dd>
<p>A pointer to a WDM DEVICE_OBJECT structure that represents the physical device object (PDO) for the device.</p>
</dd>

### -param <i>Device</i> [out]

<dd>
<p>A pointer to a location that receives a handle to the new framework device object.</p>
</dd>
</dl>

## -returns
<p>If the <b>WdfDeviceMiniportCreate</b> method encounters no errors, it returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A device object could not be allocated.</p>

<p> </p>

<p>For a list of other return values that <b>WdfDeviceMiniportCreate</b> can return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.</p>

<p>The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>If your miniport driver uses the framework, the miniport driver should call <b>WdfDeviceMiniportCreate</b> when its port driver informs it that a device is available. Miniport drivers do not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>.</p>

<p>Your miniport driver might receive its <i>DeviceObject</i>, <i>AttachedDeviceObject</i>, and <i>PDO</i> pointers from its port driver. For example, an NDIS miniport driver can obtain these pointers by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff563592">NdisMGetDeviceProperty</a>.</p>

<p>The following restrictions apply to framework device objects that a miniport driver obtains by calling <b>WdfDeviceMiniportCreate</b>:</p>

<p>The device that the device object represents must support Plug and Play.</p>

<p>The device object does not support any of the device object's event callback functions. Therefore, the port driver must handle all Plug and Play (PnP) and power management operations. </p>

<p>The device object handle cannot be passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551193">WdfWmiProviderCreate</a>, so the port driver must provide any required support for Windows Management Instrumentation (WMI).</p>

<p>The device object handle cannot be passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547401">WdfIoQueueCreate</a>, so the framework does not support I/O queues for miniport drivers.</p>

<p>The device object handle cannot be passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547345">WdfInterruptCreate</a>, so the framework does not support interrupt objects for miniport drivers.</p>

<p>The device object handle cannot be passed to any general framework device object methods except <a href="https://msdn.microsoft.com/library/windows/hardware/ff546017">WdfDeviceGetIoTarget</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff546942">WdfDeviceWdmGetDeviceObject</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff546934">WdfDeviceWdmGetAttachedDevice</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff546946">WdfDeviceWdmGetPhysicalDevice</a>.</p>

<p>The device object handle cannot be passed to any <a href="wdf_device_object_reference.htm#fdo_methods">framework FDO methods</a> except <a href="https://msdn.microsoft.com/library/windows/hardware/ff547289">WdfFdoQueryForInterface</a>.</p>

<p>The device object handle cannot be passed to any <a href="wdf_device_object_reference.htm#pdo_methods">framework PDO methods</a> or to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545615">WdfChildListCreate</a>, so the miniport driver cannot be a bus driver.</p>

<p>The driver must eventually call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a> to delete the device object that <b>WdfDeviceMiniportCreate</b> creates.</p>

<p>Framework device objects that <b>WdfDeviceMiniportCreate</b> create can be used as a parent object for any subsequently created framework object. </p>

<p>In order to send I/O requests to I/O targets, the miniport driver might pass the device object handle to <a href="https://msdn.microsoft.com/library/windows/hardware/ff546017">WdfDeviceGetIoTarget</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548591">WdfIoTargetCreate</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a>.</p>

<p>The miniport driver can pass the device object handle to <a href="https://msdn.microsoft.com/library/windows/hardware/ff546983">WdfDmaEnablerCreate</a> if the device supports DMA operations.</p>

<p>For more information about miniport drivers, see <a href="wdf.creating_kmdf_miniport_drivers">Using Kernel-Mode Driver Framework with Miniport Drivers</a>.</p>

<p>The following code example calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff563592">NdisMGetDeviceProperty</a> to obtain <i>DeviceObject</i>, <i>AttachedDeviceObject</i>, and <i>PDO</i> pointers; initializes the device object's context space, and creates a miniport device object. </p>

<p>If your miniport driver uses the framework, the miniport driver should call <b>WdfDeviceMiniportCreate</b> when its port driver informs it that a device is available. Miniport drivers do not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>.</p>

<p>Your miniport driver might receive its <i>DeviceObject</i>, <i>AttachedDeviceObject</i>, and <i>PDO</i> pointers from its port driver. For example, an NDIS miniport driver can obtain these pointers by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff563592">NdisMGetDeviceProperty</a>.</p>

<p>The following restrictions apply to framework device objects that a miniport driver obtains by calling <b>WdfDeviceMiniportCreate</b>:</p>

<p>The device that the device object represents must support Plug and Play.</p>

<p>The device object does not support any of the device object's event callback functions. Therefore, the port driver must handle all Plug and Play (PnP) and power management operations. </p>

<p>The device object handle cannot be passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551193">WdfWmiProviderCreate</a>, so the port driver must provide any required support for Windows Management Instrumentation (WMI).</p>

<p>The device object handle cannot be passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547401">WdfIoQueueCreate</a>, so the framework does not support I/O queues for miniport drivers.</p>

<p>The device object handle cannot be passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547345">WdfInterruptCreate</a>, so the framework does not support interrupt objects for miniport drivers.</p>

<p>The device object handle cannot be passed to any general framework device object methods except <a href="https://msdn.microsoft.com/library/windows/hardware/ff546017">WdfDeviceGetIoTarget</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff546942">WdfDeviceWdmGetDeviceObject</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff546934">WdfDeviceWdmGetAttachedDevice</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff546946">WdfDeviceWdmGetPhysicalDevice</a>.</p>

<p>The device object handle cannot be passed to any <a href="wdf_device_object_reference.htm#fdo_methods">framework FDO methods</a> except <a href="https://msdn.microsoft.com/library/windows/hardware/ff547289">WdfFdoQueryForInterface</a>.</p>

<p>The device object handle cannot be passed to any <a href="wdf_device_object_reference.htm#pdo_methods">framework PDO methods</a> or to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545615">WdfChildListCreate</a>, so the miniport driver cannot be a bus driver.</p>

<p>The driver must eventually call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a> to delete the device object that <b>WdfDeviceMiniportCreate</b> creates.</p>

<p>Framework device objects that <b>WdfDeviceMiniportCreate</b> create can be used as a parent object for any subsequently created framework object. </p>

<p>In order to send I/O requests to I/O targets, the miniport driver might pass the device object handle to <a href="https://msdn.microsoft.com/library/windows/hardware/ff546017">WdfDeviceGetIoTarget</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548591">WdfIoTargetCreate</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a>.</p>

<p>The miniport driver can pass the device object handle to <a href="https://msdn.microsoft.com/library/windows/hardware/ff546983">WdfDmaEnablerCreate</a> if the device supports DMA operations.</p>

<p>For more information about miniport drivers, see <a href="wdf.creating_kmdf_miniport_drivers">Using Kernel-Mode Driver Framework with Miniport Drivers</a>.</p>

<p>The following code example calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff563592">NdisMGetDeviceProperty</a> to obtain <i>DeviceObject</i>, <i>AttachedDeviceObject</i>, and <i>PDO</i> pointers; initializes the device object's context space, and creates a miniport device object. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfminiport.h (include Wdfminiport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547193">WdfDriverMiniportUnload</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552404">WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceMiniportCreate method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
