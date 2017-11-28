---
UID: NC.ndkpi.NDK_FN_QUERY_ADAPTER_INFO
title: NDK_FN_QUERY_ADAPTER_INFO
author: windows-driver-content
description: The NdkQueryAdapterInfo (NDK_FN_QUERY_ADAPTER_INFO) function retrieves information about limits and capabilities of an NDK adapter.
old-location: netvista\ndk_fn_query_adapter_info.htm
old-project: netvista
ms.assetid: A307584E-CBF6-4CEB-8A0F-D519DA7599D3
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
req.alt-api: NdkQueryAdapterInfo
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NDK_FN_QUERY_ADAPTER_INFO callback



## -description
<p>The <i>NdkQueryAdapterInfo</i> (<i>NDK_FN_QUERY_ADAPTER_INFO</i>) function retrieves information about limits and capabilities of an  NDK adapter.</p>


## -prototype

````
NDK_FN_QUERY_ADAPTER_INFO NdkQueryAdapterInfo;

NTSTATUS NdkQueryAdapterInfo(
  _In_ NDK_ADAPTER                                                            *pNdkAdapter,
       _Out_writes_bytes_to_opt_(*pBufferSize, *pBufferSize) NDK_ADAPTER_INFO *pInfo,
       _Inout_ ULONG                                                          *pBufferSize
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkAdapter</i> [in]

<dd>
<p>A pointer to an NDK adapter (<a href="..\ndkpi\ns-ndkpi--ndk-adapter.md">NDK_ADAPTER)</a> instance.</p>
</dd>

### -param <i>pInfo</i> 

<dd>
<p>A pointer to a buffer that contains an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439851">NDK_ADAPTER_INFO</a> structure. If the request completes with STATUS_SUCCESS, the NDK provider  fills  the structure with adapter information. </p>
</dd>

### -param <i>pBufferSize</i> 

<dd>
<p>On input, this parameter is a pointer to a variable that holds the size, in bytes, of the buffer that the  <i>pInfo</i> parameter  points to. On output, the variable receives the size, in bytes,  of the adapter information that was written into the buffer.
</p>
</dd>
</dl>

## -returns
<p>The 
     <i>NdkQueryAdapterInfo</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The 	request completed successfully.
</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>
The value in the <i>*pBufferSize</i> parameter specified a buffer size that was too small to hold the adapter information. <i>*pBufferSize</i> is updated with the required size.
</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p><i>NdkQueryAdapterInfo</i> retrieves the adapter information in an  <a href="https://msdn.microsoft.com/library/windows/hardware/hh439851">NDK_ADAPTER_INFO</a> structure. The structure  contains information on various limits and capabilities of the adapter.</p>

<p><i>NdkQueryAdapterInfo</i>  requires an IRQL equal to PASSIVE_LEVEL and  it blocks until the request is completed.</p>

<p><i>NdkQueryAdapterInfo</i> retrieves the adapter information in an  <a href="https://msdn.microsoft.com/library/windows/hardware/hh439851">NDK_ADAPTER_INFO</a> structure. The structure  contains information on various limits and capabilities of the adapter.</p>

<p><i>NdkQueryAdapterInfo</i>  requires an IRQL equal to PASSIVE_LEVEL and  it blocks until the request is completed.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_QUERY_ADAPTER_INFO callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
