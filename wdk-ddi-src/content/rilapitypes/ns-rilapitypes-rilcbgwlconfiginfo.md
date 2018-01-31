---
UID : NS:rilapitypes.RILCBGWLCONFIGINFO
title : RILCBGWLCONFIGINFO
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcbgwlconfiginfo_2.htm
old-project : netvista
ms.assetid : 5939b967-bbc7-42e3-af90-a1c20698a934
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.rilcbgwlconfiginfo_2, *LPRILCBGWLCONFIGINFO, RILCBGWLCONFIGINFO structure [Network Drivers Starting with Windows Vista], rilapitypes/RILCBGWLCONFIGINFO, RILCBGWLCONFIGINFO
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
req.typenames : "*LPRILCBGWLCONFIGINFO, RILCBGWLCONFIGINFO"
req.product : Windows 10 or later.
---

# RILCBGWLCONFIGINFO structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILCBGWLCONFIGINFO {
  BOOL      fAccept;
  RILRANGE  rgrrBroadcastMsgID;
} RILCBGWLCONFIGINFO, RILCBGWLCONFIGINFO;
````

## Members


`fAccept`



`rgrrBroadcastMsgID`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |