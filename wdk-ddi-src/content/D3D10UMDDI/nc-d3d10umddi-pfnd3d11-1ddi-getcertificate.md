---
UID: NC.d3d10umddi.PFND3D11_1DDI_GETCERTIFICATE
title: PFND3D11_1DDI_GETCERTIFICATE
author: windows-driver-content
description: 
ms.assetid: 11f9129f-bd27-4f40-9195-9b51f0d47841
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d10umddi.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# PFND3D11_1DDI_GETCERTIFICATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_GETCERTIFICATE Pfnd3d111DdiGetcertificate; 

// Definition

VOID Pfnd3d111DdiGetcertificate 
(
	D3D10DDI_HDEVICE hDevice
	CONST D3D11_1DDI_CERTIFICATE_INFO *pCertificateInfo
	UINT CertificateSize
	BYTE *pCertificate
)
{...}

PFND3D11_1DDI_GETCERTIFICATE 


```

## -parameters

### -param hDevice: 
### -param *pCertificateInfo: 
### -param CertificateSize: 
### -param *pCertificate: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also