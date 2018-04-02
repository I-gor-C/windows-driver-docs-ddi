---
UID: NS:ksmedia._DS3DVECTOR
title: "_DS3DVECTOR"
author: windows-driver-content
description: The DS3DVECTOR structure contains three-dimensional position coordinates, position vector components, or velocity vector components.
old-location: audio\ds3dvector.htm
old-project: audio
ms.assetid: 828bb255-4640-4508-866e-e3641ca05773
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: "*PDS3DVECTOR, DS3DVECTOR, DS3DVECTOR structure [Audio Devices], PDS3DVECTOR, PDS3DVECTOR structure pointer [Audio Devices], _DS3DVECTOR, aud-prop_3e17b5ec-c2fc-4e6c-bff1-27be36e376c9.xml, audio.ds3dvector, ksmedia/DS3DVECTOR, ksmedia/PDS3DVECTOR"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
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
-	ksmedia.h
api_name:
-	DS3DVECTOR
product: Windows
targetos: Windows
req.typenames: DS3DVECTOR, *PDS3DVECTOR
---

# _DS3DVECTOR structure
The DS3DVECTOR structure contains three-dimensional position coordinates, position vector components, or velocity vector components.

## Syntax
```
typedef struct _DS3DVECTOR {
  union {
    FLOAT dvX;
    FLOAT x;
  };
  union {
    FLOAT dvY;
    FLOAT y;
  };
  union {
    FLOAT dvZ;
    FLOAT z;
  };
} *PDS3DVECTOR, DS3DVECTOR;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksmedia.h (include Ksmedia.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537101">KSDS3D_BUFFER_ALL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff537116">KSDS3D_LISTENER_ALL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff537119">KSDS3D_LISTENER_ORIENTATION</a>