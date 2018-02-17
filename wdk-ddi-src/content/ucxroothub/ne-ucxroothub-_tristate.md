---
UID: NE:ucxroothub._TRISTATE
title: "_TRISTATE"
author: windows-driver-content
description: The TRISTATE enumeration indicates generic state values for true or false.
old-location: buses\tristate.htm
old-project: usbref
ms.assetid: 16D8981B-53D3-4886-A85F-B487701ED172
ms.author: windowsdriverdev
ms.date: 2/8/2018
ms.keywords: TriStateFalse, ucxroothub/TRISTATE, ucxroothub/TriStateUnknown, buses.tristate, ucxroothub/TriStateTrue, TriStateTrue, TRISTATE, TriStateUnknown, ucxroothub/TriStateFalse, TRISTATE enumeration [Buses], _TRISTATE
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ucxroothub.h
apiname:
-	TRISTATE
product: Windows
targetos: Windows
req.typenames: TRISTATE
req.product: Windows 10 or later.
---

# _TRISTATE Enumeration
The <b>TRISTATE</b> enumeration indicates generic state values for true or false.

## Syntax
````
typedef enum _TRISTATE { 
  TriStateUnknown  = u,
  TriStateFalse    = f,
  TriStateTrue     = t
} TRISTATE;
````

## Constants

<table>
            
                <tr>
                    <td>TriStateFalse</td>
                    <td>State is a false boolean value.</td>
                </tr>
            
                <tr>
                    <td>TriStateTrue</td>
                    <td>State is a true boolean value.</td>
                </tr>
            
                <tr>
                    <td>TriStateUnknown</td>
                    <td>State is unknown.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ucxroothub.h (include Ucxclass.h) |