---
UID : NS:ksmedia.tagKSCAMERA_EXTENDEDPROP_ROI_INFO
title : tagKSCAMERA_EXTENDEDPROP_ROI_INFO
author : windows-driver-content
description : This structure contains information about an ROI.
old-location : stream\kscamera_extendedprop_roi_info.htm
old-project : stream
ms.assetid : DAE013B7-7715-4B03-99F7-807306736C14
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : tagKSCAMERA_EXTENDEDPROP_ROI_INFO, KSCAMERA_EXTENDEDPROP_ROI_INFO, *PKSCAMERA_EXTENDEDPROP_ROI_INFO
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
req.alt-api : KSCAMERA_EXTENDEDPROP_ROI_INFO
req.alt-loc : Ksmedia.h
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
req.typenames : KSCAMERA_EXTENDEDPROP_ROI_INFO, *PKSCAMERA_EXTENDEDPROP_ROI_INFO
---

# tagKSCAMERA_EXTENDEDPROP_ROI_INFO structure
This structure contains information about an ROI.

## Syntax
````
typedef struct tagKSCAMERA_EXTENDEDPROP_ROI_INFO {
  RECT      Region;
  ULONGLONG Flags;
  LONG      Weight;
  LONG      RegionOfInterestType;
} KSCAMERA_EXTENDEDPROP_ROI_INFO, *PKSCAMERA_EXTENDEDPROP_ROI_INFO;
````

## Members

        
            `Flags`

            These are VIDEOPROCFLAG flags that indicate the op mode for the ISP control. For focus ROI, the default value is 0 representing focus region configuration without initiating a focus.
        
            `Region`

            These are the relative coordinates in Q13 format on the frame that face detection is running.
        
            `RegionOfInterestType`

            If the region is a face, this value is KSCAMERA_EXTENDEDPROP_ROITYPE_FACE. If the region is anything other than face, this value is KSCAMERA_EXTENDEDPROP_ROITYPE_UNKNOWN. For more information, see the <a href="..\ksmedia\ne-ksmedia-kscamera_extendedprop_roitype.md">KSCAMERA_EXTENDEDPROP_ROITYPE</a> enumeration.
        
            `Weight`

            This is the weight of the region (0-100).


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksmedia.h |