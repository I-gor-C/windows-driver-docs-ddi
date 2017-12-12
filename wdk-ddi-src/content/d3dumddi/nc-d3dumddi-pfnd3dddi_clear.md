---
UID: NC.d3dumddi.PFND3DDDI_CLEAR
title: PFND3DDDI_CLEAR
author: windows-driver-content
description: The Clear function performs hardware-assisted clearing on the rendering target, depth buffer, or stencil buffer.
old-location: display\clear.htm
old-project: display
ms.assetid: 1cfb5f5b-8d46-4a38-8f16-b1cecaac948a
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _DXGK_PTE, DXGK_PTE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Clear
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

# PFND3DDDI_CLEAR callback



## -description
The <b>Clear</b> function performs hardware-assisted clearing on the rendering target, depth buffer, or stencil buffer.



## -prototype

````
PFND3DDDI_CLEAR Clear;

__checkReturn HRESULT APIENTRY Clear(
  _In_       HANDLE          hDevice,
  _In_ const D3DDDIARG_CLEAR *pData,
  _In_       UINT            NumRect,
  _In_ const RECT            *pRect
)
{ ... }
````


## -parameters

### -param hDevice [in]

 A handle to the display device (graphics context).


### -param pData [in]

 A pointer to a <a href="display.d3dddiarg_clear">D3DDDIARG_CLEAR</a> structure that describes the parameters of the hardware-assisted clearing operation.


### -param NumRect [in]

 The number of rectangles in the array at <b>pRect</b> to be cleared. If the number of rectangles is set to zero, <b>Clear</b> should clear the entire render target, depth buffer, and stencil buffer. In this situation, the contents of the array at <b>pRect</b> are undefined and the driver should not attempt to read them.


### -param pRect [in]

 An array of <a href="display.rect">RECT</a> structures that indicate the rectangular areas of the buffer that the driver should clear.


## -returns
<b>Clear</b> returns S_OK or an appropriate error result if the hardware-assisted clearing operation is not successfully performed.


## -remarks
How the driver performs the clear operation depends on the number of rectangular areas that are specified in the <i>NumRect</i> parameter and the values that are set in the <b>Flags</b> member of <a href="display.d3dddiarg_clear">D3DDDIARG_CLEAR</a>. The D3DCLEAR_TARGET, D3DCLEAR_STENCIL, and D3DCLEAR_ZBUFFER values (defined in <i>D3d8types.h</i>) indicate the type of buffer to clear. The D3DCLEAR_COMPUTERECTS value (defined in <i>D3dhal.h</i>) indicates how to clear the buffer. The following settings indicate how the driver should clear the specified buffer type:

If <i>NumRect</i> is set to 0 (<i>NumRect</i>== 0) and D3DCLEAR_COMPUTERECTS is not set in <b>Flags</b>, the driver clears 0 pixels (that is, a no-op).

If <i>NumRect</i> is set to 0 and D3DCLEAR_COMPUTERECTS is set in <b>Flags</b>, the driver clears the entire viewport (not the entire surface).

If <i>NumRect</i> is set to a value greater than 0 (<i>NumRect</i>!= 0) and D3DCLEAR_COMPUTERECTS is set in <b>Flags</b>, the driver clips the rectangular areas that <b>pRect</b> specifies against the current viewport.

Scissor testing also affects how the driver performs the clear operation. An application sets the D3DRS_SCISSORTESTENABLE render state in a call to the <b>IDirect3DDevice9::SetRenderState</b> method to enable scissor testing. For more information about scissor testing, see <a href="http://go.microsoft.com/fwlink/p/?linkid=144752">Scissor Test</a>. If the D3DRS_SCISSORTESTENABLE render state is set and the D3DCLEAR_COMPUTERECTS flag is set, the driver must clip the rectangular areas that <b>pRect</b> specifies to the scissor rectangular area. 

If <i>NumRect</i> is set to a value greater than 0 (<i>NumRect</i> &gt; 0) and D3DCLEAR_COMPUTERECTS is set in <b>Flags</b>, the driver clips the specified rectangular areas to the current viewport, and to the scissor rectangle if an application previously set D3DRS_SCISSORTESTENABLE. If <i>NumRect</i> &gt; 0 and D3DCLEAR_COMPUTERECTS is not set, the driver determines that the Direct3D runtime already clipped the specified rectangular areas to the current viewport, and to the scissor rectangle if an application previously set D3DRS_SCISSORTESTENABLE.


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
<a href="display.d3dddiarg_clear">D3DDDIARG_CLEAR</a>
</dt>
<dt>
<a href="display.d3dddi_devicefuncs">D3DDDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="display.rect">RECT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_CLEAR callback function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

