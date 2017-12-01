---
UID: NE.ntddndis._NDIS_RECEIVE_QUEUE_OPERATIONAL_STATE
title: NDIS_RECEIVE_QUEUE_OPERATIONAL_STATE
author: windows-driver-content
description: The NDIS_RECEIVE_QUEUE_OPERATIONAL_STATE enumeration identifies the current queue state of a receive queue.
old-location: netvista\ndis_receive_queue_operational_state.htm
old-project: netvista
ms.assetid: a8ae7b19-9dc8-4ccc-b71e-62ec0be1fa99
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: GET_CONFIGURATION_IOCTL_INPUT, GET_CONFIGURATION_IOCTL_INPUT, *PGET_CONFIGURATION_IOCTL_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_RECEIVE_QUEUE_OPERATIONAL_STATE
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

# NDIS_RECEIVE_QUEUE_OPERATIONAL_STATE enumeration



## -description
<p>The <b>
       NDIS_RECEIVE_QUEUE_OPERATIONAL_STATE</b> enumeration identifies the current queue state of a receive
  queue.</p>


## -syntax

````
typedef enum _NDIS_RECEIVE_QUEUE_OPERATIONAL_STATE { 
  NdisReceiveQueueOperationalStateUndefined,
  NdisReceiveQueueOperationalStateRunning,
  NdisReceiveQueueOperationalStatePaused,
  NdisReceiveQueueOperationalStateDmaStopped,
  NdisReceiveQueueOperationalStateMaximum
} NDIS_RECEIVE_QUEUE_OPERATIONAL_STATE, *PNDIS_RECEIVE_QUEUE_OPERATIONAL_STATE;
````


## -enum-fields
<dl>

### -field <a id="NdisReceiveQueueOperationalStateUndefined"></a><a id="ndisreceivequeueoperationalstateundefined"></a><a id="NDISRECEIVEQUEUEOPERATIONALSTATEUNDEFINED"></a><b>NdisReceiveQueueOperationalStateUndefined</b>

<dd>
<p>The receive queue is in the 
     Undefined state. The queue is not allocated.</p>
</dd>

### -field <a id="NdisReceiveQueueOperationalStateRunning"></a><a id="ndisreceivequeueoperationalstaterunning"></a><a id="NDISRECEIVEQUEUEOPERATIONALSTATERUNNING"></a><b>NdisReceiveQueueOperationalStateRunning</b>

<dd>
<p>The receive queue is in the 
     Running state. The queue was allocated successfully, there is at least one filter set on the
     queue, and the miniport driver has completed, or will complete, the 
     <a href="netvista.oid_receive_filter_queue_allocation_complete">
     OID_RECEIVE_FILTER_QUEUE_ALLOCATION_COMPLETE</a> OID request with a success status.</p>
</dd>

### -field <a id="NdisReceiveQueueOperationalStatePaused"></a><a id="ndisreceivequeueoperationalstatepaused"></a><a id="NDISRECEIVEQUEUEOPERATIONALSTATEPAUSED"></a><b>NdisReceiveQueueOperationalStatePaused</b>

<dd>
<p>The receive queue is in the 
     Paused state. The queue was allocated successfully with the 
     <a href="netvista.oid_receive_filter_allocate_queue">
     OID_RECEIVE_FILTER_ALLOCATE_QUEUE</a> OID. There are no filters set on the queue.</p>
</dd>

### -field <a id="NdisReceiveQueueOperationalStateDmaStopped"></a><a id="ndisreceivequeueoperationalstatedmastopped"></a><a id="NDISRECEIVEQUEUEOPERATIONALSTATEDMASTOPPED"></a><b>NdisReceiveQueueOperationalStateDmaStopped</b>

<dd>
<p>The DMA operations on the queue are stopped because the queue is being freed, and the queue is in
     the 
     DMA Stopped state. The queue enters the 
     DMA Stopped state when the miniport driver receives an 
     <a href="netvista.oid_receive_filter_free_queue">
     OID_RECEIVE_FILTER_FREE_QUEUE</a> OID request, stops the DMA operations for the queue, and issues an 
     <a href="netvista.ndis_status_receive_queue_state">
     NDIS_STATUS_RECEIVE_QUEUE_STATE</a> status indication.</p>
</dd>

### -field <a id="NdisReceiveQueueOperationalStateMaximum"></a><a id="ndisreceivequeueoperationalstatemaximum"></a><a id="NDISRECEIVEQUEUEOPERATIONALSTATEMAXIMUM"></a><b>NdisReceiveQueueOperationalStateMaximum</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</p>
</dd>
</dl>

## -remarks
<p>The <b>
       NDIS_RECEIVE_QUEUE_OPERATIONAL_STATE</b> enumeration is used in the 
    <a href="..\ndis\ns-ndis--ndis-receive-queue-state.md">NDIS_RECEIVE_QUEUE_STATE</a> and 
    <a href="..\ntddndis\ns-ntddndis--ndis-receive-queue-info.md">
    NDIS_RECEIVE_QUEUE_INFO</a> structures.</p>

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
<a href="..\ntddndis\ns-ntddndis--ndis-receive-queue-info.md">NDIS_RECEIVE_QUEUE_INFO</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-receive-queue-state.md">NDIS_RECEIVE_QUEUE_STATE</a>
</dt>
<dt>
<a href="netvista.ndis_status_receive_queue_state">
   NDIS_STATUS_RECEIVE_QUEUE_STATE</a>
</dt>
<dt>
<a href="netvista.oid_receive_filter_allocate_queue">
   OID_RECEIVE_FILTER_ALLOCATE_QUEUE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569789">OID_RECEIVE_FILTER_FREE_QUEUE</a>
</dt>
<dt>
<a href="netvista.oid_receive_filter_queue_allocation_complete">
   OID_RECEIVE_FILTER_QUEUE_ALLOCATION_COMPLETE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RECEIVE_QUEUE_OPERATIONAL_STATE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
