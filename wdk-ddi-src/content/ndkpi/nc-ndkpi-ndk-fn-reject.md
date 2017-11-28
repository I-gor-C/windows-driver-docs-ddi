---
UID: NC.ndkpi.NDK_FN_REJECT
title: NDK_FN_REJECT
author: windows-driver-content
description: The NdkReject (NDK_FN_REJECT) function rejects an incoming NDK connection request.
old-location: netvista\ndk_fn_reject.htm
old-project: netvista
ms.assetid: BBD02954-C907-4EA4-8605-EC90CC62ECB7
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
req.alt-api: NdkReject
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

# NDK_FN_REJECT callback



## -description
<p>The <i>NdkReject</i> (<i>NDK_FN_REJECT</i>) function rejects an incoming NDK connection request.</p>


## -prototype

````
NDK_FN_REJECT NdkReject;

NTSTATUS NdkReject(
  _In_ NDK_CONNECTOR                                       *pNdkConnector,
       _In_reads_bytes_opt_(PrivateDataLength) CONST PVOID pPrivateData,
  _In_ ULONG                                               PrivateDataLength
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkConnector</i> [in]

<dd>
<p>A pointer to an NDK connector object
(<a href="https://msdn.microsoft.com/library/windows/hardware/hh439852">NDK_CONNECTOR</a>).</p>
</dd>

### -param <i>pPrivateData</i> 

<dd>
<p>A pointer to private data that is sent back with the reject request.

</p>
</dd>

### -param <i>PrivateDataLength</i> [in]

<dd>
<p>The length, in bytes, of the private data that is provided in the <i>pPrivateData</i> parameter.

</p>
</dd>
</dl>

## -returns
<p>The 
     <i>NdkReject</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The reject request was successful.
</p><dl>
<dt><b>STATUS_CONNECTION_ABORTED</b></dt>
</dl><p>The connecting peer abandoned the connection establishment.

</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p><i>NdkReject</i> rejects an incoming connection request over a listener. A connection request can also be rejected for a connection request where the  <i>NdkConnect</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439865">NDK_FN_CONNECT</a>) function  has been completed and the consumer rejects the connection. For example, the consumer rejects the connection because of the  values in the  <i>pInboundReadLimit</i>, <i>pOutboundReadLimit</i>, or <i>pPrivateData</i> parameters available with the <i>NdkGetConnectionData</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439890">NDK_FN_GET_CONNECTION_DATA</a>) function.</p>

<p><i>NdkReject</i> rejects an incoming connection request over a listener. A connection request can also be rejected for a connection request where the  <i>NdkConnect</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439865">NDK_FN_CONNECT</a>) function  has been completed and the consumer rejects the connection. For example, the consumer rejects the connection because of the  values in the  <i>pInboundReadLimit</i>, <i>pOutboundReadLimit</i>, or <i>pPrivateData</i> parameters available with the <i>NdkGetConnectionData</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439890">NDK_FN_GET_CONNECTION_DATA</a>) function.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439852">NDK_CONNECTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439853">NDK_CONNECTOR_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439857">NDK_FN_ACCEPT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439865">NDK_FN_CONNECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439890">NDK_FN_GET_CONNECTION_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_REJECT callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
