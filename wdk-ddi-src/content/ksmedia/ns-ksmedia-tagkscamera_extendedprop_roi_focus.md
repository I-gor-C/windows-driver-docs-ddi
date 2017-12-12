---
UID: NS.KSMEDIA.TAGKSCAMERA_EXTENDEDPROP_ROI_FOCUS
title: tagKSCAMERA_EXTENDEDPROP_ROI_FOCUS
author: windows-driver-content
description: This structure contains the ROI info structure for focus.
old-location: stream\kscamera_extendedprop_roi_focus.htm
old-project: stream
ms.assetid: 448A62D1-34D6-46EC-ADA4-9C9F832E2BDD
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: tagKSCAMERA_EXTENDEDPROP_ROI_FOCUS, KSCAMERA_EXTENDEDPROP_ROI_FOCUS, *PKSCAMERA_EXTENDEDPROP_ROI_FOCUS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_EXTENDEDPROP_ROI_FOCUS
req.alt-loc: Ksmedia.h
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
---

# tagKSCAMERA_EXTENDEDPROP_ROI_FOCUS structure



## -description
This structure contains the ROI info structure for focus.



## -syntax

````
typedef struct tagKSCAMERA_EXTENDEDPROP_ROI_FOCUS {
  KSCAMERA_EXTENDEDPROP_ROI_INFO ROIInfo;
  ULONGLONG                      Reserved;
} KSCAMERA_EXTENDEDPROP_ROI_FOCUS, *PKSCAMERA_EXTENDEDPROP_ROI_FOCUS;
````


## -struct-fields

### -field ROIInfo

See the <a href="stream.kscamera_extendedprop_roi_info">KSCAMERA_EXTENDEDPROP_ROI_INFO</a> structure for more information.


### -field Reserved

Reserved for future use.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>