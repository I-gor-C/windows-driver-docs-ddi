---
UID : NS:iddcx.IDARG_IN_OPM_GET_CERTIFICATE
title : IDARG_IN_OPM_GET_CERTIFICATE
author : windows-driver-content
description : Gives information about the OPM certificate.
old-location : display\idarg_in_opm_get_certificate.htm
old-project : display
ms.assetid : 0f6ce53f-f755-44f7-b579-ce3526e44c41
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : IDARG_IN_OPM_GET_CERTIFICATE structure [Display Devices], iddcx/IDARG_IN_OPM_GET_CERTIFICATE, IDARG_IN_OPM_GET_CERTIFICATE, display.idarg_in_opm_get_certificate
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : iddcx.h
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
req.typenames : 
---

# IDARG_IN_OPM_GET_CERTIFICATE structure
Gives information about the 
             OPM certificate.

## Syntax
````
typedef struct IDARG_IN_OPM_GET_CERTIFICATE {
  OPM_VIDEO_OUTPUT_SEMANTICS                            CertificateType;
  UINT                                                  CertificateBufferSizeInBytes;
  _Field_size_full_(CertificateBufferSizeInBytes) PVOID pCertificate;
} IDARG_IN_OPM_GET_CERTIFICATE, *IDARG_IN_OPM_GET_CERTIFICATE;
````

## Members


`CertificateBufferSizeInBytes`

[in] Size of the buffer provided for the driver to copy the certificate to.

`CertificateType`

[in] Type of certificate the information request is for.

`pCertificate`

[out] A pointer to a buffer that the driver copies the certificate to.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | iddcx.h |