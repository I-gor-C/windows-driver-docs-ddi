---
UID : NS:ntddrilapitypes.RILMSGINDELIVER
title : RILMSGINDELIVER
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgindeliver.htm
old-project : netvista
ms.assetid : a4bfdc26-46a9-404e-9cd0-10dabba01dc2
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILMSGINDELIVER structure [Network Drivers Starting with Windows Vista], netvista.rilmsgindeliver, *LPRILMSGINDELIVER, ntddrilapitypes/RILMSGINDELIVER, RILMSGINDELIVER
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
req.typenames : "*LPRILMSGINDELIVER, RILMSGINDELIVER"
---

# RILMSGINDELIVER structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILMSGINDELIVER {
  RILADDRESS        raOrigAddress;
  RILMSGPROTOCOLID  dwProtocolID;
  RILMSGDCS         rmdDataCoding;
  RILSYSTEMTIME     stSCReceiveTime;
  DWORD             dwMsgID;
  DWORD             cbHdrLength;
  DWORD             cchMsgLength;
  BYTE [256]        rgbHdr;
  BYTE [512]        rgbMsg;
} RILMSGINDELIVER, RILMSGINDELIVER;
````

## Members


`cbHdrLength`



`cchMsgLength`



`dwMsgID`



`dwProtocolID`



`raOrigAddress`



`rgbHdr`



`rgbMsg`



`rmdDataCoding`



`stSCReceiveTime`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |