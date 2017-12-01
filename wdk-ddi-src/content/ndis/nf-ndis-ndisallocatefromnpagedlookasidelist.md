---
UID: NF.ndis.NdisAllocateFromNPagedLookasideList
title: NdisAllocateFromNPagedLookasideList
author: windows-driver-content
description: The NdisAllocateFromNPagedLookasideList function removes the first entry from the given lookaside list head. If the lookaside list currently is empty, an entry is allocated from nonpaged pool.
old-location: netvista\ndisallocatefromnpagedlookasidelist.htm
old-project: netvista
ms.assetid: df690a05-359d-44f0-b063-4fc21d6c4d76
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisAllocateFromNPagedLookasideList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see       NdisAllocateFromNPagedLookasideList (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers   (see       NdisAllocateFromNPagedLookasideList (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisAllocateFromNPagedLookasideList
req.alt-loc: ndis.h
req.ddi-compliance: Irql_Miscellaneous_Function
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
---

# NdisAllocateFromNPagedLookasideList function



## -description
<p>The 
  <b>NdisAllocateFromNPagedLookasideList</b> function removes the first entry from the given lookaside list
  head. If the lookaside list currently is empty, an entry is allocated from nonpaged pool.</p>


## -syntax

````
PVOID NdisAllocateFromNPagedLookasideList(
  _In_ PNPAGED_LOOKASIDE_LIST Lookaside
);
````


## -parameters
<dl>

### -param <i>Lookaside</i> [in]

<dd>
<p>A pointer to the head of the lookaside list from which the entry will be allocated. The caller
     already initialized the list head with the 
     <a href="..\ndis\nf-ndis-ndisinitializenpagedlookasidelist.md">
     NdisInitializeNPagedLookasideList</a> function.</p>
</dd>
</dl>

## -returns
<p><b>NdisAllocateFromNPagedLookasideList</b> returns a pointer to an entry if one can be removed from the
     lookaside list or allocated; otherwise, it returns <b>NULL</b>.</p>

## -remarks
<p>If the lookaside list is not empty, 
    <b>NdisAllocateFromNPagedLookasideList</b> removes the first entry from the list and returns its address
    to the caller. If the lookaside list is empty, 
    <b>NdisAllocateFromNPagedLookasideList</b> either calls the 
    <i>Allocate</i> function, specified in the 
    <i>Allocate</i> parameter of the 
    <a href="..\ndis\nf-ndis-ndisinitializenpagedlookasidelist.md">
    NdisInitializeNPagedLookasideList</a> function, that the caller specified at list initialization, if
    any, or it allocates an entry on behalf of the caller. 
    <b>NdisAllocateFromNPagedLookasideList</b> returns <b>NULL</b> if the caller-supplied 
    <i>Allocate</i> function, if any, or if this function itself cannot allocate an nonpaged entry.</p>

<p>All entries that are allocated from a nonpaged lookaside list are of a fixed size, that was specified
    when the driver originally called 
    <b>NdisInitializeNPagedLookasideList</b>. Consequently, a lookaside list is particularly useful to
    drivers that must allocate fixed-size blocks in which to maintain state in response to dynamic I/O
    demand. For example, any connection-oriented NDIS driver might allocate the VC context areas that it
    needs from a lookaside list as VCs are created and release each such entry back to the lookaside list
    with the 
    <a href="..\ndis\nf-ndis-ndisfreetonpagedlookasidelist.md">
    NdisFreeToNPagedLookasideList</a> function as each VC is torn down.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/598e4893-ab4e-4ae2-9a92-ce3c5cce651e">
   NdisAllocateFromNPagedLookasideList (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers
   (see 
   <b>
   NdisAllocateFromNPagedLookasideList (NDIS 5.1)</b>) in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.ndis_irql_miscellaneous_function">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nf-ndis-ndisdeletenpagedlookasidelist.md">
   NdisDeleteNPagedLookasideList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfreetonpagedlookasidelist.md">
   NdisFreeToNPagedLookasideList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinitializenpagedlookasidelist.md">
   NdisInitializeNPagedLookasideList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAllocateFromNPagedLookasideList function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
