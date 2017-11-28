---
UID: NC.d3dumddi.PFND3DDDI_GENERATEMIPSUBLEVELS
title: PFND3DDDI_GENERATEMIPSUBLEVELS
author: windows-driver-content
description: The GenerateMipSubLevels function regenerates the sublevels of a MIP-map texture.
old-location: display\generatemipsublevels.htm
old-project: display
ms.assetid: 86567fc1-cf66-4709-a6e1-6b24408df963
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
req.alt-api: GenerateMipSubLevels
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

# PFND3DDDI_GENERATEMIPSUBLEVELS callback



## -description
<p>The <i>GenerateMipSubLevels</i> function regenerates the sublevels of a MIP-map texture.</p>


## -prototype

````
PFND3DDDI_GENERATEMIPSUBLEVELS GenerateMipSubLevels;

__checkReturn HRESULT APIENTRY GenerateMipSubLevels(
  _In_       HANDLE                         hDevice,
  _In_ const D3DDDIARG_GENERATEMIPSUBLEVELS *pData
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
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543135">D3DDDIARG_GENERATEMIPSUBLEVELS</a> structure that describes how to generate the sublevels of a MIP-map texture.</p>
</dd>
</dl>

## -returns
<p><i>GenerateMipSubLevels</i> returns S_OK or an appropriate error result if the sublevels of a MIP-map texture are not successfully generated.</p>

## -remarks
<p>After the user-mode display driver performs an operation that accesses only the top level of a MIP-map texture, the Microsoft Direct3D runtime calls the driver's <i>GenerateMipSubLevels</i> function to notify the driver to automatically regenerate the sublevels of the MIP-map texture by using a specific filter type.</p>

<p>After the user-mode display driver performs an operation that accesses only the top level of a MIP-map texture, the Microsoft Direct3D runtime calls the driver's <i>GenerateMipSubLevels</i> function to notify the driver to automatically regenerate the sublevels of the MIP-map texture by using a specific filter type.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543135">D3DDDIARG_GENERATEMIPSUBLEVELS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_GENERATEMIPSUBLEVELS callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
