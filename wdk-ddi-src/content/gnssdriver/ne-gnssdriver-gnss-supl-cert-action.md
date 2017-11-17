---
UID: NE.gnssdriver.GNSS_SUPL_CERT_ACTION
title: GNSS_SUPL_CERT_ACTION
author: windows-driver-content
description: This enumeration indicates the action to take upon receipt of the SUPL certificate, which is defined by the GNSS_SUPL_CERT_CONFIG structure.
old-location: sensors\gnss_supl_cert_action.htm
ms.assetid: DE51CB88-E761-40DC-B437-7572CD95FB4A
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: sensors
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_SUPL_CERT_ACTION
req.alt-loc: gnssdriver.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_, FWPS_VSWITCH_EVENT_DISPATCH_TABLE0
req.iface: 
---

# GNSS_SUPL_CERT_ACTION enumeration



## -description
<p>This enumeration indicates the action to take upon receipt of the SUPL certificate, which is defined by the <a href="https://msdn.microsoft.com/library/windows/hardware/dn925227">GNSS_SUPL_CERT_CONFIG</a> structure.</p>


## -syntax

````
typedef enum  { 
  GNSS_Supl_Cert_Inject  = 0x01,
  GNSS_Supl_Cert_Delete  = 0x02,
  GNSS_Supl_Cert_Purge   = 0x03
} GNSS_SUPL_CERT_ACTION;
````


## -enum-fields
<dl>

### -field <a id="GNSS_Supl_Cert_Inject"></a><a id="gnss_supl_cert_inject"></a><a id="GNSS_SUPL_CERT_INJECT"></a><b>GNSS_Supl_Cert_Inject</b>

<dd>
<p>Indicates that the certificate should be injected.</p>
</dd>

### -field <a id="GNSS_Supl_Cert_Delete"></a><a id="gnss_supl_cert_delete"></a><a id="GNSS_SUPL_CERT_DELETE"></a><b>GNSS_Supl_Cert_Delete</b>

<dd>
<p>Indicates that the certificate specified by the <b>SuplCertName</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn925227">GNSS_SUPL_CERT_CONFIG</a> structure should be deleted.</p>
</dd>

### -field <a id="GNSS_Supl_Cert_Purge_"></a><a id="gnss_supl_cert_purge_"></a><a id="GNSS_SUPL_CERT_PURGE_"></a><b>GNSS_Supl_Cert_Purge </b>

<dd>
<p>Indicates that all certificates previously injected into the GNSS driver should be deleted.</p>
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
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>