---
UID: NC.ndkpi.NDK_FN_BUILD_LAM
title: NDK_FN_BUILD_LAM
author: windows-driver-content
description: The NdkBuildLam (NDK_FN_BUILD_LAM) function gets an adapter logical address mapping (LAM) from the NDK provider for a virtually contiguous memory region.
old-location: netvista\ndk_fn_build_lam.htm
ms.assetid: 89183961-0A96-4ED0-8316-E6A2C99C929F
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdkBuildLam
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
ms.keywords: NDIS_WWAN_VISIBLE_PROVIDERS, NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
req.iface: 
---

# NDK_FN_BUILD_LAM callback



## -description
<p>The <i>NdkBuildLam</i> (<i>NDK_FN_BUILD_LAM</i>) function gets an adapter logical address mapping (LAM) from the NDK provider for a virtually contiguous memory region.</p>


## -prototype

````
NDK_FN_BUILD_LAM NdkBuildLam;

NTSTATUS NdkBuildLam(
  _In_     NDK_ADAPTER                                                                 *pNdkAdapter,
  _In_     MDL                                                                         *Mdl,
  _In_     SIZE_T                                                                      Length,
  _In_     NDK_FN_REQUEST_COMPLETION                                                   RequestCompletion,
  _In_opt_ PVOID                                                                       RequestContext,
           _Out_writes_bytes_to_opt_(*pLAMSize, *pLAMSize) NDK_LOGICAL_ADDRESS_MAPPING *pNdkLAM,
           _Inout_ ULONG                                                               *pLAMSize,
  _Out_    ULONG                                                                       *pFBO
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkAdapter</i> [in]

<dd>
<p>A pointer to an NDK adapter object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a>).
</p>
</dd>

### -param <i>Mdl</i> [in]

<dd>
<p> A memory descriptor list (MDL) or chain of MDLs. The portion of the MDL chain from the starting virtual address up to the number of bytes in the  <i>Length</i> parameter must represent a virtually contiguous memory region.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The number of bytes to map starting from the first MDL's virtual address.  The MDL virtual address can be obtained with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554539">MmGetMdlVirtualAddress</a> macro. <i>Length</i> must not exceed the total number of bytes represented by the MDL chain.</p>
</dd>

### -param <i>RequestCompletion</i> [in]

<dd>
<p>A pointer to a <i>NdkRequestCompletion</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439912">NDK_FN_REQUEST_COMPLETION</a>) callback function.</p>
</dd>

### -param <i>RequestContext</i> [in, optional]

<dd>
<p>A context value for the provider to pass back to the <i>NdkRequestCompletion</i> callback function that is specified in the <i>RequestCompletion</i> parameter.</p>
</dd>

### -param <i>pNdkLAM</i> 

<dd>
<p>A pointer to a buffer that will hold an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439920">NDK_LOGICAL_ADDRESS_MAPPING</a>  structure that contains an adapter page array. The  adapter page array is stored  in the <b>AdapterPageArray</b> member and the <b>AdapterPageCount</b> member contains the number of adapter page elements.</p>
</dd>

### -param <i>pLAMSize</i> 

<dd>
<p>The size, in bytes, of the buffer at the <i>pNdkLAM</i> parameter for input, or the actual number of bytes written for output.</p>
</dd>

### -param <i>pFBO</i> [out]

<dd>
<p>The first byte offset (FBO) value is returned in this location. The FBO is the starting offset within the first adapter page.</p>
</dd>
</dl>

## -returns
<p>The 
     <i>NdkBuildLam</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The request is pending, the function specified at the <i>RequestCompletion</i>  parameter(<a href="https://msdn.microsoft.com/library/windows/hardware/hh439912">NDK_FN_REQUEST_COMPLETION</a>) will be called when the LAM build operation is complete.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The portion of the MDL chain from the starting virtual address up to the number of bytes specified in the  <i>Length</i> parameter does not represent a virtually contiguous memory region. </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The  request failed due to insufficient resources. </p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer size indicated by  the <i>*pLAMSize</i> parameter is too small to hold the LAM.  In this case, the value of <i>*pLAMSize</i> is updated with the required buffer size. </p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p>The part of the MDL chain from the starting virtual address up to the number of bytes specified in the  <i>Length</i> parameter must represent a virtually contiguous memory region. Otherwise, the NDK provider must fail the request. It is the responsibility of the NDK consumer to ensure that the MDL chain is locked. That is, the pages of the MDL change are pinned in physical memory.</p>

<p>An adapter accesses physical memory with logical addresses. This is similar to a CPU accessing physical memory with virtual addresses. If an NDK consumer will use physical memory pages directly as local data buffers in send, receive, read, or write requests,  it must get an NDK adapter logical address mapping from the NDK provider and use the logical addresses rather than physical addresses. Similarly, an NDK consumer must also use logical addresses in fast-register requests.</p>

<p>An NDK consumer can call  the <i>NdkGetPrivilegedMemoryRegionToken</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439896">NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN</a>) function to  get a privileged memory region token from an NDK provider. </p>

<p>All adapter pages returned by an NDK provider must be of <b>PAGE_SIZE</b> bytes in length, where <b>PAGE_SIZE</b> is the memory page size that is supported by the host platform as defined in wdm.h.</p>

<p>The provider must treat the virtual address value that the  <a href="https://msdn.microsoft.com/library/windows/hardware/ff554539">MmGetMdlVirtualAddress</a>   macro returns for the MDL as an index to the start of the memory region being mapped. The provider must not use the virtual address value as a valid virtual address for reading or writing buffer contents.</p>

<p>If a provider has an error while processing an <i>NdkBuildLam</i> request, the provider must release any partial mappings it built internally thus far before completing the request with failure.</p>

<p>The part of the MDL chain from the starting virtual address up to the number of bytes specified in the  <i>Length</i> parameter must represent a virtually contiguous memory region. Otherwise, the NDK provider must fail the request. It is the responsibility of the NDK consumer to ensure that the MDL chain is locked. That is, the pages of the MDL change are pinned in physical memory.</p>

<p>An adapter accesses physical memory with logical addresses. This is similar to a CPU accessing physical memory with virtual addresses. If an NDK consumer will use physical memory pages directly as local data buffers in send, receive, read, or write requests,  it must get an NDK adapter logical address mapping from the NDK provider and use the logical addresses rather than physical addresses. Similarly, an NDK consumer must also use logical addresses in fast-register requests.</p>

<p>An NDK consumer can call  the <i>NdkGetPrivilegedMemoryRegionToken</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439896">NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN</a>) function to  get a privileged memory region token from an NDK provider. </p>

<p>All adapter pages returned by an NDK provider must be of <b>PAGE_SIZE</b> bytes in length, where <b>PAGE_SIZE</b> is the memory page size that is supported by the host platform as defined in wdm.h.</p>

<p>The provider must treat the virtual address value that the  <a href="https://msdn.microsoft.com/library/windows/hardware/ff554539">MmGetMdlVirtualAddress</a>   macro returns for the MDL as an index to the start of the memory region being mapped. The provider must not use the virtual address value as a valid virtual address for reading or writing buffer contents.</p>

<p>If a provider has an error while processing an <i>NdkBuildLam</i> request, the provider must release any partial mappings it built internally thus far before completing the request with failure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439850">NDK_ADAPTER_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439896">NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439910">NDK_FN_RELEASE_LAM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439912">NDK_FN_REQUEST_COMPLETION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439920">NDK_LOGICAL_ADDRESS_MAPPING</a>
</dt>
<dt>
<a href="NULL">NDKPI Object Lifetime Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_BUILD_LAM callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
