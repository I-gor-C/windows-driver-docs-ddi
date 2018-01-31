---
UID : NS:rilapitypes.RILMSGINSTATUS
title : RILMSGINSTATUS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsginstatus_2.htm
old-project : netvista
ms.assetid : 4dcc198f-5e42-4c60-bfec-19702c9ab674
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILMSGINSTATUS, rilapitypes/RILMSGINSTATUS, netvista.rilmsginstatus_2, RILMSGINSTATUS structure [Network Drivers Starting with Windows Vista], *LPRILMSGINSTATUS
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
req.typenames : RILMSGINSTATUS, *LPRILMSGINSTATUS
req.product : Windows 10 or later.
---

# RILMSGINSTATUS structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILMSGINSTATUS {
  DWORD                       dwMsgID;
  RILADDRESS                  raTgtRecipAddress;
  RILSYSTEMTIME               stTgtSCReceiveTime;
  RILSYSTEMTIME               stTgtDischargeTime;
  DWORD                       dwReserved;
  RILMSGINSTATUSTGTDLVSTATUS  dwTgtDlvStatus;
  RILMSGPROTOCOLID            dwProtocolID;
  RILMSGDCS                   rmdDataCoding;
  DWORD                       cbHdrLength;
  DWORD                       cchMsgLength;
  BYTE [MAXLENGTH_HDR]        rgbHdr;
  BYTE [MAXLENGTH_MSG]        rgbMsg;
} RILMSGINSTATUS, RILMSGINSTATUS;
````

## Members


`cbHdrLength`



`cchMsgLength`



`dwMsgID`



`dwProtocolID`



`dwReserved`



`dwTgtDlvStatus`



`raTgtRecipAddress`



`rgbHdr`



`rgbMsg`



`rmdDataCoding`



`stTgtDischargeTime`



`stTgtSCReceiveTime`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |