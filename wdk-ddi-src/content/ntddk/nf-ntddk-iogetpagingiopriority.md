---
UID: NF.ntddk.IoGetPagingIoPriority
title: IoGetPagingIoPriority function
author: windows-driver-content
description: The IoGetPagingIoPriority routine indicates the priority level of a paging I/O request.
old-location: kernel\iogetpagingiopriority.htm
old-project: kernel
ms.assetid: 3b0f4fc9-58fd-46ba-be17-2e1b36b16caa
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: IoGetPagingIoPriority
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows Server 2003 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoGetPagingIoPriority
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
req.irql: Any level
---

# IoGetPagingIoPriority function



## -description
The <b>IoGetPagingIoPriority</b> routine indicates the priority level of a paging I/O request.


## -syntax

````
IO_PAGING_PRIORITY IoGetPagingIoPriority(
  _In_ PIRP Irp
);
````


## -parameters

### -param Irp [in]

Pointer to the IRP to be tested for paging priority.

## -returns
<b>IoGetPagingIoPriority</b> returns the <a href="kernel.io_paging_priority">IO_PAGING_PRIORITY</a> value for the associated IRP.

## -remarks
For I/O requests that causing paging, the system associates an <b>IO_PAGING_PRIORITY</b> value that describes the IRP's priority. Drivers can use this value when queuing IRPs.

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
Available in Microsoft Windows Server 2003 and later versions of Windows.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
Any level
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.io_paging_priority">IO_PAGING_PRIORITY</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoGetPagingIoPriority routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
