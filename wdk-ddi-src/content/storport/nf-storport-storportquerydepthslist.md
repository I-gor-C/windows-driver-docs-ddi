---
UID: NF.storport.StorPortQueryDepthSList
title: StorPortQueryDepthSList
author: windows-driver-content
description: Retrieves the number of entries in a Storport managed singly linked list.
old-location: storage\storportquerydepthslist.htm
old-project: storage
ms.assetid: 5E1CE999-8173-49B6-8CF7-F3A5B193A230
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortQueryDepthSList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available in starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortQueryDepthSList
req.alt-loc: storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# StorPortQueryDepthSList function



## -description
<p>Retrieves the number of entries in a Storport managed singly linked list.</p>


## -syntax

````
ULONG StorPortQueryDepthSList(
  _In_    PVOID              HwDeviceExtension,
  _Inout_ PSTOR_SLIST_HEADER SListHead,
  _Out_   PSHORT             Result
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>SListHead</i> [in, out]

<dd>
<p>A pointer to an <b>STOR_SLIST_HEADER</b> structure that represents the head of a singly linked list. This structure is considered opaque and is for use by the Storport driver only.</p>
</dd>

### -param <i>Result</i> [out]

<dd>
<p>A pointer to a <b>SHORT</b> value which receives the  list depth count.</p>
</dd>
</dl>

## -returns
<p><b>StorPortQueryDepthSList</b> returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The list depth  was successfully returned.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>A pointer in <i>SListHead</i> or <i>Result</i> is <b>NULL</b>.</p>

<p> </p>

## -remarks
<p>Since <b>StorPortQueryDepthSList</b> is not interlocked, the list  depth value pointed to by <i>Result</i> on return is not reliable in when multiple threads are operating on the list.</p>

<p>Since <b>StorPortQueryDepthSList</b> is not interlocked, the list  depth value pointed to by <i>Result</i> on return is not reliable in when multiple threads are operating on the list.</p>

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
<p>Available in starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967735">StorPortInitializeSListHead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967736">StorPortInterlockedFlushSList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967737">StorPortInterlockedPopEntrySList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967738">StorPortInterlockedPushEntrySList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortQueryDepthSList routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
