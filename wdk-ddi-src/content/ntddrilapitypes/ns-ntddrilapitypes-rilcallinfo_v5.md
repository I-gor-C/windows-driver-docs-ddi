---
UID: NS:ntddrilapitypes.RILCALLINFO_V5
title: RILCALLINFO_V5
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallinfo_v5.htm
old-project: netvista
ms.assetid: 76d6c066-f455-45d4-ac39-76d1420fe8c9
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*LPRILCALLINFO, *LPRILCALLINFO_V5, RILCALLINFO, RILCALLINFO_V5, RILCALLINFO_V5 structure [Network Drivers Starting with Windows Vista], netvista.rilcallinfo_v5, ntddrilapitypes/RILCALLINFO_V5"
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
-	RILCALLINFO_V5
product:
- Windows
targetos: Windows
req.typenames: RILCALLINFO_V5, *LPRILCALLINFO_V5, RILCALLINFO, *LPRILCALLINFO
---

# RILCALLINFO_V5 structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef struct RILCALLINFO_V5 {
  DWORD                          cbSize;
  DWORD                          dwParams;
  DWORD                          dwExecutor;
  DWORD                          dwID;
  RILCALLINFODIRECTION           dwDirection;
  RILCALLINFOSTATUS              dwStatus;
  RILCALLTYPE                    dwType;
  RILCALLINFOMULTIPARTY          dwMultiparty;
  RILADDRESS                     raAddress;
  RILSUBADDRESS                  rsaSubAddress;
  WCHAR                          wszDescription[256];
  RILREMOTEPARTYINFOVALUE        dwNumberPresentationIndicator;
  RILREMOTEPARTYINFOVALUE        dwNamePresentationIndicator;
  DWORD                          dwFlags;
  RILCALLINFODISCONNECTINITIATOR dwDisconnectInitiator;
  RILCALLINFODISCONNECTREASON    dwDisconnectReason;
  RILCALLDISCONNECTDETAILS       stDisconnectDetails;
  RILCALLMEDIAOFFERANSWERSET     rcmOfferAnswer;
  RILCALLHANDOVERSTATE           rchsHandoverState;
  RILCALLMODIFICATIONCAUSECODE   dwCallModificationCauseCode;
  RILCALLRTT                     stRTTInfo;
} *LPRILCALLINFO_V5, *LPRILCALLINFO, RILCALLINFO, RILCALLINFO_V5;
```

## Members


`cbSize`



`dwParams`



`dwExecutor`



`dwID`



`dwDirection`



`dwStatus`



`dwType`



`dwMultiparty`



`raAddress`



`rsaSubAddress`



`wszDescription`



`dwNumberPresentationIndicator`



`dwNamePresentationIndicator`



`dwFlags`



`dwDisconnectInitiator`



`dwDisconnectReason`



`stDisconnectDetails`



`rcmOfferAnswer`



`rchsHandoverState`



`dwCallModificationCauseCode`



`stRTTInfo`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h) |