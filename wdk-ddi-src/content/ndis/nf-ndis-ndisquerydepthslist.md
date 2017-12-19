---
UID: NF.ndis.NdisQueryDepthSList
title: NdisQueryDepthSList macro
author: windows-driver-content
description: The NdisQueryDepthSList function returns the current number of entries in a given sequenced, singly linked list.
old-location: netvista\ndisquerydepthslist.htm
old-project: NetVista
ms.assetid: 76b076d1-640b-4378-bf6d-36d87a8a5042
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NdisQueryDepthSList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisQueryDepthSList (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisQueryDepthSList (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisQueryDepthSList
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
---

# NdisQueryDepthSList macro



## -description
The 
  <b>NdisQueryDepthSList</b> function returns the current number of entries in a given sequenced, singly
  linked list.



## -syntax

````
USHORT NdisQueryDepthSList(
  [in] PSLIST_HEADER SListHead
);
````


## -parameters

### -param SListHead [in]

A pointer to the head of the S-List to be queried, which the caller already initialized with 
     <a href="netvista.ndisinitializeslisthead">NdisInitializeSListHead</a>.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/87b647b4-bb14-44f1-b0b0-48bc21630ce8">NdisQueryDepthSList (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisQueryDepthSList (NDIS
   5.1)</b>) in Windows XP.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
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
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.ndis_irql_miscellaneous_function">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndisinitializeslisthead">NdisInitializeSListHead</a>
</dt>
<dt>
<a href="netvista.ndisinterlockedpushentryslist">
   NdisInterlockedPushEntrySList</a>
</dt>
<dt>
<a href="netvista.ndisinterlockedpopentryslist">NdisInterlockedPopEntrySList</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NdisQueryDepthSList macro%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

