---
UID: NC.ndis.NDIS_SWITCH_FREE_NET_BUFFER_LIST_FORWARDING_CONTEXT
title: NDIS_SWITCH_FREE_NET_BUFFER_LIST_FORWARDING_CONTEXT
author: windows-driver-content
description: The FreeNetBufferListForwardingContext function releases resources in the out-of-band (OOB) extensible switch forwarding context of a NET_BUFFER_LIST structure.
old-location: netvista\FreeNetBufferListForwardingContext.htm
ms.assetid: 08AE3160-276F-4D1F-9D02-AD5AF38CDED2
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FreeNetBufferListForwardingContext
req.alt-loc: Ndis.h
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
ms.keywords: RxNameCacheInitialize
req.iface: 
---

# NDIS_SWITCH_FREE_NET_BUFFER_LIST_FORWARDING_CONTEXT callback



## -description
<p>
<p>The <i>FreeNetBufferListForwardingContext</i> function releases resources in the out-of-band (OOB) extensible switch forwarding context of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. This data was used for send or receive operations in a Hyper-V extensible switch, and was previously allocated  by calling the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function.</p>
</p>
<p>The <i>FreeNetBufferListForwardingContext</i> function releases resources in the out-of-band (OOB) extensible switch forwarding context of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. This data was used for send or receive operations in a Hyper-V extensible switch, and was previously allocated  by calling the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function.</p>


## -prototype

````
NDIS_SWITCH_FREE_NET_BUFFER_LIST_FORWARDING_CONTEXT FreeNetBufferListForwardingContext;

NDIS_STATUS FreeNetBufferListForwardingContext(
  _In_    NDIS_SWITCH_CONTEXT NdisSwitchContext,
  _Inout_ PNET_BUFFER_LIST    NetBufferList
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisSwitchContext</i> [in]

<dd>
<p>An NDIS_SWITCH_CONTEXT value that contains the handle of the extensible switch module to which the Hyper-V extensible switch extension is attached. When the extension calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>,  this handle is returned through the <i>NdisSwitchContext</i> parameter.</p>
</dd>

### -param <i>NetBufferList</i> [in, out]

<dd>
<p>A pointer to a linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures.</p>
<div class="alert"><b>Note</b>  This structure must contain an extensible switch forwarding context that was previously allocated by calling the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function.</div>
<div> </div>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns NDIS_STATUS_SUCCESS. Otherwise, it returns an NDIS_STATUS_<i>Xxx</i> error code that is defined in Ndis.h.

</p>

## -remarks
<p>The extensible switch extension can originate packet send operations within the extensible switch data path. For example, the extension can send packets to any port on the extensible switch. For more information about this data path, see <a href="NULL">Hyper-V Extensible Switch Data Path</a>.</p>

<p>If the extensible switch extension originates a packet send  operation, the extension must  call the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function. This function allocates and initializes the forwarding context  for the specified  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. For more information about this context, see <a href="NULL">Hyper-V Extensible Switch Forwarding Context</a>.</p>

<p>When the send operation is complete, the extension must call the <i>FreeNetBufferListForwardingContext</i> function to deallocate the forwarding context.</p>

<p> For more information on how to originate send operations, see <a href="NULL">Filter Module Send and Receive Operations</a>.</p>

<p>The extensible switch extension can originate packet send operations within the extensible switch data path. For example, the extension can send packets to any port on the extensible switch. For more information about this data path, see <a href="NULL">Hyper-V Extensible Switch Data Path</a>.</p>

<p>If the extensible switch extension originates a packet send  operation, the extension must  call the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function. This function allocates and initializes the forwarding context  for the specified  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. For more information about this context, see <a href="NULL">Hyper-V Extensible Switch Forwarding Context</a>.</p>

<p>When the send operation is complete, the extension must call the <i>FreeNetBufferListForwardingContext</i> function to deallocate the forwarding context.</p>

<p> For more information on how to originate send operations, see <a href="NULL">Filter Module Send and Receive Operations</a>.</p>

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
<p>Supported in NDIS 6.30 and later.</p>
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
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562583">NdisFreeNetBufferList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_FREE_NET_BUFFER_LIST_FORWARDING_CONTEXT callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
