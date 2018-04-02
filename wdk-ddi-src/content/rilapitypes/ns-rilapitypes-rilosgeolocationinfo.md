---
UID: NS:rilapitypes.RILOSGEOLOCATIONINFO
title: RILOSGEOLOCATIONINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilosgeolocationinfo.htm
old-project: netvista
ms.assetid: 9a56152e-fb38-4470-8834-a0cbdd7b70ec
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*LPRILOSGEOLOCATIONINFO, RILOSGEOLOCATIONINFO, RILOSGEOLOCATIONINFO structure [Network Drivers Starting with Windows Vista], netvista.rilosgeolocationinfo, ntddrilapitypes/RILOSGEOLOCATIONINFO"
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
-	RILOSGEOLOCATIONINFO
product: Windows
targetos: Windows
req.typenames: RILOSGEOLOCATIONINFO, *LPRILOSGEOLOCATIONINFO
req.product: Windows 10 or later.
---

# RILOSGEOLOCATIONINFO structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef struct RILOSGEOLOCATIONINFO {
  DWORD                  cbSize;
  DWORD                  dwParams;
  DWORD                  dwLatitude;
  DWORD                  dwLongitude;
  DWORD                  dwAltitude;
  DWORD                  dwAccuracy;
  RILGEOLOCATIONTYPEMASK dwLocationInformationMask;
  RILSYSTEMTIME          stTimeStamp;
  WCHAR                  wszAddressLine1[76];
  WCHAR                  wszAddressLine2[76];
  WCHAR                  wszCity[76];
  WCHAR                  wszState[76];
  WCHAR                  wszCountry[76];
  WCHAR                  wszPostalCode[15];
  WCHAR                  wszFormattedAddress[256];
  WCHAR                  wszCountryCode[11];
  WCHAR                  wszRegionCode[11];
} *LPRILOSGEOLOCATIONINFO, RILOSGEOLOCATIONINFO;
```

## Members


`cbSize`



`dwParams`



`dwLatitude`



`dwLongitude`



`dwAltitude`



`dwAccuracy`



`dwLocationInformationMask`



`stTimeStamp`



`wszAddressLine1`



`wszAddressLine2`



`wszCity`



`wszState`



`wszCountry`



`wszPostalCode`



`wszFormattedAddress`



`wszCountryCode`



`wszRegionCode`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |