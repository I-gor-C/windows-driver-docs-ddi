---
UID: NS:gnssdriver.GNSS_SUPL_CERT_CONFIG
title: GNSS_SUPL_CERT_CONFIG
author: windows-driver-content
description: This structure contains SUPL certificate information.
old-location: sensors\gnss_supl_cert_config.htm
old-project: sensors
ms.assetid: F974D5E2-7230-4F85-9C1A-7CE7E240DBE1
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: "*PGNSS_SUPL_CERT_CONFIG, GNSS_SUPL_CERT_CONFIG, GNSS_SUPL_CERT_CONFIG structure [Sensor Devices], PGNSS_SUPL_CERT_CONFIG, PGNSS_SUPL_CERT_CONFIG structure pointer [Sensor Devices], gnssdriver/GNSS_SUPL_CERT_CONFIG, gnssdriver/PGNSS_SUPL_CERT_CONFIG, sensors.gnss_supl_cert_config"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: gnssdriver.h
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
-	gnssdriver.h
api_name:
-	GNSS_SUPL_CERT_CONFIG
product: Windows
targetos: Windows
req.typenames: GNSS_SUPL_CERT_CONFIG, *PGNSS_SUPL_CERT_CONFIG
---

# GNSS_SUPL_CERT_CONFIG structure
This structure contains SUPL certificate information.

## Syntax
```
typedef struct GNSS_SUPL_CERT_CONFIG {
  ULONG                 Size;
  ULONG                 Version;
  GNSS_SUPL_CERT_ACTION CertAction;
  CHAR                  SuplCertName[MAX_PATH];
  ULONG                 CertSize;
  BYTE                  Unused[512];
  BYTE                  CertData[ANYSIZE_ARRAY];
} *PGNSS_SUPL_CERT_CONFIG, GNSS_SUPL_CERT_CONFIG;
```

## Members


`Size`

Structure size.

`Version`

Version number.

`CertAction`

A <a href="https://msdn.microsoft.com/library/windows/hardware/dn925225">GNSS_SUPL_CERT_ACTION</a> enumeration value that specifies the action to take on the certificate.

<table></table>
 

<table>
<tr>
<td>
<b>GNSS_SUPL_CERT_INJECT</b>

</td>
<td>
Inject the certificate.

</td>
</tr>
<tr>
<td>
<b>GNSS_SUPL_CERT_DELETE</b>

</td>
<td>
Delete the certificate specified by <b>SuplCertName</b>. The values of <b>CertSize</b> and <b>CertData</b> are ignored.

</td>
</tr>
<tr>
<td>
<b>GNSS_SUPL_CERT_PURGE</b>

</td>
<td>
Delete all the certificates injected to the GNSS driver previously. The values of <b>SuplCertName</b> , <b>CertSize</b>, and <b>CertData</b> are ignored.

</td>
</tr>
</table>

`SuplCertName`



`CertSize`

The size of the certificate in bytes.

`Unused`



`CertData`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | gnssdriver.h |