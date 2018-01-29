---
UID : NS:bdatypes._BDA_WMDRM_RENEWLICENSE
title : _BDA_WMDRM_RENEWLICENSE
author : windows-driver-content
description : .
old-location : stream\bda_wmdrm_renewlicense.htm
old-project : stream
ms.assetid : 73AB73F1-CB9B-46A3-8ECC-19E93210D30E
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : BDA_WMDRM_RENEWLICENSE structure [Streaming Media Devices], PBDA_WMDRM_RENEWLICENSE structure pointer [Streaming Media Devices], BDA_WMDRM_RENEWLICENSE, *PBDA_WMDRM_RENEWLICENSE, bdatypes/BDA_WMDRM_RENEWLICENSE, bdatypes/PBDA_WMDRM_RENEWLICENSE, _BDA_WMDRM_RENEWLICENSE, PBDA_WMDRM_RENEWLICENSE, stream.bda_wmdrm_renewlicense
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : bdatypes.h
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
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : BDA_WMDRM_RENEWLICENSE, *PBDA_WMDRM_RENEWLICENSE
---

# _BDA_WMDRM_RENEWLICENSE structure


## Syntax
````
typedef struct _BDA_WMDRM_RENEWLICENSE {
  PBDARESULT lResult;
  ULONG      ulDescrambleStatus;
  ULONG      ulXmrLicenseOutputLength;
  BYTE       argbXmrLicenceOutputBuffer[MIN_DIMENSION];
} BDA_WMDRM_RENEWLICENSE, *PBDA_WMDRM_RENEWLICENSE;
````

## Members


`argbXmrLicenceOutputBuffer`

Specifies the license and entitlement token buffer.

`lResult`



`ulDescrambleStatus`



`ulXmrLicenseOutputLength`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | bdatypes.h |