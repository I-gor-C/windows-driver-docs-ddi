---
UID: NF.wdfdevice.WdfDeviceAddDependentUsageDeviceObject
title: WdfDeviceAddDependentUsageDeviceObject function
author: windows-driver-content
description: The WdfDeviceAddDependentUsageDeviceObject method indicates that a specified device depends on another device when the specified device is used to store special files.
old-location: wdf\wdfdeviceadddependentusagedeviceobject.htm
old-project: wdf
ms.assetid: 025046e2-ffa1-4210-b4aa-ab3d6b211066
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfDeviceAddDependentUsageDeviceObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDeviceAddDependentUsageDeviceObject
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
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceAddDependentUsageDeviceObject function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceAddDependentUsageDeviceObject</b> method indicates that a specified device depends on another device when the specified device is used to store <a href="wdf.wdf_special_file_type">special files</a>. 



## -syntax

````
NTSTATUS WdfDeviceAddDependentUsageDeviceObject(
  _In_ WDFDEVICE      Device,
  _In_ PDEVICE_OBJECT DependentDevice
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.


### -param DependentDevice [in]

A pointer to a caller-supplied <a href="kernel.device_object">DEVICE_OBJECT</a> structure that identifies a device that <i>Device</i> depends on.


## -returns
If the operation succeeds, <b>WdfDeviceAddDependentUsageDeviceObject</b> method returns STATUS_SUCCESS. Additional return values include:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><i>DependentDevice</i> is <b>NULL</b>.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>A memory allocation failed.

 

The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

A bug check occurs if the driver supplies an invalid object handle.


## -remarks
Your driver can call <b>WdfDeviceAddDependentUsageDeviceObject</b> to indicate that the device identified by <i>Device</i> depends on the device identified by <i>DependentDevice</i>, when <i>Device</i> supports special files. If your driver calls <b>WdfDeviceAddDependentUsageDeviceObject</b>, the framework calls the <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_usage_notification.md">EvtDeviceUsageNotification</a> callback functions in <i>DependentDevice</i>'s drivers before it calls the <i>EvtDeviceUsageNotification</i> callback functions in <i>Device</i>'s drivers.

Your driver can call <b>WdfDeviceAddDependentUsageDeviceObject</b> multiple times to identify multiple devices that <i>Device</i> depends on to support special files.

After a driver has called <b>WdfDeviceAddDependentUsageDeviceObject</b>, it can call <a href="wdf.wdfdeviceremovedependentusagedeviceobject">WdfDeviceRemoveDependentUsageDeviceObject</a> to remove the device identified by <i>DependentDevice</i> from the list of devices that <i>Device</i> depends on.

For more information about special files, see <a href="wdf.supporting_special_files">Supporting Special Files</a>. 

The following code example adds a device (<b>pDeviceObject</b>) to the list of devices that another device (<b>Device</b>) depends on.


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
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_usage_notification.md">EvtDeviceUsageNotification</a>
</dt>
<dt>
<a href="wdf.wdfdeviceremovedependentusagedeviceobject">WdfDeviceRemoveDependentUsageDeviceObject</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceAddDependentUsageDeviceObject method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

