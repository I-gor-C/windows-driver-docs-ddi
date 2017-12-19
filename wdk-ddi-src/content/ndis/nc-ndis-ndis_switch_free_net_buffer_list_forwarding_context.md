---
UID: NC.ndis.NDIS_SWITCH_FREE_NET_BUFFER_LIST_FORWARDING_CONTEXT
title: NDIS_SWITCH_FREE_NET_BUFFER_LIST_FORWARDING_CONTEXT
author: windows-driver-content
description: The FreeNetBufferListForwardingContext function releases resources in the out-of-band (OOB) extensible switch forwarding context of a NET_BUFFER_LIST structure.
old-location: netvista\FreeNetBufferListForwardingContext.htm
old-project: NetVista
ms.assetid: 08AE3160-276F-4D1F-9D02-AD5AF38CDED2
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
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
---

# NDIS_SWITCH_FREE_NET_BUFFER_LIST_FORWARDING_CONTEXT callback



## -description

The <i>FreeNetBufferListForwardingContext</i> function releases resources in the out-of-band (OOB) extensible switch forwarding context of a <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure. This data was used for send or receive operations in a Hyper-V extensible switch, and was previously allocated  by calling the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function.



The <i>FreeNetBufferListForwardingContext</i> function releases resources in the out-of-band (OOB) extensible switch forwarding context of a <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure. This data was used for send or receive operations in a Hyper-V extensible switch, and was previously allocated  by calling the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function.



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

### -param NdisSwitchContext [in]

An NDIS_SWITCH_CONTEXT value that contains the handle of the extensible switch module to which the Hyper-V extensible switch extension is attached. When the extension calls <a href="netvista.ndisfgetoptionalswitchhandlers">NdisFGetOptionalSwitchHandlers</a>,  this handle is returned through the <i>NdisSwitchContext</i> parameter.


### -param NetBufferList [in, out]

A pointer to a linked list of <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures.

<div class="alert"><b>Note</b>  This structure must contain an extensible switch forwarding context that was previously allocated by calling the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function.</div>
<div> </div>

## -returns
If the call succeeds, the function returns NDIS_STATUS_SUCCESS. Otherwise, it returns an NDIS_STATUS_<i>Xxx</i> error code that is defined in Ndis.h.




## -remarks
The extensible switch extension can originate packet send operations within the extensible switch data path. For example, the extension can send packets to any port on the extensible switch. For more information about this data path, see <a href="netvista.hyper_v_extensible_switch_data_path">Hyper-V Extensible Switch Data Path</a>.

If the extensible switch extension originates a packet send  operation, the extension must  call the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function. This function allocates and initializes the forwarding context  for the specified  <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure. For more information about this context, see <a href="netvista.hyper_v_extensible_switch_forwarding_context">Hyper-V Extensible Switch Forwarding Context</a>.

When the send operation is complete, the extension must call the <i>FreeNetBufferListForwardingContext</i> function to deallocate the forwarding context.

 For more information on how to originate send operations, see <a href="netvista.filter_module_send_and_receive_operations">Filter Module Send and Receive Operations</a>.


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
Supported in NDIS 6.30 and later.

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
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a>
</dt>
<dt>
<a href="netvista.ndisfreenetbufferlist">NdisFreeNetBufferList</a>
</dt>
<dt>
<a href="netvista.ndisfgetoptionalswitchhandlers">NdisFGetOptionalSwitchHandlers</a>
</dt>
<dt>
<a href="netvista.net_buffer_list">NET_BUFFER_LIST</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NDIS_SWITCH_FREE_NET_BUFFER_LIST_FORWARDING_CONTEXT callback function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

