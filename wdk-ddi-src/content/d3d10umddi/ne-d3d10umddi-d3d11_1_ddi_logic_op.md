---
UID: NE:d3d10umddi.D3D11_1_DDI_LOGIC_OP
title: D3D11_1_DDI_LOGIC_OP
author: windows-driver-content
description: Indicates shader logic operations used in a blend state.
old-location: display\d3d11_1_ddi_logic_op.htm
old-project: display
ms.assetid: 5ea964a2-7d80-4846-bee8-a5476cc8d0fa
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D11_1_DDI_LOGIC_OP, D3D11_1_DDI_LOGIC_OP enumeration [Display Devices], D3D11_1_DDI_LOGIC_OP_AND, D3D11_1_DDI_LOGIC_OP_AND_INVERTED, D3D11_1_DDI_LOGIC_OP_AND_REVERSE, D3D11_1_DDI_LOGIC_OP_CLEAR, D3D11_1_DDI_LOGIC_OP_COPY, D3D11_1_DDI_LOGIC_OP_COPY_INVERTED, D3D11_1_DDI_LOGIC_OP_EQUIV, D3D11_1_DDI_LOGIC_OP_INVERT, D3D11_1_DDI_LOGIC_OP_NAND, D3D11_1_DDI_LOGIC_OP_NOOP, D3D11_1_DDI_LOGIC_OP_NOR, D3D11_1_DDI_LOGIC_OP_OR, D3D11_1_DDI_LOGIC_OP_OR_INVERTED, D3D11_1_DDI_LOGIC_OP_OR_REVERSE, D3D11_1_DDI_LOGIC_OP_SET, D3D11_1_DDI_LOGIC_OP_XOR, d3d10umddi/D3D11_1_DDI_LOGIC_OP, d3d10umddi/D3D11_1_DDI_LOGIC_OP_AND, d3d10umddi/D3D11_1_DDI_LOGIC_OP_AND_INVERTED, d3d10umddi/D3D11_1_DDI_LOGIC_OP_AND_REVERSE, d3d10umddi/D3D11_1_DDI_LOGIC_OP_CLEAR, d3d10umddi/D3D11_1_DDI_LOGIC_OP_COPY, d3d10umddi/D3D11_1_DDI_LOGIC_OP_COPY_INVERTED, d3d10umddi/D3D11_1_DDI_LOGIC_OP_EQUIV, d3d10umddi/D3D11_1_DDI_LOGIC_OP_INVERT, d3d10umddi/D3D11_1_DDI_LOGIC_OP_NAND, d3d10umddi/D3D11_1_DDI_LOGIC_OP_NOOP, d3d10umddi/D3D11_1_DDI_LOGIC_OP_NOR, d3d10umddi/D3D11_1_DDI_LOGIC_OP_OR, d3d10umddi/D3D11_1_DDI_LOGIC_OP_OR_INVERTED, d3d10umddi/D3D11_1_DDI_LOGIC_OP_OR_REVERSE, d3d10umddi/D3D11_1_DDI_LOGIC_OP_SET, d3d10umddi/D3D11_1_DDI_LOGIC_OP_XOR, display.d3d11_1_ddi_logic_op
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3d10umddi.h
api_name:
-	D3D11_1_DDI_LOGIC_OP
product: Windows
targetos: Windows
req.typenames: D3D11_1_DDI_LOGIC_OP
---

# D3D11_1_DDI_LOGIC_OP Enumeration
Indicates shader logic operations used in a blend state.

In the following notation, the output value of each logic operation is given in terms of these values:<dl>
<dd><i>s</i> is the pixel shader output</dd>
<dd><i>d</i> is the contents of the render target view (RTV)</dd>
</dl>

## Syntax
```
typedef enum D3D11_1_DDI_LOGIC_OP {
  D3D11_1_DDI_LOGIC_OP_CLEAR          ,
  D3D11_1_DDI_LOGIC_OP_SET            ,
  D3D11_1_DDI_LOGIC_OP_COPY           ,
  D3D11_1_DDI_LOGIC_OP_COPY_INVERTED  ,
  D3D11_1_DDI_LOGIC_OP_NOOP           ,
  D3D11_1_DDI_LOGIC_OP_INVERT         ,
  D3D11_1_DDI_LOGIC_OP_AND            ,
  D3D11_1_DDI_LOGIC_OP_NAND           ,
  D3D11_1_DDI_LOGIC_OP_OR             ,
  D3D11_1_DDI_LOGIC_OP_NOR            ,
  D3D11_1_DDI_LOGIC_OP_XOR            ,
  D3D11_1_DDI_LOGIC_OP_EQUIV          ,
  D3D11_1_DDI_LOGIC_OP_AND_REVERSE    ,
  D3D11_1_DDI_LOGIC_OP_AND_INVERTED   ,
  D3D11_1_DDI_LOGIC_OP_OR_REVERSE     ,
  D3D11_1_DDI_LOGIC_OP_OR_INVERTED
} ;
```

## Constants

<table>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_CLEAR</td>
                    <td>0</td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_SET</td>
                    <td>1</td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_COPY</td>
                    <td><i>s</i></td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_COPY_INVERTED</td>
                    <td>~<i>s</i></td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_NOOP</td>
                    <td><i>d</i></td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_INVERT</td>
                    <td>~<i>d</i></td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_AND</td>
                    <td><i>s</i> AND <i>d</i></td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_NAND</td>
                    <td>~(<i>s</i> AND <i>d</i>)</td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_OR</td>
                    <td><i>s</i> | <i>d</i></td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_NOR</td>
                    <td>~(<i>s</i> | <i>d</i>)</td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_XOR</td>
                    <td><i>s</i> ^ <i>d</i></td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_EQUIV</td>
                    <td>~(<i>s</i> ^ <i>d</i>)</td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_AND_REVERSE</td>
                    <td><i>s</i> AND ~<i>d</i></td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_AND_INVERTED</td>
                    <td>~<i>s</i> AND <i>d</i></td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_OR_REVERSE</td>
                    <td><i>s</i> | ~<i>d</i></td>
                </tr>
            
                <tr>
                    <td>D3D11_1_DDI_LOGIC_OP_OR_INVERTED</td>
                    <td>~<i>s</i> | <i>d</i></td>
                </tr>
</table>

## Remarks

The <b>D3D11_1_DDI_LOGIC_OP</b> blend state  logic operations are specified by the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451041">D3D11_1_DDI_BLEND_DESC</a>.<b>LogicOp</b> member in a call to the <a href="https://msdn.microsoft.com/5956412e-ae35-4960-afc0-a82c6a2aa9f1">CreateBlendState(D3D11_1)</a> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/5956412e-ae35-4960-afc0-a82c6a2aa9f1">CreateBlendState(D3D11_1)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451041">D3D11_1_DDI_BLEND_DESC</a>