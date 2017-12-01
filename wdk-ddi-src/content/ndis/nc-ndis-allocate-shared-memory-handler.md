---
UID: NC.ndis.ALLOCATE_SHARED_MEMORY_HANDLER
title: ALLOCATE_SHARED_MEMORY_HANDLER
author: windows-driver-content
description: The NetAllocateSharedMemory function (ALLOCATE_SHARED_MEMORY_HANDLER entry point) is called by NDIS when a driver allocates shared memory from a shared memory provider.
old-location: netvista\netallocatesharedmemory.htm
old-project: netvista
ms.assetid: d85b4f28-707b-4525-afd8-83e1ceb2674e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NetAllocateSharedMemory
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# ALLOCATE_SHARED_MEMORY_HANDLER callback



## -description
<p>The 
  <i>NetAllocateSharedMemory</i> function (ALLOCATE_SHARED_MEMORY_HANDLER entry point) is called by NDIS when
  a driver allocates shared memory from a shared memory provider.</p>


## -prototype

````
ALLOCATE_SHARED_MEMORY_HANDLER NetAllocateSharedMemory;

NDIS_STATUS NetAllocateSharedMemory(
  _In_    NDIS_HANDLE                    ProviderContext,
  _In_    PNDIS_SHARED_MEMORY_PARAMETERS SharedMemoryParameters,
  _Inout_ PNDIS_HANDLE                   pSharedMemoryProviderContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>ProviderContext</i> [in]

<dd>
<p>An NDIS_HANDLE to a block of driver-allocated context information that identifies the provider.
     The provider supplied this information in the 
     <b>ProviderContext</b> member of the 
     <a href="..\ndis\ns-ndis--ndis-shared-memory-provider-characteristics.md">
     NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a> structure.</p>
</dd>

### -param <i>SharedMemoryParameters</i> [in]

<dd>
<p>A pointer to an 
     <a href="..\ndis\ns-ndis--ndis-shared-memory-parameters.md">
     NDIS_SHARED_MEMORY_PARAMETERS</a> structure that defines the requested attributes for the shared
     memory.</p>
</dd>

### -param <i>pSharedMemoryProviderContext</i> [in, out]

<dd>
<p>A pointer to a handle for a shared memory context area. The shared memory provider provides a
     handle that identifies the shared memory that it allocated.</p>
</dd>
</dl>

## -returns
<p><i>NetAllocateSharedMemory</i> can return the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>The operation failed because there were insufficient resources to complete the operation.</p><dl>
<dt><b>NDIS_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The operation failed because of an invalid input parameter.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>The operation failed for unspecified reasons.</p>

<p> </p>

## -remarks
<p>NDIS calls the 
    <i>NetAllocateSharedMemory</i> function of a shared memory provider when a driver calls the 
    <a href="..\ndis\nf-ndis-ndisallocatesharedmemory.md">
    NdisAllocateSharedMemory</a> function.</p>

<p>The shared memory provider specified the entry point (ALLOCATE_SHARED_MEMORY_HANDLER) for 
    <i>NetAllocateSharedMemory</i> in the 
    <a href="..\ndis\ns-ndis--ndis-shared-memory-provider-characteristics.md">
    NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a> structure.</p>

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
<p>Supported in NDIS 6.20 and later.</p>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\ns-ndis--ndis-shared-memory-parameters.md">NDIS_SHARED_MEMORY_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-shared-memory-provider-characteristics.md">
   NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatesharedmemory.md">NdisAllocateSharedMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20ALLOCATE_SHARED_MEMORY_HANDLER callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
