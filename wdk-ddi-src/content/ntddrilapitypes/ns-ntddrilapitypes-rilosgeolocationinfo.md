---
UID : NS:ntddrilapitypes.RILOSGEOLOCATIONINFO
title : RILOSGEOLOCATIONINFO
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilosgeolocationinfo.htm
old-project : netvista
ms.assetid : 9a56152e-fb38-4470-8834-a0cbdd7b70ec
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILOSGEOLOCATIONINFO structure [Network Drivers Starting with Windows Vista], netvista.rilosgeolocationinfo, *LPRILOSGEOLOCATIONINFO, RILOSGEOLOCATIONINFO, ntddrilapitypes/RILOSGEOLOCATIONINFO
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
req.typenames : "*LPRILOSGEOLOCATIONINFO, RILOSGEOLOCATIONINFO"
---

# RILOSGEOLOCATIONINFO structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILOSGEOLOCATIONINFO {
  DWORD                   cbSize;
  DWORD                   dwParams;
  DWORD                   dwLatitude;
  DWORD                   dwLongitude;
  DWORD                   dwAltitude;
  DWORD                   dwAccuracy;
  RILGEOLOCATIONTYPEMASK  dwLocationInformationMask;
  RILSYSTEMTIME           stTimeStamp;
  WCHAR [76]              wszAddressLine1;
  WCHAR [76]              wszAddressLine2;
  WCHAR [76]              wszCity;
  WCHAR [76]              wszState;
  WCHAR [76]              wszCountry;
  WCHAR [15]              wszPostalCode;
  WCHAR [256]             wszFormattedAddress;
  WCHAR [11]              wszCountryCode;
  WCHAR [11]              wszRegionCode;
} RILOSGEOLOCATIONINFO, RILOSGEOLOCATIONINFO;
````

## Members


`cbSize`



`dwAccuracy`



`dwAltitude`



`dwLatitude`



`dwLocationInformationMask`



`dwLongitude`



`dwParams`



`stTimeStamp`



`wszAddressLine1`



`wszAddressLine2`



`wszCity`



`wszCountry`



`wszCountryCode`



`wszFormattedAddress`



`wszPostalCode`



`wszRegionCode`



`wszState`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |