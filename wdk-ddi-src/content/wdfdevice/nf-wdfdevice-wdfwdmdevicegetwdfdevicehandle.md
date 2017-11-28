---
UID: NF.wdfdevice.WdfWdmDeviceGetWdfDeviceHandle
title: WdfWdmDeviceGetWdfDeviceHandle
author: windows-driver-content
description: The WdfWdmDeviceGetWdfDeviceHandle method returns a handle to the framework device object that is associated with a specified WDM device object.
old-location: wdf\wdfwdmdevicegetwdfdevicehandle.htm
old-project: wdf
ms.assetid: 8083af10-1b35-4600-b409-e895d35f7ccc
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfWdmDeviceGetWdfDeviceHandle
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
req.alt-api: WdfWdmDeviceGetWdfDeviceHandle
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfWdmDeviceGetWdfDeviceHandle function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfWdmDeviceGetWdfDeviceHandle</b> method returns a handle to the framework device object that is associated with a specified WDM device object.</p>


## -syntax

````
WDFDEVICE WdfWdmDeviceGetWdfDeviceHandle(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>A pointer to a WDM <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure that the calling driver created.</p>
</dd>
</dl>

## -returns
<p>If the specified WDM device object is valid, <b>WdfWdmDeviceGetWdfDeviceHandle</b> returns a handle to the associated framework device object. Otherwise, the method returns <b>NULL</b>.</p>

## -remarks
<p>The WDM DEVICE_OBJECT structure that the driver specifies for the <i>DeviceObject</i> parameter must represent a device object that the calling driver created. For example, the structure cannot represent any of the WDM device objects that the driver specified in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff546802">WdfDeviceMiniportCreate</a>.</p>

<p>The following code example obtains a handle to the framework device object that is associated with a WDM device object that the calling driver created.</p>

<p>The WDM DEVICE_OBJECT structure that the driver specifies for the <i>DeviceObject</i> parameter must represent a device object that the calling driver created. For example, the structure cannot represent any of the WDM device objects that the driver specified in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff546802">WdfDeviceMiniportCreate</a>.</p>

<p>The following code example obtains a handle to the framework device object that is associated with a WDM device object that the calling driver created.</p>

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
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546802">WdfDeviceMiniportCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfWdmDeviceGetWdfDeviceHandle method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
