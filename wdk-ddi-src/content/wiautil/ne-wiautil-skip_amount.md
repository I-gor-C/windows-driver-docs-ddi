---
UID: NE:wiautil.SKIP_AMOUNT
title: SKIP_AMOUNT
author: windows-driver-content
description: The SKIP_AMOUNT enumeration is used to indicate whether the file and informational headers of an image should be skipped over.
old-location: image\skip_amount.htm
old-project: image
ms.assetid: 4e21b3e9-0383-4464-b87e-beea88123124
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: SKIP_AMOUNT, SKIP_AMOUNT enumeration [Imaging Devices], SKIP_BOTHHDR, SKIP_FILEHDR, SKIP_OFF, image.skip_amount, wiauFncs_8f521aa0-0663-4f84-a9c9-91747fcb13e8.xml, wiautil/SKIP_AMOUNT, wiautil/SKIP_BOTHHDR, wiautil/SKIP_FILEHDR, wiautil/SKIP_OFF
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wiautil.h
req.include-header: Wiautil.h, Wiamindr.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows XP and later.
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
-	wiautil.h
api_name:
-	SKIP_AMOUNT
product: Windows
targetos: Windows
req.typenames: SKIP_AMOUNT
req.product: Windows 10 or later.
---

# SKIP_AMOUNT Enumeration
The SKIP_AMOUNT enumeration is used to indicate whether the file and informational headers of an image should be skipped over.

## Syntax
```
typedef enum SKIP_AMOUNT {
  SKIP_OFF      ,
  SKIP_FILEHDR  ,
  SKIP_BOTHHDR
} ;
```

## Constants

<table>
            
                <tr>
                    <td>SKIP_OFF</td>
                    <td>Do not skip over either header.</td>
                </tr>
            
                <tr>
                    <td>SKIP_FILEHDR</td>
                    <td>Skip over the file header.</td>
                </tr>
            
                <tr>
                    <td>SKIP_BOTHHDR</td>
                    <td>Skip over both the file and info headers.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows XP and later. Available in Windows XP and later. |
| **Header** | wiautil.h (include Wiautil.h, Wiamindr.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540369">CWiauFormatConverter::ConvertToBmp</a>