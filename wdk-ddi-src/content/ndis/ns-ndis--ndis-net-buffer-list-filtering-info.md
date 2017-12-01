---
UID: NS.ndis._NDIS_NET_BUFFER_LIST_FILTERING_INFO
title: NDIS_NET_BUFFER_LIST_FILTERING_INFO
author: windows-driver-content
description: The NDIS_NET_BUFFER_LIST_FILTERING_INFO structure defines filtering information that is associated with a NET_BUFFER_LIST structure.
old-location: netvista\ndis_net_buffer_list_filtering_info.htm
old-project: netvista
ms.assetid: 992a4c77-e22f-4123-81e8-86c8030accfa
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_NET_BUFFER_LIST_FILTERING_INFO, NDIS_NET_BUFFER_LIST_FILTERING_INFO, *PNDIS_NET_BUFFER_LIST_FILTERING_INFO
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
req.alt-api: NDIS_NET_BUFFER_LIST_FILTERING_INFO
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
req.irql: See Remarks section
req.iface: 
---

# NDIS_NET_BUFFER_LIST_FILTERING_INFO structure



## -description
<p>The <b>NDIS_NET_BUFFER_LIST_FILTERING_INFO</b> structure defines filtering information that is associated
  with a 
  <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure.</p>


## -syntax

````
typedef struct _NDIS_NET_BUFFER_LIST_FILTERING_INFO {
  union {
    struct {
      USHORT FilterId;
#if (NDIS_SUPPORT_NDIS630)
      union {
#endif 
        USHORT QueueId;
#if (NDIS_SUPPORT_NDIS630)
        USHORT VPortId;
      } QueueVPortInfo;
#endif 
    } FilteringInfo;
    PVOID Value;
  };
} NDIS_NET_BUFFER_LIST_FILTERING_INFO, *PNDIS_NET_BUFFER_LIST_FILTERING_INFO;
````


## -struct-fields
<dl>

### -field <b>FilteringInfo</b>

<dd>
<p>A structure that contains the following members:</p>
<dl>

### -field <b>FilterId</b>

<dd>
<p>A USHORT value that contains a receive filter identifier. The receive filter identifier is an
       integer from one to the number of receive filters that the network adapter supports. </p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.20, this member must be set to zero.</div>
<div> </div>
</dd>

### -field <b>QueueVPortInfo</b>

<dd>
<p>A union that contains the following members:</p>
<dl>

### -field <b>QueueId</b>

<dd>
<p>A USHORT value that contains an identifier for a virtual machine  queue (VMQ) receive queue. The queue identifier is an integer between zero
       and the number of queues that the network adapter supports. A value of NDIS_DEFAULT_RECEIVE_QUEUE_ID specifies
     the default receive queue.</p>
<div class="alert"><b>Note</b>  Starting with Windows Server 2012, the value of this member must always be set to NDIS_DEFAULT_RECEIVE_QUEUE_ID  by miniport drivers that support the SR-IOV interface.</div>
<div> </div>
</dd>

### -field <b>VPortId</b>

<dd>
<p>A USHORT value that contains the identifier for a virtual port (VPort). A value of DEFAULT_VPORT_ID specifies the default VPort on the NIC switch. 

The VPort with the specified VPortId value must have previously been created through a set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>.</p>
<div class="alert"><b>Note</b>  For the VMQ interface, this member must be set to NDIS_DEFAULT_VPORT_ID.</div>
<div> </div>
</dd>
</dl>
</dd>
</dl>
</dd>

### -field <b>Value</b>

<dd>
<p>A PVOID type value that is in a union with the 
      <b>FilteringInfo</b> member. This member lets a driver access all the information in the
      <b>NDIS_NET_BUFFER_LIST_FILTERING_INFO</b> structure as one PVOID value.</p>
</dd>
</dl>

## -remarks
<p>Starting with NDIS 6.20, miniport drivers  use the <b>NDIS_NET_BUFFER_LIST_FILTERING_INFO</b> structure to specify receive
    filter information that accompanies the 
    <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structures that are associated with a 
    <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure.</p>

<p>To access the <b>NDIS_NET_BUFFER_LIST_FILTERING_INFO</b> structure from the NET_BUFFER_LIST OOB data, an NDIS
    driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> macro and specifies
    the 
    <b>NetBufferListFilteringInfo</b>  information type.</p>

<p>To access the identifier values directly, use the 
    <a href="netvista.net_buffer_list_receive_filter_id">
    NET_BUFFER_LIST_RECEIVE_FILTER_ID</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh439946">NET_BUFFER_LIST_RECEIVE_FILTER_VPORT_ID</a>, or 
    <a href="netvista.net_buffer_list_receive_queue_id">
    NET_BUFFER_LIST_RECEIVE_QUEUE_ID</a> macros.</p>

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
<a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="netvista.net_buffer_list_receive_filter_id">
   NET_BUFFER_LIST_RECEIVE_FILTER_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439946">NET_BUFFER_LIST_RECEIVE_FILTER_VPORT_ID</a>
</dt>
<dt>
<a href="netvista.net_buffer_list_receive_queue_id">
   NET_BUFFER_LIST_RECEIVE_QUEUE_ID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NET_BUFFER_LIST_FILTERING_INFO structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
