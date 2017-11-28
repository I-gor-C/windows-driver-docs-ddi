---
UID: NE.ndis.NDIS_PD_QUEUE_TYPE
title: NDIS_PD_QUEUE_TYPE
author: windows-driver-content
description: The NDIS_PD_QUEUE_TYPE enumeration defines types of PacketDirect Provider Interface (PDPI) queues. Its enumeration values are used in the QueueType member of the NDIS_PD_QUEUE_PARAMETERS structure.
old-location: netvista\ndis_pd_queue_type.htm
old-project: netvista
ms.assetid: 4536B3AB-6170-4819-975A-47D9A6223EAE
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ndis.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PD_QUEUE_TYPE
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

# NDIS_PD_QUEUE_TYPE enumeration



## -description
<p>The <b>NDIS_PD_QUEUE_TYPE</b> enumeration defines types of PacketDirect Provider Interface (PDPI)  queues. Its enumeration values are used in the <b>QueueType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn931846">NDIS_PD_QUEUE_PARAMETERS</a> structure.</p>


## -syntax

````
typedef enum _NDIS_PD_QUEUE_TYPE { 
  PDQueueTypeUnknown,
  PDQueueTypeReceive,
  PDQueueTypeTransmit,
  PDQueueTypeMax
} NDIS_PD_QUEUE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="PDQueueTypeUnknown"></a><a id="pdqueuetypeunknown"></a><a id="PDQUEUETYPEUNKNOWN"></a><b>PDQueueTypeUnknown</b>

<dd>
<p>The queue type is not known.</p>
</dd>

### -field <a id="PDQueueTypeReceive"></a><a id="pdqueuetypereceive"></a><a id="PDQUEUETYPERECEIVE"></a><b>PDQueueTypeReceive</b>

<dd>
<p>The queue is a receive queue.</p>
</dd>

### -field <a id="PDQueueTypeTransmit"></a><a id="pdqueuetypetransmit"></a><a id="PDQUEUETYPETRANSMIT"></a><b>PDQueueTypeTransmit</b>

<dd>
<p>The queue is a transmit queue.</p>
</dd>

### -field <a id="PDQueueTypeMax"></a><a id="pdqueuetypemax"></a><a id="PDQUEUETYPEMAX"></a><b>PDQueueTypeMax</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of NDIS header files and binaries.

</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn931846">NDIS_PD_QUEUE_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-ndis-pd-allocate-queue.md">NdisPDAllocateQueue</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PD_QUEUE_TYPE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
