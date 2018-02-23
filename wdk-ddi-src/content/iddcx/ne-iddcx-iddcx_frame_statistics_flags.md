---
UID: NE:iddcx.IDDCX_FRAME_STATISTICS_FLAGS
title: IDDCX_FRAME_STATISTICS_FLAGS
author: windows-driver-content
description: Indicates whether a frame was altered by the driver.
old-location: display\iddcx_frame_statistics_flags.htm
old-project: display
ms.assetid: 85ae47d8-228c-4fff-9be0-bf56868b9319
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: IDDCX_FRAME_STATISTICS_FLAGS enumeration [Display Devices], iddcx/IDDCX_FRAME_STATISTICS_FLAGS, IDDCX_FRAME_STATISTICS_FLAGS_NONE, iddcx/IDDCX_FRAME_STATISTICS_FLAGS_NONE, display.iddcx_frame_statistics_flags, IDDCX_FRAME_STATISTICS_FLAGS, IDDCX_FRAME_STATISTICS_FLAGS_REDUCED_COLOR_FIDELITY, iddcx/IDDCX_FRAME_STATISTICS_FLAGS_REDUCED_COLOR_FIDELITY
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	iddcx.h
apiname:
-	IDDCX_FRAME_STATISTICS_FLAGS
product: Windows
targetos: Windows
req.typenames: 
---

# IDDCX_FRAME_STATISTICS_FLAGS Enumeration
Indicates whether a frame was altered by the driver.

## Syntax
````
typedef enum _IDDCX_FRAME_STATISTICS_FLAGS { 
  IDDCX_FRAME_STATISTICS_FLAGS_NONE                    = 0,
  IDDCX_FRAME_STATISTICS_FLAGS_REDUCED_COLOR_FIDELITY  = 1
} IDDCX_FRAME_STATISTICS_FLAGS;
````

## Constants

<table>
            
                <tr>
                    <td>IDDCX_FRAME_STATISTICS_FLAGS_NONE</td>
                    <td>Indicates that there are no alterations to the frame.</td>
                </tr>
            
                <tr>
                    <td>IDDCX_FRAME_STATISTICS_FLAGS_REDUCED_COLOR_FIDELITY</td>
                    <td>If set indicates that the driver reduced the color fidelity of the desktop image while processing and transmitting this frame.</td>
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