---
UID: NE:netdispumdddi.MIRACAST_CHUNK_TYPE
title: MIRACAST_CHUNK_TYPE
author: windows-driver-content
description: Specifies the types of wireless display (Miracast) chunk info that is to be processed.
old-location: display\miracast_chunk_type.htm
old-project: display
ms.assetid: 39911172-f916-4ca2-8d98-9d53fbc30807
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: MIRACAST_CHUNK_TYPE, MIRACAST_CHUNK_TYPE enumeration [Display Devices], MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE, MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE, MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1, MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_2, MIRACAST_CHUNK_TYPE_ENCODE_FORCE_UINT32, MIRACAST_CHUNK_TYPE_FRAME_DROPPED, MIRACAST_CHUNK_TYPE_FRAME_START, MIRACAST_CHUNK_TYPE_UNKNOWN, display.miracast_chunk_type, netdispumdddi/MIRACAST_CHUNK_TYPE, netdispumdddi/MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE, netdispumdddi/MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE, netdispumdddi/MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1, netdispumdddi/MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_2, netdispumdddi/MIRACAST_CHUNK_TYPE_ENCODE_FORCE_UINT32, netdispumdddi/MIRACAST_CHUNK_TYPE_FRAME_DROPPED, netdispumdddi/MIRACAST_CHUNK_TYPE_FRAME_START, netdispumdddi/MIRACAST_CHUNK_TYPE_UNKNOWN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
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
-	Netdispumdddi.h
api_name:
-	MIRACAST_CHUNK_TYPE
product:
- Windows
targetos: Windows
req.typenames: MIRACAST_CHUNK_TYPE
---

# MIRACAST_CHUNK_TYPE Enumeration
Specifies the types of wireless display (Miracast) chunk info that is to be processed.

## Syntax
```
typedef enum MIRACAST_CHUNK_TYPE {
  MIRACAST_CHUNK_TYPE_UNKNOWN                  ,
  MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE   ,
  MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE          ,
  MIRACAST_CHUNK_TYPE_FRAME_START              ,
  MIRACAST_CHUNK_TYPE_FRAME_DROPPED            ,
  MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1  ,
  MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_2  ,
  MIRACAST_CHUNK_TYPE_ENCODE_FORCE_UINT32
} ;
```

## Constants

<table>
            
                <tr>
                    <td>MIRACAST_CHUNK_TYPE_UNKNOWN</td>
                    <td>An unknown or undefined chunk type.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE</td>
                    <td>Color conversion has completed on the chunk.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE</td>
                    <td>Encoding has completed on the chunk.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_CHUNK_TYPE_FRAME_START</td>
                    <td>The chunk is at the start of the Wi-Fi frame.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_CHUNK_TYPE_FRAME_DROPPED</td>
                    <td>The chunk is in a dropped Wi-Fi frame.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1</td>
                    <td>Encoding is driver-defined, of type 1.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_2</td>
                    <td>Encoding is driver-defined, of type 2.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_CHUNK_TYPE_ENCODE_FORCE_UINT32</td>
                    <td>Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. You should not use this value.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | netdispumdddi.h (include Netdispumdddi.h) |