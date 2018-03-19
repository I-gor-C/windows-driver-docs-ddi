---
UID: NE:iddcx.IDDCX_PATH_FLAGS
title: IDDCX_PATH_FLAGS
author: windows-driver-content
description: Indicates the state of the path.
old-location: display\iddcx_path_flags.htm
old-project: display
ms.assetid: f7a9b20a-753c-487d-a2d5-3e1c08317519
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IDDCX_PATH_FLAGS, IDDCX_PATH_FLAGS enumeration [Display Devices], IDDCX_PATH_FLAGS_ACTIVE, IDDCX_PATH_FLAGS_CHANGED, IDDCX_PATH_FLAGS_NONE, display.iddcx_path_flags, iddcx/IDDCX_PATH_FLAGS, iddcx/IDDCX_PATH_FLAGS_ACTIVE, iddcx/IDDCX_PATH_FLAGS_CHANGED, iddcx/IDDCX_PATH_FLAGS_NONE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: iddcx.h
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
req.irql: "_requires_same_"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	iddcx.h
api_name:
-	IDDCX_PATH_FLAGS
product: Windows
targetos: Windows
req.typenames: 
---

# IDDCX_PATH_FLAGS Enumeration
Indicates the state of the path.

## Syntax
````
typedef enum _IDDCX_PATH_FLAGS { 
  IDDCX_PATH_FLAGS_NONE     = 0,
  IDDCX_PATH_FLAGS_CHANGED  = 1,
  IDDCX_PATH_FLAGS_ACTIVE   = 2
} IDDCX_PATH_FLAGS;
````

## Constants

<table>
            
                <tr>
                    <td>IDDCX_PATH_FLAGS_NONE</td>
                    <td>Indicates that the path is not active and has not changed.</td>
                </tr>
            
                <tr>
                    <td>IDDCX_PATH_FLAGS_CHANGED</td>
                    <td>Indicates if this path has changed</td>
                </tr>
            
                <tr>
                    <td>IDDCX_PATH_FLAGS_ACTIVE</td>
                    <td>Indicates if this path is active</td>
                </tr>
            
                <tr>
                    <td>UINT</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | iddcx.h |