---
UID: NE:lamp.LAMP_MODE
title: LAMP_MODE
author: windows-driver-content
description: This enumeration contains the operating modes of a lamp device.
old-location: stream\lamp_mode.htm
old-project: stream
ms.assetid: B379B6EF-C3AD-4E6F-B32D-F85228DB6A72
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: LAMP_MODE, LAMP_MODE enumeration [Streaming Media Devices], LAMP_MODE_COLOR, LAMP_MODE_WHITE, lamp/LAMP_MODE, lamp/LAMP_MODE_COLOR, lamp/LAMP_MODE_WHITE, stream.lamp_mode
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: lamp.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	lamp.h
api_name:
-	LAMP_MODE
product: Windows
targetos: Windows
req.typenames: LAMP_MODE
---

# LAMP_MODE Enumeration
This enumeration contains the operating modes of a lamp device.

## Syntax
```
typedef enum LAMP_MODE {
  LAMP_MODE_WHITE  ,
  LAMP_MODE_COLOR
} ;
```

## Constants

<table>
            
                <tr>
                    <td>LAMP_MODE_WHITE</td>
                    <td>Required. White light only.</td>
                </tr>
            
                <tr>
                    <td>LAMP_MODE_COLOR</td>
                    <td>Optional. Color light.</td>
                </tr>
</table>

## Remarks

This is the I/O parameter type of <a href="https://msdn.microsoft.com/library/windows/hardware/dn925071">IOCTL_LAMP_GET_MODE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/dn925081">IOCTL_LAMP_SET_MODE</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | lamp.h |