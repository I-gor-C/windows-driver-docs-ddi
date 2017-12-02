---
UID: NS.ndis._NDIS_SCATTER_GATHER_LIST_PARAMETERS
title: NDIS_SCATTER_GATHER_LIST_PARAMETERS
author: windows-driver-content
description: The NDIS_SCATTER_GATHER_LIST_PARAMETERS structure specifies parameters that NDIS uses to build a scatter/gather list for a buffer.
old-location: netvista\ndis_scatter_gather_list_parameters.htm
old-project: netvista
ms.assetid: 5c14a6ed-3180-41d6-a09a-b3ae0a0c8b36
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_SCATTER_GATHER_LIST_PARAMETERS, NDIS_SCATTER_GATHER_LIST_PARAMETERS, *PNDIS_SCATTER_GATHER_LIST_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SCATTER_GATHER_LIST_PARAMETERS
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NDIS_SCATTER_GATHER_LIST_PARAMETERS structure



## -description
<p>The NDIS_SCATTER_GATHER_LIST_PARAMETERS structure specifies parameters that NDIS uses to build a
  scatter/gather list for a buffer.</p>


## -syntax

````
typedef struct _NDIS_SCATTER_GATHER_LIST_PARAMETERS {
  NDIS_OBJECT_HEADER           Header;
  ULONG                        Flags;
  NDIS_RECEIVE_QUEUE_ID        QueueId;
  NDIS_SHARED_MEMORY_USAGE     SharedMemoryUsage;
  PMDL                         Mdl;
  PVOID                        CurrentVa;
  ULONG                        Length;
  NDIS_PROCESS_SG_LIST_HANDLER ProcessSGListHandler;
  PVOID                        Context;
  PSCATTER_GATHER_LIST         ScatterGatherListBuffer;
  ULONG                        ScatterGatherListBufferSize;
  ULONG                        ScatterGatherListBufferSizeNeeded;
} NDIS_SCATTER_GATHER_LIST_PARAMETERS, *PNDIS_SCATTER_GATHER_LIST_PARAMETERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     structure (NDIS_SCATTER_GATHER_LIST_PARAMETERS). The driver sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
     <b>Revision</b> member to NDIS_SCATTER_GATHER_LIST_PARAMETERS_REVISION_1 and the 
     <b>Size</b> member to NDIS_SIZEOF_SCATTER_GATHER_LIST_PARAMETERS_REVISION_1.</p>
</dd>

### -field Flags

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field QueueId

<dd>
<p>An NDIS_RECEIVE_QUEUE_ID type value that contains a queue identifier. The queue identifier is an
     integer between zero and the number of queues that the miniport adapter supports. A zero value indicates
     the default queue.</p>
</dd>

### -field SharedMemoryUsage

<dd>
<p>An 
     <a href="..\ndis\ne-ndis--ndis-shared-memory-usage.md">NDIS_SHARED_MEMORY_USAGE</a> enumeration
     value that specifies the purpose of the shared memory.</p>
</dd>

### -field Mdl

<dd>
<p>A pointer to a memory descriptor list (MDL) that describes the shared memory buffer.</p>
</dd>

### -field CurrentVa

<dd>
<p>A ULONG value for the current virtual address.</p>
</dd>

### -field Length

<dd>
<p>A ULONG value that contains the length, in bytes, of the shared memory buffer.</p>
</dd>

### -field ProcessSGListHandler

<dd>
<p>A pointer to a 
     <a href="..\ndis\nc-ndis-ndis-process-sg-list.md">NetProcessSGList</a> function
     (NDIS_PROCESS_SG_LIST_HANDLER entry point).</p>
</dd>

### -field Context

<dd>
<p>A pointer to a block of driver-allocated context information that stores information about the
     scatter/gather list. NDIS passes the context information in calls to 
     <a href="..\ndis\nc-ndis-ndis-process-sg-list.md">NetProcessSGList</a> at the 
     <i>Context</i> parameter.</p>
</dd>

### -field ScatterGatherListBuffer

<dd>
<p>A pointer to a 
     <a href="..\wdm\ns-wdm--scatter-gather-list.md">SCATTER_GATHER_LIST</a> structure.</p>
</dd>

### -field ScatterGatherListBufferSize

<dd>
<p>A ULONG value that contains the length, in bytes, of the scatter/gather list.</p>
</dd>

### -field ScatterGatherListBufferSizeNeeded

<dd>
<p>A ULONG value where NDIS writes the total number of bytes that NDIS requires to build the
     scatter/gather list successfully.</p>
</dd>
</dl>

## -remarks
<p>To build a scatter/gather list, an NDIS driver passes the NDIS_SCATTER_GATHER_LIST_PARAMETERS
    structure to the 
    <a href="..\ndis\nf-ndis-ndisbuildscattergatherlist.md">
    NdisBuildScatterGatherList</a> function.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\ne-ndis--ndis-shared-memory-usage.md">NDIS_SHARED_MEMORY_USAGE</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisbuildscattergatherlist.md">NdisBuildScatterGatherList</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-ndis-process-sg-list.md">NetProcessSGList</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--scatter-gather-list.md">SCATTER_GATHER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SCATTER_GATHER_LIST_PARAMETERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
