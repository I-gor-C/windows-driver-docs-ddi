---
UID: NS.ntddndis._NDIS_RECEIVE_QUEUE_INFO
title: NDIS_RECEIVE_QUEUE_INFO
author: windows-driver-content
description: The NDIS_RECEIVE_QUEUE_INFO structure contains information about a receive queue on a network adapter.
old-location: netvista\ndis_receive_queue_info.htm
old-project: netvista
ms.assetid: 7cdc45d4-e8aa-437a-b6fc-8b8c0dc17585
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_RECEIVE_QUEUE_INFO, NDIS_RECEIVE_QUEUE_INFO, *PNDIS_RECEIVE_QUEUE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_RECEIVE_QUEUE_INFO
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
req.iface: 
---

# NDIS_RECEIVE_QUEUE_INFO structure



## -description
<p>The <b>NDIS_RECEIVE_QUEUE_INFO</b> structure contains information about a receive queue on a network adapter.</p>


## -syntax

````
typedef struct _NDIS_RECEIVE_QUEUE_INFO {
  NDIS_OBJECT_HEADER                   Header;
  ULONG                                Flags;
  NDIS_RECEIVE_QUEUE_TYPE              QueueType;
  NDIS_RECEIVE_QUEUE_ID                QueueId;
  NDIS_RECEIVE_QUEUE_GROUP_ID          QueueGroupId;
  NDIS_RECEIVE_QUEUE_OPERATIONAL_STATE QueueState;
  GROUP_AFFINITY                       ProcessorAffinity;
  ULONG                                NumSuggestedReceiveBuffers;
  ULONG                                MSIXTableEntry;
  ULONG                                LookaheadSize;
  NDIS_VM_NAME                         VmName;
  NDIS_QUEUE_NAME                      QueueName;
#if (NDIS_SUPPORT_NDIS630)
  ULONG                                NumFilters;
  ULONG                                InterruptCoalescingDomainId;
#endif 
} NDIS_RECEIVE_QUEUE_INFO, *PNDIS_RECEIVE_QUEUE_INFO;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_RECEIVE_QUEUE_INFO</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_RECEIVE_QUEUE_INFO</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to one of the following values: </p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_QUEUE_INFO_REVISION_2"></a><a id="ndis_receive_queue_info_revision_2"></a>NDIS_RECEIVE_QUEUE_INFO_REVISION_2

<dd>
<p>Added additional members for NDIS 6.30.</p>
<div class="alert"><b>Note</b>  Revision 2 of this structure is  supported only on Windows Server 2012 and later versions of Windows Server.</div>
<div> </div>
<p>Set the <b>Size</b> member to <b>NDIS_SIZEOF_RECEIVE_QUEUE_INFO_REVISION_2</b>.</p>
</dd>

### -field <a id="NDIS_RECEIVE_QUEUE_INFO_REVISION_1"></a><a id="ndis_receive_queue_info_revision_1"></a>NDIS_RECEIVE_QUEUE_INFO_REVISION_1

<dd>
<p>Original version for NDIS 6.20.</p>
<p>Set the <b>Size</b> member to <b>NDIS_SIZEOF_RECEIVE_QUEUE_INFO_REVISION_1</b>.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>QueueType</b>

<dd>
<p>An 
     <a href="..\ntddndis\ne-ntddndis--ndis-receive-queue-type.md">NDIS_RECEIVE_QUEUE_TYPE</a> enumeration
     value that specifies the type of the receive queue.</p>
</dd>

### -field <b>QueueId</b>

<dd>
<p>An <b>NDIS_RECEIVE_QUEUE_ID</b> type value that contains a receive queue identifier. This identifier is an
     integer value between zero and the number of queues that the network adapter supports. A value of <b>NDIS_DEFAULT_RECEIVE_QUEUE_ID</b> specifies
     the default receive queue.</p>
</dd>

### -field <b>QueueGroupId</b>

<dd>
<p>This member is reserved for NDIS.</p>
</dd>

### -field <b>QueueState</b>

<dd>
<p>An 
     <a href="..\ntddndis\ne-ntddndis--ndis-receive-queue-operational-state.md">
     NDIS_RECEIVE_QUEUE_OPERATIONAL_STATE</a> enumeration value that specifies the operational state of the
     receive queue.</p>
</dd>

### -field <b>ProcessorAffinity</b>

<dd>
<p>A <b>GROUP_AFFINITY</b> bitmap that specifies the CPU that the queue has affinity with. For example,
     setting bit 0 indicates that CPU 0 is used, setting bit 1 indicates that CPU 1 is used, and so on. Because a VM queue is associated with one CPU, all receive indications for the queue are handled on that processor.</p>
</dd>

### -field <b>NumSuggestedReceiveBuffers</b>

<dd>
<p>A <b>ULONG</b> value that contains a suggested value for the number of receive buffers that the network adapter should use to support the queue. This number can be adjusted relative to the resources that the
     miniport driver has available or in proportion to the number that the network adapter uses for other
     queues. For example, the actual number of receive buffers could be double or half of this suggested
     value.</p>
</dd>

### -field <b>MSIXTableEntry</b>

<dd>
<p>A <b>ULONG</b> value that contains the MSI-X table entry index for the queue.</p>
</dd>

### -field <b>LookaheadSize</b>

<dd>
<p>A <b>ULONG</b> value for the size, in bytes, of the lookahead size requirement for this queue. A network adapter that supports lookahead in VM queues splits a received packet at an offset that is equal to or
     greater than the requested lookahead size and uses DMA to transfer the lookahead data and the
     post-lookahead data to separate shared memory segments.</p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported. The value of this member must be set to zero.</div>
<div> </div>
</dd>

### -field <b>VmName</b>

<dd>
<p>An <b>NDIS_VM_NAME</b> value that contains the user-friendly description of the virtual machine.</p>
</dd>

### -field <b>QueueName</b>

<dd>
<p>An <b>NDIS_QUEUE_NAME</b> value that contains the user-friendly description of the queue.</p>
</dd>

### -field <b>NumFilters</b>

<dd>
<p>A ULONG value that specifies the number of receive filters that have been configured on the network adapter.</p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, the miniport driver must maintain a counter for the current number of receive filters that are set on the network adapter. The driver must increment the counter each time a receive filter is set through an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569795">OID_RECEIVE_FILTER_SET_FILTER</a>.  The driver must also decrement the counter each time a receive filter is  cleared through an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569785">OID_RECEIVE_FILTER_CLEAR_FILTER</a>.</div>
<div> </div>
</dd>

### -field <b>InterruptCoalescingDomainId</b>

<dd>
<p>A ULONG value that is reserved for use by NDIS. This value is used for informational purposes by the miniport driver.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_RECEIVE_QUEUE_INFO</b> structure is used with the 
    <a href="..\ntddndis\ns-ntddndis--ndis-receive-queue-info-array.md">
    NDIS_RECEIVE_QUEUE_INFO_ARRAY</a> structure for the 
    <a href="netvista.oid_receive_filter_enum_queues">
    OID_RECEIVE_FILTER_ENUM_QUEUES</a> OID that enumerates receive queues on a network adapter.</p>

<p>With a successful return from the <a href="netvista.oid_receive_filter_enum_queues">
    OID_RECEIVE_FILTER_ENUM_QUEUES</a>, NDIS provides an
    <a href="..\ntddndis\ns-ntddndis--ndis-receive-queue-info-array.md">NDIS_RECEIVE_QUEUE_INFO_ARRAY</a> structure that defines the properties of the receive queue array. Each
    element in the array is an <b>NDIS_RECEIVE_QUEUE_INFO</b> structure.</p>

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
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-receive-queue-info-array.md">NDIS_RECEIVE_QUEUE_INFO_ARRAY</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-receive-queue-operational-state.md">
   NDIS_RECEIVE_QUEUE_OPERATIONAL_STATE</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-receive-queue-type.md">NDIS_RECEIVE_QUEUE_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569788">OID_RECEIVE_FILTER_ENUM_QUEUES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569785">OID_RECEIVE_FILTER_CLEAR_FILTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569795">OID_RECEIVE_FILTER_SET_FILTER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RECEIVE_QUEUE_INFO structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
