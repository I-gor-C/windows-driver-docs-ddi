---
UID: NF.poscx.POS_CX_ATTRIBUTES_INIT
title: POS_CX_ATTRIBUTES_INIT
author: windows-driver-content
description: POS_CX_ATTRIBUTES_INIT initializes a POS_CX_ATTRIBUTE structure.
old-location: pos\pos_cx_attributes_init.htm
ms.assetid: A1287386-E831-474A-858C-89787741FD57
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: pos
req.header: poscx.h
req.include-header: Poscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: POS_CX_ATTRIBUTES_INIT
req.alt-loc: poscx.h
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
ms.keywords: POS_CX_ATTRIBUTES_INIT
req.iface: 
req.product: Windows 10 or later.
---

# POS_CX_ATTRIBUTES_INIT function



## -description
<p>POS_CX_ATTRIBUTES_INIT initializes a <a href="https://msdn.microsoft.com/A91B8EAA-2FCB-4468-8CF3-A3C4D9D7E355">POS_CX_ATTRIBUTE</a> structure.</p>


## -syntax

````
VOID POS_CX_ATTRIBUTES_INIT(
  _Out_ POS_CX_ATTRIBUTE *PosCxAttrPtr
);
````


## -parameters
<dl>

### -param <i>PosCxAttrPtr</i> [out]

<dd>
<p>A pointer to the caller-allocated <a href="https://msdn.microsoft.com/A91B8EAA-2FCB-4468-8CF3-A3C4D9D7E355">POS_CX_ATTRIBUTE</a> structure to initialize.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Product</p>
</th>
<td width="70%">
<p>Windows 10 or later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Poscx.h (include Poscx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/A91B8EAA-2FCB-4468-8CF3-A3C4D9D7E355">POS_CX_ATTRIBUTE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt593125">PosCxInit</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [pos\pos]:%20POS_CX_ATTRIBUTES_INIT function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
