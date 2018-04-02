---
UID: NS:rilapitypes.RILMSGINDELIVER
title: RILMSGINDELIVER
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgindeliver.htm
old-project: netvista
ms.assetid: a4bfdc26-46a9-404e-9cd0-10dabba01dc2
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*LPRILMSGINDELIVER, RILMSGINDELIVER, RILMSGINDELIVER structure [Network Drivers Starting with Windows Vista], netvista.rilmsgindeliver, ntddrilapitypes/RILMSGINDELIVER"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: Rilapitypes.h
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
-	ntddrilapitypes.h
api_name:
-	RILMSGINDELIVER
product:
- Windows
targetos: Windows
req.typenames: RILMSGINDELIVER, *LPRILMSGINDELIVER
req.product: Windows 10 or later.
---

# RILMSGINDELIVER structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef struct RILMSGINDELIVER {
  RILADDRESS       raOrigAddress;
  RILMSGPROTOCOLID dwProtocolID;
  RILMSGDCS        rmdDataCoding;
  RILSYSTEMTIME    stSCReceiveTime;
  DWORD            dwMsgID;
  DWORD            cbHdrLength;
  DWORD            cchMsgLength;
  BYTE             rgbHdr[256];
  BYTE             rgbMsg[512];
}  *LPRILMSGINDELIVER;
```

## Members


`raOrigAddress`



`dwProtocolID`



`rmdDataCoding`



`stSCReceiveTime`



`dwMsgID`



`cbHdrLength`



`cchMsgLength`



`rgbHdr`



`rgbMsg`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |