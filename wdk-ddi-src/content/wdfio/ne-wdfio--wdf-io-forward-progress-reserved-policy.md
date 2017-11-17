---
UID: NE.wdfio._WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY
title: WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY
author: windows-driver-content
description: The WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY enumeration identifies actions that the framework can take when it receives an I/O request for your driver, if a low-memory situation exists.
old-location: wdf\wdf_io_forward_progress_reserved_policy.htm
ms.assetid: 6d530cf2-de06-4aa3-9f4d-08619906c9ed
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfio.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.9
req.umdf-ver: 
req.alt-api: WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY
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
req.irql: <= DISPATCH_LEVEL (see Remarks section)
ms.keywords: WDF_INTERRUPT_INFO, WDF_INTERRUPT_INFO, *PWDF_INTERRUPT_INFO
req.iface: 
req.product: Windows 10 or later.
---

# WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY</b> enumeration identifies actions that the framework can take when it receives an I/O request for your driver, if a low-memory situation exists.</p>


## -syntax

````
typedef enum _WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY { 
  WdfIoForwardProgressInvalidPolicy                           = 0x0,
  WdfIoForwardProgressReservedPolicyAlwaysUseReservedRequest  = 0x1,
  WdfIoForwardProgressReservedPolicyUseExamine                = 0x2,
  WdfIoForwardProgressReservedPolicyPagingIO                  = 0x3
} WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY;
````


## -enum-fields
<dl>

### -field <a id="WdfIoForwardProgressInvalidPolicy"></a><a id="wdfioforwardprogressinvalidpolicy"></a><a id="WDFIOFORWARDPROGRESSINVALIDPOLICY"></a><b>WdfIoForwardProgressInvalidPolicy</b>

<dd></dd>

### -field <a id="WdfIoForwardProgressReservedPolicyAlwaysUseReservedRequest"></a><a id="wdfioforwardprogressreservedpolicyalwaysusereservedrequest"></a><a id="WDFIOFORWARDPROGRESSRESERVEDPOLICYALWAYSUSERESERVEDREQUEST"></a><b>WdfIoForwardProgressReservedPolicyAlwaysUseReservedRequest</b>

<dd>
<p>In a low-memory situation, the framework always uses a reserved request object, if one is available.</p>
</dd>

### -field <a id="WdfIoForwardProgressReservedPolicyUseExamine"></a><a id="wdfioforwardprogressreservedpolicyuseexamine"></a><a id="WDFIOFORWARDPROGRESSRESERVEDPOLICYUSEEXAMINE"></a><b>WdfIoForwardProgressReservedPolicyUseExamine</b>

<dd>
<p>In a low-memory situation, the framework calls the driver's <a href="https://msdn.microsoft.com/71974802-954d-4856-a32b-1dcc45c36ba5">EvtIoWdmIrpForForwardProgress</a> callback function.</p>
</dd>

### -field <a id="WdfIoForwardProgressReservedPolicyPagingIO"></a><a id="wdfioforwardprogressreservedpolicypagingio"></a><a id="WDFIOFORWARDPROGRESSRESERVEDPOLICYPAGINGIO"></a><b>WdfIoForwardProgressReservedPolicyPagingIO</b>

<dd>
<p>In a low-memory situation, if the <b>Flags</b> member of the I/O request's <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a> structure indicates a paging operation, the framework uses a reserved request object, if one is available. If the I/O request is not a paging operation, the framework completes the I/O request with an error status value.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY</b> enumeration is used as a member type in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552364">WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY</a> structure.</p>

<p>The <b>WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY</b> enumeration is used as a member type in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552364">WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY</a> structure.</p>

<p>The <b>WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY</b> enumeration is used as a member type in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552364">WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY</a> structure.</p>

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