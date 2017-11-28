---
UID: NC.ndis.NDIS_SWITCH_GET_NET_BUFFER_LIST_SWITCH_CONTEXT
title: NDIS_SWITCH_GET_NET_BUFFER_LIST_SWITCH_CONTEXT
author: windows-driver-content
description: The Hyper-V extensible switch extension calls the GetNetBufferListSwitchContext function to retrieve the switch context previously set on the NET_BUFFER_LIST.
old-location: netvista\getnetbufferlistswitchcontext.htm
old-project: netvista
ms.assetid: 68270219-7003-489B-8362-8D6867D571FD
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: GetNetBufferListSwitchContext
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

# NDIS_SWITCH_GET_NET_BUFFER_LIST_SWITCH_CONTEXT callback



## -description
<p>The Hyper-V extensible switch extension calls the GetNetBufferListSwitchContext function to retrieve the switch context previously set on the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>. </p>


## -prototype

````
NDIS_SWITCH_GET_NET_BUFFER_LIST_SWITCH_CONTEXT GetNetBufferListSwitchContext;

PVOID GetNetBufferListSwitchContext(
  _In_ NDIS_SWITCH_CONTEXT                       NdisSwitchContext,
  _In_ PNET_BUFFER_LIST                          NetBufferList,
  _In_ PNDIS_SWITCH_NET_BUFFER_LIST_CONTEXT_TYPE ContextType
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisSwitchContext</i> [in]

<dd>
<p>An NDIS_SWITCH_CONTEXT value that contains the handle of the extensible switch module to which the Hyper-V extensible switch extension is attached. When the extension calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>, this handle is returned through the <i>NdisSwitchContext</i> parameter.</p>
</dd>

### -param <i>NetBufferList</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure for a single packet that contains the context to be retrieved.</p>
<div class="alert"><b>Note</b>  This structure must contain an extensible switch forwarding context. If the extension created or cloned the packet, it must have previously allocated this structure by calling the AllocateNetBufferListForwardingContext function.</div>
<div> </div>
</dd>

### -param <i>ContextType</i> [in]

<dd>
<p>Context</p>
<p>Context type declared using the <i>NDIS_DECLARE_SWITCH_NET_BUFFER_LIST_CONTEXT_TYPE</i> that was used when setting the context. </p>
</dd>
</dl>

## -returns
<p>NULL if no context was found in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> that matches the specified context type. Otherwise, a non-NULL pointer to the buffer is returned. </p>

## -remarks
<p>The <a href="..\ndis\nc-ndis-ndis-switch-set-net-buffer-list-switch-context.md">SetNetBufferListSwitchContext</a> APIs allow extensions to attach context to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> on ingress and retrieve it on egress. Even so, extensions should be resilient to the ingress context not being present on egress. The switch context is not preserved when an NET_BUFFER_LIST is cloned, so in scenarios where the NET_BUFFER_LIST is cloned between ingress and egress, the NET_BUFFER_LIST will not have the original's switch context.</p>

<p>The extension must manage the lifetime of the context. One approach is to allocate NDIS NET_BUFFER_LIST context (using <a href="https://msdn.microsoft.com/library/windows/hardware/ff561610">NdisAllocateNetBufferListContext</a>, or preconfigured if the extension owns the NET_BUFFER_LIST pool), and use the <a href="..\ndis\nc-ndis-ndis-switch-set-net-buffer-list-switch-context.md">SetNetBufferListSwitchContext</a> to associate a context type identifier with the NDIS NET_BUFFER_LIST context. When the NBL is completed, the extension can free the NDIS NET_BUFFER_LIST context (using <a href="https://msdn.microsoft.com/library/windows/hardware/ff562587">NdisFreeNetBufferListContext</a>, or freeing the NET_BUFFER_LIST itself if it was originated by the extension).</p>

<p>For more information about the extensible switch forwarding context, see <a href="NULL">Hyper-V Extensible Switch Forwarding Context</a>.</p>

<p>The <a href="..\ndis\nc-ndis-ndis-switch-set-net-buffer-list-switch-context.md">SetNetBufferListSwitchContext</a> APIs allow extensions to attach context to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> on ingress and retrieve it on egress. Even so, extensions should be resilient to the ingress context not being present on egress. The switch context is not preserved when an NET_BUFFER_LIST is cloned, so in scenarios where the NET_BUFFER_LIST is cloned between ingress and egress, the NET_BUFFER_LIST will not have the original's switch context.</p>

<p>The extension must manage the lifetime of the context. One approach is to allocate NDIS NET_BUFFER_LIST context (using <a href="https://msdn.microsoft.com/library/windows/hardware/ff561610">NdisAllocateNetBufferListContext</a>, or preconfigured if the extension owns the NET_BUFFER_LIST pool), and use the <a href="..\ndis\nc-ndis-ndis-switch-set-net-buffer-list-switch-context.md">SetNetBufferListSwitchContext</a> to associate a context type identifier with the NDIS NET_BUFFER_LIST context. When the NBL is completed, the extension can free the NDIS NET_BUFFER_LIST context (using <a href="https://msdn.microsoft.com/library/windows/hardware/ff562587">NdisFreeNetBufferListContext</a>, or freeing the NET_BUFFER_LIST itself if it was originated by the extension).</p>

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
<a href="..\ndis\nc-ndis-ndis-switch-set-net-buffer-list-switch-context.md">SetNetBufferListSwitchContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598224">NDIS_SWITCH_PORT_DESTINATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561830">NdisFOidRequest</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_GET_NET_BUFFER_LIST_SWITCH_CONTEXT callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
