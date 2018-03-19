---
UID: NS:pepfx._PEP_PPM_QUERY_VETO_REASONS
title: "_PEP_PPM_QUERY_VETO_REASONS"
author: windows-driver-content
description: The PEP_PPM_QUERY_VETO_REASONS structure specifies the total number of veto reasons that the PEP uses in calls to the ProcessorIdleVeto and PlatformIdleVeto routines.
old-location: kernel\pep_ppm_query_veto_reasons.htm
old-project: kernel
ms.assetid: 59D0D139-00E4-4EEE-A326-0A2979B2085B
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: "*PPEP_PPM_QUERY_VETO_REASONS, PEP_PPM_QUERY_VETO_REASONS, PEP_PPM_QUERY_VETO_REASONS structure [Kernel-Mode Driver Architecture], PPEP_PPM_QUERY_VETO_REASONS, PPEP_PPM_QUERY_VETO_REASONS structure pointer [Kernel-Mode Driver Architecture], _PEP_PPM_QUERY_VETO_REASONS, kernel.pep_ppm_query_veto_reasons, pepfx/PEP_PPM_QUERY_VETO_REASONS, pepfx/PPEP_PPM_QUERY_VETO_REASONS"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
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
-	PEP_PPM_QUERY_VETO_REASONS
product: Windows
targetos: Windows
req.typenames: PEP_PPM_QUERY_VETO_REASONS, *PPEP_PPM_QUERY_VETO_REASONS
---

# _PEP_PPM_QUERY_VETO_REASONS structure
The <b>PEP_PPM_QUERY_VETO_REASONS</b> structure specifies the total number of veto reasons that the PEP uses in calls to the <a href="..\pepfx\nc-pepfx-pofxcallbackprocessoridleveto.md">ProcessorIdleVeto</a> and <a href="..\pepfx\nc-pepfx-pofxcallbackplatformidleveto.md">PlatformIdleVeto</a> routines.

## Syntax
````
typedef struct _PEP_PPM_QUERY_VETO_REASONS {
  ULONG VetoReasonCount;
} PEP_PPM_QUERY_VETO_REASONS, *PPEP_PPM_QUERY_VETO_REASONS;
````

## Members


`VetoReasonCount`

[out] The number of veto codes used by the PEP.

## Remarks
This structure is used by the <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186829">PEP_NOTIFY_PPM_QUERY_VETO_REASONS</a> notification. The <b>VetoReasonCount</b> member contains an output value that the PEP writes to this member in response to the notification.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | pepfx.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186829">PEP_NOTIFY_PPM_QUERY_VETO_REASONS</a>