---
UID: NC.ndisndk.OPEN_NDK_ADAPTER_HANDLER
title: OPEN_NDK_ADAPTER_HANDLER
author: windows-driver-content
description: The OpenNDKAdapterHandler (OPEN_NDK_ADAPTER_HANDLER) function opens an NDK adapter instance on an NDK-capable NDIS miniport adapter.
old-location: netvista\open_ndk_adapter_handler.htm
ms.assetid: 85888B9A-669C-478F-9318-EE9821BC3AF3
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndisndk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OpenNdkAdapterHandler
req.alt-loc: ndisndk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: TCP_OFFLOAD_STATS, TCP_OFFLOAD_STATS, *PTCP_OFFLOAD_STATS
req.iface: 
---

# OPEN_NDK_ADAPTER_HANDLER callback



## -description
<p>The <i>OpenNDKAdapterHandler</i> (<i>OPEN_NDK_ADAPTER_HANDLER</i>) function opens an NDK adapter instance on an NDK-capable NDIS miniport adapter.</p>


## -prototype

````
OPEN_NDK_ADAPTER_HANDLER OpenNdkAdapterHandler;

NDIS_STATUS OpenNdkAdapterHandler(
  _In_ NDIS_HANDLE                       MiniportAdapterContext,
  _In_ PNDIS_OPEN_NDK_ADAPTER_PARAMETERS Parameters,
       _Outptr_ NDK_ADAPTER              **ppNdkAdapter
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportAdapterContext</i> [in]

<dd>
<p>A handle to a context area that the miniport driver allocated in its <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function. The miniport driver uses this context area to maintain state information for an NDIS miniport adapter.

</p>
</dd>

### -param <i>Parameters</i> [in]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/hh451599">NDIS_OPEN_NDK_ADAPTER_PARAMETERS</a> structure that defines the input parameters to open an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a> instance.</p>
<p>The  <a href="https://msdn.microsoft.com/library/windows/hardware/hh451599">NDIS_OPEN_NDK_ADAPTER_PARAMETERS</a> structure must specify the  NDKPI major version, and the lowest NDKPI minor version that the NDK consumer can support. 
</p>
<p>If the provider does not support the consumer-specified major version, the provider must fail the request with  NDIS_STATUS_BAD_VERSION. </p>
<p>If the provider supports the consumer-specified major version and the specified minor version is less than or equal to the highest minor version that the provider supports, the provider must succeed the request and use the highest minor version that     the provider supports.</p>
<p> For example, if the consumer requests version 1.0, and the provider supports 1.1, the provider must report version  1.1  in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439851">NDK_ADAPTER_INFO</a> structure and  NDK object headers. </p>
<div class="alert"><b>Note</b>  Higher minor versions at the provider are always fully backward-compatible with (that is, a superset of) lower minor versions. </div>
<div> </div>
<p>If the provider supports the consumer-specified major version and the specified minor version is greater than the highest minor version that the provider supports, the provider must fail the request with NDIS_STATUS_BAD_VERSION.</p>
</dd>

### -param <i>ppNdkAdapter</i> 

<dd>
<p>A pointer to a variable that holds the pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a> structure. On return from  <i>OPEN_NDK_ADAPTER_HANDLER</i>, the <b>NDK_ADAPTER</b> structure referenced by  <i>ppNdkAdapter</i> identifies the newly opened NDK adapter instance. </p>
</dd>
</dl>

## -returns
<p><i>OPEN_NDK_ADAPTER_HANDLER</i> can return one of the following values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The NDK adapter instance was successfully opened.</p><dl>
<dt><b>NDIS_STATUS_BAD_VERSION</b></dt>
</dl><p>The requested version number is not supported.</p><dl>
<dt><b>NDIS_STATUS_ADAPTER_NOT_READY</b></dt>
</dl><p>The NDK functionality of the miniport adapter is not enabled.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>NDIS was unable to open the NDK adapter due to insufficient resources.</p>

<p> </p>

## -remarks
<p><i>OPEN_NDK_ADAPTER_HANDLER</i> opens an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a> instance on an NDK-capable NDIS miniport adapter.
Multiple <b>NDK_ADAPTER</b> instances can be created on the same NDIS miniport adapter. Each <b>NDK_ADAPTER</b> instance contains a pointer to a table of dispatch  functions that implement the NDK application programming interface.
The miniport driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439355">CLOSE_NDK_ADAPTER_HANDLER</a> function to close the  NDK adapter instance and release the associated resources.</p>

<p><i>OPEN_NDK_ADAPTER_HANDLER</i> opens an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a> instance on an NDK-capable NDIS miniport adapter.
Multiple <b>NDK_ADAPTER</b> instances can be created on the same NDIS miniport adapter. Each <b>NDK_ADAPTER</b> instance contains a pointer to a table of dispatch  functions that implement the NDK application programming interface.
The miniport driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439355">CLOSE_NDK_ADAPTER_HANDLER</a> function to close the  NDK adapter instance and release the associated resources.</p>

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
<dt>Ndisndk.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439355">CLOSE_NDK_ADAPTER_HANDLER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451599">NDIS_OPEN_NDK_ADAPTER_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439850">NDK_ADAPTER_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439851">NDK_ADAPTER_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20OPEN_NDK_ADAPTER_HANDLER callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
