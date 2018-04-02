---
UID: NC:iddcx.EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP
title: EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP
author: windows-driver-content
description: EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP is called by the OS to set a gamma ramp on the specified monitor.
old-location: display\evt_idd_cx_monitor_set_gamma_ramp.htm
old-project: display
ms.assetid: 3e0828ee-307a-48fd-a8ea-b469ac6214d0
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP, EvtIddCxMonitorSetGammaRamp, EvtIddCxMonitorSetGammaRamp callback function [Display Devices], PFN_IDD_CX_MONITOR_SET_GAMMA_RAMP, PFN_IDD_CX_MONITOR_SET_GAMMA_RAMP callback function pointer [Display Devices], display.evt_idd_cx_monitor_set_gamma_ramp, iddcx/EvtIddCxMonitorSetGammaRamp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
req.irql: "_requires_same_"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	iddcx.h
api_name:
-	PFN_IDD_CX_MONITOR_SET_GAMMA_RAMP
product:
- Windows
targetos: Windows
req.typenames: WCS_PROFILE_MANAGEMENT_SCOPE
---


# EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP callback function
<b>EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP</b> is called by the OS to set a gamma ramp on the specified monitor.

## Syntax

```
EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP EvtIddCxMonitorSetGammaRamp;

_IRQL_requires_same_ NTSTATUS EvtIddCxMonitorSetGammaRamp(
  IDDCX_MONITOR MonitorObject,
  const IDARG_IN_SET_GAMMARAMP *pInArgs
)
{...}
```

## Parameters

`MonitorObject`

A handle by the OS to identify the monitor to set a gamma ramp for.

`pInArgs`

Input arguments used by <b>EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP</b>.


## Return Value

(NTSTATUS) If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise, an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | iddcx.h |
| **IRQL** | "_requires_same_" |