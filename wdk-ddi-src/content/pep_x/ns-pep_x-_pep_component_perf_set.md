---
UID: NS:pep_x._PEP_COMPONENT_PERF_SET
title: "_PEP_COMPONENT_PERF_SET"
author: windows-driver-content
description: The PEP_COMPONENT_PERF_SET structure describes the performance states (P-states) in a P-state set.
old-location: kernel\pep_component_perf_set.htm
old-project: kernel
ms.assetid: E4EB8052-545C-46AE-A879-1F216B7FD20B
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: "*PPEP_COMPONENT_PERF_SET, PEP_COMPONENT_PERF_SET, PEP_COMPONENT_PERF_SET structure [Kernel-Mode Driver Architecture], PPEP_COMPONENT_PERF_SET, PPEP_COMPONENT_PERF_SET structure pointer [Kernel-Mode Driver Architecture], _PEP_COMPONENT_PERF_SET, kernel.pep_component_perf_set, pepfx/PEP_COMPONENT_PERF_SET, pepfx/PPEP_COMPONENT_PERF_SET"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pep_x.h
req.include-header: Pep_x.h
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
-	pepfx.h
api_name:
-	PEP_COMPONENT_PERF_SET
product: Windows
targetos: Windows
req.typenames: PEP_COMPONENT_PERF_SET, *PPEP_COMPONENT_PERF_SET, PEP_COMPONENT_PERF_SET, *PPEP_COMPONENT_PERF_SET
---

# _PEP_COMPONENT_PERF_SET structure
The <b>PEP_COMPONENT_PERF_SET</b> structure describes the performance states (P-states) in a P-state set.

## Syntax
````
typedef struct _PEP_COMPONENT_PERF_SET {
  UNICODE_STRING      Name;
  ULONGLONG           Flags;
  PEP_PERF_STATE_UNIT Unit;
  PEP_PERF_STATE_TYPE Type;
  union {
    struct {
      ULONG           Count;
      PPEP_PERF_STATE States;
    } Discrete;
    struct {
      ULONGLONG Minimum;
      ULONGLONG Maximum;
    } Range;
  };
} PEP_COMPONENT_PERF_SET, *PPEP_COMPONENT_PERF_SET;
````

## Members


`Name`

An optional string that describes the device property controlled by this P-state set.  For example, this string might be "Clock frequency" or "Memory bandwidth". If no such string is available for this P-state, the <b>Name</b> member is set to NULL. Otherwise, this member contains a pointer to a <a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a> structure that contains the string.

`Flags`

Set to zero. No flag bits are currently defined for this member.

`Unit`

A <a href="..\pepfx\ne-pepfx-_pep_perf_state_unit.md">PEP_PERF_STATE_UNIT</a> structure that specifies the units in which the performance values for this P-state set are expressed. Component performance can be expressed in hertz (frequency) or in bits per second (bandwidth).

`Type`

A <a href="..\pepfx\ne-pepfx-_pep_perf_state_type.md">PEP_PERF_STATE_TYPE</a> enumeration value that indicates the type of performance information that is specified for this component. This member indicates whether the performance values for this P-state set are specified as a list of discrete values or as a continuous range of values.

## Remarks
The <b>PerfStateSets</b> member of the <a href="..\pepfx\ns-pepfx-_pep_component_perf_info.md">PEP_COMPONENT_PERF_INFO</a> is the first element in an array of <b>PEP_COMPONENT_PERF_SET</b> structures. All members of the <b>PEP_COMPONENT_PERF_SET</b> structure contain input values that are supplied by the Windows <a href="https://msdn.microsoft.com/B08F8ABF-FD43-434C-A345-337FBB799D9B">power management framework</a> (PoFx). The platform extension plug-in (PEP) must not write to this structure.

Device drivers use the <a href="..\wudfwdm\ns-wudfwdm-_po_fx_component_perf_set.md">PO_FX_COMPONENT_PERF_SET</a> structure, which is similar to the <b>PEP_COMPONENT_PERF_SET</b> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | pep_x.h (include Pep_x.h) |

## See Also

<a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a>



<a href="..\pepfx\ns-pepfx-_pep_perf_state.md">PEP_PERF_STATE</a>



<a href="..\wudfwdm\ns-wudfwdm-_po_fx_component_perf_set.md">PO_FX_COMPONENT_PERF_SET</a>



<a href="..\pepfx\ne-pepfx-_pep_perf_state_type.md">PEP_PERF_STATE_TYPE</a>



<a href="..\pepfx\ns-pepfx-_pep_component_perf_info.md">PEP_COMPONENT_PERF_INFO</a>



<a href="..\pepfx\ne-pepfx-_pep_perf_state_unit.md">PEP_PERF_STATE_UNIT</a>