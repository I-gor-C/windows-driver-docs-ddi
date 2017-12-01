---
UID: NC.ndis.NDIS_SWITCH_SET_NET_BUFFER_LIST_SWITCH_CONTEXT
title: NDIS_SWITCH_SET_NET_BUFFER_LIST_SWITCH_CONTEXT
author: windows-driver-content
description: The Hyper-V extensible switch extension calls the SetNetBufferListSwitchContext function to attach an extension-allocated context buffer to the NET_BUFFER_LIST.
old-location: netvista\setnetbufferlistswitchcontext.htm
old-project: netvista
ms.assetid: BFA54990-E1BB-4E86-B806-F3021FB0075B
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.iface: 
---

# NDIS_SWITCH_SET_NET_BUFFER_LIST_SWITCH_CONTEXT callback



## -description
<p>The Hyper-V extensible switch extension calls the <i>SetNetBufferListSwitchContext</i> function to attach an extension-allocated context buffer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>. The context is then accessible for the lifetime of that NET_BUFFER_LIST, including if the context is set on ingress and the NBL is seen again on egress, regardless of whether other extensions set their own context. This type of access is not possible using the existing NDIS NET_BUFFER_LIST context APIs (<a href="..\ndis\nf-ndis-ndisallocatenetbufferlistcontext.md">NdisAllocateNetBufferListContext</a>/ <a href="https://msdn.microsoft.com/library/windows/hardware/ff568391">NET_BUFFER_LIST_CONTEXT_DATA_START</a>) because another extension can allocate NDIS context when it gets ownership of the NET_BUFFER_LIST, at which point the pointer to the original NDIS context is lost. </p>


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
<dl>

### -param <i>NdisSwitchContext</i> [in]

<dd>
<p>An NDIS_SWITCH_CONTEXT value that contains the handle of the extensible switch module to which the Hyper-V extensible switch extension is attached. When the extension calls <a href="..\ndis\nf-ndis-ndisfgetoptionalswitchhandlers.md">NdisFGetOptionalSwitchHandlers</a>, this handle is returned through the <i>NdisSwitchContext</i> parameter.</p>
</dd>

### -param <i>NetBufferList</i> [in, out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure for a single packet that receives the context association.</p>
<div class="alert"><b>Note</b>  This structure must contain an extensible switch forwarding context. If the extension created or cloned the packet, it must have previously allocated this structure by calling the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function.</div>
<div> </div>
</dd>

### -param <i>ContextType</i> [in]

<dd>
<p>The context type declared using <i>NDIS_DECLARE_SWITCH_NET_BUFFER_LIST_CONTEXT_TYPE</i> that will be used as the key when retrieving the context.</p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>The pointer to the context that will be retrievable using the specified <i>ContextType</i>.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns NDIS_STATUS_SUCCESS. Otherwise, it returns an NDIS_STATUS_<i>Xxx</i> error code that is defined in Ndis.h.

</p>

## -remarks
<p>The <i>SetNetBufferListSwitchContext</i> APIs allow extensions to attach context to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> on ingress and retrieve it on egress. Even so, extensions should be resilient to the ingress context not being present on egress. The switch context is not preserved when an NET_BUFFER_LIST is cloned, so in scenarios where the NET_BUFFER_LIST is cloned between ingress and egress, the NET_BUFFER_LIST will not have the original's switch context. </p>

<p>The extension must manage the lifetime of the context. One approach is to allocate NDIS NET_BUFFER_LIST context (using <a href="..\ndis\nf-ndis-ndisallocatenetbufferlistcontext.md">NdisAllocateNetBufferListContext</a>, or preconfigured if the extension owns the NET_BUFFER_LIST pool), and use the <i>SetNetBufferListSwitchContext</i> to associate a context type identifier with the NDIS NET_BUFFER_LIST context. When the NBL is completed, the extension can free the NDIS NET_BUFFER_LIST context (using <a href="..\ndis\nf-ndis-ndisfreenetbufferlistcontext.md">NdisFreeNetBufferListContext</a>, or freeing the NET_BUFFER_LIST itself if it was originated by the extension).</p>

<p>For more information about the extensible switch forwarding context, see <a href="NULL">Hyper-V Extensible Switch Forwarding Context</a>.</p>

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
<a href="netvista.GetNetBufferListDestinations">GetNetBufferListDestinations</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-ndis-switch-get-net-buffer-list-switch-context.md">GetNetBufferListSwitchContext</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-switch-port-destination.md">NDIS_SWITCH_PORT_DESTINATION</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfgetoptionalswitchhandlers.md">NdisFGetOptionalSwitchHandlers</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfoidrequest.md">NdisFOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_SET_NET_BUFFER_LIST_SWITCH_CONTEXT callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
