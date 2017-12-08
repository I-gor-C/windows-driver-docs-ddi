---
UID: NC.ndis.NDIS_SWITCH_SET_NET_BUFFER_LIST_SWITCH_CONTEXT
title: NDIS_SWITCH_SET_NET_BUFFER_LIST_SWITCH_CONTEXT
author: windows-driver-content
description: The Hyper-V extensible switch extension calls the SetNetBufferListSwitchContext function to attach an extension-allocated context buffer to the NET_BUFFER_LIST.
old-location: netvista\setnetbufferlistswitchcontext.htm
old-project: netvista
ms.assetid: BFA54990-E1BB-4E86-B806-F3021FB0075B
ms.author: windowsdriverdev
ms.date: 12/6/2017
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
req.alt-api: SetNetBufferListSwitchContext
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

# NDIS_SWITCH_SET_NET_BUFFER_LIST_SWITCH_CONTEXT callback



## -description
The Hyper-V extensible switch extension calls the <i>SetNetBufferListSwitchContext</i> function to attach an extension-allocated context buffer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>. The context is then accessible for the lifetime of that NET_BUFFER_LIST, including if the context is set on ingress and the NBL is seen again on egress, regardless of whether other extensions set their own context. This type of access is not possible using the existing NDIS NET_BUFFER_LIST context APIs (<a href="netvista.ndisallocatenetbufferlistcontext">NdisAllocateNetBufferListContext</a>/ <a href="https://msdn.microsoft.com/library/windows/hardware/ff568391">NET_BUFFER_LIST_CONTEXT_DATA_START</a>) because another extension can allocate NDIS context when it gets ownership of the NET_BUFFER_LIST, at which point the pointer to the original NDIS context is lost. 


## -prototype

````
NDIS_SWITCH_SET_NET_BUFFER_LIST_SWITCH_CONTEXT SetNetBufferListSwitchContext;

NDIS_STATUS SetNetBufferListSwitchContext(
  _In_    NDIS_SWITCH_CONTEXT                       NdisSwitchContext,
  _Inout_ PNET_BUFFER_LIST                          NetBufferList,
  _In_    PNDIS_SWITCH_NET_BUFFER_LIST_CONTEXT_TYPE ContextType,
  _In_    PVOID                                     Context
)
{ ... }
````


## -parameters

### -param NdisSwitchContext [in]

An NDIS_SWITCH_CONTEXT value that contains the handle of the extensible switch module to which the Hyper-V extensible switch extension is attached. When the extension calls <a href="netvista.ndisfgetoptionalswitchhandlers">NdisFGetOptionalSwitchHandlers</a>, this handle is returned through the <i>NdisSwitchContext</i> parameter.

### -param NetBufferList [in, out]

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure for a single packet that receives the context association.
<div class="alert"><b>Note</b>  This structure must contain an extensible switch forwarding context. If the extension created or cloned the packet, it must have previously allocated this structure by calling the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function.</div>
<div> </div>

### -param ContextType [in]

The context type declared using <i>NDIS_DECLARE_SWITCH_NET_BUFFER_LIST_CONTEXT_TYPE</i> that will be used as the key when retrieving the context.

### -param Context [in]

The pointer to the context that will be retrievable using the specified <i>ContextType</i>.

## -returns
If the call succeeds, the function returns NDIS_STATUS_SUCCESS. Otherwise, it returns an NDIS_STATUS_<i>Xxx</i> error code that is defined in Ndis.h.



## -remarks
The <i>SetNetBufferListSwitchContext</i> APIs allow extensions to attach context to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> on ingress and retrieve it on egress. Even so, extensions should be resilient to the ingress context not being present on egress. The switch context is not preserved when an NET_BUFFER_LIST is cloned, so in scenarios where the NET_BUFFER_LIST is cloned between ingress and egress, the NET_BUFFER_LIST will not have the original's switch context. 

The extension must manage the lifetime of the context. One approach is to allocate NDIS NET_BUFFER_LIST context (using <a href="netvista.ndisallocatenetbufferlistcontext">NdisAllocateNetBufferListContext</a>, or preconfigured if the extension owns the NET_BUFFER_LIST pool), and use the <i>SetNetBufferListSwitchContext</i> to associate a context type identifier with the NDIS NET_BUFFER_LIST context. When the NBL is completed, the extension can free the NDIS NET_BUFFER_LIST context (using <a href="netvista.ndisfreenetbufferlistcontext">NdisFreeNetBufferListContext</a>, or freeing the NET_BUFFER_LIST itself if it was originated by the extension).

For more information about the extensible switch forwarding context, see <a href="netvista.hyper_v_extensible_switch_forwarding_context">Hyper-V Extensible Switch Forwarding Context</a>.

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
<a href="netvista.GetNetBufferListDestinations">GetNetBufferListDestinations</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-ndis_switch_get_net_buffer_list_switch_context.md">GetNetBufferListSwitchContext</a>
</dt>
<dt>
<a href="netvista.ndis_switch_port_destination">NDIS_SWITCH_PORT_DESTINATION</a>
</dt>
<dt>
<a href="netvista.ndisfgetoptionalswitchhandlers">NdisFGetOptionalSwitchHandlers</a>
</dt>
<dt>
<a href="netvista.ndisfoidrequest">NdisFOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_SET_NET_BUFFER_LIST_SWITCH_CONTEXT callback function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
