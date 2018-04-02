---
UID: NE:ucxroothub._TRISTATE
title: "_TRISTATE"
author: windows-driver-content
description: The TRISTATE enumeration indicates generic state values for true or false.
old-location: buses\tristate.htm
old-project: usbref
ms.assetid: 16D8981B-53D3-4886-A85F-B487701ED172
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: TRISTATE, TRISTATE enumeration [Buses], TriStateFalse, TriStateTrue, TriStateUnknown, _TRISTATE, buses.tristate, ucxroothub/TRISTATE, ucxroothub/TriStateFalse, ucxroothub/TriStateTrue, ucxroothub/TriStateUnknown
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ucxroothub.h
req.include-header: Ucxclass.h
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
req.irql: DISPATCH_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ucxroothub.h
api_name:
-	TRISTATE
product:
- Windows
targetos: Windows
req.typenames: TRISTATE
req.product: Windows 10 or later.
---

# _TRISTATE Enumeration
The <b>TRISTATE</b> enumeration indicates generic state values for true or false.

## Syntax
```
typedef enum _TRISTATE {
  TriStateUnknown  ,
  TriStateFalse    ,
  TriStateTrue
} TRISTATE;
```

## Constants

<table>
            
                <tr>
                    <td>TriStateUnknown</td>
                    <td>State is unknown.</td>
                </tr>
            
                <tr>
                    <td>TriStateFalse</td>
                    <td>State is a false boolean value.</td>
                </tr>
            
                <tr>
                    <td>TriStateTrue</td>
                    <td>State is a true boolean value.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ucxroothub.h (include Ucxclass.h) |