---
UID: NC.d3dumddi.PFND3DDDI_SETINDICESUM
title: PFND3DDDI_SETINDICESUM
author: windows-driver-content
description: The SetIndicesUM function sets the current index buffer to the given user memory buffer.
old-location: display\setindicesum.htm
old-project: display
ms.assetid: 9ca38004-8953-4416-8552-c76813192561
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetIndicesUM
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
req.iface: 
---

# PFND3DDDI_SETINDICESUM callback



## -description
<p>The <i>SetIndicesUM</i> function sets the current index buffer to the given user memory buffer. </p>


## -prototype

````
PFND3DDDI_SETINDICESUM SetIndicesUM;

__checkReturn HRESULT APIENTRY SetIndicesUM(
  _In_       HANDLE hDevice,
  _In_       UINT   IndexSize,
  _In_ const VOID   *pUMBuffer
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>IndexSize</i> [in]

<dd>
<p> The size, in bytes, of the indices that are contained in the index buffer. The value of this parameter is 2 if the indices are 16-bit quantities or 4 if the indices are 32-bit quantities. </p>
</dd>

### -param <i>pUMBuffer</i> [in]

<dd>
<p> A pointer to the user-memory buffer that supplies the indices for the index buffer.</p>
</dd>
</dl>

## -returns
<p><i>SetIndicesUM</i> returns S_OK or an appropriate error result if the index buffer is not successfully set to the given user memory buffer.</p>

## -remarks


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
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicefuncs.md">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETINDICESUM callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
