---
UID: NS:ntddrilapitypes.RILMSGCDMAOUTSUBMIT
title: RILMSGCDMAOUTSUBMIT
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmaoutsubmit.htm
old-project: netvista
ms.assetid: 3ed93cff-7974-4cf9-9b89-f4a8e52c4c3d
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*LPRILMSGCDMAOUTSUBMIT, RILMSGCDMAOUTSUBMIT, RILMSGCDMAOUTSUBMIT structure [Network Drivers Starting with Windows Vista], netvista.rilmsgcdmaoutsubmit, ntddrilapitypes/RILMSGCDMAOUTSUBMIT"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
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
-	RILMSGCDMAOUTSUBMIT
product:
- Windows
targetos: Windows
req.typenames: RILMSGCDMAOUTSUBMIT, *LPRILMSGCDMAOUTSUBMIT
---

# RILMSGCDMAOUTSUBMIT structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef struct RILMSGCDMAOUTSUBMIT {
  RILADDRESS               raDestAddress;
  RILSUBADDRESS            rsaDestSubaddr;
  BOOL                     bDigit;
  RILSYSTEMTIME            stValidityPeriodAbs;
  RILSYSTEMTIME            stValidityPeriodRel;
  RILSYSTEMTIME            stDeferredDelTimeAbs;
  RILSYSTEMTIME            stDeferredDelTimeRel;
  BOOL                     bDeliveryAckRequest;
  BOOL                     bUserAckRequest;
  BOOL                     bBearerReplyRequest;
  DWORD                    dwReplySeqNumber;
  RILMSGCDMAMSGDISPLAYMODE dwMsgDisplayMode;
  RILADDRESS               raCallBackNumber;
  RILMSGCDMAMSGPRIORITY    dwMsgPriority;
  RILMSGCDMAMSGPRIVACY     dwMsgPrivacy;
  DWORD                    dwTeleservice;
  DWORD                    dwMsgID;
  RILMSGCDMALANGUAGE       dwMsgLang;
  RILMSGCDMAMSGENCODING    dwMsgEncoding;
  DWORD                    cbHdrLength;
  DWORD                    cchMsgLength;
  BYTE                     rgbHdr[140];
  BYTE                     rgbMsg[256];
}  *LPRILMSGCDMAOUTSUBMIT;
```

## Members


`raDestAddress`



`rsaDestSubaddr`



`bDigit`



`stValidityPeriodAbs`



`stValidityPeriodRel`



`stDeferredDelTimeAbs`



`stDeferredDelTimeRel`



`bDeliveryAckRequest`



`bUserAckRequest`



`bBearerReplyRequest`



`dwReplySeqNumber`



`dwMsgDisplayMode`



`raCallBackNumber`



`dwMsgPriority`



`dwMsgPrivacy`



`dwTeleservice`



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
| **Header** | ntddrilapitypes.h (include Rilapitypes.h) |