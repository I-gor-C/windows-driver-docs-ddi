---
UID: NS.rilapitypes.RILCALLDISCONNECTDETAILS
title: RILCALLDISCONNECTDETAILS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcalldisconnectdetails_2.htm
ms.assetid: 57b4d120-e12a-4821-a379-a392b804590c
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCALLDISCONNECTDETAILS
req.alt-loc: rilapitypes.h
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
ms.keywords: RILCALLDISCONNECTDETAILS, RILCALLDISCONNECTDETAILS
req.iface: 
req.product: Windows 10 or later.
---

# RILCALLDISCONNECTDETAILS structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILCALLDISCONNECTDETAILS {
  RILCALLDISCONNECTDETAILSDISCONNECTGROUP  dwDisconnectGroup;
  NULL                                     RILCAUSEUNION;
  RILCAUSEUNION                            causeUnion;
  NULL                                     switch_is;
  NULL                                     dwDisconnectGroup;
  RILGPPCAUSE                              unGPPCause;
  NULL                                     case;
  NULL                                     RIL_CD_3GPP_NETWORK_CAUSE;
  RILGPPREJECTCAUSE                        unGPPRejectCause;
  NULL                                     case;
  NULL                                     RIL_CD_3GPP_REJECT_CAUSE;
  RILGPP2CAUSE                             unGPP2Cause;
  NULL                                     case;
  NULL                                     RIL_CD_3GPP2_VENDOR_CAUSE;
  RILIMSSIPCAUSE                           unIMSSIPCause;
  NULL                                     case;
  NULL                                     RIL_CD_IMS_SIP_CAUSE;
  RILCALLDISCONNECTDETAILSASCODE           dwASCode;
  NULL                                     case;
  NULL                                     RIL_CD_AS_CAUSE;
  DWORD                                    dwOtherCode;
  NULL                                     case;
  NULL                                     RIL_CD_OTHER_CAUSE;
} RILCALLDISCONNECTDETAILS, RILCALLDISCONNECTDETAILS;
````


## -struct-fields
<dl>

### -field <b>dwDisconnectGroup</b>

<dd></dd>

### -field <b>RILCAUSEUNION</b>

<dd></dd>

### -field <b>causeUnion</b>

<dd></dd>

### -field <b>switch_is</b>

<dd></dd>

### -field <b>dwDisconnectGroup</b>

<dd></dd>

### -field <b>unGPPCause</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_CD_3GPP_NETWORK_CAUSE</b>

<dd></dd>

### -field <b>unGPPRejectCause</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_CD_3GPP_REJECT_CAUSE</b>

<dd></dd>

### -field <b>unGPP2Cause</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_CD_3GPP2_VENDOR_CAUSE</b>

<dd></dd>

### -field <b>unIMSSIPCause</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_CD_IMS_SIP_CAUSE</b>

<dd></dd>

### -field <b>dwASCode</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_CD_AS_CAUSE</b>

<dd></dd>

### -field <b>dwOtherCode</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_CD_OTHER_CAUSE</b>

<dd></dd>
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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>