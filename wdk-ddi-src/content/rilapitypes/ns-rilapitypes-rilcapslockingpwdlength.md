---
UID : NS:rilapitypes.RILCAPSLOCKINGPWDLENGTH
title : RILCAPSLOCKINGPWDLENGTH
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcapslockingpwdlength_2.htm
old-project : netvista
ms.assetid : 7ab6ea03-cfe6-4679-91ff-e52aae7a5200
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.rilcapslockingpwdlength_2, RILCAPSLOCKINGPWDLENGTH, *LPRILCAPSLOCKINGPWDLENGTH, RILCAPSLOCKINGPWDLENGTH structure [Network Drivers Starting with Windows Vista], rilapitypes/RILCAPSLOCKINGPWDLENGTH
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
req.typenames : RILCAPSLOCKINGPWDLENGTH, *LPRILCAPSLOCKINGPWDLENGTH
req.product : Windows 10 or later.
---

# RILCAPSLOCKINGPWDLENGTH structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILCAPSLOCKINGPWDLENGTH {
  DWORD  cbSize;
  DWORD  dwParams;
  DWORD  dwPersoFeature;
  DWORD  dwPasswordLength;
} RILCAPSLOCKINGPWDLENGTH, RILCAPSLOCKINGPWDLENGTH;
````

## Members


`cbSize`



`dwParams`



`dwPasswordLength`



`dwPersoFeature`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |