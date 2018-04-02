---
UID: NE:rilapitypes.RILADDRESSTYPE
title: RILADDRESSTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riladdresstype_2.htm
old-project: netvista
ms.assetid: de21f647-9372-4572-bf45-581361032911
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: RILADDRESSTYPE, RILADDRESSTYPE enumeration [Network Drivers Starting with Windows Vista], RIL_ADDRTYPE_ABBREV, RIL_ADDRTYPE_ALPHANUM, RIL_ADDRTYPE_EMAIL, RIL_ADDRTYPE_INTERNATIONAL, RIL_ADDRTYPE_IP, RIL_ADDRTYPE_MAX, RIL_ADDRTYPE_NATIONAL, RIL_ADDRTYPE_NETWKSPECIFIC, RIL_ADDRTYPE_SUBSCRIBER, RIL_ADDRTYPE_URI, netvista.riladdresstype_2, rilapitypes/RILADDRESSTYPE, rilapitypes/RIL_ADDRTYPE_ABBREV, rilapitypes/RIL_ADDRTYPE_ALPHANUM, rilapitypes/RIL_ADDRTYPE_EMAIL, rilapitypes/RIL_ADDRTYPE_INTERNATIONAL, rilapitypes/RIL_ADDRTYPE_IP, rilapitypes/RIL_ADDRTYPE_MAX, rilapitypes/RIL_ADDRTYPE_NATIONAL, rilapitypes/RIL_ADDRTYPE_NETWKSPECIFIC, rilapitypes/RIL_ADDRTYPE_SUBSCRIBER, rilapitypes/RIL_ADDRTYPE_URI
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
-	RILADDRESSTYPE
product:
- Windows
targetos: Windows
req.typenames: RILADDRESSTYPE
req.product: Windows 10 or later.
---

# RILADDRESSTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILADDRESSTYPE { 
  RIL_ADDRTYPE_INTERNATIONAL,
  RIL_ADDRTYPE_NATIONAL,
  RIL_ADDRTYPE_NETWKSPECIFIC,
  RIL_ADDRTYPE_SUBSCRIBER,
  RIL_ADDRTYPE_ALPHANUM,
  RIL_ADDRTYPE_ABBREV,
  RIL_ADDRTYPE_IP,
  RIL_ADDRTYPE_EMAIL,
  RIL_ADDRTYPE_URI,
  RIL_ADDRTYPE_MAX
} RILADDRESSTYPE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_ADDRTYPE_UNKNOWN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_ADDRTYPE_INTERNATIONAL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_ADDRTYPE_NATIONAL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_ADDRTYPE_NETWKSPECIFIC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_ADDRTYPE_SUBSCRIBER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_ADDRTYPE_ALPHANUM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_ADDRTYPE_ABBREV</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_ADDRTYPE_IP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_ADDRTYPE_EMAIL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_ADDRTYPE_URI</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_ADDRTYPE_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |