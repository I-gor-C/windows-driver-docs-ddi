---
UID: NE:d3dkmddi._DXGK_PROTECTED_SESSION_STATUS
title: "_DXGK_PROTECTED_SESSION_STATUS"
author: windows-driver-content
description: Used to indicate the status of the current session.
old-location: display\dxgk_protected_session_status.htm
old-project: display
ms.assetid: B6FCA052-FFAE-4F7D-8BDE-CDB84772B5E5
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_PROTECTED_SESSION_STATUS, DXGK_PROTECTED_SESSION_STATUS enumeration [Display Devices], DXGK_PROTECTED_SESSION_STATUS_INVALID, DXGK_PROTECTED_SESSION_STATUS_OK, _DXGK_PROTECTED_SESSION_STATUS, d3dkmddi/DXGK_PROTECTED_SESSION_STATUS, d3dkmddi/DXGK_PROTECTED_SESSION_STATUS_INVALID, d3dkmddi/DXGK_PROTECTED_SESSION_STATUS_OK, display.dxgk_protected_session_status
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
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
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_PROTECTED_SESSION_STATUS
product:
- Windows
targetos: Windows
req.typenames: DXGK_PROTECTED_SESSION_STATUS
---

# _DXGK_PROTECTED_SESSION_STATUS Enumeration
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

Used to indicate the status of the current session.

## Syntax
```
typedef enum _DXGK_PROTECTED_SESSION_STATUS {
  DXGK_PROTECTED_SESSION_STATUS_OK       ,
  DXGK_PROTECTED_SESSION_STATUS_INVALID
} DXGK_PROTECTED_SESSION_STATUS;
```

## Constants

<table>
            
                <tr>
                    <td>DXGK_PROTECTED_SESSION_STATUS_OK</td>
                    <td>Indicates that the status is okay.</td>
                </tr>
            
                <tr>
                    <td>DXGK_PROTECTED_SESSION_STATUS_INVALID</td>
                    <td>Indicates that the status is invalid.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |