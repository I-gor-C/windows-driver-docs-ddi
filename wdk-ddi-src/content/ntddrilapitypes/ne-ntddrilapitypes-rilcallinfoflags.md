---
UID: NE:ntddrilapitypes.RILCALLINFOFLAGS
title: RILCALLINFOFLAGS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallinfoflags.htm
old-project: netvista
ms.assetid: c4edec8f-a001-491b-a3e6-03d19ac94f18
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: RILCALLINFOFLAGS, RILCALLINFOFLAGS enumeration [Network Drivers Starting with Windows Vista], RILCALLINFO_FLAG_ALIENCALL, RILCALLINFO_FLAG_EMERGENCYCALL, netvista.rilcallinfoflags, ntddrilapitypes/RILCALLINFOFLAGS, ntddrilapitypes/RILCALLINFO_FLAG_ALIENCALL, ntddrilapitypes/RILCALLINFO_FLAG_EMERGENCYCALL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: Rilapitypes.h
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
-	ntddrilapitypes.h
api_name:
-	RILCALLINFOFLAGS
product: Windows
targetos: Windows
req.typenames: RILCALLINFOFLAGS
---

# RILCALLINFOFLAGS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLINFOFLAGS { 
  RILCALLINFO_FLAG_ALIENCALL,
  RILCALLINFO_FLAG_EMERGENCYCALL
} RILCALLINFOFLAGS;
````

## Constants

<table>
            
                <tr>
                    <td>RILCALLINFO_FLAG_NONE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RILCALLINFO_FLAG_ALIENCALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RILCALLINFO_FLAG_EMERGENCYCALL</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h) |