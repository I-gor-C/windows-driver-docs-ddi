---
UID : NC:d3dumddi.PFND3DDDI_CLEAR
title : PFND3DDDI_CLEAR
author : windows-driver-content
description : The Clear function performs hardware-assisted clearing on the rendering target, depth buffer, or stencil buffer.
old-location : display\clear.htm
old-project : display
ms.assetid : 1cfb5f5b-8d46-4a38-8f16-b1cecaac948a
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_PTE, DXGK_PTE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : Clear
req.alt-loc : d3dumddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : DXGK_PTE
---


# PFND3DDDI_CLEAR callback function
The <b>Clear</b> function performs hardware-assisted clearing on the rendering target, depth buffer, or stencil buffer.

## Syntax

```
PFND3DDDI_CLEAR Pfnd3dddiClear;

HRESULT Pfnd3dddiClear(
  HANDLE hDevice,
  CONST D3DDDIARG_CLEAR *,
   UINT,
  CONST RECT *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`



`UINT`



`*`




## Return Value

<b>Clear</b> returns S_OK or an appropriate error result if the hardware-assisted clearing operation is not successfully performed.

## Remarks

How the driver performs the clear operation depends on the number of rectangular areas that are specified in the <i>NumRect</i> parameter and the values that are set in the <b>Flags</b> member of <a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_clear.md">D3DDDIARG_CLEAR</a>. The D3DCLEAR_TARGET, D3DCLEAR_STENCIL, and D3DCLEAR_ZBUFFER values (defined in <i>D3d8types.h</i>) indicate the type of buffer to clear. The D3DCLEAR_COMPUTERECTS value (defined in <i>D3dhal.h</i>) indicates how to clear the buffer. The following settings indicate how the driver should clear the specified buffer type:

If <i>NumRect</i> is set to 0 (<i>NumRect</i>== 0) and D3DCLEAR_COMPUTERECTS is not set in <b>Flags</b>, the driver clears 0 pixels (that is, a no-op).

If <i>NumRect</i> is set to 0 and D3DCLEAR_COMPUTERECTS is set in <b>Flags</b>, the driver clears the entire viewport (not the entire surface).

If <i>NumRect</i> is set to a value greater than 0 (<i>NumRect</i>!= 0) and D3DCLEAR_COMPUTERECTS is set in <b>Flags</b>, the driver clips the rectangular areas that <b>pRect</b> specifies against the current viewport.

Scissor testing also affects how the driver performs the clear operation. An application sets the D3DRS_SCISSORTESTENABLE render state in a call to the <b>IDirect3DDevice9::SetRenderState</b> method to enable scissor testing. For more information about scissor testing, see <a href="http://go.microsoft.com/fwlink/p/?linkid=144752">Scissor Test</a>. If the D3DRS_SCISSORTESTENABLE render state is set and the D3DCLEAR_COMPUTERECTS flag is set, the driver must clip the rectangular areas that <b>pRect</b> specifies to the scissor rectangular area. 

If <i>NumRect</i> is set to a value greater than 0 (<i>NumRect</i> &gt; 0) and D3DCLEAR_COMPUTERECTS is set in <b>Flags</b>, the driver clips the specified rectangular areas to the current viewport, and to the scissor rectangle if an application previously set D3DRS_SCISSORTESTENABLE. If <i>NumRect</i> &gt; 0 and D3DCLEAR_COMPUTERECTS is not set, the driver determines that the Direct3D runtime already clipped the specified rectangular areas to the current viewport, and to the scissor rectangle if an application previously set D3DRS_SCISSORTESTENABLE.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_clear.md">D3DDDIARG_CLEAR</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_CLEAR callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>