---
UID: NC.d3dumddi.PFND3DDDI_SETINDICES
title: PFND3DDDI_SETINDICES
author: windows-driver-content
description: The SetIndices function sets the current index buffer.
old-location: display\setindices.htm
ms.assetid: 5348b3f9-78c5-4915-ba68-296d6f9f916c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetIndices
req.alt-loc: d3dumddi.h
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# PFND3DDDI_SETINDICES callback



## -description
<p>The <i>SetIndices</i> function sets the current index buffer. </p>


## -prototype

````
PFND3DDDI_SETINDICES SetIndices;

__checkReturn HRESULT APIENTRY SetIndices(
  _In_       HANDLE               hDevice,
  _In_ const D3DDDIARG_SETINDICES *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543313">D3DDDIARG_SETINDICES</a> structure that describes parameters for setting the current index buffer.</p>
</dd>
</dl>

## -returns
<p><i>SetIndices</i> returns S_OK or an appropriate error result if the index buffer is not successfully set.</p>

## -remarks
<p>The Microsoft Direct3D runtime supplies a handle value of zero in the <b>hIndexBuffer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543313">D3DDDIARG_SETINDICES</a> structure that is pointed to by the <i>pData</i> parameter to clear the current index buffer. The driver should handle subsequent attempts to draw indexed primitives (before a new current index buffer is established) so that a crash does not occur. The debug version of your driver should display informative messages to the debug output stream when this error condition is detected.</p>

<p>The Microsoft Direct3D runtime supplies a handle value of zero in the <b>hIndexBuffer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543313">D3DDDIARG_SETINDICES</a> structure that is pointed to by the <i>pData</i> parameter to clear the current index buffer. The driver should handle subsequent attempts to draw indexed primitives (before a new current index buffer is established) so that a crash does not occur. The debug version of your driver should display informative messages to the debug output stream when this error condition is detected.</p>

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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543313">D3DDDIARG_SETINDICES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETINDICES callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
