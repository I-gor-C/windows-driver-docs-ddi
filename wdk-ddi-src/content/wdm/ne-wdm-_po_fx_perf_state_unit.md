---
UID: NE:wdm._PO_FX_PERF_STATE_UNIT
title: "_PO_FX_PERF_STATE_UNIT"
author: windows-driver-content
description: The PO_FX_PERF_STATE_UNIT enumeration contains values that describe the type of unit that is controlled by the performance states in a PO_FX_COMPONENT_PERF_SET.
old-location: kernel\po_fx_perf_state_unit.htm
old-project: kernel
ms.assetid: E16657AE-9EEF-4E36-AAC5-5BF822006F1C
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PPO_FX_PERF_STATE_UNIT, PO_FX_PERF_STATE_UNIT, PO_FX_PERF_STATE_UNIT enumeration [Kernel-Mode Driver Architecture], PPO_FX_PERF_STATE_UNIT, PPO_FX_PERF_STATE_UNIT enumeration pointer [Kernel-Mode Driver Architecture], PoFxPerfStateUnitBandwidth, PoFxPerfStateUnitFrequency, PoFxPerfStateUnitMaximum, PoFxPerfStateUnitOther, _PO_FX_PERF_STATE_UNIT, kernel.po_fx_perf_state_unit, wdm/PO_FX_PERF_STATE_UNIT, wdm/PPO_FX_PERF_STATE_UNIT, wdm/PoFxPerfStateUnitBandwidth, wdm/PoFxPerfStateUnitFrequency, wdm/PoFxPerfStateUnitMaximum, wdm/PoFxPerfStateUnitOther"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wudfwdm.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
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
-	PO_FX_PERF_STATE_UNIT
product: Windows
targetos: Windows
req.typenames: PO_FX_PERF_STATE_UNIT, *PPO_FX_PERF_STATE_UNIT
req.product: Windows 10 or later.
---

# _PO_FX_PERF_STATE_UNIT Enumeration
The <b>PO_FX_PERF_STATE_UNIT</b> enumeration contains values that describe the type of unit that is controlled by the performance states in a <a href="https://msdn.microsoft.com/library/windows/hardware/dn939833">PO_FX_COMPONENT_PERF_SET</a>.

## Syntax
```
typedef enum _PO_FX_PERF_STATE_UNIT {
  PoFxPerfStateUnitOther      ,
  PoFxPerfStateUnitFrequency  ,
  PoFxPerfStateUnitBandwidth  ,
  PoFxPerfStateUnitMaximum
} PO_FX_PERF_STATE_UNIT, *PPO_FX_PERF_STATE_UNIT;
```

## Constants

<table>
            
                <tr>
                    <td>PoFxPerfStateUnitOther</td>
                    <td>Indicates that the performance states control a unit other than frequency or bandwidth.</td>
                </tr>
            
                <tr>
                    <td>PoFxPerfStateUnitFrequency</td>
                    <td>Indicates that the performance states control frequency, measured in Hz.</td>
                </tr>
            
                <tr>
                    <td>PoFxPerfStateUnitBandwidth</td>
                    <td>Indicates that the performance states control bandwidth, measured in bits per second.</td>
                </tr>
            
                <tr>
                    <td>PoFxPerfStateUnitMaximum</td>
                    <td>This value is reserved for system use.</td>
                </tr>
</table>

## Remarks

The <b>Unit</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn939833">PO_FX_COMPONENT_PERF_SET</a> structure is a value from the <b>PO_FX_PERF_STATE_UNIT</b> enumeration.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | wdm.h (include Wudfwdm.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn939833">PO_FX_COMPONENT_PERF_SET</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn939778">PoFxRegisterComponentPerfStates</a>