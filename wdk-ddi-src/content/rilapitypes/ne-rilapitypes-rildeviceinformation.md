---
UID: NE.rilapitypes.RILDEVICEINFORMATION
title: RILDEVICEINFORMATION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildeviceinformation_2.htm
old-project: netvista
ms.assetid: a67a637e-92ac-4a42-bfef-8a42ce26b9b3
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: RILDEVICEINFORMATION, RILDEVICEINFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILDEVICEINFORMATION
req.alt-loc: rilapitypes.h
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
req.product: Windows 10 or later.
---

# RILDEVICEINFORMATION enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef enum _RILDEVICEINFORMATION { 
  RIL_DEVICEINFO_MODEL,
  RIL_DEVICEINFO_REVISION,
  RIL_DEVICEINFO_SERIALNUMBER_GW,
  RIL_DEVICEINFO_SERIALNUMBER_CDMA,
  RIL_DEVICEINFO_ARG_SMALLEST,
  RIL_DEVICEINFO_ARG_LARGEST,
  RIL_DEVICEINFO_MIN,
  RIL_DEVICEINFO_MAX
} RILDEVICEINFORMATION;
````


## -enum-fields

### -field RIL_DEVICEINFO_MODEL


### -field RIL_DEVICEINFO_REVISION


### -field RIL_DEVICEINFO_SERIALNUMBER_GW


### -field RIL_DEVICEINFO_SERIALNUMBER_CDMA


### -field RIL_DEVICEINFO_ARG_SMALLEST


### -field RIL_DEVICEINFO_ARG_LARGEST


### -field RIL_DEVICEINFO_MIN


### -field RIL_DEVICEINFO_MAX


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>