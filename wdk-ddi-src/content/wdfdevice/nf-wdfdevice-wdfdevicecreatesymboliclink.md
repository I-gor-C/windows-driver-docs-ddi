---
UID: NF.wdfdevice.WdfDeviceCreateSymbolicLink
title: WdfDeviceCreateSymbolicLink
author: windows-driver-content
description: The WdfDeviceCreateSymbolicLink method creates a symbolic link to a specified device.
old-location: wdf\wdfdevicecreatesymboliclink.htm
ms.assetid: c22035a2-8ceb-42e9-9d54-8997ce0dd8da
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
req.alt-api: WdfDeviceCreateSymbolicLink
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
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
ms.keywords: WdfDeviceCreateSymbolicLink
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceCreateSymbolicLink function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfDeviceCreateSymbolicLink</b> method creates a symbolic link to a specified device.</p>


## -syntax

````
NTSTATUS WdfDeviceCreateSymbolicLink(
  _In_ WDFDEVICE        Device,
  _In_ PCUNICODE_STRING SymbolicLinkName
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>SymbolicLinkName</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure that contains a user-visible name for the device.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the <b>WdfDeviceCreateSymbolicLink</b> returns STATUS_SUCCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The system cannot allocate space to store the device name.</p>

<p> </p>

<p>The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>If a driver creates a symbolic link for a device, applications can use the symbolic link name to access the device. Typically, instead of providing symbolic links, framework-based drivers provide <a href="wdf.using_device_interfaces">device interfaces</a> that applications can use to access their devices.</p>

<p>If the device is removed unexpectedly (surprise-removed), the framework removes the symbolic link to the device. The driver can then use the symbolic link name for a new instance of the device.</p>

<p>The following code example from a KMDF driver creates an <a href="https://msdn.microsoft.com/9be6da8f-0641-4a67-9443-8e2056335bef">MS-DOS device name</a> that an application can use to access a device.</p>

<p>A UMDF driver must provide a symbolic link name in the global <b>DosDevices</b> namespace, as the following code example illustrates.</p>

<p>For information about global and local <b>\DosDevices</b> namespaces, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554302">Local and Global MS-DOS Device Names</a>.</p>

<p>If a driver creates a symbolic link for a device, applications can use the symbolic link name to access the device. Typically, instead of providing symbolic links, framework-based drivers provide <a href="wdf.using_device_interfaces">device interfaces</a> that applications can use to access their devices.</p>

<p>If the device is removed unexpectedly (surprise-removed), the framework removes the symbolic link to the device. The driver can then use the symbolic link name for a new instance of the device.</p>

<p>The following code example from a KMDF driver creates an <a href="https://msdn.microsoft.com/9be6da8f-0641-4a67-9443-8e2056335bef">MS-DOS device name</a> that an application can use to access a device.</p>

<p>A UMDF driver must provide a symbolic link name in the global <b>DosDevices</b> namespace, as the following code example illustrates.</p>

<p>For information about global and local <b>\DosDevices</b> namespaces, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554302">Local and Global MS-DOS Device Names</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceCreateSymbolicLink method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
