---
UID: NC.d3d12umddi.PFND3D12DDI_SET_PREDICATION
title: PFND3D12DDI_SET_PREDICATION
author: windows-driver-content
description: The pfnSetPredication callback function denotes that subsequent video operations and resource manipulation commands are not actually performed if the resulting predicate data of the predicate is equal to the operation specified.
old-location: display\pfnd3d12ddi_set_predication.htm
old-project: display
ms.assetid: C5830688-4FC6-4D3F-82EB-15354B28C5F1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnSetPredication
req.alt-loc: D3d12umddi.h
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

# PFND3D12DDI_SET_PREDICATION callback



## -description
<p>The <i>pfnSetPredication</i> callback function denotes that subsequent video operations and resource manipulation commands are not actually performed if the resulting predicate data of the predicate is equal to the operation specified.</p>


## -prototype

````
PFND3D12DDI_SET_PREDICATION pfnSetPredication;

VOID APIENTRY* pfnSetPredication(
   D3D12DDI_HCOMMANDLIST   hCommandList,
   D3D12DDI_HRESOURCE      hResource,
   UINT64                  Uint64,
   D3D12DDI_PREDICATION_OP PredicationOp
)
{ ... }
````


## -parameters
<dl>

### -param <i>hCommandList</i> 

<dd>
<p>The handle of a command list.</p>
</dd>

### -param <i>hResource</i> 

<dd>
<p>The handle of a resource.</p>
</dd>

### -param <i>Uint64</i> 

<dd>
<p>An integer.</p>
</dd>

### -param <i>PredicationOp</i> 

<dd>
<p>A predication operation. For more information, see the <a href="..\d3d12umddi\ne-d3d12umddi-d3d12ddi-predication-op.md">D3D12DDI_PREDICATION_OP</a> enumeration.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d12umddi\ne-d3d12umddi-d3d12ddi-predication-op.md">D3D12DDI_PREDICATION_OP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D12DDI_SET_PREDICATION callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
