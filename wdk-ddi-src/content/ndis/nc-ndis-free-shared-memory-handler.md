---
UID: NC.ndis.FREE_SHARED_MEMORY_HANDLER
title: FREE_SHARED_MEMORY_HANDLER
author: windows-driver-content
description: The NetFreeSharedMemory function (FREE_SHARED_MEMORY_HANDLER entry point) is called by NDIS when a driver frees shared memory from a shared memory provider.
old-location: netvista\netfreesharedmemory.htm
old-project: netvista
ms.assetid: fdc3dfe7-6980-493d-ad41-aed501db3a6b
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: NetFreeSharedMemory
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

# FREE_SHARED_MEMORY_HANDLER callback



## -description
<p>The 
  <i>NetFreeSharedMemory</i> function (FREE_SHARED_MEMORY_HANDLER entry point) is called by NDIS when a driver
  frees shared memory from a shared memory provider.</p>


## -prototype

````
FREE_SHARED_MEMORY_HANDLER NetFreeSharedMemory;

VOID NetFreeSharedMemory(
  _In_ NDIS_HANDLE ProviderContext,
  _In_ NDIS_HANDLE SharedMemoryProviderContext
)
{ ... }
````


## -parameters
<dl>

### -param ProviderContext [in]

<dd>
<p>An NDIS_HANDLE to a block of driver-allocated context information that identifies the provider.
     The provider supplied this information in the 
     <b>ProviderContext</b> member of the 
     <a href="..\ndis\ns-ndis--ndis-shared-memory-provider-characteristics.md">
     NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a> structure.</p>
</dd>

### -param SharedMemoryProviderContext [in]

<dd>
<p>A handle for a context area that identifies the shared memory block. This is the handle that the
     shared memory provider supplied at the 
     <i>pSharedMemoryProviderContext</i> parameter of the 
     <a href="..\ndis\nc-ndis-allocate-shared-memory-handler.md">
     NetAllocateSharedMemory</a> function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>NDIS calls the 
    <i>NetFreeSharedMemory</i> function of a shared memory provider when a driver calls the 
    <a href="..\ndis\nf-ndis-ndisfreesharedmemory.md">NdisFreeSharedMemory</a> function.</p>

<p>The shared memory provider specified the entry point (FREE_SHARED_MEMORY_HANDLER) for 
    <i>NetFreeSharedMemory</i> in the 
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
<a href="..\ndis\ns-ndis--ndis-shared-memory-provider-characteristics.md">
   NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfreesharedmemory.md">NdisFreeSharedMemory</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-allocate-shared-memory-handler.md">NetAllocateSharedMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FREE_SHARED_MEMORY_HANDLER callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
