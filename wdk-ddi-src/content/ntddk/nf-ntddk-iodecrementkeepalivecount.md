---
UID: NF.ntddk.IoDecrementKeepAliveCount
title: IoDecrementKeepAliveCount function
author: windows-driver-content
description: The IoDecrementKeepAliveCount routine decrements a reference count associated with an Windows app on a specific device.
old-location: kernel\iodecrementkeepalivecount.htm
old-project: kernel
ms.assetid: 2A8BC777-291C-4EC4-8EF9-AA78C6295700
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: IoDecrementKeepAliveCount
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
req.alt-api: IoDecrementKeepAliveCount
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

# IoDecrementKeepAliveCount function



## -description
The <b>IoDecrementKeepAliveCount</b> routine decrements a reference count associated with an Windows app on a specific device. This routine is called by a kernel mode driver when the app's I/O process has completed.  If the app's reference count drops to 0, Windows can suspend the app.



## -syntax

````
NTSTATUS IoDecrementKeepAliveCount(
  _Inout_           FileObject,
  _Inout_ PEPROCESS Process
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