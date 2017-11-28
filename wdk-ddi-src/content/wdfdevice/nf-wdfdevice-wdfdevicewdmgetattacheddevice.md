---
UID: NF.wdfdevice.WdfDeviceWdmGetAttachedDevice
title: WdfDeviceWdmGetAttachedDevice
author: windows-driver-content
description: The WdfDeviceWdmGetAttachedDevice method returns the next-lower WDM device object in the device stack.
old-location: wdf\wdfdevicewdmgetattacheddevice.htm
old-project: wdf
ms.assetid: 216fe649-18c0-4782-8040-21ce87fbd888
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfDeviceWdmGetAttachedDevice
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
req.alt-api: WdfDeviceWdmGetAttachedDevice
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceWdmGetAttachedDevice function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDeviceWdmGetAttachedDevice</b> method returns the next-lower WDM device object in the <a href="wdf.wdm_concepts_for_kmdf_drivers#device_stacks#device_stacks">device stack</a>.</p>


## -syntax

````
PDEVICE_OBJECT WdfDeviceWdmGetAttachedDevice(
  _In_ WDFDEVICE Device
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>
</dl>

## -returns
<p><b>WdfDeviceWdmGetAttachedDevice</b> returns a pointer to a WDM <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure. If the specified object handle represents a physical device object (PDO), the method returns <b>NULL</b>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>The pointer that the <b>WdfDeviceWdmGetAttachedDevice</b> method returns is valid until the framework device object is deleted. If the driver provides an <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-cleanup.md">EvtCleanupCallback</a> function for the framework device object, the pointer is valid until the callback function returns.</p>

<p>The following code example creates a tracing message that contains pointers to the WDM device objects that represent a device's PDO, FDO, and next-lower device.</p>

<p>The pointer that the <b>WdfDeviceWdmGetAttachedDevice</b> method returns is valid until the framework device object is deleted. If the driver provides an <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-cleanup.md">EvtCleanupCallback</a> function for the framework device object, the pointer is valid until the callback function returns.</p>

<p>The following code example creates a tracing message that contains pointers to the WDM device objects that represent a device's PDO, FDO, and next-lower device.</p>

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
<p>&lt;= DISPATCH_LEVEL</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546946">WdfDeviceWdmGetPhysicalDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546942">WdfDeviceWdmGetDeviceObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceWdmGetAttachedDevice method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
