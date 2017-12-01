---
UID: NE.d3dkmthk._D3DKMT_VIDSCHESCAPETYPE
title: D3DKMT_VIDSCHESCAPETYPE
author: windows-driver-content
description: The D3DKMT_VIDMMESCAPETYPE enumeration is used with the D3DKMT_VIDSCH_ESCAPE structure.
old-location: display\d3dkmt_vidschescapetype.htm
old-project: display
ms.assetid: 8388A03F-995A-4A33-B541-4FF2422DEE83
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: TBD
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_VIDSCHESCAPETYPE
req.alt-loc: d3dkmthk.h
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
---

# D3DKMT_VIDSCHESCAPETYPE enumeration



## -description
<p><b>Do not use the D3DKMT_VIDSCHESCAPETYPE enumeration; it is for testing purposes only.</b></p>
<p>The D3DKMT_VIDMMESCAPETYPE enumeration is used with the <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-vidsch-escape.md">D3DKMT_VIDSCH_ESCAPE</a> structure.</p>


## -syntax

````
typedef enum _D3DKMT_VIDSCHESCAPETYPE { 
  D3DKMT_VIDSCHESCAPETYPE_PREEMPTIONCONTROL    = 0,
  D3DKMT_VIDSCHESCAPETYPE_SUSPENDSCHEDULER     = 1,
  D3DKMT_VIDSCHESCAPETYPE_TDRCONTROL           = 2,
  D3DKMT_VIDSCHESCAPETYPE_SUSPENDRESUME        = 3,
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
  D3DKMT_VIDSCHESCAPETYPE_ENABLECONTEXTDELAY   = 4,
#endif 
  D3DKMT_VIDSCHESCAPETYPE_CONFIGURE_TDR_LIMIT  = 5
} D3DKMT_VIDSCHESCAPETYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMT_VIDSCHESCAPETYPE_PREEMPTIONCONTROL"></a><a id="d3dkmt_vidschescapetype_preemptioncontrol"></a><b>D3DKMT_VIDSCHESCAPETYPE_PREEMPTIONCONTROL</b>

<dd></dd>

### -field <a id="D3DKMT_VIDSCHESCAPETYPE_SUSPENDSCHEDULER"></a><a id="d3dkmt_vidschescapetype_suspendscheduler"></a><b>D3DKMT_VIDSCHESCAPETYPE_SUSPENDSCHEDULER</b>

<dd></dd>

### -field <a id="D3DKMT_VIDSCHESCAPETYPE_TDRCONTROL"></a><a id="d3dkmt_vidschescapetype_tdrcontrol"></a><b>D3DKMT_VIDSCHESCAPETYPE_TDRCONTROL</b>

<dd></dd>

### -field <a id="D3DKMT_VIDSCHESCAPETYPE_SUSPENDRESUME"></a><a id="d3dkmt_vidschescapetype_suspendresume"></a><b>D3DKMT_VIDSCHESCAPETYPE_SUSPENDRESUME</b>

<dd></dd>

### -field <a id="D3DKMT_VIDSCHESCAPETYPE_ENABLECONTEXTDELAY"></a><a id="d3dkmt_vidschescapetype_enablecontextdelay"></a><b>D3DKMT_VIDSCHESCAPETYPE_ENABLECONTEXTDELAY</b>

<dd></dd>

### -field <a id="D3DKMT_VIDSCHESCAPETYPE_CONFIGURE_TDR_LIMIT"></a><a id="d3dkmt_vidschescapetype_configure_tdr_limit"></a><b>D3DKMT_VIDSCHESCAPETYPE_CONFIGURE_TDR_LIMIT</b>

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
<dt>D3dkmthk.h (include TBD)</dt>
</dl>
</td>
</tr>
</table>