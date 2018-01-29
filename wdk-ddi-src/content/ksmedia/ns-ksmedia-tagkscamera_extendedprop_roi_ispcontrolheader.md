---
UID : NS:ksmedia.tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER
title : tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER
author : windows-driver-content
description : This structure contains the header information for ROI ISP controls.
old-location : stream\kscamera_extendedprop_roi_ispcontrolheader.htm
old-project : stream
ms.assetid : F57B0E44-A6A1-4C43-83EE-8DF4A605C0D0
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER, ksmedia/PKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER, ksmedia/KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER, PKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER structure pointer [Streaming Media Devices], stream.kscamera_extendedprop_roi_ispcontrolheader, KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER structure [Streaming Media Devices], PKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER, tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER, *PKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ksmedia.h
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
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER, KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER"
---

# tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER structure
This structure contains the header information for ROI ISP controls.

## Syntax
````
typedef struct tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER {
  ULONG     Size;
  ULONG     ControlCount;
  ULONGLONG Reserved;
} KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER, *PKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER;
````

## Members


`ControlCount`

The number of ISP controls. If this value is 0, the ROI control will remove all ROIs previously configured. This effectively clears up all ROIs configured and resets the driver to the default ROI.

`Reserved`

Reserved for future use.

`Size`

The sum of this structure size, all <a href="..\ksmedia\ns-ksmedia-tagkscamera_extendedprop_roi_ispcontrol.md">KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL</a> structures, and all KSCAMERA_EXTENDEDPROP_ROI_RECTINFO structures that follow


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksmedia.h |