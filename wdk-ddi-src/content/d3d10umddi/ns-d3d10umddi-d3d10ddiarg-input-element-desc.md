---
UID: NS.d3d10umddi.D3D10DDIARG_INPUT_ELEMENT_DESC
title: D3D10DDIARG_INPUT_ELEMENT_DESC
author: windows-driver-content
description: The D3D10DDIARG_INPUT_ELEMENT_DESC structure describes an element of a layout.
old-location: display\d3d10ddiarg_input_element_desc.htm
old-project: display
ms.assetid: cc052b73-8837-4756-a192-620dcd5cacb5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D10DDIARG_INPUT_ELEMENT_DESC, D3D10DDIARG_INPUT_ELEMENT_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10DDIARG_INPUT_ELEMENT_DESC
req.alt-loc: d3d10umddi.h
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
---

# D3D10DDIARG_INPUT_ELEMENT_DESC structure



## -description
<p>The D3D10DDIARG_INPUT_ELEMENT_DESC structure describes an element of a layout.</p>


## -syntax

````
typedef struct D3D10DDIARG_INPUT_ELEMENT_DESC {
  UINT                           InputSlot;
  UINT                           AlignedByteOffset;
  DXGI_FORMAT                    Format;
  D3D10_DDI_INPUT_CLASSIFICATION InputSlotClass;
  UINT                           InstanceDataStepRate;
  UINT                           InputRegister;
} D3D10DDIARG_INPUT_ELEMENT_DESC;
````


## -struct-fields
<dl>

### -field <b>InputSlot</b>

<dd>
<p>[in] The number of the input slot for the element. </p>
</dd>

### -field <b>AlignedByteOffset</b>

<dd>
<p>[in] The aligned offset, in bytes, for the element. </p>
</dd>

### -field <b>Format</b>

<dd>
<p>[in] A DXGI_FORMAT-typed value that indicates the format of the element.</p>
</dd>

### -field <b>InputSlotClass</b>

<dd>
<p>[in] A value that specifies the type of element. This member must be set to one of the following values from the D3D10_DDI_INPUT_CLASSIFICATION enumeration.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3D10_DDI_INPUT_PER_VERTEX_DATA (0)</p>
</td>
<td>
<p>The <b>InstanceDataStepRate</b> member holds the number of instances to render.</p>
</td>
</tr>
<tr>
<td>
<p>D3D10_DDI_INPUT_PER_INSTANCE_DATA (1)</p>
</td>
<td>
<p><b>InstanceDataStepRate</b> is set to zero.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>InstanceDataStepRate</b>

<dd>
<p>[in] The number of instances to render before incrementing to the next data element, if the <b>InputSlotClass</b> member is set to D3D10_DDI_INPUT_PER_INSTANCE_DATA. <b>InstanceDataStepRate</b> is set to zero if <b>InputSlotClass</b> is set to D3D10_DDI_INPUT_PER_VERTEX_DATA. </p>
</dd>

### -field <b>InputRegister</b>

<dd>
<p>[in] The number of the input register for the element.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-createelementlayout.md">D3D10DDIARG_CREATEELEMENTLAYOUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10DDIARG_INPUT_ELEMENT_DESC structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
