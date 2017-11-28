---
UID: NF.wdm.IoWMIDeviceObjectToProviderId
title: IoWMIDeviceObjectToProviderId
author: windows-driver-content
description: The IoWMIDeviceObjectToProviderId routine translates the specified device object into the corresponding WMI Provider ID.
old-location: kernel\iowmideviceobjecttoproviderid.htm
old-project: kernel
ms.assetid: 211d41ae-18d3-4ca5-b9f5-868d97fab6fb
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoWMIDeviceObjectToProviderId
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoWMIDeviceObjectToProviderId
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoWMIDeviceObjectToProviderId function



## -description
<p>The <b>IoWMIDeviceObjectToProviderId</b> routine translates the specified device object into the corresponding WMI Provider ID.</p>


## -syntax

````
ULONG IoWMIDeviceObjectToProviderId(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to a device object. </p>
</dd>
</dl>

## -returns
<p><b>IoWMIDeviceObjectToProviderId </b>returns the WMI Provider ID associated with the specified device object.</p>

## -remarks
<p><b>IoWMIDeviceObjectToProviderId</b> should be used when filling in the <b>ProviderId</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566375">WNODE_HEADER</a> structure in those cases when the <b>WNODEHEADER</b> structure is being initialized as part of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566373">WNODE_EVENT_ITEM</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff566374">WNODE_EVENT_REFERENCE</a> structure. (If the <b>WNODE_HEADER</b> is being used for other purposes, <i>ProviderId</i> is reserved.)</p>

<p>When running on a 32-bit operating system, the provider ID and the device object are identical. When running on a 64-bit operating system, <b>IoWMIDeviceObjectToProviderId</b> will convert the 64-bit device object to a 32-bit provider ID.</p>

<p><b>IoWMIDeviceObjectToProviderId</b> should be used when filling in the <b>ProviderId</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566375">WNODE_HEADER</a> structure in those cases when the <b>WNODEHEADER</b> structure is being initialized as part of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566373">WNODE_EVENT_ITEM</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff566374">WNODE_EVENT_REFERENCE</a> structure. (If the <b>WNODE_HEADER</b> is being used for other purposes, <i>ProviderId</i> is reserved.)</p>

<p>When running on a 32-bit operating system, the provider ID and the device object are identical. When running on a 64-bit operating system, <b>IoWMIDeviceObjectToProviderId</b> will convert the 64-bit device object to a 32-bit provider ID.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566375">WNODE_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566373">WNODE_EVENT_ITEM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566374">WNODE_EVENT_REFERENCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoWMIDeviceObjectToProviderId routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
