---
UID: NC.ndkpi.NDK_FN_ACCEPT
title: NDK_FN_ACCEPT
author: windows-driver-content
description: The NdkAccept (NDK_FN_ACCEPT) function accepts an incoming connection request over a listener object.
old-location: netvista\ndk_fn_accept.htm
old-project: netvista
ms.assetid: 1010F6AD-2D2F-46E5-816E-C5CE68ED11CF
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_WWAN_VISIBLE_PROVIDERS, NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdkAccept
req.alt-loc: ndkpi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# NDK_FN_ACCEPT callback



## -description
<p>The <i>NdkAccept</i> (<i>NDK_FN_ACCEPT</i>) function accepts  an incoming connection request over a listener object.</p>


## -prototype

````
NDK_FN_ACCEPT NdkAccept;

NTSTATUS NdkAccept(
  _In_     NDK_CONNECTOR                                       *pNdkConnector,
  _In_     NDK_QP                                              *pNdkQp,
  _In_     ULONG                                               InboundReadLimit,
  _In_     ULONG                                               OutboundReadLimit,
           _In_reads_bytes_opt_(PrivateDataLength) CONST PVOID pPrivateData,
  _In_     ULONG                                               PrivateDataLength,
  _In_opt_ NDK_FN_DISCONNECT_EVENT_CALLBACK                    DisconnectEvent,
  _In_opt_ PVOID                                               DisconnectEventContext,
  _In_     NDK_FN_REQUEST_COMPLETION                           RequestCompletion,
  _In_opt_ PVOID                                               RequestContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkConnector</i> [in]

<dd>
<p>A pointer to an NDK connector object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439852">NDK_CONNECTOR</a>).</p>
</dd>

### -param <i>pNdkQp</i> [in]

<dd>
<p>A pointer to an NDK queue pair (QP) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439933">NDK_QP</a>) to associate with the connection.</p>
</dd>

### -param <i>InboundReadLimit</i> [in]

<dd>
<p>The consumer-supplied maximum number of incoming in-progress read operations to allow on the QP. If the underlying provider has a lower <b>MaxInboundReadLimit</b> value in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439851">NDK_ADAPTER_INFO</a> structure, then the provider will cap the consumer-supplied value to the provider maximum. If the peer has a lower <i>OutboundReadLimit</i> value, then the provider will use that value as the effective <i>InboundReadLimit</i>. The consumer can retrieve the effective <i>InboundReadLimit</i> by calling the <i>NdkGetConnectionData</i> function (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439890">NDK_FN_GET_CONNECTION_DATA</a>).</p>
</dd>

### -param <i>OutboundReadLimit</i> [in]

<dd>
<p>The consumer-supplied maximum number of outgoing in-progress read operations to allow on the QP. If the underlying provider has a lower <b>MaxOutboundReadLimit</b> value  in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439851">NDK_ADAPTER_INFO</a> structure, then the provider will cap the consumer supplied value to the provider maximum. If the peer has a lower <i>InboundReadLimit</i>, then the provider will use that value as the effective <i>OutboundReadLimit</i>. The     consumer can retrieve the effective <i>OutboundReadLimit</i> by calling the <i>NdkGetConnectionData</i> function (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439890">NDK_FN_GET_CONNECTION_DATA</a>).</p>
</dd>

### -param <i>pPrivateData</i> 

<dd>
<p>A pointer to private data that is sent back with the accept request.</p>
</dd>

### -param <i>PrivateDataLength</i> [in]

<dd>
<p>The length, in bytes, of the private data that is provided in the <i>pPrivateData</i> parameter.</p>
</dd>

### -param <i>DisconnectEvent</i> [in, optional]

<dd>
<p>An entry point for an optional disconnect notification callback function <i>NdkDisconnectEventCallback</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439886">NDK_FN_DISCONNECT_EVENT_CALLBACK</a>). The provider calls this callback function when the peer disconnects.</p>
</dd>

### -param <i>DisconnectEventContext</i> [in, optional]

<dd>
<p>A context value to pass to the <i>DisconnectEventContext</i> parameter of the  callback function that is specified in the <i>DisconnectEvent</i> parameter.</p>
</dd>

### -param <i>RequestCompletion</i> [in]

<dd>
<p>A pointer to a request completion callback routine <i>NdkRequestCompletion</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439912">NDK_FN_REQUEST_COMPLETION</a>).</p>
</dd>

### -param <i>RequestContext</i> [in, optional]

<dd>
<p>A context value to pass to the <i>Context</i> parameter of the  callback function that is specified in the <i>RequestCompletion</i> parameter.</p>
</dd>
</dl>

## -returns
<p>The 
     <i>NDK_FN_ACCEPT</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p> The operation is pending and will be completed later. The driver will call the specified <i>RequestCompletion</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439912">NDK_FN_REQUEST_COMPLETION</a>) function to complete the pending operation.
 </p><dl>
<dt><b>STATUS_CONNECTION_ABORTED</b></dt>
</dl><p>The connecting peer abandoned the pending connection establishment.</p><dl>
<dt><b>STATUS_IO_TIMEOUT</b></dt>
</dl><p>The peer did not call the CompleteConnect (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439864">NDK_FN_COMPLETE_CONNECT</a>) function to complete the pending connection request. </p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p>The  NDK consumer calls <i>NdkAccept</i> to accept  an incoming connection request over a listener object.</p>

<p>The <i>NdkCreateListener</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439874">NDK_FN_CREATE_LISTENER</a>) function creates an NDK listener object and provides an <i>NdkConnectEventCallback</i> function (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439867">NDK_FN_CONNECT_EVENT_CALLBACK</a>).

</p>

<p>The <i>NdkConnectEventCallback</i> function is used by the NDK provider to notify the consumer about each incoming connection request.
</p>

<p>The  NDK consumer calls <i>NdkAccept</i> to accept  an incoming connection request over a listener object.</p>

<p>The <i>NdkCreateListener</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439874">NDK_FN_CREATE_LISTENER</a>) function creates an NDK listener object and provides an <i>NdkConnectEventCallback</i> function (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439867">NDK_FN_CONNECT_EVENT_CALLBACK</a>).

</p>

<p>The <i>NdkConnectEventCallback</i> function is used by the NDK provider to notify the consumer about each incoming connection request.
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
<dt>Ndkpi.h (include Ndkpi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439851">NDK_ADAPTER_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439852">NDK_CONNECTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439853">NDK_CONNECTOR_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439864">NDK_FN_COMPLETE_CONNECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439867">NDK_FN_CONNECT_EVENT_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439874">NDK_FN_CREATE_LISTENER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439886">NDK_FN_DISCONNECT_EVENT_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439890">NDK_FN_GET_CONNECTION_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439909">NDK_FN_REJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439912">NDK_FN_REQUEST_COMPLETION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439933">NDK_QP</a>
</dt>
<dt>
<a href="NULL">NDKPI Object Lifetime Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_ACCEPT callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
