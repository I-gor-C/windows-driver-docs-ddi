---
UID: NF.ks.KsCreateAllocator2
title: KsCreateAllocator2
author: windows-driver-content
description: Creates a handle to an allocator for the given sink connection handle. This function does not complete the IRP or set the status in the IRP.
old-location: stream\kscreateallocator2.htm
old-project: stream
ms.assetid: f0efa17c-9318-46a4-bc08-d4d372cc07ba
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsCreateAllocator2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsCreateAllocator2
req.alt-loc: Ks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# KsCreateAllocator2 function



## -description
<p>Creates a handle to an allocator for the given sink connection handle. This function does not complete the IRP or set the status in the IRP.</p>
<p>Supported starting in Windows 8.</p>


## -syntax

````
 KSDDKAPI HRESULT WINAPI KsCreateAllocator2(
  _In_  HANDLE               ConnectionHandle,
  _In_  PKSALLOCATOR_FRAMING AllocatorFraming,
  _Out_ PHANDLE              AllocatorHandle
);
````


## -parameters
<dl>

### -param <i>ConnectionHandle</i> [in]

<dd>
<p>Specifies the handle to the sink connection on which to create the allocator.</p>
</dd>

### -param <i>AllocatorFraming</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560979">KSALLOCATOR_FRAMING</a> structure that specifies framing for the allocator.</p>
</dd>

### -param <i>AllocatorHandle</i> [out]

<dd>
<p>Specifies the pointer to a handle to store the allocator handle.</p>
</dd>
</dl>

## -returns
<p>Returns <b>NOERROR</b> if successful; otherwise, returns an error code.</p>

## -remarks
<p>This is a new version of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561633">KsCreateAllocator</a> function and uses the device broker to create the handle to the kernel streaming object. In addition, the Component Object Model (COM) <a href="com.coinitialize">CoInitialize</a> function must be called before this function is called.</p>

<p>This is a new version of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561633">KsCreateAllocator</a> function and uses the device broker to create the handle to the kernel streaming object. In addition, the Component Object Model (COM) <a href="com.coinitialize">CoInitialize</a> function must be called before this function is called.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="com.coinitialize">CoInitialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560979">KSALLOCATOR_FRAMING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561633">KsCreateAllocator</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsCreateAllocator2 function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
