---
UID: NS:rilapitypes.RILMSGCDMAINDELIVER
title: RILMSGCDMAINDELIVER
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmaindeliver.htm
old-project: netvista
ms.assetid: fdff17ac-2ffd-45b0-8f01-a21af1ffa9d0
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*LPRILMSGCDMAINDELIVER, RILMSGCDMAINDELIVER, RILMSGCDMAINDELIVER structure [Network Drivers Starting with Windows Vista], netvista.rilmsgcdmaindeliver, ntddrilapitypes/RILMSGCDMAINDELIVER"
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
-	RILMSGCDMAINDELIVER
product:
- Windows
targetos: Windows
req.typenames: RILMSGCDMAINDELIVER, *LPRILMSGCDMAINDELIVER
req.product: Windows 10 or later.
---

# RILMSGCDMAINDELIVER structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef struct RILMSGCDMAINDELIVER {
  RILADDRESS               raOrigAddress;
  RILSUBADDRESS            rsaOrigSubaddr;
  RILSYSTEMTIME            stSCReceiveTime;
  RILSYSTEMTIME            stValidityPeriodAbs;
  RILSYSTEMTIME            stValidityPeriodRel;
  RILSYSTEMTIME            stDeferredDelTimeAbs;
  RILSYSTEMTIME            stDeferredDelTimeRel;
  DWORD                    dwNumMsgs;
  RILADDRESS               raCallBackNumber;
  RILMSGCDMAMSGPRIORITY    dwMsgPriority;
  DWORD                    dwAlertOnMsgDelivery;
  RILMSGCDMAMSGPRIVACY     dwMsgPrivacy;
  BOOL                     bUserAckRequest;
  RILMSGCDMAMSGDISPLAYMODE dwMsgDisplayMode;
  DWORD                    dwTeleservice;
  DWORD                    dwServiceID;
  DWORD                    dwMsgID;
  RILMSGCDMALANGUAGE       dwMsgLang;
  RILMSGCDMAMSGENCODING    dwMsgEncoding;
  DWORD                    cbHdrLength;
  DWORD                    cchMsgLength;
  BYTE                     rgbHdr[140];
  BYTE                     rgbMsg[256];
}  *LPRILMSGCDMAINDELIVER;
```

## Members


`raOrigAddress`



`rsaOrigSubaddr`



`stSCReceiveTime`



`stValidityPeriodAbs`



`stValidityPeriodRel`



`stDeferredDelTimeAbs`



`stDeferredDelTimeRel`



`dwNumMsgs`



`raCallBackNumber`



`dwMsgPriority`



`dwAlertOnMsgDelivery`



`dwMsgPrivacy`



`bUserAckRequest`



`dwMsgDisplayMode`



`dwTeleservice`



`dwServiceID`



`dwMsgID`



`dwMsgLang`



`dwMsgEncoding`



`cbHdrLength`



`cchMsgLength`



`rgbHdr`



`rgbMsg`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |