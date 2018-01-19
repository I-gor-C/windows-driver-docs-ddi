---
UID : NS:d3d10umddi.D3D11_1DDIARG_CREATECRYPTOSESSION
title : D3D11_1DDIARG_CREATECRYPTOSESSION
author : windows-driver-content
description : Specifies the attributes of the cryptographic session to be created by the user-mode driver's CreateCryptoSession function.
old-location : display\d3d11_1ddiarg_createcryptosession.htm
old-project : display
ms.assetid : 9e63a4eb-050b-4f12-ad43-00e62021abd3
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D11_1DDIARG_CREATECRYPTOSESSION, D3D11_1DDIARG_CREATECRYPTOSESSION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Windows
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3D11_1DDIARG_CREATECRYPTOSESSION
req.alt-loc : D3d10umddi.h
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
req.typenames : D3D11_1DDIARG_CREATECRYPTOSESSION
---

# D3D11_1DDIARG_CREATECRYPTOSESSION structure
Specifies the attributes of the cryptographic session to be created by the user-mode driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createcryptosession.md">CreateCryptoSession</a> function.

## Syntax
````
typedef struct D3D11_1DDIARG_CREATECRYPTOSESSION {
  GUID CryptoType;
  GUID DecodeProfile;
  GUID KeyExchangeType;
} D3D11_1DDIARG_CREATECRYPTOSESSION;
````

## Members

        
            `CryptoType`

            a GUID that indicates the encryption type, which the driver uses for the encryption session that the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createcryptosession.md">CreateCryptoSession</a> function creates. The GUID can be one of the following:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `DecodeProfile`

            A GUID that specifies the DirectX Video Acceleration (DXVA) decode profile that the driver uses for the encryption session that the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createcryptosession.md">CreateCryptoSession</a> function creates. For a list of possible values, see <b>CreateCryptoSession</b>. If DXVA decoding will not be used, set this parameter to <b>NULL_GUID</b>.
        
            `KeyExchangeType`

            A GUID that specifies the type of key exchange.
The following GUID is defined.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |