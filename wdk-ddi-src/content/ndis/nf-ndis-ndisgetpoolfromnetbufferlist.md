---
UID: NF.ndis.NdisGetPoolFromNetBufferList
title: NdisGetPoolFromNetBufferList function
author: windows-driver-content
description: Call the NdisGetPoolFromNetBufferList function to get the NET_BUFFER_LIST structure pool handle that is associated with a specified NET_BUFFER_LIST structure.
old-location: netvista\ndisgetpoolfromnetbufferlist.htm
old-project: netvista
ms.assetid: 645fd5f6-32b5-4ef6-9583-1418291d55d3
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisGetPoolFromNetBufferList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisGetPoolFromNetBufferList
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_NetBuffer_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
---

# NdisGetPoolFromNetBufferList function



## -description
Call the 
  <b>NdisGetPoolFromNetBufferList</b> function to get the 
  <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure pool handle that is
  associated with a specified NET_BUFFER_LIST structure.



## -syntax

````
NDIS_HANDLE NdisGetPoolFromNetBufferList(
  _In_ PNET_BUFFER_LIST NetBufferList
);
````


## -parameters

### -param NetBufferList [in]

A pointer to a previously allocated 
     <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure.


## -returns
<b>NdisGetPoolFromNetBufferList</b> returns a handle to the NET_BUFFER_LIST structure pool that is
     associated with the specified NET_BUFFER_LIST structure.


## -remarks
The handle that 
    <b>NdisGetPoolFromNetBufferList</b> returns is a required parameter in calls to NDIS functions that
    manipulate the 
    <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures that are from the
    associated NET_BUFFER_LIST structure pool.


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
Supported in NDIS 6.0 and later.

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
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="devtest.ndis_irql_netbuffer_function">Irql_NetBuffer_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.net_buffer_list">NET_BUFFER_LIST</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisGetPoolFromNetBufferList function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

