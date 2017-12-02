---
UID: NC.ndkpi.NDK_FN_REGISTER_MR
title: NDK_FN_REGISTER_MR
author: windows-driver-content
description: The NdkRegisterMr (NDK_FN_REGISTER_MR) function registers a virtually contiguous memory region with an NDK adapter.
old-location: netvista\ndk_fn_register_mr.htm
old-project: netvista
ms.assetid: 082BBDE1-1B80-4306-96A1-DCD23910B0F7
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: NdkRegisterMr
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

# NDK_FN_REGISTER_MR callback



## -description
<p>The <i>NdkRegisterMr</i> (<i>NDK_FN_REGISTER_MR</i>) function registers a virtually contiguous memory region with an NDK adapter.</p>


## -prototype

````
NDK_FN_REGISTER_MR NdkRegisterMr;

NTSTATUS NdkRegisterMr(
  _In_     NDK_MR                    *pNdkMr,
  _In_     MDL                       *Mdl,
  _In_     SIZE_T                    Length,
  _In_     ULONG                     Flags,
  _In_     NDK_FN_REQUEST_COMPLETION RequestCompletion,
  _In_opt_ PVOID                     RequestContext
)
{ ... }
````


## -parameters
<dl>

### -param pNdkMr [in]

<dd>
<p>A pointer to an NDK memory region (MR) object
(<a href="..\ndkpi\ns-ndkpi--ndk-mr.md">NDK_MR</a>).</p>
</dd>

### -param Mdl [in]

<dd>
<p>An MDL or chain of MDLs that represent a virtually contiguous memory region from the starting virtual address up to the number of bytes specified in the <i>Length</i> parameter.
</p>
</dd>

### -param Length [in]

<dd>
<p>The number of bytes to register starting from the first MDL's virtual address. The first MDL's virtual address can be obtained by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554539">MmGetMdlVirtualAddress</a> macro. The length must not exceed the total number of bytes represented by the MDL chain.</p>
</dd>

### -param Flags [in]

<dd>
<p>A bitmask of flags that specify the access permissions for the registered memory region. The following flags can be set:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDK_MR_FLAG_ALLOW_LOCAL_READ"></a><a id="ndk_mr_flag_allow_local_read"></a><dl>

### -param NDK_MR_FLAG_ALLOW_LOCAL_READ


### -param 0x00000000

</dl>
</td>
<td width="60%"></td>
</tr>
<tr>
<td width="40%"><a id="NDK_MR_FLAG_ALLOW_LOCAL_WRITE"></a><a id="ndk_mr_flag_allow_local_write"></a><dl>

### -param NDK_MR_FLAG_ALLOW_LOCAL_WRITE


### -param 0x00000001

</dl>
</td>
<td width="60%"></td>
</tr>
<tr>
<td width="40%"><a id="NDK_MR_FLAG_ALLOW_REMOTE_READ"></a><a id="ndk_mr_flag_allow_remote_read"></a><dl>

### -param NDK_MR_FLAG_ALLOW_REMOTE_READ


### -param 0x00000002

</dl>
</td>
<td width="60%"></td>
</tr>
<tr>
<td width="40%"><a id="NDK_MR_FLAG_ALLOW_REMOTE_WRITE"></a><a id="ndk_mr_flag_allow_remote_write"></a><dl>

### -param NDK_MR_FLAG_ALLOW_REMOTE_WRITE


### -param 0x00000005

</dl>
</td>
<td width="60%"></td>
</tr>
<tr>
<td width="40%"><a id="NDK_MR_FLAG_RDMA_READ_SINK"></a><a id="ndk_mr_flag_rdma_read_sink"></a><dl>

### -param NDK_MR_FLAG_RDMA_READ_SINK


### -param 0x00000008

</dl>
</td>
<td width="60%"></td>
</tr>
</table>
<p> </p>
</dd>

### -param RequestCompletion [in]

<dd>
<p>A pointer to a request completion callback routine <i>NdkRequestCompletion</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-request-completion.md">NDK_FN_REQUEST_COMPLETION</a>).</p>
</dd>

### -param RequestContext [in, optional]

<dd>
<p>A context value to pass to the <i>Context</i> parameter of the  callback function that is specified in the <i>RequestCompletion</i> parameter.</p>
</dd>
</dl>

## -returns
<p>The 
     <i>NdkRegisterMr</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The MR registration was completed successfully.
</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p> The operation is pending and will be completed later. The driver will call the specified <i>RequestCompletion</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-request-completion.md">NDK_FN_REQUEST_COMPLETION</a>) function to complete the pending operation.
 </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The part of the MDL chain from the starting virtual address up to the length in bytes does not represent a virtually contiguous memory region. 
</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The request failed due to insufficient resources. </p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p>On an <a href="..\ndkpi\ns-ndkpi--ndk-mr.md">NDK_MR</a> object that was created with  the <i>FastRegister</i> parameter set to FALSE, <i>NdkRegisterMr</i> is used to register a virtually contiguous memory region with the adapter. </p>

<p>The NDK consumer must pass an MDL or chain of MDLs that represent virtually contiguous memory region that is pinned in physical memory. The base virtual address for the memory region being registered is the virtual address indicated by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554539">MmGetMdlVirtualAddress</a> macro. If the MDL chain does not represent a virtually contiguous memory region from the starting virtual address up to the specified length in bytes, the NDK provider must fail the request.</p>

<p>The provider must treat the virtual  address that <a href="https://msdn.microsoft.com/library/windows/hardware/ff554539">MmGetMdlVirtualAddress</a> returns as an index to the start of the memory region being registered. The provider must not use the virtual address as a valid virtual address for reading or writing buffer contents.</p>

<p>The NDK consumer must not use the MDL chain while the registration request is pending.</p>

<p><i>NdkRegisterMr</i> does not support zero-based virtual addresses.</p>

<p>An NDK consumer must pass the <b>NDK_MR_FLAG_RDMA_READ_SINK</b> flag when it registers memory that might be used as the sink buffer for an RDMA read request. Certain NDK providers might require enabling special access rights on the sink buffer for an RDMA read request on adapters for which the <b>NDK_ADAPTER_FLAG_RDMA_READ_SINK_NOT_REQUIRED</b> flag is not set in the <b>AdapterFlags</b> member of the <a href="netvista.ndk_adapter_info">NDK_ADAPTER_INFO</a> structure. The <b>NDK_MR_FLAG_RDMA_READ_SINK</b> flag allows such providers to support registration requests appropriately. </p>

<p>If an NDK consumer passes the <b>NDK_MR_FLAG_RDMA_READ_SINK</b> flag on an adapter for which the <b>NDK_ADAPTER_FLAG_RDMA_READ_SINK_NOT_REQUIRED</b> flag is set in the <b>AdapterFlags</b> member of the <a href="netvista.ndk_adapter_info">NDK_ADAPTER_INFO</a> structure, the provider is not required to handle the <b>NDK_MR_FLAG_RDMA_READ_SINK</b> flag and must not fail the request  due to the presence of this flag.</p>

<p>To deregister the memory region, use the <i>NdkDeregisterMr</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-deregister-mr.md">NDK_FN_DEREGISTER_MR</a>) function.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554539">MmGetMdlVirtualAddress</a>
</dt>
<dt>
<a href="netvista.ndk_adapter_info">NDK_ADAPTER_INFO</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-deregister-mr.md">NDK_FN_DEREGISTER_MR</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-request-completion.md">NDK_FN_REQUEST_COMPLETION</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-mr.md">NDK_MR</a>
</dt>
<dt>
<a href="netvista.ndkpi_object_lifetime_requirements">NDKPI Object Lifetime Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_REGISTER_MR callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
