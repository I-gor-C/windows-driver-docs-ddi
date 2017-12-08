---
UID: NC.d3dumddi.PFND3DDDI_SETPIXELSHADERCONSTB
title: PFND3DDDI_SETPIXELSHADERCONSTB
author: windows-driver-content
description: The SetPixelShaderConstB function sets one or more pixel shader constant registers with Boolean values.
old-location: display\setpixelshaderconstb.htm
old-project: display
ms.assetid: 6f7c8932-9332-4ff2-89ab-2f9a66783326
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGK_PTE, DXGK_PTE
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
req.alt-api: SetPixelShaderConstB
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
---

# PFND3DDDI_SETPIXELSHADERCONSTB callback



## -description
The <i>SetPixelShaderConstB</i> function sets one or more pixel shader constant registers with Boolean values. 


## -prototype

````
PFND3DDDI_SETPIXELSHADERCONSTB SetPixelShaderConstB;

__checkReturn HRESULT APIENTRY SetPixelShaderConstB(
  _In_       HANDLE                         hDevice,
  _In_ const D3DDDIARG_SETPIXELSHADERCONSTB *pData,
  _In_ const BOOL                           *pRegisters
)
{ ... }
````


## -parameters

### -param hDevice [in]

 A handle to the display device (graphics context).

### -param pData [in]

 A pointer to a <a href="display.d3dddiarg_setpixelshaderconst">D3DDDIARG_SETPIXELSHADERCONST</a> structure that describes how to set the pixel shader constant registers.

### -param pRegisters [in]

 A pointer to a buffer that contains BOOL values to copy.

## -returns
<i>SetPixelShaderConstB</i> returns S_OK or an appropriate error result if the pixel shader constant registers are not successfully set with Boolean values.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="display.d3dddiarg_setpixelshaderconst">D3DDDIARG_SETPIXELSHADERCONST</a>
</dt>
<dt>
<a href="display.d3dddi_devicefuncs">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETPIXELSHADERCONSTB callback function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
