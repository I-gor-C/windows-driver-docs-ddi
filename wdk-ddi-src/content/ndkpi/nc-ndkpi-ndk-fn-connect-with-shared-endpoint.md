---
UID: NC.ndkpi.NDK_FN_CONNECT_WITH_SHARED_ENDPOINT
title: NDK_FN_CONNECT_WITH_SHARED_ENDPOINT
author: windows-driver-content
description: The NdkConnectWithSharedEndpoint (NDK_FN_CONNECT_WITH_SHARED_ENDPOINT) function initiates an NDK connect request from a shared local address to a remote address.
old-location: netvista\ndk_fn_connect_with_shared_endpoint.htm
old-project: netvista
ms.assetid: E97C0B87-C031-4C91-8FFF-86B5E8324FB8
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
req.alt-api: NdkConnectWithSharedEndpoint
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

# NDK_FN_CONNECT_WITH_SHARED_ENDPOINT callback



## -description
<p>The <i>NdkConnectWithSharedEndpoint</i> (<i>NDK_FN_CONNECT_WITH_SHARED_ENDPOINT</i>) function initiates an NDK connect request from a shared local address to a remote address. </p>


## -prototype

````
NDK_FN_CONNECT_WITH_SHARED_ENDPOINT NdkConnectWithSharedEndpoint;

NTSTATUS NdkConnectWithSharedEndpoint(
  _In_     NDK_CONNECTOR                                        *pNdkConnector,
  _In_     NDK_QP                                               *pNdkQp,
  _In_     NDK_SHARED_ENDPOINT                                  *pNdkSharedEndpoint,
            _In_reads_bytes_(DestAddressLength) CONST PSOCKADDR pDestAddress,
  _In_     ULONG                                                DestAddressLength,
  _In_     ULONG                                                InboundReadLimit,
  _In_     ULONG                                                OutboundReadLimit,
           _In_reads_bytes_opt_(PrivateDataLength) CONST PVOID  pPrivateData,
  _In_     ULONG                                                PrivateDataLength,
  _In_     NDK_FN_REQUEST_COMPLETION                            RequestCompletion,
  _In_opt_ PVOID                                                RequestContext
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
<p>A pointer to an NDK queue pair (QP) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439933">NDK_QP</a>) to be associated with the connection.</p>
</dd>

### -param <i>pNdkSharedEndpoint</i> [in]

<dd>
<p>A pointer to an NDK shared endpoint object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439937">NDK_SHARED_ENDPOINT</a>) that determines the local address for the connection.</p>
</dd>

### -param <i>pDestAddress</i> 

<dd>
<p>A destination address.  For AF_INET or AF_INET6 <i>pDestAddress</i>  is the destination IP address and the destination ND port.</p>
</dd>

### -param <i>DestAddressLength</i> [in]

<dd>
<p>The size, in bytes,  of destination address data at the <i>pDestAddress.</i> parameter.</p>
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
<p>A pointer to private data that is sent with the connect request.</p>
</dd>

### -param <i>PrivateDataLength</i> [in]

<dd>
<p>The length, in bytes, of the private data that is provided in the <i>pPrivateData</i> parameter.</p>
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
     <i>NdkConnectWithSharedEndpoint</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The connect request was completed successfully.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p> The operation is pending and will be completed later. The driver will call the specified <i>RequestCompletion</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439912">NDK_FN_REQUEST_COMPLETION</a>) function to complete the pending operation.
 </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The  request failed due to insufficient resources. </p><dl>
<dt><b>STATUS_NETWORK_UNREACHABLE</b></dt>
</dl><p>The request failed because the remote network was not reachable. The connection attempt may be retried. </p><dl>
<dt><b>STATUS_HOST_UNREACHABLE</b></dt>
</dl><p>The request failed because the remote system was not reachable. The connection attempt may be retried. </p><dl>
<dt><b>STATUS_CONNECTION_REFUSED</b></dt>
</dl><p>The request failed because the remote system refused the connection request. This can be due to lack of listener, backlog limits, or the peer actively rejecting the connection request. The connection attempt may be retried. </p><dl>
<dt><b>STATUS_IO_TIMEOUT</b></dt>
</dl><p>The request failed because the connection request timed out. The connection attempt may be retried. Timeout values are selected by Network Direct providers to match their respective network characteristics.</p><dl>
<dt><b>STATUS_ADDRESS_ALREADY_EXISTS</b></dt>
</dl><p>The request failed because a connection with the combination of local address, local port, remote address, and remote port already exists. </p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p><i>NdkConnectWithSharedEndpoint</i> initiates a connect request from a shared local address to a specific remote address. <i>NdkConnectWithSharedEndpoint</i> allows an NDK consumer to use the same local address (for example, 10.1.1.1:9999) for many outgoing connections when the destination addresses for the connections are different.</p>

<p><i>NdkConnectWithSharedEndpoint</i> initiates a connect request from a shared local address to a specific remote address. <i>NdkConnectWithSharedEndpoint</i> allows an NDK consumer to use the same local address (for example, 10.1.1.1:9999) for many outgoing connections when the destination addresses for the connections are different.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439890">NDK_FN_GET_CONNECTION_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439912">NDK_FN_REQUEST_COMPLETION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439933">NDK_QP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439937">NDK_SHARED_ENDPOINT</a>
</dt>
<dt>
<a href="NULL">NDKPI Object Lifetime Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_CONNECT_WITH_SHARED_ENDPOINT callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
