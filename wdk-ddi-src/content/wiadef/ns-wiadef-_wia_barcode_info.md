---
UID: NS:wiadef._WIA_BARCODE_INFO
title: "_WIA_BARCODE_INFO"
author: windows-driver-content
description: The WIA_BARCODE_INFO structure stores information for one decoded barcode.
old-location: image\wia_barcode_info.htm
old-project: image
ms.assetid: 2E659DDC-4012-4EA2-8E6C-033F2AB526B8
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: WIA_BARCODE_INFO structure [Imaging Devices], wiadef/WIA_BARCODE_INFO, WIA_BARCODE_INFO, _WIA_BARCODE_INFO, image.wia_barcode_info
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wiadef.h
req.include-header: Wiadef.h
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
req.irql: See Remarks section.
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	wiadef.h
apiname:
-	WIA_BARCODE_INFO
product: Windows
targetos: Windows
req.typenames: WIA_BARCODE_INFO
req.product: Windows 10 or later.
---

# _WIA_BARCODE_INFO structure
The <b>WIA_BARCODE_INFO</b> structure stores information for one decoded barcode.

## Syntax
````
typedef struct _WIA_BARCODE_INFO {
  DWORD Size;
  DWORD Type;
  DWORD Page;
  DWORD Confidence;
  DWORD Xoffset;
  DWORD Yoffset;
  DWORD Rotation;
  DWORD Length;
  WCHAR Text[1];
} WIA_BARCODE_INFO;
````

## Members


`Confidence`

The confidence level. A value in the range from 0 (no confidence) to 10 (maximum confidence).

`Length`

The number of text characters in the character string containing the decoded barcode text, excluding the length of the NULL terminator.

`Page`

The page number where the barcode was detected. A zero-based index referring to the current scan job.

`Rotation`

The rotation of the barcode, in degrees. A value in the rage from 0 to 359. This value can be 0 if it is unknown.

`Size`

The total size of this structure, in bytes.

`Text`

Placeholder for the character string containing the decoded barcode text (double byte characters, NULL terminated).

`Type`

The barcode type. One of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh706268">WIA_IPS_SUPPORTED_BARCODE_TYPES</a> values.

`XOffset`



`YOffset`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wiadef.h (include Wiadef.h) |