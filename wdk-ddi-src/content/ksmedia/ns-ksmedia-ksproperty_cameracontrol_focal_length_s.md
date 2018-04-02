---
UID: NS:ksmedia.KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S
title: KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S
author: windows-driver-content
description: The KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S structure returns filter-specific data requested using the KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH property.
old-location: stream\ksproperty_cameracontrol_focal_length_s.htm
old-project: stream
ms.assetid: bf236fb9-8aa6-4f80-a8e3-85adfedd1f49
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S, KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S, KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S structure [Streaming Media Devices], PKSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S, PKSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S structure pointer [Streaming Media Devices], ksmedia/KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S, ksmedia/PKSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S, stream.ksproperty_cameracontrol_focal_length_s, vidcapstruct_d3d5d26e-e8be-4ce5-9a9a-03b125134bf7.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ksmedia.h
api_name:
-	KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S
product:
- Windows
targetos: Windows
req.typenames: KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S, *PKSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S
---

# KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S structure
The KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S structure returns filter-specific data requested using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564406">KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH</a> property.

## Syntax
```
typedef struct KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S {
  KSPROPERTY Property;
  LONG       lOcularFocalLength;
  LONG       lObjectiveFocalLengthMin;
  LONG       lObjectiveFocalLengthMax;
} *PKSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S, KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S;
```

## Members


`Property`

Specifies an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> structure that describes the property set, property ID, and request type.

`lOcularFocalLength`

Specifies a value of type LONG containing the focal length of the lens closest to the camera user.

`lObjectiveFocalLengthMin`

Specifies a value of type LONG containing the minimum focal length of the lens closest to the camera subject.

`lObjectiveFocalLengthMax`

Specifies a value of type LONG containing the maximum focal length of the lens closest to the camera subject.

## Remarks
If the camera has only one lens, these values can be used to represent zoom ratios. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff564406">KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksmedia.h (include Ksmedia.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff564406">KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff564418">KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567802">PROPSETID_VIDCAP_CAMERACONTROL</a>