---
UID: NS:rilapitypes.RILCALLINFO_V5
title: RILCALLINFO_V5
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallinfo_v5_2.htm
old-project: netvista
ms.assetid: a2cadee5-40e4-4044-b631-1824099e2fd7
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: "*LPRILCALLINFO, *LPRILCALLINFO_V5, RILCALLINFO, RILCALLINFO_V5, RILCALLINFO_V5 structure [Network Drivers Starting with Windows Vista], netvista.rilcallinfo_v5_2, rilapitypes/RILCALLINFO_V5"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	rilapitypes.h
api_name:
-	RILCALLINFO_V5
product: Windows
targetos: Windows
req.typenames: RILCALLINFO_V5, *LPRILCALLINFO_V5, RILCALLINFO, *LPRILCALLINFO
req.product: Windows 10 or later.
---

# RILCALLINFO_V5 structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILCALLINFO_V5 {
  DWORD                           cbSize;
  DWORD                           dwParams;
  DWORD                           dwExecutor;
  DWORD                           dwID;
  RILCALLINFODIRECTION            dwDirection;
  RILCALLINFOSTATUS               dwStatus;
  RILCALLTYPE                     dwType;
  RILCALLINFOMULTIPARTY           dwMultiparty;
  RILADDRESS                      raAddress;
  RILSUBADDRESS                   rsaSubAddress;
  WCHAR [MAXLENGTH_DESCRIPTION]   wszDescription;
  RILREMOTEPARTYINFOVALUE         dwNumberPresentationIndicator;
  RILREMOTEPARTYINFOVALUE         dwNamePresentationIndicator;
  DWORD                           dwFlags;
  RILCALLINFODISCONNECTINITIATOR  dwDisconnectInitiator;
  RILCALLINFODISCONNECTREASON     dwDisconnectReason;
  RILCALLDISCONNECTDETAILS        stDisconnectDetails;
  RILCALLMEDIAOFFERANSWERSET      rcmOfferAnswer;
  RILCALLHANDOVERSTATE            rchsHandoverState;
  RILCALLMODIFICATIONCAUSECODE    dwCallModificationCauseCode;
  RILCALLRTT                      stRTTInfo;
} RILCALLINFO_V5, RILCALLINFO_V5;
````

## Members


`cbSize`



`dwCallModificationCauseCode`



`dwDirection`



`dwDisconnectInitiator`



`dwDisconnectReason`



`dwExecutor`



`dwFlags`



`dwID`



`dwMultiparty`



`dwNamePresentationIndicator`



`dwNumberPresentationIndicator`



`dwParams`



`dwStatus`



`dwType`



`raAddress`



`rchsHandoverState`



`rcmOfferAnswer`



`rsaSubAddress`



`stDisconnectDetails`



`stRTTInfo`



`wszDescription`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |