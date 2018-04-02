---
UID: NC:d3d10umddi.PFND3D11_1DDI_GETCERTIFICATESIZE
title: PFND3D11_1DDI_GETCERTIFICATESIZE
author: windows-driver-content
description: Queries the size in bytes of the certificate that the display miniport driver uses for either the cryptographic session certificate or authenticated channel.
old-location: display\getcertificatesize.htm
old-project: display
ms.assetid: 7f9a2a76-ee50-4f72-a588-d7b9145c14a6
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11_1DDI_GETCERTIFICATESIZE, d3d10umddi/pfnGetCertificateSize, display.getcertificatesize, pfnGetCertificateSize, pfnGetCertificateSize callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	UserDefined
api_location:
-	D3d10umddi.h
api_name:
-	pfnGetCertificateSize
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_GETCERTIFICATESIZE callback function
Queries the size in bytes of the certificate that the display miniport driver uses for either the cryptographic  session certificate or authenticated channel.

## Syntax

```
PFND3D11_1DDI_GETCERTIFICATESIZE Pfnd3d111DdiGetcertificatesize;

void Pfnd3d111DdiGetcertificatesize(
  D3D10DDI_HDEVICE hDevice,
  CONST D3D11_1DDI_CERTIFICATE_INFO *pCertificateInfo,
  UINT *pCertificateSize
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*pCertificateInfo`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406435">D3D11_1DDI_CERTIFICATE_INFO</a> structure that specifies the cryptographic  session certificate or authenticated channel to query.

`*pCertificateSize`

The size, in bytes, of the specified certificate.


## Return Value

This callback function does not return a value.

## Remarks

Based on the data in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406435">D3D11_1DDI_CERTIFICATE_INFO</a> structure, the <b>GetCertificateSize</b> function returns the size in bytes of the certificate chain for either the cryptographic session or the authenticated channel. The driver uses this certificate to establish trust and perform key exchange for the session or channel.

<div class="alert"><b>Note</b>  The driver's certificate  can be queried by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451652">GetCertificate</a>.</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406435">D3D11_1DDI_CERTIFICATE_INFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451652">GetCertificate</a>