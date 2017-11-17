---
UID: NS.ntddndis._NDIS_RECEIVE_QUEUE_INFO_ARRAY
title: NDIS_RECEIVE_QUEUE_INFO_ARRAY
author: windows-driver-content
description: The NDIS_RECEIVE_QUEUE_INFO_ARRAY structure specifies a list of receive queues on a network adapter.
old-location: netvista\ndis_receive_queue_info_array.htm
ms.assetid: 6a026c2b-e2ed-41bf-9482-0fdc64b175f2
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_RECEIVE_QUEUE_INFO_ARRAY
req.alt-loc: Ntddndis.h
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
ms.keywords: NDIS_RECEIVE_QUEUE_INFO_ARRAY, NDIS_RECEIVE_QUEUE_INFO_ARRAY, *PNDIS_RECEIVE_QUEUE_INFO_ARRAY
req.iface: 
---

# NDIS_RECEIVE_QUEUE_INFO_ARRAY structure



## -description
<p>The <b>NDIS_RECEIVE_QUEUE_INFO_ARRAY</b> structure specifies a list of receive queues on a network adapter.</p>


## -syntax

````
typedef struct _NDIS_RECEIVE_QUEUE_INFO_ARRAY {
  NDIS_OBJECT_HEADER Header;
  ULONG              FirstElementOffset;
  ULONG              NumElements;
  ULONG              ElementSize;
} NDIS_RECEIVE_QUEUE_INFO_ARRAY, *PNDIS_RECEIVE_QUEUE_INFO_ARRAY;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_RECEIVE_QUEUE_INFO_ARRAY</b>  structure. The driver sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to <b>NDIS_OBJECT_TYPE_DEFAULT</b>, the 
     <b>Revision</b> member to <b>NDIS_RECEIVE_QUEUE_INFO_ARRAY_REVISION_1</b>, and the 
     <b>Size</b> member to <b>NDIS_SIZEOF_RECEIVE_QUEUE_INFO_ARRAY_REVISION_1</b>.</p>
</dd>

### -field <b>FirstElementOffset</b>

<dd>
<p>A ULONG value that specifies the offset, in bytes, to the first element in an array of elements that follow this structure. The offset is measured from the start of the <b>NDIS_RECEIVE_QUEUE_INFO_ARRAY</b> structure up to the beginning of the first element. Each element in the array is an <a href="https://msdn.microsoft.com/7cdc45d4-e8aa-437a-b6fc-8b8c0dc17585">
     NDIS_RECEIVE_QUEUE_INFO</a> structure.

</p>
<div class="alert"><b>Note</b>  If <b>NumElements</b> is set to zero, this member is ignored.  </div>
<div> </div>
</dd>

### -field <b>NumElements</b>

<dd>
<p>A <b>ULONG</b> value that represents the number of elements in the list of elements that follow the
     <b>NDIS_RECEIVE_QUEUE_INFO_ARRAY</b> structure.</p>
</dd>

### -field <b>ElementSize</b>

<dd>
<p>A <b>ULONG</b> value that specifies the size, in bytes, of each element in the array.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_RECEIVE_QUEUE_INFO_ARRAY</b> structure is used in the 
    <a href="netvista.oid_receive_filter_enum_queues">
    OID_RECEIVE_FILTER_ENUM_QUEUES</a> OID that enumerates receive queues on a network adapter. Each
    element in the array is an 
    <a href="https://msdn.microsoft.com/7cdc45d4-e8aa-437a-b6fc-8b8c0dc17585">
    NDIS_RECEIVE_QUEUE_INFO</a> structure.</p>

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
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567204">NDIS_RECEIVE_QUEUE_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569788">OID_RECEIVE_FILTER_ENUM_QUEUES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RECEIVE_QUEUE_INFO_ARRAY structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
