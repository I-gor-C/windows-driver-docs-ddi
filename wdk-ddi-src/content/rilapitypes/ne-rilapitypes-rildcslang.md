---
UID: NE:rilapitypes.RILDCSLANG
title: RILDCSLANG
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildcslang_2.htm
old-project: netvista
ms.assetid: b6d50c5d-edc5-4037-9223-679fd19f195f
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: rilapitypes/RIL_DCSLANG_ARABIC, rilapitypes/RIL_DCSLANG_FINNISH, rilapitypes/RIL_DCSLANG_HUNGARIAN, RIL_DCSLANG_UNKNOWN, RIL_DCSLANG_SWEDISH, rilapitypes/RIL_DCSLANG_POLISH, RIL_DCSLANG_HEBREW, RIL_DCSLANG_FRENCH, RIL_DCSLANG_FINNISH, RIL_DCSLANG_TURKISH, netvista.rildcslang_2, RIL_DCSLANG_HUNGARIAN, rilapitypes/RIL_DCSLANG_CZECH, RIL_DCSLANG_ALL, rilapitypes/RIL_DCSLANG_FRENCH, rilapitypes/RIL_DCSLANG_RUSSIAN, RIL_DCSLANG_ICELANDIC, rilapitypes/RIL_DCSLANG_UNKNOWN, rilapitypes/RIL_DCSLANG_GREEK, RILDCSLANG enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_DCSLANG_SWEDISH, RIL_DCSLANG_PORTUGUESE, RIL_DCSLANG_GERMAN, rilapitypes/RIL_DCSLANG_GERMAN, rilapitypes/RIL_DCSLANG_ALL, RIL_DCSLANG_ITALIAN, RIL_DCSLANG_NORWEGIAN, rilapitypes/RIL_DCSLANG_ITALIAN, rilapitypes/RIL_DCSLANG_PORTUGUESE, rilapitypes/RIL_DCSLANG_HEBREW, rilapitypes/RIL_DCSLANG_ICELANDIC, RIL_DCSLANG_SPANISH, RIL_DCSLANG_RUSSIAN, RIL_DCSLANG_ARABIC, rilapitypes/RIL_DCSLANG_DANISH, rilapitypes/RIL_DCSLANG_TURKISH, rilapitypes/RIL_DCSLANG_NORWEGIAN, RIL_DCSLANG_ENGLISH, RIL_DCSLANG_POLISH, rilapitypes/RIL_DCSLANG_SPANISH, RIL_DCSLANG_CZECH, RILDCSLANG, rilapitypes/RILDCSLANG, RIL_DCSLANG_DUTCH, RIL_DCSLANG_DANISH, rilapitypes/RIL_DCSLANG_ENGLISH, RIL_DCSLANG_GREEK, rilapitypes/RIL_DCSLANG_DUTCH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
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
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	rilapitypes.h
apiname:
-	RILDCSLANG
product: Windows
targetos: Windows
req.typenames: RILDCSLANG
req.product: Windows 10 or later.
---

# RILDCSLANG Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILDCSLANG { 
  RIL_DCSLANG_UNKNOWN,
  RIL_DCSLANG_GERMAN,
  RIL_DCSLANG_ENGLISH,
  RIL_DCSLANG_ITALIAN,
  RIL_DCSLANG_FRENCH,
  RIL_DCSLANG_SPANISH,
  RIL_DCSLANG_DUTCH,
  RIL_DCSLANG_SWEDISH,
  RIL_DCSLANG_DANISH,
  RIL_DCSLANG_PORTUGUESE,
  RIL_DCSLANG_FINNISH,
  RIL_DCSLANG_NORWEGIAN,
  RIL_DCSLANG_GREEK,
  RIL_DCSLANG_TURKISH,
  RIL_DCSLANG_HUNGARIAN,
  RIL_DCSLANG_POLISH,
  RIL_DCSLANG_CZECH,
  RIL_DCSLANG_HEBREW,
  RIL_DCSLANG_ARABIC,
  RIL_DCSLANG_RUSSIAN,
  RIL_DCSLANG_ICELANDIC,
  RIL_DCSLANG_ALL
} RILDCSLANG;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_DCSLANG_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_ARABIC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_CZECH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_DANISH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_DUTCH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_ENGLISH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_FINNISH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_FRENCH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_GERMAN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_GREEK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_HEBREW</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_HUNGARIAN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_ICELANDIC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_ITALIAN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_None</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_NORWEGIAN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_POLISH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_PORTUGUESE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_RUSSIAN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_SPANISH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_SWEDISH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_TURKISH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSLANG_UNKNOWN</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |