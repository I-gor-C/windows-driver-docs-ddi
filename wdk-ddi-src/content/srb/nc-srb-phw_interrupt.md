---
UID: NC:srb.PHW_INTERRUPT
title: PHW_INTERRUPT
author: windows-driver-content
description: The PHW_INTERRUPT routine prototype declares the miniport driver's interrupt handler routine.
old-location: storage\phw_interrupt.htm
old-project: storage
ms.assetid: d61892c6-f6ca-4077-909e-a21076375e5a
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "(*PHW_INTERRUPT), (*PHW_INTERRUPT) callback function [Storage Devices], ide_minikr_d0fa2a3d-deef-45c5-9251-a3c30c7af434.xml, srb/(*PHW_INTERRUPT), storage.phw_interrupt"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: srb.h
req.include-header: Storport.h, Srb.h, Storport.h
req.target-type: Desktop
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	srb.h
api_name:
-	(*PHW_INTERRUPT)
product: Windows
targetos: Windows
req.typenames: SPB_CONTROLLER_CONFIG, *PSPB_CONTROLLER_CONFIG
req.product: Windows 10 or later.
---


# PHW_INTERRUPT callback function
The PHW_INTERRUPT routine prototype declares the miniport driver's interrupt handler routine.

## Syntax

```
PHW_INTERRUPT PhwInterrupt;

BOOLEAN PhwInterrupt(
  PVOID DeviceExtension
)
{...}
```

## Parameters

`DeviceExtension`

Pointer to the miniport driver's per-HBA storage area.


## Return Value

If the interrupt handler routine determines that its HBA generated the interrupt, it returns <b>TRUE</b>. If the interrupt handler determines that its HBA did not generate the interrupt, it should return <b>FALSE</b> as soon as possible.

## Remarks

The interrupt handler routine for both SCSI and StorPort miniport drivers are declared using this prototype. 

For more information about the SCSI miniport driver's interrupt handler routine see <a href="..\strmini\nc-strmini-phw_interrupt.md">HwScsiInterrupt</a>. 

For more information about the miniport driver's interrupt handler routine that is used with the StorPort driver see <a href="..\storport\nc-storport-hw_interrupt.md">HwStorInterrupt</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | srb.h (include Storport.h, Srb.h, Storport.h) |

## See Also

<a href="..\strmini\nc-strmini-phw_interrupt.md">HwScsiInterrupt</a>



<a href="..\storport\nc-storport-hw_interrupt.md">HwStorInterrupt</a>