---
UID: NF.ndis.NdisCopySendNetBufferListInfo
title: NdisCopySendNetBufferListInfo
author: windows-driver-content
description: Intermediate drivers call the NdisCopySendNetBufferListInfo function to copy the NET_BUFFER_LIST information in a transmit NET_BUFFER_LIST structure.
old-location: netvista\ndiscopysendnetbufferlistinfo.htm
old-project: netvista
ms.assetid: 9c8227ea-53e4-47c9-ab74-84e42b0cbbe5
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NdisCopySendNetBufferListInfo
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
req.alt-api: NdisCopySendNetBufferListInfo
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
req.iface: 
---

# NdisCopySendNetBufferListInfo function



## -description
<p>Intermediate drivers call the 
  <b>NdisCopySendNetBufferListInfo</b> function to copy the 
  <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> information in a transmit
  <b>NET_BUFFER_LIST</b> structure.</p>


## -syntax

````
VOID NdisCopySendNetBufferListInfo(
  _In_ PNET_BUFFER_LIST DestNetBufferList,
  _In_ PNET_BUFFER_LIST SrcNetBufferList
);
````


## -parameters
<dl>

### -param DestNetBufferList [in]

<dd>
<p>A pointer to the destination <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure.</p>
</dd>

### -param SrcNetBufferList [in]

<dd>
<p>A pointer to the source <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>When an intermediate driver or filter driver receives a transmit request from an overlying driver, it
    can, for example, clone the 
    <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure or allocate a new
    structure to propagate the request to underlying drivers. The driver should use 
    <b>NdisCopySendNetBufferListInfo</b> to copy the <b>NET_BUFFER_LIST</b> information, including private NDIS
    information, to the new structure.</p>

<p>To copy the <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> information on the receive path, use the 
    <a href="..\ndis\nf-ndis-ndiscopyreceivenetbufferlistinfo.md">
    NdisCopyReceiveNetBufferListInfo</a> function.</p>

<p>The following <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> items are copied in a call to <b>NdisCopySendNetBufferListInfo</b>:</p>

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
<p>Supported in NDIS 6.0 and later.</p>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="devtest.ndis_irql_netbuffer_function">Irql_NetBuffer_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="netvista.net_buffer_list_structure">NET_BUFFER_LIST Structure</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscopyreceivenetbufferlistinfo.md">
   NdisCopyReceiveNetBufferListInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisCopySendNetBufferListInfo function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
