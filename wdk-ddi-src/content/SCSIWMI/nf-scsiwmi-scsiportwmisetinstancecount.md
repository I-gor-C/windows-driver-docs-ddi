---
UID: NF.scsiwmi.ScsiPortWmiSetInstanceCount
title: ScsiPortWmiSetInstanceCount
author: windows-driver-content
description: The ScsiPortWmiSetInstanceCount specifies the number of instances for which data buffers must be set aside within the WNODE_ALL_DATA structure in the request context.
old-location: storage\scsiportwmisetinstancecount.htm
ms.assetid: 0de2c766-cd3c-46ff-bb78-f1e4c37af2c0
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: scsiwmi.h
req.include-header: Miniport.h, Scsi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ScsiPortWmiSetInstanceCount
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
ms.keywords: ScsiPortWmiSetInstanceCount
req.iface: 
req.product: Windows 10 or later.
---

# ScsiPortWmiSetInstanceCount function



## -description
<p>The <b>ScsiPortWmiSetInstanceCount</b> specifies the number of instances for which data buffers must be set aside within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566372">WNODE_ALL_DATA</a> structure in the request context. </p>


## -syntax

````
BOOLEAN ScsiPortWmiSetInstanceCount(
  _In_  PSCSIWMI_REQUEST_CONTEXT RequestContext,
  _In_  ULONG                    InstanceCount,
  _Out_ PULONG                   BufferAvail,
  _Out_ PULONG                   SizeNeeded
);
````


## -parameters
<dl>

### -param <i>RequestContext</i> [in]

<dd>
<p>Pointer to a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff564946">SCSIWMI_REQUEST_CONTEXT</a> that contains the request context for a WMI SRB. </p>
</dd>

### -param <i>InstanceCount</i> [in]

<dd>
<p>Contains the number of instances for which the minidriver will provide data. </p>
</dd>

### -param <i>BufferAvail</i> [out]

<dd>
<p>Contains, on return, the number of bytes of buffer space available for describing instance names and data. The value that is returned in this member can be passed to routines <a href="https://msdn.microsoft.com/library/windows/hardware/ff564799">ScsiPortWmiSetData</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff564810">ScsiPortWmiSetInstanceName</a> in the <i>BufferAvail </i>parameter of those routines. </p>
<p>The <b>ScsiPortWmiSetInstanceCount</b> routine initializes an array of pointers to data buffers, with one array element for each instance. If there is not enough memory available in the WNODE to initialize an array of size <i>InstanceCount</i>, a zero will be returned in this member. </p>
</dd>

### -param <i>SizeNeeded</i> [out]

<dd>
<p>Indicates, on input, the number of bytes needed to describe the entire WNODE <i>before </i>configuring the internal arrays in the WNODE. On return, this member will contain the size of the entire WNODE, including the newly initialized arrays within the WNODE. </p>
</dd>
</dl>

## -returns
<p>The <b>ScsiPortWmiSetInstanceCount</b> routine returns <b>TRUE</b> if the operation succeeds and <b>FALSE</b> if the WNODE contained within the request context is not of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff566372">WNODE_ALL_DATA</a>.</p>

## -remarks
<p>The minidriver must call <b>ScsiPortWmiSetInstanceCount</b> before calling either <a href="https://msdn.microsoft.com/library/windows/hardware/ff564799">ScsiPortWmiSetData</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff564810">ScsiPortWmiSetInstanceName</a>. The minidriver should only call <b>ScsiPortWmiSetInstanceCount</b> once. </p>

<p>The parameter <b>RequestContext</b> points to a request context structure, <a href="https://msdn.microsoft.com/library/windows/hardware/ff564946">SCSIWMI_REQUEST_CONTEXT</a>, that contains information associated with a <a href="https://msdn.microsoft.com/5c2ed322-0fc9-4004-9a5f-f4d3c6a59fe9">Windows Management Instrumentation</a> (WMI) SCSI request block (SRB). The request context structure, in turn, contains one of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566371">WMI WNODE_XXX Structures</a> used by the WMI system to pass data between user-mode data consumers and kernel-mode data providers such as drivers. </p>

<p>The <b>ScsiPortWmiSetInstanceCount</b> routine requires the WNODE structure that is defined within the request context to be of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff566372">WNODE_ALL_DATA</a>. This is because <b>ScsiPortWmiSetInstanceCount</b> sets aside a data area that will hold information for multiple instances associated with a WMI data block. Unlike the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566377">WNODE_SINGLE_INSTANCE</a> structure which contains information about a single instance, the WNODE_ALL_DATA structure contains an array of pointers to buffer areas for different instances, and <b>ScsiPortWmiSetInstanceCount</b> initializes this array, so that each buffer of instance data can be accessed individually using an instance index.</p>

<p>The memory allocated for the request context must remain valid until after the miniport driver calls <b>ScsiPortWmiPostProcess</b>, and <b>ScsiPortWmiPostProcess</b> returns the final SRB status and buffer size. If the SRB can pend, the memory for the request context should be allocated from the SRB extension. If the SRB cannot pend, the memory can be allocated from a stack frame that does not go out of scope.</p>

<p>The minidriver must call <b>ScsiPortWmiSetInstanceCount</b> before calling either <a href="https://msdn.microsoft.com/library/windows/hardware/ff564799">ScsiPortWmiSetData</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff564810">ScsiPortWmiSetInstanceName</a>. The minidriver should only call <b>ScsiPortWmiSetInstanceCount</b> once. </p>

<p>The parameter <b>RequestContext</b> points to a request context structure, <a href="https://msdn.microsoft.com/library/windows/hardware/ff564946">SCSIWMI_REQUEST_CONTEXT</a>, that contains information associated with a <a href="https://msdn.microsoft.com/5c2ed322-0fc9-4004-9a5f-f4d3c6a59fe9">Windows Management Instrumentation</a> (WMI) SCSI request block (SRB). The request context structure, in turn, contains one of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566371">WMI WNODE_XXX Structures</a> used by the WMI system to pass data between user-mode data consumers and kernel-mode data providers such as drivers. </p>

<p>The <b>ScsiPortWmiSetInstanceCount</b> routine requires the WNODE structure that is defined within the request context to be of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff566372">WNODE_ALL_DATA</a>. This is because <b>ScsiPortWmiSetInstanceCount</b> sets aside a data area that will hold information for multiple instances associated with a WMI data block. Unlike the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566377">WNODE_SINGLE_INSTANCE</a> structure which contains information about a single instance, the WNODE_ALL_DATA structure contains an array of pointers to buffer areas for different instances, and <b>ScsiPortWmiSetInstanceCount</b> initializes this array, so that each buffer of instance data can be accessed individually using an instance index.</p>

<p>The memory allocated for the request context must remain valid until after the miniport driver calls <b>ScsiPortWmiPostProcess</b>, and <b>ScsiPortWmiPostProcess</b> returns the final SRB status and buffer size. If the SRB can pend, the memory for the request context should be allocated from the SRB extension. If the SRB cannot pend, the memory can be allocated from a stack frame that does not go out of scope.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Scsiwmi.h (include Miniport.h or Scsi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564946">SCSIWMI_REQUEST_CONTEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566377">WNODE_SINGLE_INSTANCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566372">WNODE_ALL_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20ScsiPortWmiSetInstanceCount function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
