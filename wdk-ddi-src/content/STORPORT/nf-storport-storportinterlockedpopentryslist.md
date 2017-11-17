---
UID: NF.storport.StorPortInterlockedPopEntrySList
title: StorPortInterlockedPopEntrySList
author: windows-driver-content
description: Removes an item from the front of a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system. Syntax.
old-location: storage\storportinterlockedpopentryslist.htm
ms.assetid: 9DA0A057-1472-4B42-9149-A961F7D84B2E
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available in starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortInterlockedPopEntrySList
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
ms.keywords: StorPortInterlockedPopEntrySList
req.iface: 
req.product: Windows 10 or later.
---

# StorPortInterlockedPopEntrySList function



## -description
<p>Removes an item from the front of a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system.
 
Syntax</p>


## -syntax

````
ULONG StorPortInterlockedPopEntrySList(
  _In_    PVOID               HwDeviceExtension,
  _Inout_ PSTOR_SLIST_HEADER  SListHead,
  _Out_   PSTOR_SLIST_ENTRY * Result
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
<p>A pointer to a list entry pointer. The value returned is a pointer to  the item removed  from the front of the list. If the list is empty, then <b>NULL</b> is returned in the value pointed to by <i>Result</i>.</p>
</dd>
</dl>

## -returns
<p><b>StorPortInterlockedPopEntrySList</b> returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The list item was successfully removed from  the list or is already empty.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>A pointer in <i>SListHead</i> or <i>Result</i> is <b>NULL</b>.</p>

<p> </p>

## -remarks
<p>The <b>StorPortInterlockedPopEntrySList</b> will also return <b>STATUS_SUCCESS</b> when no entries are in the list. The pointer value referenced by <i>Result</i> must be evaluated for <b>NULL</b> to verify that no entry was returned.</p>

<p><b>StorPortInterlockedPopEntrySList</b> does  not free the list entry it returns. Any deallocation code for the list must take care to free memory allocated for a list entry at the location obtained prior to any adjustment for boundary alignment. The value pointed to by <i>Result</i> may not be the original buffer location allocated due to an adjustment for <b>MEMORY_ALLOCATION_ALIGNMENT</b>. See remarks for <a href="https://msdn.microsoft.com/library/windows/hardware/hh967738">StorPortInterlockedPushEntrySList</a>.</p>

<p>The <b>StorPortInterlockedPopEntrySList</b> will also return <b>STATUS_SUCCESS</b> when no entries are in the list. The pointer value referenced by <i>Result</i> must be evaluated for <b>NULL</b> to verify that no entry was returned.</p>

<p><b>StorPortInterlockedPopEntrySList</b> does  not free the list entry it returns. Any deallocation code for the list must take care to free memory allocated for a list entry at the location obtained prior to any adjustment for boundary alignment. The value pointed to by <i>Result</i> may not be the original buffer location allocated due to an adjustment for <b>MEMORY_ALLOCATION_ALIGNMENT</b>. See remarks for <a href="https://msdn.microsoft.com/library/windows/hardware/hh967738">StorPortInterlockedPushEntrySList</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967738">StorPortInterlockedPushEntrySList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967739">StorPortQueryDepthSList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20StorPortInterlockedPopEntrySList routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
