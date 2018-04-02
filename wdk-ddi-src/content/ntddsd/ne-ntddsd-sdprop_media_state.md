---
UID: NE:ntddsd.SDPROP_MEDIA_STATE
title: SDPROP_MEDIA_STATE
author: windows-driver-content
description: The SDPROP_MEDIA_STATE enumeration lists the values associated with the media states property.
old-location: sd\sdprop_media_state.htm
old-project: SD
ms.assetid: b59fd639-f2e2-4765-bcc7-01934df3a0bc
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: SD.sdprop_media_state, SDPMS_MEDIA_INSERTED, SDPMS_NO_MEDIA, SDPROP_MEDIA_STATE, SDPROP_MEDIA_STATE enumeration [Buses], ntddsd/SDPMS_MEDIA_INSERTED, ntddsd/SDPMS_NO_MEDIA, ntddsd/SDPROP_MEDIA_STATE, sd-structs_a2064f73-cec7-4703-95ec-8ab8adc0b4b2.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddsd.h
req.include-header: Ntddsd.h
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
-	ntddsd.h
api_name:
-	SDPROP_MEDIA_STATE
product:
- Windows
targetos: Windows
req.typenames: SDPROP_MEDIA_STATE
---

# SDPROP_MEDIA_STATE Enumeration
The SDPROP_MEDIA_STATE enumeration lists the values associated with the media states property.

## Syntax
```
typedef enum SDPROP_MEDIA_STATE {
  SDPMS_NO_MEDIA        ,
  SDPMS_MEDIA_INSERTED
} ;
```

## Constants

<table>
            
                <tr>
                    <td>SDPMS_NO_MEDIA</td>
                    <td>Indicates that the media is not present.</td>
                </tr>
            
                <tr>
                    <td>SDPMS_MEDIA_INSERTED</td>
                    <td>Indicates that the media is inserted.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddsd.h (include Ntddsd.h) |

## See Also

<a href="https://msdn.microsoft.com/09b30bf0-fe85-4ad5-bd3e-113ed3a093ac">SDBUS_REQUEST_PACKET</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff537909">SdBusSubmitRequest</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff537914">SdBusSubmitRequestAsync</a>