---
UID: NF.ndis.NdisMPauseComplete
title: NdisMPauseComplete
author: windows-driver-content
description: A miniport driver must call the NdisMPauseComplete function to complete a pause operation if the driver returned NDIS_STATUS_PENDING from its MiniportPause function.
old-location: netvista\ndismpausecomplete.htm
old-project: netvista
ms.assetid: 08a9dccf-53bc-4b96-a794-14ead08a7b0b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisMPauseComplete
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
req.alt-api: NdisMPauseComplete
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miniport_Driver_Function
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

# NdisMPauseComplete function



## -description
<p>A miniport driver must call the 
  <b>NdisMPauseComplete</b> function to complete a pause operation if the driver returned NDIS_STATUS_PENDING
  from its 
  <a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a> function.</p>


## -syntax

````
VOID NdisMPauseComplete(
  _In_ NDIS_HANDLE MiniportAdapterHandle
);
````


## -parameters
<dl>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>The miniport adapter handle that NDIS passed to the 
     <i>MiniportAdapterHandle</i> parameter of 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>NDIS calls a miniport driver's 
    <a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a> function to initiate a
    pause request for a miniport adapter. The miniport adapter remains in the 
    <i>Pausing</i> state until the pause operation is complete.</p>

<p>After a miniport driver completes all outstanding send requests and NDIS returns all the network data
    structures in outstanding receive indications to the driver, the driver calls 
    <b>NdisMPauseComplete</b> to complete the pending pause request. After the driver calls 
    <b>NdisMPauseComplete</b>, the miniport adapter is in the 
    <i>Paused</i> state.</p>

<p>NDIS calls the 
    <a href="..\ndis\nc-ndis-miniport-restart.md">MiniportRestart</a> function to initiate a
    restart request for a miniport adapter that is paused.</p>

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
<a href="devtest.ndis_irql_miniport_driver_function">Irql_Miniport_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-restart.md">MiniportRestart</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMPauseComplete function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
