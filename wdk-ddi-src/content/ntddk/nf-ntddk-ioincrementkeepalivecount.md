---
UID: NF.ntddk.IoIncrementKeepAliveCount
title: IoIncrementKeepAliveCount
author: windows-driver-content
description: The IoIncrementKeepAliveCount routine increments a reference count associated with an Windows app process on a specific device.
old-location: kernel\ioincrementkeepalivecount.htm
old-project: kernel
ms.assetid: A80754BD-0F23-4EE9-898F-30743AA82C72
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoIncrementKeepAliveCount
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoIncrementKeepAliveCount
req.alt-loc: Ntoskrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: Ntoskrnl.exe
req.irql: 
req.iface: 
---

# IoIncrementKeepAliveCount function



## -description
<p>The <b>IoIncrementKeepAliveCount</b> routine increments a reference count associated with an Windows app process on a specific device. This routine is called by a kernel mode driver in response to the app opening a process for I/O. This prevents Windows from suspending the app before the I/O process is complete.</p>


## -syntax

````
NTSTATUS IoIncrementKeepAliveCount(
  _Inout_ PFILE_OBJECT FileObject,
  _Inout_ PEPROCESS    Process
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in, out]

<dd>
<p>The file object handle to the device.</p>
</dd>

### -param <i>Process</i> [in, out]

<dd>
<p>The process associated with the device.</p>
</dd>
</dl>

## -returns
<p>This routine returns <b>STATUS_SUCCESS</b> on success, or the appropriate <b>NTSTATUS</b> error code on failure. <b>NTSTATUS</b> error codes are defined in Ntstatus.h.</p>

## -remarks


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
<p>Available in Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.exe</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-iodecrementkeepalivecount.md">IoDecrementKeepAliveCount</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoIncrementKeepAliveCount routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
