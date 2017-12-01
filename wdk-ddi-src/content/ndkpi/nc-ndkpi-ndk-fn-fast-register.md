---
UID: NC.ndkpi.NDK_FN_FAST_REGISTER
title: NDK_FN_FAST_REGISTER
author: windows-driver-content
description: The NdkFastRegister (NDK_FN_FAST_REGISTER) function fast-registers an array of adapter logical pages over an existing memory region.
old-location: netvista\ndk_fn_fast_register.htm
old-project: netvista
ms.assetid: 4A37BEF6-8526-430D-AAE6-294363D0EDE7
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: NdkFastRegister
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

# NDK_FN_FAST_REGISTER callback



## -description
<p>The <i>NdkFastRegister</i> (<i>NDK_FN_FAST_REGISTER</i>) function fast-registers an array of adapter logical pages over an existing memory region.</p>


## -prototype

````
NDK_FN_FAST_REGISTER NdkFastRegister;

NTSTATUS NdkFastRegister(
  _In_     NDK_QP                                                 *pNdkQp,
  _In_opt_ PVOID                                                  RequestContext,
  _In_     NDK_MR                                                 *pMr,
  _In_     ULONG                                                  AdapterPageCount,
           _In_reads_(AdapterPageCount) CONST NDK_LOGICAL_ADDRESS *AdapterPageArray,
  _In_     ULONG                                                  FBO,
  _In_     SIZE_T                                                 Length,
  _In_     PVOID                                                  BaseVirtualAddress,
  _In_     ULONG                                                  Flags
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkQp</i> [in]

<dd>
<p>A pointer to an NDK queue pair (QP) object (<a href="..\ndkpi\ns-ndkpi--ndk-qp.md">NDK_QP</a>).</p>
</dd>

### -param <i>RequestContext</i> [in, optional]

<dd>
<p>A  context value to return in the <b>RequestContext</b> member of the <a href="..\ndkpi\ns-ndkpi--ndk-result.md">NDK_RESULT</a> structure for this request.
</p>
</dd>

### -param <i>pMr</i> [in]

<dd>
<p>A pointer to an NDK memory region (MR) object (<a href="..\ndkpi\ns-ndkpi--ndk-mr.md">NDK_MR</a>) that was initialized for fast registration.</p>
</dd>

### -param <i>AdapterPageCount</i> [in]

<dd>
<p>The number of pages in the <i>AdapterPageArray</i> parameter. The size of each page in the <i>AdapterPageArray</i> is <b>PAGE_SIZE</b> bytes.</p>
</dd>

### -param <i>AdapterPageArray</i> 

<dd>
<p>An array of adapter logical addresses (<a href="..\ndkpi\ns-ndkpi--ndk-logical-address-mapping.md">NDK_LOGICAL_ADDRESS</a>) where each address is the starting logical address for a page. Each address must be aligned  pages that are <b>PAGE_SIZE</b> bytes in length. Consecutive addresses in the array are not necessarily consecutive in terms of the logical address space, but the array as a whole represents a virtually contiguous memory region from the perspective of the host system.</p>
</dd>

### -param <i>FBO</i> [in]

<dd>
<p>The first byte offset (FBO) within the first page. The registered region starts at this offset.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The length, in bytes, of the region being registered starting at the FBO. The length must be less than or equal to the total number of bytes that are represented by the first set (<i>AdapterPageCount</i>) of pages that are contained in the <i>AdapterPageArray</i> array minus the FBO.</p>
</dd>

### -param <i>BaseVirtualAddress</i> [in]

<dd>
<p>The consumer-specified virtual address value to refer to the first byte location of the memory region. This value must be a multiple of <b>PAGE_SIZE</b> plus FBO. So, the allowed values include  FBO, or FBO plus  n times the <b>PAGE_SIZE</b> where n is greater than or equal to zero. Zero is a valid value only if FBO is zero.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A bitwise OR of flags which specifies the operations that are allowed. The following flags are supported:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDK_OP_FLAG_SILENT_SUCCESS"></a><a id="ndk_op_flag_silent_success"></a><dl>

### -param <b>NDK_OP_FLAG_SILENT_SUCCESS</b>


### -param 0x00000001

</dl>
</td>
<td width="60%">
<p>Indicates the successful completion of this request does not generate a completion event in the outbound completion queue. However, requests that fail do generate an event in the completion queue.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDK_OP_FLAG_READ_FENCE"></a><a id="ndk_op_flag_read_fence"></a><dl>

### -param <b>NDK_OP_FLAG_READ_FENCE</b>


### -param 0x00000002

</dl>
</td>
<td width="60%">
<p>Indicates that all prior read requests must be complete before the hardware begins processing this request.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDK_OP_FLAG_ALLOW_REMOTE_READ"></a><a id="ndk_op_flag_allow_remote_read"></a><dl>

### -param <b>NDK_OP_FLAG_ALLOW_REMOTE_READ</b>


### -param 0x00000008

</dl>
</td>
<td width="60%">
<p>Enable read access to the memory region for any connected peer. To access the memory region,  the connected peers must have a valid token.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDK_OP_FLAG_ALLOW_LOCAL_WRITE"></a><a id="ndk_op_flag_allow_local_write"></a><dl>

### -param <b>NDK_OP_FLAG_ALLOW_LOCAL_WRITE</b>


### -param 0x00000010

</dl>
</td>
<td width="60%">
<p>Allow local write access to the memory region.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDK_OP_FLAG_ALLOW_REMOTE_WRITE"></a><a id="ndk_op_flag_allow_remote_write"></a><dl>

### -param <b>NDK_OP_FLAG_ALLOW_REMOTE_WRITE</b>


### -param 0x00000030

</dl>
</td>
<td width="60%">
<p>Enable write access to the memory region for any connected peer. To access the memory region,  the connected peers must have a valid token.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDK_OP_FLAG_DEFER"></a><a id="ndk_op_flag_defer"></a><dl>

### -param <b>NDK_OP_FLAG_DEFER</b>


### -param 0x00000200

</dl>
</td>
<td width="60%">
<p>Indicates to the NDK provider that it may defer indicating the request to hardware for processing. For more information about this flag, see <a href="NULL">NDKPI Deferred Processing Scheme</a>.</p>
<p><b>Note</b>  This flag is supported only in NDKPI 1.2 (Windows Server 2012 R2) and later.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>The 
     <i>NDK_FN_FAST_REGISTER</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The request was posted successfully. A completion entry will be queued to the CQ when the work request is completed.</p><dl>
<dt><b>STATUS_CONNECTION_INVALID</b></dt>
</dl><p>The QP is not connected.</p><dl>
<dt><b>STATUS_ACCESS_VIOLATION</b></dt>
</dl><p>The memory region was not initialized for remote access during fast-register initialization but the fast-register work request specified <b>NDK_OP_FLAG_ALLOW_REMOTE_READ</b> or <b>NDK_OP_FLAG_ALLOW_REMOTE_WRITE</b>.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p><i>NdkFastRegister</i> fast-registers an array of adapter logical pages over an existing memory region that is  initialized for fast registration.</p>

<p>After  this call returns, the memory region token for remote access is available with the <i>NdkGetRemoteTokenFromMr</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-get-remote-token-from-mr.md">NDK_FN_GET_REMOTE_TOKEN_FROM_MR</a>)  function of the MR.</p>

<p><i>NdkFastRegister</i> does not support zero-based virtual addresses.</p>

<p>If the <b>NDK_ADAPTER_FLAG_RDMA_READ_SINK_NOT_REQUIRED</b> flag is not set in the <b>AdapterFlags</b> member of the <a href="netvista.ndk_adapter_info">NDK_ADAPTER_INFO</a> structure, an NDK consumer must pass the <b>NDK_OP_FLAG_RDMA_READ_SINK</b> flag when it registers memory that might be used as the sink buffer for an RDMA read request. Certain NDK providers might require the enabling of special access rights on the sink buffer for an RDMA read request. This flag allows such providers to support registration requests appropriately. Note that buffers might be registered for multiple purposes, therefore this flag might be accompanied by others. </p>

<p>If an NDK consumer passes the <b>NDK_OP_FLAG_RDMA_READ_SINK</b> flag on an adapter for which the <b>NDK_ADAPTER_FLAG_RDMA_READ_SINK_NOT_REQUIRED</b> flag is set in the <b>AdapterFlags</b> member of the  <a href="netvista.ndk_adapter_info">NDK_ADAPTER_INFO</a> structure, the provider is not required to handle the <b>NDK_OP_FLAG_RDMA_READ_SINK</b> flag and must not fail the request  due to the presence of this flag.</p>

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
<a href="..\ndkpi\nc-ndkpi-ndk-fn-get-remote-token-from-mr.md">NDK_FN_GET_REMOTE_TOKEN_FROM_MR</a>
</dt>
<dt>
<a href="netvista.ndk_adapter_info">NDK_ADAPTER_INFO</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-logical-address-mapping.md">NDK_LOGICAL_ADDRESS</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-mr.md">NDK_MR</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-qp.md">NDK_QP</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-result.md">NDK_RESULT</a>
</dt>
<dt>
<a href="NULL">NDKPI Deferred Processing Scheme</a>
</dt>
<dt>
<a href="NULL">NDKPI Work Request Posting Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_FAST_REGISTER callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
