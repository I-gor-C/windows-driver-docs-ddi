---
UID: NS:wudfwdm._PO_FX_PERF_STATE_CHANGE
title: "_PO_FX_PERF_STATE_CHANGE"
author: windows-driver-content
description: The PO_FX_PERF_STATE_CHANGE structure contains information about a change to a performance state that is being requested by calling the PoFxIssueComponentPerfStateChange or PoFxIssueComponentPerfStateChangeMultiple routine.
old-location: kernel\po_fx_perf_state_change.htm
old-project: kernel
ms.assetid: AE7A79DE-0202-4816-A36C-5A15C4539392
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*PPO_FX_PERF_STATE_CHANGE, PO_FX_PERF_STATE_CHANGE, PO_FX_PERF_STATE_CHANGE structure [Kernel-Mode Driver Architecture], PPO_FX_PERF_STATE_CHANGE, PPO_FX_PERF_STATE_CHANGE structure pointer [Kernel-Mode Driver Architecture], _PO_FX_PERF_STATE_CHANGE, kernel.po_fx_perf_state_change, wdm/PO_FX_PERF_STATE_CHANGE, wdm/PPO_FX_PERF_STATE_CHANGE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wudfwdm.h
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
req.irql: Any level (see Remarks section)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Wdm.h
api_name:
-	PO_FX_PERF_STATE_CHANGE
product: Windows
targetos: Windows
req.typenames: PO_FX_PERF_STATE_CHANGE, *PPO_FX_PERF_STATE_CHANGE
req.product: Windows 10 or later.
---

# _PO_FX_PERF_STATE_CHANGE structure
The <b>PO_FX_PERF_STATE_CHANGE</b> structure contains information about a change to a performance state that is being requested by calling the <a href="..\wdm\nf-wdm-pofxissuecomponentperfstatechange.md">PoFxIssueComponentPerfStateChange</a> or <a href="..\wdm\nf-wdm-pofxissuecomponentperfstatechangemultiple.md">PoFxIssueComponentPerfStateChangeMultiple</a> routine.

## Syntax
````
typedef struct _PO_FX_PERF_STATE_CHANGE {
  ULONG Set;
  union {
    ULONG     StateIndex;
    ULONGLONG StateValue;
  };
} PO_FX_PERF_STATE_CHANGE, *PPO_FX_PERF_STATE_CHANGE;
````

## Members


`Set`

The index of the performance state set that is being changed within the collection of performance state sets for the component.

## Remarks
The <b>PO_FX_PERF_STATE_CHANGE</b> structure is used for the <i>PerfChange</i> parameter of the <a href="..\wdm\nf-wdm-pofxissuecomponentperfstatechange.md">PoFxIssueComponentPerfStateChange</a> routine and the  <i>PerfChanges</i> parameter of the <a href="..\wdm\nf-wdm-pofxissuecomponentperfstatechangemultiple.md">PoFxIssueComponentPerfStateChangeMultiple</a> routine.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | wudfwdm.h (include Wudfwdm.h) |

## See Also

<a href="https://msdn.microsoft.com/D5341D6D-7C71-43CB-9C70-7E939B32C33F">Device Performance State Management</a>



<a href="..\wdm\nf-wdm-pofxissuecomponentperfstatechange.md">PoFxIssueComponentPerfStateChange</a>



<a href="..\wdm\nf-wdm-pofxissuecomponentperfstatechangemultiple.md">PoFxIssueComponentPerfStateChangeMultiple</a>