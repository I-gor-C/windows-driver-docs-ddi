---
UID : NS:d3dkmddi._DXGKARG_DISPLAYDETECTCONTROL
title : _DXGKARG_DISPLAYDETECTCONTROL
author : windows-driver-content
description : Used to hold the arguments for DXGKDDI_DISPLAYDETECTCONTROL.
old-location : display\dxgkarg_displaydetectcontrol.htm
old-project : display
ms.assetid : A0B5798E-FF4D-4133-BFA9-39B37CC387F6
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : DXGKARG_DISPLAYDETECTCONTROL, PDXGKARG_DISPLAYDETECTCONTROL, display.dxgkarg_displaydetectcontrol, DXGKARG_DISPLAYDETECTCONTROL structure [Display Devices], d3dkmddi/DXGKARG_DISPLAYDETECTCONTROL, d3dkmddi/PDXGKARG_DISPLAYDETECTCONTROL, _DXGKARG_DISPLAYDETECTCONTROL, PDXGKARG_DISPLAYDETECTCONTROL structure pointer [Display Devices]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DXGKARG_DISPLAYDETECTCONTROL
---

# _DXGKARG_DISPLAYDETECTCONTROL structure
Used to hold the arguments for <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_displaydetectcontrol.md">DXGKDDI_DISPLAYDETECTCONTROL</a>.

## Syntax
````
typedef struct _DXGKARG_DISPLAYDETECTCONTROL {
  D3DDDI_VIDEO_PRESENT_TARGET_ID TargetID  :24;
  DXGK_DISPLAYDETECTCONTROLTYPE  Type  :4;
  UINT                           NonDestructiveOnly  :1;
  UINT                           Reserved  :3;
} DXGKARG_DISPLAYDETECTCONTROL, *PDXGKARG_DISPLAYDETECTCONTROL;
````

## Members


`NonDestructiveOnly`

Only used for polling the types of requests.
If TRUE, the driver should attempt to poll the specified target(s) without causing any visual artifacts. 
If FALSE, the driver should perform any action necessary to detect the status of the specified target(s) even if it would cause visual artifacts on the target(s) in question or other targets.

`Reserved`

This value is reserved for system use.

`TargetId`



`Type`

Detection action type requested.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h |