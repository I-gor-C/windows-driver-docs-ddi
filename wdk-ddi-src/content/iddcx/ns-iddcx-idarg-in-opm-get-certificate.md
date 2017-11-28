---
UID: NS.iddcx.IDARG_IN_OPM_GET_CERTIFICATE
title: IDARG_IN_OPM_GET_CERTIFICATE
author: windows-driver-content
description: Gives information about the OPM certificate.
old-location: display\idarg_in_opm_get_certificate.htm
old-project: display
ms.assetid: 0f6ce53f-f755-44f7-b579-ce3526e44c41
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_IN_OPM_GET_CERTIFICATE,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDARG_IN_OPM_GET_CERTIFICATE
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _Must_inspect_result_
req.iface: 
---

# IDARG_IN_OPM_GET_CERTIFICATE structure



## -description
<p>
                 Gives information about the 
             OPM certificate.</p>


## -syntax

````
typedef struct IDARG_IN_OPM_GET_CERTIFICATE {
  OPM_VIDEO_OUTPUT_SEMANTICS                            CertificateType;
  UINT                                                  CertificateBufferSizeInBytes;
  _Field_size_full_(CertificateBufferSizeInBytes) PVOID pCertificate;
} IDARG_IN_OPM_GET_CERTIFICATE, *IDARG_IN_OPM_GET_CERTIFICATE;
````


## -struct-fields
<dl>

### -field <b>CertificateType</b>

<dd>
<p>
                     [in] Type of certificate the information request is for.
                 </p>
</dd>

### -field <b>CertificateBufferSizeInBytes</b>

<dd>
<p>
                     [in] Size of the buffer provided for the driver to copy the certificate to.
                 </p>
</dd>

### -field <b>pCertificate</b>

<dd>
<p>
                     [out] A pointer to a buffer that the driver copies the certificate to.
                 </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>