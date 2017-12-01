---
UID: NS.ndkpi._NDK_SGE
title: NDK_SGE
author: windows-driver-content
description: The NDK_SGE structure specifies the local buffers for NDK work requests.
old-location: netvista\ndk_sge.htm
old-project: netvista
ms.assetid: D64DD5F0-2BCA-4A6B-A7BA-04A2B8E3B9FE
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDK_SGE, NDK_SGE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDK_SGE
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

# NDK_SGE structure



## -description
<p>The  <b>NDK_SGE</b> structure specifies the local buffers for NDK work requests.</p>


## -syntax

````
typedef struct _NDK_SGE {
  union {
    PVOID               VirtualAddress;
    NDK_LOGICAL_ADDRESS LogicalAddress;
  };
  ULONG  Length;
  UINT32 MemoryRegionToken;
} NDK_SGE;
````


## -struct-fields
<dl>

### -field <b>VirtualAddress</b>

<dd>
<p>A virtual address.</p>
</dd>

### -field <b>LogicalAddress</b>

<dd>
<p>A logical address.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>The length, in bytes, of the buffer.</p>
</dd>

### -field <b>MemoryRegionToken</b>

<dd>
<p>A memory region token. When <b>MemoryRegionToken</b> is set to the token returned by <i>NdkGetPrivilegedMemoryRegionToken</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-get-privileged-memory-region-token.md">NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN</a>), the <b>NDK_SGE</b> must contain a <b>LogicalAddress</b>. When <b>MemoryRegionToken</b> is not equal to the token returned by <i>NdkGetPrivilegedMemoryRegionToken</i>, the <b>NDK_SGE</b> structure must contain a <b>VirtualAddress</b>. When an <b>NDK_SGE</b> structure is used in a work request with the <b>NDK_OP_FLAG_INLINE</b> flag, <b>MemoryRegionToken</b> might be invalid. See the remarks section for more information about the <b>MemoryRegionToken</b>. </p>
</dd>
</dl>

## -remarks
<p>The <b>NDK_SGE</b> structure specifies the local buffers for send, receive, read, and write work requests. </p>

<p>When the <b>MemoryRegionToken</b> member is set to the token returned by <i>NdkGetPrivilegedMemoryRegionToken</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-get-privileged-memory-region-token.md">NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN</a>), the <b>NDK_SGE</b> must contain a logical address returned by the <i>NdkBuildLam</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-build-lam.md">NDK_FN_BUILD_LAM</a>) function with the <a href="..\ndkpi\ns-ndkpi--ndk-logical-address-mapping.md">NDK_LOGICAL_ADDRESS_MAPPING</a> structure. Note that consecutive entries in the <b>AdapterPageArray</b> member of an <b>NDK_LOGICAL_ADDRESS_MAPPING</b> are not necessarily contiguous pages in the adapter's logical address space. Therefore, an NDK consumer might use multiple SGEs to cover all of the pages in an adapter page array.</p>

<p>When the token in the <b>MemoryRegionToken</b> member is not equal to the token that is returned by <i>NdkGetPrivilegedMemoryRegionToken</i>, the <b>NDK_SGE</b> structure must contain a virtual address that falls within the virtual address span of a previously registered memory region.</p>

<p>When an <b>NDK_SGE</b> structure is used in a work request with the <b>NDK_OP_FLAG_INLINE</b> flag,  the token in <b>MemoryRegionToken</b> might  be invalid, so it must be ignored by the NDK provider. When the <b>NDK_OP_FLAG_INLINE</b> flag is specified, the <b>VirtualAddress</b> member  of any <b>NDK_SGE</b> structure that is  passed to the work request function must point to a buffer that can be accessed by the NDK provider at an  IRQL less than or equal to  <b>DISPATCH_LEVEL</b>, That is, the buffer must be guaranteed to be resident in physical memory until the work request function returns. The total size of inline data that is passed to the provider in a single call must not exceed the  value in the  <i>InlineDataSize</i> parameter  that was  specified when the queue pair (QP) was  created.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-logical-address-mapping.md">NDK_LOGICAL_ADDRESS_MAPPING</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-build-lam.md">NDK_FN_BUILD_LAM</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-get-privileged-memory-region-token.md">NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-read.md">NDK_FN_READ</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-receive.md">NDK_FN_RECEIVE</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-send.md">NDK_FN_SEND</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-srq-receive.md">NDK_FN_SRQ_RECEIVE</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-write.md">NDK_FN_WRITE</a>
</dt>
<dt>
<a href="NULL">NDKPI Object Lifetime Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_SGE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
