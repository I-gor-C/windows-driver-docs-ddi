---
UID: NF.ntddk.IoIncrementKeepAliveCount
title: IoIncrementKeepAliveCount function
author: windows-driver-content
description: The IoIncrementKeepAliveCount routine increments a reference count associated with an Windows app process on a specific device.
old-location: kernel\ioincrementkeepalivecount.htm
old-project: kernel
ms.assetid: A80754BD-0F23-4EE9-898F-30743AA82C72
ms.author: windowsdriverdev
ms.date: 12/6/2017
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
---

# IoIncrementKeepAliveCount function



## -description
The <b>IoIncrementKeepAliveCount</b> routine increments a reference count associated with an Windows app process on a specific device. This routine is called by a kernel mode driver in response to the app opening a process for I/O. This prevents Windows from suspending the app before the I/O process is complete.


## -syntax

````
NTSTATUS IoIncrementKeepAliveCount(
  _Inout_ PFILE_OBJECT FileObject,
  _Inout_ PEPROCESS    Process
);
````


## -parameters

### -param FileObject [in, out]

The file object handle to the device.

### -param Process [in, out]

The process associated with the device.

## -returns
This routine returns <b>STATUS_SUCCESS</b> on success, or the appropriate <b>NTSTATUS</b> error code on failure. <b>NTSTATUS</b> error codes are defined in Ntstatus.h.

## -remarks


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
Version
</th>
<td width="70%">
Available in Windows 8.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
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
<a href="kernel.iodecrementkeepalivecount">IoDecrementKeepAliveCount</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoIncrementKeepAliveCount routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
