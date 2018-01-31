---
UID : NS:ntddrilapitypes.RILCALLMODIFICATIONINFO
title : RILCALLMODIFICATIONINFO
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallmodificationinfo.htm
old-project : netvista
ms.assetid : 568603d9-0f96-49f7-a6f8-3c69d889cea7
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.rilcallmodificationinfo, RILCALLMODIFICATIONINFO, *LPRILCALLMODIFICATIONINFO, RILCALLMODIFICATIONINFO structure [Network Drivers Starting with Windows Vista], ntddrilapitypes/RILCALLMODIFICATIONINFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddrilapitypes.h
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
req.typenames : RILCALLMODIFICATIONINFO, *LPRILCALLMODIFICATIONINFO
---

# RILCALLMODIFICATIONINFO structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILCALLMODIFICATIONINFO {
  DWORD                                    cbSize;
  DWORD                                    dwParams;
  DWORD                                    dwExecutor;
  DWORD                                    dwID;
  RILCALLMODIFICATIONINFOMODIFICATIONTYPE  dwModificationType;
  RILCALLTYPE                              dwOldCallType;
  RILCALLTYPE                              dwNewCallType;
  RILADDRESS                               raAddress;
  RILALPHAIDENTIFIER                       aiIdentifier;
} RILCALLMODIFICATIONINFO, RILCALLMODIFICATIONINFO;
````

## Members


`aiIdentifier`



`cbSize`



`dwExecutor`



`dwID`



`dwModificationType`



`dwNewCallType`



`dwOldCallType`



`dwParams`



`raAddress`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |