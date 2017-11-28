---
UID: NS.wmistr.tagWNODE_METHOD_ITEM
title: tagWNODE_METHOD_ITEM
author: windows-driver-content
description: The WNODE_METHOD_ITEM structure indicates a method associated with an instance of a data block and contains any input data for the method.
old-location: kernel\wnode_method_item.htm
old-project: kernel
ms.assetid: c5e1af58-a00d-4801-b591-fc9ec9b50502
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: tagWNODE_METHOD_ITEM, WNODE_METHOD_ITEM, *PWNODE_METHOD_ITEM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wmistr.h
req.include-header: Wmistr.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WNODE_METHOD_ITEM
req.alt-loc: wmistr.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# tagWNODE_METHOD_ITEM structure



## -description
<p>The <b>WNODE_METHOD_ITEM</b> structure indicates a method associated with an instance of a data block and contains any input data for the method.</p>


## -syntax

````
typedef struct tagWNODE_METHOD_ITEM {
  struct _WNODE_HEADER  WnodeHeader;
  ULONG                OffsetInstanceName;
  ULONG                InstanceIndex;
  ULONG                MethodId;
  ULONG                DataBlockOffset;
  ULONG                SizeDataBlock;
  UCHAR                VariableData[];
} WNODE_METHOD_ITEM, *PWNODE_METHOD_ITEM;
````


## -struct-fields
<dl>

### -field <b>WnodeHeader</b>

<dd>
<p>Is a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566375">WNODE_HEADER</a> structure that contains information common to all <b>WNODE_<i>XXX</i></b> structures, such as the buffer size, the GUID that represents a data block associated with a request, and flags that provide information about the <b>WNODE_<i>XXX</i></b> data being passed or returned.</p>
</dd>

### -field <b>OffsetInstanceName</b>

<dd>
<p>Indicates the offset in bytes from the beginning of this structure to the dynamic instance name of this instance, aligned on a USHORT boundary. This member is valid only if WNODE_FLAG_STATIC_INSTANCE_NAMES is clear in <b>WnodeHeader.Flags</b>. If the data block was registered with static instance names, WMI ignores <b>OffsetInstanceName</b>.</p>
</dd>

### -field <b>InstanceIndex</b>

<dd>
<p>Indicates the index of this instance into the driver's list of static instance names for this data block. This member is valid only if the data block was registered with static instance names and WNODE_FLAG_STATIC_INSTANCE_NAMES is set in <b>WnodeHeader.Flags</b>. If the data block was registered with dynamic instance names, WMI ignores <b>InstanceIndex</b>.</p>
</dd>

### -field <b>MethodId</b>

<dd>
<p>Specifies the ID of the method to run. </p>
</dd>

### -field <b>DataBlockOffset</b>

<dd>
<p>Indicates the offset from the beginning of an input <b>WNODE_METHOD_ITEM</b> to input data for the method, or the offset from the beginning of an output <b>WNODE_METHOD_ITEM</b> to output data from the method.</p>
</dd>

### -field <b>SizeDataBlock</b>

<dd>
<p>Indicates the size of the input data in an input <b>WNODE_METHOD_ITEM</b>, or zero if there is no input. In an output <b>WNODE_METHOD_ITEM</b>, <b>SizeDataBlock </b>indicates the size of the output data, or zero if there is no output. </p>
</dd>

### -field <b>VariableData</b>

<dd>
<p>Contains additional data, including the dynamic instance name if any, and the input for or output from the method aligned on an 8-byte boundary. </p>
</dd>
</dl>

## -remarks
<p>WMI passes a <b>WNODE_METHOD_ITEM</b> with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550868">IRP_MN_EXECUTE_METHOD</a> request to specify a method to run in an instance of a data block, plus any input data required by the method.</p>

<p>If a method generates output, a driver overwrites the input data with the output at <b>DataBlockOffset</b> in the buffer at <b>IrpStack-&gt;Parameters.WMI.Buffer</b>, and sets <b>SizeDataBlock</b> in the <b>WNODE_METHOD_ITEM</b> to specify the size of the output data.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wmistr.h (include Wmistr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566375">WNODE_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20WNODE_METHOD_ITEM structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
