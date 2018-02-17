---
UID: NE:d3dkmddi._DXGK_INTERRUPT_STATE
title: "_DXGK_INTERRUPT_STATE"
author: windows-driver-content
description: "."
old-location: display\dxgk_interrupt_state.htm
old-project: display
ms.assetid: C72DF96B-5D12-4AC0-8FBB-904E087807DB
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: "_DXGK_INTERRUPT_STATE, DXGK_INTERRUPT_STATE enumeration [Display Devices], DXGK_INTERRUPT_ENABLE, DXGK_INTERRUPT_DISABLE, display.dxgk_interrupt_state, d3dkmddi/DXGK_INTERRUPT_DISABLE, d3dkmddi/DXGK_INTERRUPT_ENABLE, d3dkmddi/DXGK_INTERRUPT_STATE, DXGK_INTERRUPT_STATE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10.
req.target-min-winversvr: 
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
req.irql: PASSIVE_LEVEL
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dkmddi.h
apiname:
-	DXGK_INTERRUPT_STATE
product: Windows
targetos: Windows
req.typenames: DXGK_INTERRUPT_STATE
---

# _DXGK_INTERRUPT_STATE Enumeration
Provides additional information for <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_controlinterrupt2.md">DxgkDdi_ControlInterrupt2 </a>when VSYNC is not being utilized.
<div class="alert"><b>Note</b>  This enumeration uses Enable as 0 and Disable as 1 in the bivalent state, which is the opposite of the Boolean value previously used in <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_controlinterrupt.md">DxgkDdi_ControlInterrupt</a>
</div><div> </div>

## Syntax
````
typedef enum _DXGK_INTERRUPT_STATE { 
  DXGK_INTERRUPT_ENABLE      = 0,
  DXGK_INTERRUPT_DISABLE     = 1
} DXGK_INTERRUPT_STATE;
````

## Constants

<table>
            
                <tr>
                    <td>DXGK_INTERRUPT_DISABLE</td>
                    <td>Indicates that the interrupt is disabled.</td>
                </tr>
            
                <tr>
                    <td>DXGK_INTERRUPT_ENABLE</td>
                    <td>Indicates that the interrupt is enabled.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 10. Available in Windows 10. |
| **Header** | d3dkmddi.h |