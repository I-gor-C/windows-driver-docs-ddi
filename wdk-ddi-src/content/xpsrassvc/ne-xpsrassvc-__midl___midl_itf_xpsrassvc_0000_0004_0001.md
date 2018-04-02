---
UID: NE:xpsrassvc.__MIDL___MIDL_itf_xpsrassvc_0000_0004_0001
title: "__MIDL___MIDL_itf_xpsrassvc_0000_0004_0001"
author: windows-driver-content
description: XPSRAS_BACKGROUND_COLOR specifies the background clear color to be used by an XPS rasterizer:
old-location: print\xpsras_background_color.htm
old-project: print
ms.assetid: 0B4C1BAC-173E-42E9-8805-028FE165D49D
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: XPSRAS_BACKGROUND_COLOR, XPSRAS_BACKGROUND_COLOR enumeration [Print Devices], XPSRAS_BACKGROUND_COLOR_OPAQUE, XPSRAS_BACKGROUND_COLOR_TRANSPARENT, __MIDL___MIDL_itf_xpsrassvc_0000_0004_0001, print.xpsras_background_color, xpsrassvc/XPSRAS_BACKGROUND_COLOR, xpsrassvc/XPSRAS_BACKGROUND_COLOR_OPAQUE, xpsrassvc/XPSRAS_BACKGROUND_COLOR_TRANSPARENT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: xpsrassvc.h
req.include-header: Xpsrassvc.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
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
-	xpsrassvc.h
api_name:
-	XPSRAS_BACKGROUND_COLOR
product:
- Windows
targetos: Windows
req.typenames: XPSRAS_BACKGROUND_COLOR
req.product: Windows 10 or later.
---

# __MIDL___MIDL_itf_xpsrassvc_0000_0004_0001 Enumeration
<b>XPSRAS_BACKGROUND_COLOR</b> specifies the background clear color to be used by an XPS rasterizer:

## Syntax
```
typedef enum __MIDL___MIDL_itf_xpsrassvc_0000_0004_0001 {
  XPSRAS_BACKGROUND_COLOR_TRANSPARENT  ,
  XPSRAS_BACKGROUND_COLOR_OPAQUE
} XPSRAS_BACKGROUND_COLOR;
```

## Constants

<table>
            
                <tr>
                    <td>XPSRAS_BACKGROUND_COLOR_TRANSPARENT</td>
                    <td>Use transparent white as clear color.</td>
                </tr>
            
                <tr>
                    <td>XPSRAS_BACKGROUND_COLOR_OPAQUE</td>
                    <td>Use opaque white as clear color.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | xpsrassvc.h (include Xpsrassvc.h) |

## See Also

<a href="https://msdn.microsoft.com/C31681A0-17C6-4255-9068-7486A2101AB7">IXpsRasterizationFactory2::CreateRasterizer</a>