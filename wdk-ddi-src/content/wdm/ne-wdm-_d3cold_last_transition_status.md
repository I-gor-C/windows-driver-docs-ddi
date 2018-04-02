---
UID: NE:wdm._D3COLD_LAST_TRANSITION_STATUS
title: "_D3COLD_LAST_TRANSITION_STATUS"
author: windows-driver-content
description: The D3COLD_LAST_TRANSITION_STATUS enumeration indicates whether the most recent transition to the D3hot device power state was followed by a transition to the D3cold device power state.
old-location: kernel\d3cold_last_transition_status.htm
old-project: kernel
ms.assetid: 21E89D92-9902-4785-B022-8D17268FE75F
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PD3COLD_LAST_TRANSITION_STATUS, D3COLD_LAST_TRANSITION_STATUS, D3COLD_LAST_TRANSITION_STATUS enumeration [Kernel-Mode Driver Architecture], LastDStateTransitionD3cold, LastDStateTransitionD3hot, LastDStateTransitionStatusUnknown, _D3COLD_LAST_TRANSITION_STATUS, kernel.d3cold_last_transition_status, wdm/D3COLD_LAST_TRANSITION_STATUS, wdm/LastDStateTransitionD3cold, wdm/LastDStateTransitionD3hot, wdm/LastDStateTransitionStatusUnknown"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Windows
req.target-min-winverclnt: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Wdm.h
api_name:
-	D3COLD_LAST_TRANSITION_STATUS
product: Windows
targetos: Windows
req.typenames: D3COLD_LAST_TRANSITION_STATUS, *PD3COLD_LAST_TRANSITION_STATUS
req.product: Windows 10 or later.
---

# _D3COLD_LAST_TRANSITION_STATUS Enumeration
The <b>D3COLD_LAST_TRANSITION_STATUS</b> enumeration indicates whether the most recent transition to the D3hot device power state was followed by a transition to the D3cold device power state.

## Syntax
```
typedef enum _D3COLD_LAST_TRANSITION_STATUS {
  LastDStateTransitionStatusUnknown  ,
  LastDStateTransitionD3hot          ,
  LastDStateTransitionD3cold
} *PD3COLD_LAST_TRANSITION_STATUS, D3COLD_LAST_TRANSITION_STATUS;
```

## Constants

<table>
            
                <tr>
                    <td>LastDStateTransitionStatusUnknown</td>
                    <td>Information is not available from the bus driver or platform firmware about whether the most recent transition to D3hot was followed by a transition to D3cold.</td>
                </tr>
            
                <tr>
                    <td>LastDStateTransitionD3hot</td>
                    <td>The most recent transition to the D3hot device power state was not followed by a transition to the D3cold device power state.</td>
                </tr>
            
                <tr>
                    <td>LastDStateTransitionD3cold</td>
                    <td>The most recent transition to the D3hot device power state was followed by a transition to the D3cold device power state.</td>
                </tr>
</table>

## Remarks

The <i>LastTransitionStatus</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967713">GetLastTransitionStatus</a> routine is a pointer to a variable of type <b>D3COLD_LAST_TRANSITION_STATUS</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh967713">GetLastTransitionStatus</a>