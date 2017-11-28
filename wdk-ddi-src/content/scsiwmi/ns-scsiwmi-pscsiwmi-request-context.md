---
UID: NS.scsiwmi.PSCSIWMI_REQUEST_CONTEXT
title: PSCSIWMI_REQUEST_CONTEXT
author: windows-driver-content
description: A SCSIWMI_REQUEST_CONTEXT structure contains context information for a WMI SRB.
old-location: storage\scsiwmi_request_context.htm
old-project: storage
ms.assetid: 524150d8-d4a7-4b61-89c4-0074c938559b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PSCSIWMI_REQUEST_CONTEXT, SCSIWMI_REQUEST_CONTEXT, *PSCSIWMI_REQUEST_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: scsiwmi.h
req.include-header: Scsiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SCSIWMI_REQUEST_CONTEXT
req.alt-loc: scsiwmi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# PSCSIWMI_REQUEST_CONTEXT structure



## -description
<p>A SCSIWMI_REQUEST_CONTEXT structure contains context information for a WMI SRB. </p>


## -syntax

````
typedef struct {
  PVOID  UserContext;
  ULONG  BufferSize;
  PUCHAR Buffer;
  UCHAR  MinorFunction;
  UCHAR  ReturnStatus;
  ULONG  ReturnSize;
} SCSIWMI_REQUEST_CONTEXT, *PSCSIWMI_REQUEST_CONTEXT;
````


## -struct-fields
<dl>

### -field <b>UserContext</b>

<dd>
<p>Points to a miniport driver buffer that contains any data the miniport driver requires to process the SRB. This can be a pointer to  the miniport driver's HW_DEVICE_EXTENSION structure or some other buffer.</p>
</dd>

### -field <b>BufferSize</b>

<dd>
<p>Reserved for system use and not available for use by miniport drivers.</p>
</dd>

### -field <b>Buffer</b>

<dd>
<dl>

### -field Pointer to a structure of type WNODE_XXX. For more information about these sorts of structures, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff566371">WMI WNODE_XXX Structures</a>. 


### -field This member is set by <a href="https://msdn.microsoft.com/library/windows/hardware/ff564766">ScsiPortWmiDispatchFunction</a>. Miniport drivers should not assign values to this member. 

</dl>
</dd>

### -field <b>MinorFunction</b>

<dd>
<p>Reserved for system use and not available for use by miniport drivers.</p>
</dd>

### -field <b>ReturnStatus</b>

<dd>
<p>Indicates the return status of the SRB. This member is not valid until after the miniport driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff564796">ScsiPortWmiPostProcess</a> to update the request context.</p>
</dd>

### -field <b>ReturnSize</b>

<dd>
<p>Indicates the number of bytes of data transferred for the SRB. This member is not valid until after the miniport driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff564796">ScsiPortWmiPostProcess</a> to update the request context.</p>
</dd>
</dl>

## -remarks
<p>When the miniport driver receives an SRB in which the <b>Function</b> member is set to SRB_FUNCTION_WMI, it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff564766">ScsiPortWmiDispatchFunction</a> with request parameters, including a pointer to a request context. <b>ScsiPortWmiDispatchFunction</b> passes the request context to the miniport driver's appropriate <b>HwScsiWmi</b><b><i>Xxx</i></b> routine.</p>

<p>When the miniport driver is done processing the SRB and prior to completing the SRB, the miniport driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff564796">ScsiPortWmiPostProcess</a> to update the <b>ReturnStatus</b> and <b>ReturnSize</b> members of the request context. The miniport driver updates the SRB's data transfer length and status to these values by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff564789">ScsiPortWmiGetReturnSize</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff564791">ScsiPortWmiGetReturnStatus</a>. respectively.</p>

<p>A request context must remain valid throughout the processing of an SRB. If the SRB can pend, the miniport driver must allocate the SCSIWMI_REQUEST_CONTEXT structure from the SRB extension so it remains valid until the SRB completes. For nonpending SRBs the structure can be allocated from a stack frame that does not go out of scope.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Scsiwmi.h (include Scsiwmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564766">ScsiPortWmiDispatchFunction</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564789">ScsiPortWmiGetReturnSize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564791">ScsiPortWmiGetReturnStatus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564796">ScsiPortWmiPostProcess</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SCSIWMI_REQUEST_CONTEXT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
