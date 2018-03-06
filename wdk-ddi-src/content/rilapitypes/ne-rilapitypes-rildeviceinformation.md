---
UID: NE:rilapitypes.RILDEVICEINFORMATION
title: RILDEVICEINFORMATION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildeviceinformation_2.htm
old-project: netvista
ms.assetid: a67a637e-92ac-4a42-bfef-8a42ce26b9b3
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: RILDEVICEINFORMATION, RILDEVICEINFORMATION enumeration [Network Drivers Starting with Windows Vista], RIL_DEVICEINFO_ARG_LARGEST, RIL_DEVICEINFO_ARG_SMALLEST, RIL_DEVICEINFO_MAX, RIL_DEVICEINFO_MIN, RIL_DEVICEINFO_MODEL, RIL_DEVICEINFO_REVISION, RIL_DEVICEINFO_SERIALNUMBER_CDMA, RIL_DEVICEINFO_SERIALNUMBER_GW, netvista.rildeviceinformation_2, rilapitypes/RILDEVICEINFORMATION, rilapitypes/RIL_DEVICEINFO_ARG_LARGEST, rilapitypes/RIL_DEVICEINFO_ARG_SMALLEST, rilapitypes/RIL_DEVICEINFO_MAX, rilapitypes/RIL_DEVICEINFO_MIN, rilapitypes/RIL_DEVICEINFO_MODEL, rilapitypes/RIL_DEVICEINFO_REVISION, rilapitypes/RIL_DEVICEINFO_SERIALNUMBER_CDMA, rilapitypes/RIL_DEVICEINFO_SERIALNUMBER_GW
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	rilapitypes.h
api_name:
-	RILDEVICEINFORMATION
product: Windows
targetos: Windows
req.typenames: RILDEVICEINFORMATION
req.product: Windows 10 or later.
---

# RILDEVICEINFORMATION Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
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

## Constants

<table>
            
                <tr>
                    <td>RIL_DEVICEINFO_ARG_LARGEST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_ARG_SMALLEST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_MANUFACTURER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_MIN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_MODEL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_REVISION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_SERIALNUMBER_CDMA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_SERIALNUMBER_GW</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |