---
UID: NS.wdfio._WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY
title: WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY
author: windows-driver-content
description: The WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY structure contains driver-supplied information that the framework uses to enable guaranteed forward progress for an I/O queue.
old-location: wdf\wdf_io_queue_forward_progress_policy.htm
old-project: wdf
ms.assetid: cee3de1f-eaee-40e9-97a9-979e75e22c0a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY, WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY, *PWDF_IO_QUEUE_FORWARD_PROGRESS_POLICY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfio.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.9
req.umdf-ver: 
req.alt-api: WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY
req.alt-loc: wdfio.h
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
req.product: Windows 10 or later.
---

# WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY</b> structure contains driver-supplied information that the framework uses to enable <a href="wdf.guaranteeing_forward_progress_of_i_o_operations">guaranteed forward progress</a> for an I/O queue.</p>


## -syntax

````
typedef struct _WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY {
  ULONG                                              Size;
  ULONG                                              TotalForwardProgressRequests;
  WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY            ForwardProgressReservedPolicy;
  WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS   ForwardProgressReservePolicySettings;
  PFN_WDF_IO_ALLOCATE_RESOURCES_FOR_RESERVED_REQUEST EvtIoAllocateResourcesForReservedRequest;
  PFN_WDF_IO_ALLOCATE_REQUEST_RESOURCES              EvtIoAllocateRequestResources;
} WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY, *PWDF_IO_QUEUE_FORWARD_PROGRESS_POLICY;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The length, in bytes, of this structure.</p>
</dd>

### -field <b>TotalForwardProgressRequests</b>

<dd>
<p>The number of request objects that the framework will attempt to reserve for use in low-memory situations. This number must be greater than zero.</p>
</dd>

### -field <b>ForwardProgressReservedPolicy</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552357">WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY</a>-typed value that specifies how the framework will allocate request objects during low-memory situations. </p>
</dd>

### -field <b>ForwardProgressReservePolicySettings</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552358">WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS</a> structure that contains additional values that are specific to the policy that the <b>ForwardProgressReservedPolicy</b> member specifies. This member should be <b>NULL</b> unless the driver provides an <a href="..\wdfio\nc-wdfio-evt-wdf-io-wdm-irp-for-forward-progress.md">EvtIoWdmIrpForForwardProgress</a> callback function.</p>
</dd>

### -field <b>EvtIoAllocateResourcesForReservedRequest</b>

<dd>
<p>A pointer to the driver's queue-specific <a href="..\wdfio\nc-wdfio-evt-wdf-io-allocate-resources-for-reserved-request.md">EvtIoAllocateResourcesForReservedRequest</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtIoAllocateRequestResources</b>

<dd>
<p>A pointer to the driver's queue-specific <a href="..\wdfio\nc-wdfio-evt-wdf-io-allocate-request-resources.md">EvtIoAllocateRequestResources</a> callback function, or <b>NULL</b>.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547395">WdfIoQueueAssignForwardProgressPolicy</a> method.</p>

<p>Drivers must initialize the <b>WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY</b> structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552365">WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY_DEFAULT_INIT</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552366">WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY_EXAMINE_INIT</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff552367">WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY_PAGINGIO_INIT</a> before they call <a href="https://msdn.microsoft.com/library/windows/hardware/ff547395">WdfIoQueueAssignForwardProgressPolicy</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfio.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>