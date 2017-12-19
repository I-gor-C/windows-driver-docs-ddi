---
UID: NF.wdm.ExQueryDepthSList
title: ExQueryDepthSList function
author: windows-driver-content
description: The ExQueryDepthSList routine returns the number of entries currently in a given sequenced singly linked list.
old-location: kernel\exquerydepthslist.htm
old-project: kernel
ms.assetid: fdf40535-4e0d-4db9-9e95-744029eb2bd5
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: ExQueryDepthSList
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
req.alt-api: ExQueryDepthSList
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
req.product: Windows 10 or later.
---

# ExQueryDepthSList function



## -description
The <b>ExQueryDepthSList</b> routine returns the number of entries currently in a given sequenced singly linked list.



## -syntax

````
USHORT ExQueryDepthSList(
  _In_ PSLIST_HEADER SListHead
);
````


## -parameters

### -param SListHead [in]

A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563810">SLIST_HEADER</a> structure that serves as the header for the sequenced singly linked list. <i>SListHead</i> must have been initialized by calling <a href="kernel.exinitializeslisthead">ExInitializeSListHead</a>.


## -returns
<b>ExQueryDepthSList</b> returns the current number of entries in the list.


## -remarks
For more information about using this routine to implement a sequenced singly linked list, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563802">Singly and Doubly Linked Lists</a>.


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
Available starting with Windows 2000.

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
&lt;= DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exinitializeslisthead">ExInitializeSListHead</a>
</dt>
<dt>
<a href="kernel.exinterlockedpushentryslist">ExInterlockedPushEntrySList</a>
</dt>
<dt>
<a href="kernel.exinterlockedpopentryslist">ExInterlockedPopEntrySList</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExQueryDepthSList routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

