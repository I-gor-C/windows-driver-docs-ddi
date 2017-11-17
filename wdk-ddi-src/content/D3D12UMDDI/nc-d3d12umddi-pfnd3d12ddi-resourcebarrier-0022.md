---
UID: NC.d3d12umddi.PFND3D12DDI_RESOURCEBARRIER_0022
title: PFND3D12DDI_RESOURCEBARRIER_0022
author: windows-driver-content
description: The pfnResourceBarrier callback function supports resource barriers.
old-location: display\pfnd3d12ddi_resourcebarrier_0022.htm
ms.assetid: AD42B7FC-9928-4386-B3EB-C9F0302415DA
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnResourceBarrier
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
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
req.iface: 
---

# PFND3D12DDI_RESOURCEBARRIER_0022 callback



## -description
<p>The <i>pfnResourceBarrier</i> callback function supports resource barriers. </p>


## -prototype

````
PFND3D12DDI_RESOURCEBARRIER_0022 pfnResourceBarrier;

VOID APIENTRY* pfnResourceBarrier(
             D3D12DDI_HCOMMANDLIST                            hDrvCommandList,
             UINT                                             Count,
  _In_ const _reads_(Count) D3D12DDIARG_RESOURCE_BARRIER_0022 *ResourceBarrier
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDrvCommandList</i> 

<dd>
<p>The handle of a command list.</p>
</dd>

### -param <i>Count</i> 

<dd>
<p>Specifies a count.</p>
</dd>

### -param <i>ResourceBarrier</i> [in]

<dd>
<p>A pointer to a resource barrier as a <a href="https://msdn.microsoft.com/ED597BB0-F9ED-4311-9E2F-06AEA2755B37">D3D12DDIARG_RESOURCE_BARRIER_0022</a> structure. </p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>Access this callback function by using a command list functions structure, such as the <b>D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_0020</b> structure. </p>

<p>Access this callback function by using a command list functions structure, such as the <b>D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_0020</b> structure. </p>

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
<a href="https://msdn.microsoft.com/ED597BB0-F9ED-4311-9E2F-06AEA2755B37">D3D12DDIARG_RESOURCE_BARRIER_0022</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D12DDI_RESOURCEBARRIER_0022 callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
