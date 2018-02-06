---
UID: NE:rilapitypes.RILPHONEBOOKENTRYPARAMMASK
title: RILPHONEBOOKENTRYPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebookentryparammask_2.htm
old-project: netvista
ms.assetid: c7c82022-b82d-4f8e-a736-3912d3286189
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: rilapitypes/RIL_PARAM_PBE_ADDITIONALNUMCOUNT, RIL_PARAM_PBE_ADDITIONALNUMSIZE, RIL_PARAM_PBE_EMAILOFFSET, RIL_PARAM_PBE_GROUPIDCOUNT, RIL_PARAM_PBE_ADDITIONALNUMCOUNT, rilapitypes/RIL_PARAM_PBE_TEXT, RIL_PARAM_PBE_ADDRESS, rilapitypes/RILPHONEBOOKENTRYPARAMMASK, rilapitypes/RIL_PARAM_PBE_ADDITIONALNUMSIZE, RIL_PARAM_PBE_EMAILSIZE, RILPHONEBOOKENTRYPARAMMASK enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_PARAM_PBE_SECONDNAME, rilapitypes/RIL_PARAM_PBE_EMAILOFFSET, rilapitypes/RIL_PARAM_PBE_GROUPID, rilapitypes/RIL_PARAM_PBE_ADDRESS, RIL_PARAM_PBE_TEXT, rilapitypes/RIL_PARAM_PBE_ADDITIONALNUMOFFSET, rilapitypes/RIL_PARAM_PBE_ALL, RIL_PARAM_PBE_ALL, RIL_PARAM_PBE_EMAILCOUNT, rilapitypes/RIL_PARAM_PBE_EMAILSIZE, rilapitypes/RIL_PARAM_PBE_EMAILCOUNT, RIL_PARAM_PBE_SECONDNAME, rilapitypes/RIL_PARAM_PBE_GROUPIDCOUNT, RIL_PARAM_PBE_GROUPID, RILPHONEBOOKENTRYPARAMMASK, netvista.rilphonebookentryparammask_2, RIL_PARAM_PBE_ADDITIONALNUMOFFSET
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	rilapitypes.h
apiname:
-	RILPHONEBOOKENTRYPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILPHONEBOOKENTRYPARAMMASK
req.product: Windows 10 or later.
---

# RILPHONEBOOKENTRYPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPHONEBOOKENTRYPARAMMASK { 
  RIL_PARAM_PBE_ADDRESS,
  RIL_PARAM_PBE_TEXT,
  RIL_PARAM_PBE_SECONDNAME,
  RIL_PARAM_PBE_GROUPIDCOUNT,
  RIL_PARAM_PBE_GROUPID,
  RIL_PARAM_PBE_ADDITIONALNUMCOUNT,
  RIL_PARAM_PBE_ADDITIONALNUMSIZE,
  RIL_PARAM_PBE_ADDITIONALNUMOFFSET,
  RIL_PARAM_PBE_EMAILCOUNT,
  RIL_PARAM_PBE_EMAILSIZE,
  RIL_PARAM_PBE_EMAILOFFSET,
  RIL_PARAM_PBE_ALL
} RILPHONEBOOKENTRYPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_PBE_ADDITIONALNUMCOUNT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBE_ADDITIONALNUMOFFSET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBE_ADDITIONALNUMSIZE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBE_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBE_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBE_EMAILCOUNT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBE_EMAILOFFSET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBE_EMAILSIZE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBE_GROUPID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBE_GROUPIDCOUNT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBE_INDEX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBE_SECONDNAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBE_TEXT</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |