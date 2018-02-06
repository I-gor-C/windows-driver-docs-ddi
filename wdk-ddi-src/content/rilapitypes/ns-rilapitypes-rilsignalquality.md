---
UID: NS:rilapitypes.RILSIGNALQUALITY
title: RILSIGNALQUALITY
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsignalquality_2.htm
old-project: netvista
ms.assetid: cc5bf370-3996-46de-b27d-8a390a6f407e
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RILSIGNALQUALITY, rilapitypes/RILSIGNALQUALITY, *LPRILSIGNALQUALITY, RILSIGNALQUALITY structure [Network Drivers Starting with Windows Vista], netvista.rilsignalquality_2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
req.lib: 
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
-	RILSIGNALQUALITY
product: Windows
targetos: Windows
req.typenames: "*LPRILSIGNALQUALITY, RILSIGNALQUALITY"
req.product: Windows 10 or later.
---

# RILSIGNALQUALITY structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILSIGNALQUALITY {
  DWORD  cbSize;
  DWORD  dwParams;
  DWORD  dwExecutor;
  DWORD  dwSystemType;
  int    nNumSignalBars;
  int    nSignalStrength;
  int    nSNRStrength;
} RILSIGNALQUALITY, RILSIGNALQUALITY;
````

## Members


`cbSize`



`dwExecutor`



`dwParams`



`dwSystemType`



`nNumSignalBars`



`nSignalStrength`



`nSNRStrength`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |