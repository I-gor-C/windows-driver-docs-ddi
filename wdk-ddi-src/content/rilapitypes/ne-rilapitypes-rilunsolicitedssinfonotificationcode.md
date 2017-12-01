---
UID: NE.rilapitypes.RILUNSOLICITEDSSINFONOTIFICATIONCODE
title: RILUNSOLICITEDSSINFONOTIFICATIONCODE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilunsolicitedssinfonotificationcode_2.htm
old-project: netvista
ms.assetid: 3747f429-9893-44bd-ab3c-c3e78d8a264c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILUNSOLICITEDSSINFONOTIFICATIONCODE
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
req.iface: 
req.product: Windows 10 or later.
---

# RILUNSOLICITEDSSINFONOTIFICATIONCODE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILUNSOLICITEDSSINFONOTIFICATIONCODE { 
  RIL_UNSSSCODE_CUGCALL,
  RIL_UNSSSCODE_CALLPUTONHOLD,
  RIL_UNSSSCODE_CALLRETRIEVED,
  RIL_UNSSSCODE_ENTEREDMULTIPARTY,
  RIL_UNSSSCODE_HELDCALLRELEASED,
  RIL_UNSSSCODE_FORWARDCHECKSS,
  RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER,
  RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER,
  RIL_UNSSSCODE_DEFLECTEDCALL,
  RIL_UNSSSCODE_ADDITIONALINCOMINGCF,
  RIL_UNSSSCODE_UNCONDITIONALCFACTIVE,
  RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE,
  RIL_UNSSSCODE_CALLWASFORWARDED,
  RIL_UNSSSCODE_CALLISWAITING,
  RIL_UNSSSCODE_OUTGOINGCALLSBARRED,
  RIL_UNSSSCODE_INCOMINGCALLSBARRED,
  RIL_UNSSSCODE_CLIRSUPPRESSREJECT,
  RIL_UNSSSCODE_MAX
} RILUNSOLICITEDSSINFONOTIFICATIONCODE;
````


## -enum-fields
<dl>

### -field <a id="RIL_UNSSSCODE_CUGCALL"></a><a id="ril_unssscode_cugcall"></a><b>RIL_UNSSSCODE_CUGCALL</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_CALLPUTONHOLD"></a><a id="ril_unssscode_callputonhold"></a><b>RIL_UNSSSCODE_CALLPUTONHOLD</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_CALLRETRIEVED"></a><a id="ril_unssscode_callretrieved"></a><b>RIL_UNSSSCODE_CALLRETRIEVED</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_ENTEREDMULTIPARTY"></a><a id="ril_unssscode_enteredmultiparty"></a><b>RIL_UNSSSCODE_ENTEREDMULTIPARTY</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_HELDCALLRELEASED"></a><a id="ril_unssscode_heldcallreleased"></a><b>RIL_UNSSSCODE_HELDCALLRELEASED</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_FORWARDCHECKSS"></a><a id="ril_unssscode_forwardcheckss"></a><b>RIL_UNSSSCODE_FORWARDCHECKSS</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER"></a><a id="ril_unssscode_alertingexplicitcallxfer"></a><b>RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER"></a><a id="ril_unssscode_connectedexplicitcallxfer"></a><b>RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_DEFLECTEDCALL"></a><a id="ril_unssscode_deflectedcall"></a><b>RIL_UNSSSCODE_DEFLECTEDCALL</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_ADDITIONALINCOMINGCF"></a><a id="ril_unssscode_additionalincomingcf"></a><b>RIL_UNSSSCODE_ADDITIONALINCOMINGCF</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_UNCONDITIONALCFACTIVE"></a><a id="ril_unssscode_unconditionalcfactive"></a><b>RIL_UNSSSCODE_UNCONDITIONALCFACTIVE</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE"></a><a id="ril_unssscode_someconditionalcfactive"></a><b>RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_CALLWASFORWARDED"></a><a id="ril_unssscode_callwasforwarded"></a><b>RIL_UNSSSCODE_CALLWASFORWARDED</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_CALLISWAITING"></a><a id="ril_unssscode_calliswaiting"></a><b>RIL_UNSSSCODE_CALLISWAITING</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_OUTGOINGCALLSBARRED"></a><a id="ril_unssscode_outgoingcallsbarred"></a><b>RIL_UNSSSCODE_OUTGOINGCALLSBARRED</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_INCOMINGCALLSBARRED"></a><a id="ril_unssscode_incomingcallsbarred"></a><b>RIL_UNSSSCODE_INCOMINGCALLSBARRED</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_CLIRSUPPRESSREJECT"></a><a id="ril_unssscode_clirsuppressreject"></a><b>RIL_UNSSSCODE_CLIRSUPPRESSREJECT</b>

<dd></dd>

### -field <a id="RIL_UNSSSCODE_MAX"></a><a id="ril_unssscode_max"></a><b>RIL_UNSSSCODE_MAX</b>

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