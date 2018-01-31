---
UID : NS:rilapitypes.RILCBCDMACONFIGINFO
title : RILCBCDMACONFIGINFO
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcbcdmaconfiginfo_2.htm
old-project : netvista
ms.assetid : a12254b0-fb4d-49ff-a046-cae99c12f535
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.rilcbcdmaconfiginfo_2, RILCBCDMACONFIGINFO, RILCBCDMACONFIGINFO structure [Network Drivers Starting with Windows Vista], rilapitypes/RILCBCDMACONFIGINFO, *LPRILCBCDMACONFIGINFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : rilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : RILCBCDMACONFIGINFO, *LPRILCBCDMACONFIGINFO
req.product : Windows 10 or later.
---

# RILCBCDMACONFIGINFO structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILCBCDMACONFIGINFO {
  BOOL   fAccept;
  DWORD  dwBroadcastMsgLang;
  DWORD  dwBroadcastServiceCategory;
} RILCBCDMACONFIGINFO, RILCBCDMACONFIGINFO;
````

## Members


`dwBroadcastMsgLang`



`dwBroadcastServiceCategory`



`fAccept`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |