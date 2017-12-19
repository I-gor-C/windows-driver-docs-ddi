---
UID: NC.d3dumddi.PFND3DDDI_SETVERTEXSHADERCONSTB
title: PFND3DDDI_SETVERTEXSHADERCONSTB
author: windows-driver-content
description: The SetVertexShaderConstB function sets one or more vertex shader constant registers with Boolean values.
old-location: display\setvertexshaderconstb.htm
old-project: display
ms.assetid: 41ca823e-4370-4cba-9129-067e25a43a69
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
req.alt-api: SetVertexShaderConstB
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

# PFND3DDDI_SETVERTEXSHADERCONSTB callback



## -description
The <i>SetVertexShaderConstB</i> function sets one or more vertex shader constant registers with Boolean values.



## -prototype

````
PFND3DDDI_SETVERTEXSHADERCONSTB SetVertexShaderConstB;

__checkReturn HRESULT APIENTRY SetVertexShaderConstB(
  _In_       HANDLE                         hDevice,
  _In_ const D3DDDIARG_SETVERTEXSHADERCONST *pData,
  _In_ const BOOL                           *pRegisters
)
{ ... }
````


## -parameters

### -param hDevice [in]

 A handle to the display device (graphics context).


### -param pData [in]

 A pointer to a <a href="display.d3dddiarg_setvertexshaderconst">D3DDDIARG_SETVERTEXSHADERCONST</a> structure that specifies how to set the vertex shader constant registers.


### -param pRegisters [in]

 A pointer to a buffer that contains BOOL values to copy.


## -returns
<i>SetVertexShaderConstB</i> returns S_OK or an appropriate error result if the vertex shader constant registers are not successfully set with Boolean values.


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
<a href="display.d3dddiarg_setvertexshaderconst">D3DDDIARG_SETVERTEXSHADERCONST</a>
</dt>
<dt>
<a href="display.d3dddi_devicefuncs">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETVERTEXSHADERCONSTB callback function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

