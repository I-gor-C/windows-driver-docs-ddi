---
UID: NS:ksmedia._KS_COLCON
title: "_KS_COLCON"
author: windows-driver-content
description: The KS_COLCON structure is used to describe color and contrast settings.
old-location: stream\ks_colcon.htm
old-project: stream
ms.assetid: 8328c1b1-e72d-4e34-b69e-e02b3f5850bf
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKS_COLCON, KS_COLCON, KS_COLCON structure [Streaming Media Devices], PKS_COLCON, PKS_COLCON structure pointer [Streaming Media Devices], _KS_COLCON, dvdref_96e0b7a1-6131-445b-9a4f-9157997338aa.xml, ksmedia/KS_COLCON, ksmedia/PKS_COLCON, stream.ks_colcon"
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
-	KS_COLCON
product:
- Windows
targetos: Windows
req.typenames: KS_COLCON, *PKS_COLCON
---

# _KS_COLCON structure
The KS_COLCON structure is used to describe color and contrast settings.

## Syntax
```
typedef struct _KS_COLCON {
  UCHAR  : 4 emph1col;
  UCHAR  : 4 emph2col;
  UCHAR  : 4 backcol;
  UCHAR  : 4 patcol;
  UCHAR  : 4 emph1con;
  UCHAR  : 4 emph2con;
  UCHAR  : 4 backcon;
  UCHAR  : 4 patcon;
} KS_COLCON, *PKS_COLCON;
```

## Members


`emph1col`

Indicates

`emph2col`

Indicates

`backcol`

Indicates

`patcol`

Indicates

`emph1con`

Indicates

`emph2con`

Indicates

`backcon`

Indicates

`patcon`

Indicates

## Remarks
The KS_COLCON structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565627">KSPROPERTY_SPHLI</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksmedia.h (include Ksmedia.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff565627">KSPROPERTY_SPHLI</a>